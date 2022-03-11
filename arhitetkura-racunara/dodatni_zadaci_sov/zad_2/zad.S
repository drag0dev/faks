#autor Dragoslav Tamindzija SV47/2021
# kalkulator neoznacenih 64bitnih brojeva
.section .data
unos_str: .ascii "Unesite izraz: "
unos_str_len = . - unos_str

izlaz_str: .ascii "Rezultat: "
izlaz_str_len = . - izlaz_str

greska_str_operacija: .ascii "Nepoznata operacija!\n"
greska_str_operacija_len = . - greska_str_operacija

greska_str_operand: .ascii "Pogresan operand!\n"
greska_str_operand_len = . - greska_str_operand

greska_str_prekoracenje: .ascii "Prekoracenje kod operanda!\n"
greska_str_prekoracenje_len = . - greska_str_prekoracenje

ulazni_str: .fill 51, 1, 0 # 50 karaktera + null

izlazni_str: .fill 21, 1, 0 # 20 karaktera + null

operacija: .fill 1, 1, 0
broj_1: .quad 0
broj_2: .quad 0
.section .text
.globl main
main:
	# ispis poruke za unos
	movl $4, %eax
	movl $1, %ebx
	movl $unos_str, %ecx
	movl $unos_str_len, %edx
	int $0x80

	# unos stringa
	movl $3, %eax
	movl $0, %ebx
	movl $ulazni_str, %ecx
	movl $50, %edx
	int $0x80

	xorl %eax, %eax # broj
	movl $0, %ebx # broj unetih operanada
	movl $ulazni_str, %ecx # ecx pokzivac na uneti string

	cmpb $10, (%ecx) # ako je prazan string
	jz kraj

petlja:
	cmpb $10, (%ecx)
	jz racunaj
	cmpb $0, (%ecx)
	jz racunaj
	cmpb $' ', (%ecx)
	jz space

	cmpb $'&', (%ecx)
	jz znak
	cmpb $'|', (%ecx)
	jz znak
	cmpb $'^', (%ecx)
	jz znak

	xorl %eax, %eax
	xorl %edi, %edi
	xorl %esi, %esi
	jmp broj
space:
	addl $1, %ecx
	jmp petlja

znak:
	movb (%ecx), %al
	movb %al, operacija
	addl $1, %ecx
	jmp petlja

broj:
	cmpb $' ', (%ecx)
	jz izlaz_konverzija
	cmpb $10, (%ecx)
	jz izlaz_konverzija
	cmpb $0, (%ecx)
	jz izlaz_konverzija
	# esi nizi deo
	# edi visi deo
	movl $4, %eax
mnozenje: # broj * 16
	shll %esi
	rcll %edi
	jc greska_prekoracenje
	subl $1, %eax
	jnz mnozenje

	movb (%ecx), %al
	cmpb $'0', %al # al < '0'
	jb greska_operand

	cmpb $'9', %al # al <= '9'
	jbe broj_karakter

	cmpb $'a', %al # ! al >= 'a'
	jnae slovo_karakter

	subb $32, %al # veliko slovo u malo
	jmp slovo_karakter
	
broj_karakter:
	subb $'0', %al
	addl %eax, %esi
	adcl $0, %edi
	jc greska_prekoracenje

	addl $1, %ecx
	jmp broj	

slovo_karakter:
	subb $55, %al # slovo u broj
	addl %eax, %esi
	adcl $0, %edi
	jc greska_prekoracenje

	addl $1, %ecx
	jmp broj

izlaz_konverzija:
	movl $broj_1, %eax
	cmpl $1, %ebx
	jz drugi_broj
	movl %edi, 4(%eax)
	movl %esi, (%eax)
	addl $1, %ebx
	jmp petlja
drugi_broj:
	movl $broj_2, %eax
	movl %edi, 4(%eax)
	movl %esi, (%eax)
	addl $1, %ebx

racunaj:
	cmpl $2, %ebx
	jnz greska_operand

	movl $broj_1, %eax
	movl 4(%eax), %edx
	movl (%eax), %eax

	movl $broj_2, %ecx
	movl 4(%ecx), %ebx
	movl (%ecx), %ecx

	movl $izlazni_str, %esi
	movl $16, %edi
	pushl $0 # broj karaktera u izlaznom stringu

	cmpb $'&', operacija
	jz and
	cmpb $'|', operacija
	jz or
	
xor:
	xorl %eax, %ecx
	xorl %edx, %ebx
	jmp konvert_to_str
and:
	andl %eax, %ecx
	andl %edx, %ebx
	jmp konvert_to_str
or:
	orl %eax, %ecx
	orl %edx, %ebx

# podeli se se 16, posto to moze da utice samo na prvhi 4 bita shiftuje se u desno 4 puta
# da bi se izbacili ti bitovi
konvert_to_str:
	popl %edx
	addl $1, %edx
	pushl %edx

	xorl %edx, %edx
	xorl %eax, %eax

	movb %cl, %al # uzima se prvih 8 bita
	andb $15, %al # skoloni se gornjih 4 bita

	divl %edi # prva 4 bita / 16

	cmpl $9, %edx # dl > 9
	ja to_slovo
	
to_broj:
	addb $'0', %dl
	movb %dl, (%esi)
	addl $1, %esi
	movl $4, %edx
	jmp pomeranje_4_bita
to_slovo:
	addb $55, %dl
	movb %dl, (%esi)
	addl $1, %esi
	movl $4, %edx

pomeranje_4_bita:
	shrl %ebx
	rcrl %ecx
	subl $1, %edx
	jnz pomeranje_4_bita

	andl %ecx, %ecx
	jz kraj_konverzija_u_str
	jmp konvert_to_str


kraj_konverzija_u_str: # provera da li je visi deo 0
	andl %ebx, %ebx
	jz invert_str
	jmp konvert_to_str

invert_str:
	movl $10, (%esi)
	subl $1, %esi
	movl $izlazni_str, %edi

zamena:
	movb (%esi), %al
	movb (%edi), %bl
	movb %bl, (%esi)
	movb %al, (%edi)
	addl $1, %edi
	subl $1, %esi
	cmpl %edi, %esi
	jbe ispis_rez
	jmp zamena

ispis_rez:
	# ispis poruke za rezultat
	movl $4, %eax
	movl $1, %ebx
	movl $izlaz_str, %ecx
	movl $izlaz_str_len, %edx
	int $0x80

	# ispis rezultat
	movl $4, %eax
	movl $1, %ebx
	movl $izlazni_str, %ecx
	popl %edx
	addl $1, %edx
	int $0x80

	movl $0, %ebx
	jmp kraj

greska_operacija:
	# ispis poruke za gresku
	movl $4, %eax
	movl $1, %ebx
	movl $greska_str_operacija, %ecx
	movl $greska_str_operacija_len,  %edx
	int $0x80

	movl $1, %ebx
	jmp kraj

greska_operand:
	# ispis poruke za gresku
	movl $4, %eax
	movl $1, %ebx
	movl $greska_str_operand, %ecx
	movl $greska_str_operand_len,  %edx
	int $0x80

	movl $2, %ebx
	jmp kraj

greska_prekoracenje:
	# ispis poruke za gresku
	movl $4, %eax
	movl $1, %ebx
	movl $greska_str_prekoracenje, %ecx
	movl $greska_str_prekoracenje_len,  %edx
	int $0x80

	movl $3, %ebx
	jmp kraj

kraj:
	movl $1, %eax
	int $0x80
