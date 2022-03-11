#autor Dragoslav Tamindzija
#bajtovi oznacenog heksdecimalnog broja
.section .data
unos_str: .ascii "Unesite 64-bitni dekadni ceo broj: "
unos_str_len = . - unos_str

ispis_str: .ascii "Broj se sastoji iz ovih bajtova (redosled od najnizeg): "
ispis_str_len = . - ispis_str

greska_cifra: .ascii "Pogresna cifra!\n"
greska_cifra_len = . - greska_cifra

greska_prekoracenje: .ascii "Prekoracenje!\n"
greska_prekoracenje_len = . - greska_prekoracenje

ulazni_str: .fill 21, 1, 0 # 20 karaktera + null

izlazni_str: .fill 51, 1, 0 # 50 karaktera + null
.section .text
.globl main
main:
	# ispis poruke za unos broja
	movl $4, %eax
	movl $1, %ebx
	movl $unos_str, %ecx
	movl $unos_str_len, %edx
	int $0x80

	# unos stringa
	movl $3, %eax
	movl $0, %ebx
	movl $ulazni_str, %ecx
	movl $20, %edx
	int $0x80

	movl $ulazni_str, %ecx # ecx pokazivac na string
	xorl %eax, %eax # donji deo broja
	xorl %ebx, %ebx # gornji deo broja

	cmpb $10, (%ecx) # prazan string
	jz greska_baza
	cmpb $'-', (%ecx)
	jnz petlja
	addl $1, %ecx

petlja:
	cmpb $0, (%ecx)
	jz provera_znaka
	cmpb $10, (%ecx)
	jz provera_znaka

	# broj * 10
	movl $9, %edx
	movl %eax, %esi # esi donji deo broja
	movl %ebx, %edi # edi visi deo broja
mnozenje:
	addl %esi, %eax
	adcl %edi, %ebx
	jc greska_prekor
	subl $1, %edx
	jnz mnozenje

	xorl %edx, %edx # edx = 0
	movb (%ecx), %dl

	cmpb $'0', %dl # dl < '0'
	jb greska_baza

	cmpb $'9', %dl # dl > '9'
	ja greska_baza

	subb $'0', %dl

	addl %edx, %eax
	adcl $0, %ebx
	jc greska_prekor

	addl $1, %ecx
	jmp petlja

provera_znaka:
	movl $ulazni_str, %ecx
	cmpb $'-', (%ecx)
	jnz konverzija_to_str

	# komplement
	not %ebx
	not %eax
	addl $1, %eax

konverzija_to_str:

	movl $izlazni_str, %ecx # ecx pokazivac na izlazni string
	pushl $1 # broj karatera u izlaznom stringu, 1 zbog \n
	xorl %edi, %edi # broj bajtova, na parni broj ' ' u string staviti
	xorl %esi, %esi # broj bajtova
to_str:
	cmpl $8, %esi
	jz ispis

	popl %edx
	addl $1, %edx
	pushl %edx

	addl $1, %edi

	xorl %edx, %edx
	movb %al, %dl

	andb $15, %dl # gornja 4 bita u 0

	cmpb $9, %dl # dl <= 9
	jbe broj

slovo:
	addb $55, %dl
	movb %dl, (%ecx)
	addl $1, %ecx
	movl $4, %edx
	jz ispis
	jmp pomeranje

broj:
	addb $'0', %dl
	movb %dl, (%ecx)
	addl $1, %ecx
	movl $4, %edx
	jz ispis

pomeranje:
	shrl %ebx
	rcrl %eax
	subl $1, %edx
	jnz pomeranje

	cmpl $1, %edi
	jz to_str

	testl $1, %edi # provera da li je neparan
	jnz to_str

	addl $1, %esi
	# zamena dva slova
	pushl -2(%ecx)
	pushl -1(%ecx)
	popl -2(%ecx)
	popl -1(%ecx)

	movb $' ', (%ecx)
	addl $1, %ecx

	popl %edx
	addl $1, %edx
	pushl %edx

	jmp to_str

ispis:
	movb $10, (%ecx)
	popl %edx
	addl $1, %edx
	pushl %edx
	# poruka za ispis rezultata
	movl $4, %eax
	movl $1, %ebx
	movl $ispis_str, %ecx
	movl $ispis_str_len, %edx
	int $0x80

	# ispis bajtova
	movl $4, %eax
	movl $1, %ebx
	movl $izlazni_str, %ecx
	popl %edx
	int $0x80
	jmp kraj

greska_baza:
	# ispis greske za cifru
	movl $4, %eax
	movl $1, %ebx
	movl $greska_cifra, %ecx
	movl $greska_cifra_len, %edx
	int $0x80
	movl $1, %ebx
	jmp kraj

greska_prekor:
	# ispis greske za prekoracenje
	movl $4, %eax
	movl $1, %ebx
	movl $greska_prekoracenje, %ecx
	movl $greska_prekoracenje_len, %edx
	int $0x80

kraj:
	movl $1, %eax
	int $0x80
