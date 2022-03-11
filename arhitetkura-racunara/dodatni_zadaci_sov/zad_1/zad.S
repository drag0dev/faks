#autor Dragoslav Tamindzija SV47/2021
# inverzna poljska notacija
.section .data
unos_str: .ascii "Unesite izraz: "
unos_str_len = . - unos_str

rez_str: .ascii "Rezultat je: "
rez_str_len = . - rez_str

poruka_greska1: .ascii "Ulazni string je prazan!\n"
poruka_greska1_len = . - poruka_greska1

poruka_greska2: .ascii "Cifra ne pripada brojnom sistemu!\n"
poruka_greska2_len = . - poruka_greska2

poruka_greska3: .ascii "Prekoracenje pri konverziji!\n"
poruka_greska3_len = . - poruka_greska3

poruka_greska4: .ascii "Prekoracenje pri sabiranju!\n"
poruka_greska4_len = . - poruka_greska4

ulazni_str: .fill 101, 1, 0 # 100 karaktera + null

izlazni_str: .fill 21, 1, 0 # 20 karaktera + null

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
	movl $100, %edx
	int $0x80

	xorl %eax, %eax # trenutni operand
	movl $10, %ebx # baza broja
	movl $ulazni_str, %ecx # ecx pokazivac na string

	cmpb $10, (%ecx)
	jz greska_prazan

petlja:
	cmpb $10, (%ecx)
	jz izlazak
	cmpb $0, (%ecx)
	jz izlazak

	cmpb $' ', (%ecx)
	jz space

	cmpb $'+', (%ecx)
	jz sabiraj

	jmp broj

space:
	addl $1, %ecx
	jmp petlja

broj:
	xorl %edx, %edx
	mull %ebx # broj * baza

	andl %edx, %edx
	jnz greska_konverzija

	movb (%ecx), %dl
	cmpb $'0', %dl # dl < '0'
	jb greska_cifra

	cmpb $'9', %dl # dl > '9'
	ja greska_cifra

	subb $'0', %dl
	addl %edx, %eax
	jc greska_sabiranje

	addl $1, %ecx
	cmpb $0, (%ecx)
	jz broj_na_stack
	cmpb $10, (%ecx)
	jz broj_na_stack
	cmpb $' ', (%ecx)
	jz broj_na_stack
	jmp broj

broj_na_stack:
	pushl %eax
	xorl %eax, %eax
	jmp petlja

sabiraj:
	popl %eax
	popl %edx	
	addl %edx, %eax
	jc greska_sabiranje
	pushl %eax
	addl $1, %ecx
	xorl %eax, %eax
	jmp petlja

izlazak:
	popl %eax
	movl $izlazni_str, %ecx
	movl $0, %esi # broj karaketra

konvert_str:
	xorl %edx, %edx
	divl %ebx # rez / baza

	addb $'0', %dl
	movb %dl, (%ecx)

	addl $1, %ecx
	addl $1, %esi
	
	andl %eax, %eax
	jnz konvert_str

	movb $10, (%ecx)
	addl $1, %esi

	movl $izlazni_str, %edi
	subl $1, %ecx

invert_str:
	movb (%ecx), %al
	movb (%edi), %bl
	movb %al, (%edi)
	movb %bl, (%ecx)
	addl $1, %edi
	subl $1, %ecx
	cmpl %edi, %ecx
	jnbe invert_str

	# ispis poruke za rez
	movl $4, %eax
	movl $1, %ebx
	movl $rez_str, %ecx
	movl $rez_str_len, %edx
	int $0x80

	# ispis rezultata
	movl $4, %eax
	movl $1, %ebx
	movl $izlazni_str, %ecx
	movl %esi, %edx
	int $0x80

	movl $0, %ebx
	jmp kraj
	

greska_prazan:
	# ispis greske
	movl $4, %eax
	movl $1, %ebx
	movl $poruka_greska1, %ecx
	movl $poruka_greska1_len, %edx
	int $0x80

	movl $1, %ebx
	jmp kraj

greska_cifra:
	# ispis greske
	movl $4, %eax
	movl $1, %ebx
	movl $poruka_greska2, %ecx
	movl $poruka_greska2_len, %edx
	int $0x80

	movl $2, %ebx
	jmp kraj

greska_konverzija:
	# ispis greske
	movl $4, %eax
	movl $1, %ebx
	movl $poruka_greska3, %ecx
	movl $poruka_greska3_len, %edx
	int $0x80

	movl $3, %ebx
	jmp kraj

greska_sabiranje:
	# ispis greske
	movl $4, %eax
	movl $1, %ebx
	movl $poruka_greska4, %ecx
	movl $poruka_greska4_len, %edx
	int $0x80

	movl $4, %ebx

kraj:
	movl $1, %eax
	int $0x80
