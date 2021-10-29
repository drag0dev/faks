#nalazenje indeksa svih min i max
#autor: Dragoslav Tamindzija
.section .data
NELEM = 10
niz: .quad 65,1,99,1,64,65,99,1,99,10
niz_indeks_min: .fill 10,1,0 #dva niza gde pamtimo gde su najveci
niz_indeks_max: .fill 10,1,0 #i najmanji index tako sto navimo 1 na
#isti index kao i u samom nizu tj. ova dva niza nam govore na kojim
#mestima su min i max
min: .quad 0
max: .quad 0
.section .text
.global main
main:
	movl $0, %esi #index
	movl $niz, %eax #baza niza
	movl $niz_indeks_min, %ebx #baza min indexa
	movl $niz_indeks_max, %ecx #baza max indexa

	#podesavamo pocetne vrednosti min i max
	movl (%eax), %ebp #visi deo
	movl %ebp, min
	movl %ebp, max

	movl 4(%eax), %ebp #nizi deo
	movl %ebp, min+4
	movl %ebp, max+4

trazenje_min_i_max:
	incl %esi
	cmpl $NELEM, %esi #provera da li smo dosli do kraja
	je priprema #ako jesmo idemo na pripremu
	addl $8, %eax #posto radimo sa quad moramo dodavati 8
	#ovde je odma dodato jer necemo uporedjivati prvi element

	movl (%eax), %ebp #visi deo elementa niza
	movl 4(%eax), %edx #nizi deo elementa niza
	cmpl %ebp, min #proveravamo visi deo min
 	jge novi_min

	cmpl %ebp, max #proveravamo visi deo max
	jle novi_max

	jmp trazenje_min_i_max
novi_max:
	cmpl min+4, %edx #moramo proveriti i nizi
	jl trazenje_min_i_max
	movl %ebp, max #ako jeste prebacujemo novi max
	movl %edx, max+4
	jmp trazenje_min_i_max
novi_min:
	cmpl min+4, %edx #moramo proveriti i nizi
	jg trazenje_min_i_max
	movl %ebp, min #ako jeste prebaucjemo novi min
	movl %edx, min+4
	jmp trazenje_min_i_max

#sledeci deo programa trazi gde su iste min i max
priprema:
	movl $-1, %esi #resetujemo index
	movl $niz, %eax #baza za a #resetujemo adresu
petlja_za_indexe:
	incl %esi
	cmpl $NELEM-1, %esi #provera da li je kraj
	je kraj

	movl (%eax), %ebp #u registar se stavlja element
	movl 4(%eax), %edx
poredjenje_min: #proveravamo da li je dati element =min
	addl $8, %eax #posto ce ovde uvek doci ovde pomeram na sledece el

	cmpl min, %ebp
	jne poredjenje_max #ako visi deo nije jednak skace na max
	cmpl min+4, %edx
	jne poredjenje_max #ako nizi deo nije jednak skace na max
	movb $1, (%ebx,%esi,1) #ako jeste onda stavljamo 1 u niz
poredjenje_max: # proveravamo da li je dati element =max
	cmpl max, %ebp #proveravamo visi deo
	jne petlja_za_indexe #ako nije idemo nazad u petlju
	cmpl max+4, %edx #proveravamo i nizi deo
	jne petlja_za_indexe
	movb $1, (%ecx, %esi, 1) #ako jeste onda stavljamo 1 u niz
	jmp petlja_za_indexe
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
