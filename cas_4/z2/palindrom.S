.section .data
poruka: .ascii "Unesite string:\0"
poruka_len = . - poruka
nijep:  .ascii "String nije palindrom.\n\0"
nijep_len = . - nijep
jestep: .ascii "String je palindrom.\n\0"
jestep_len = . - jestep
unos:   .fill 50,1,42
unos_len = . -unos -1
.section .text
.globl main
main:
	#ispis poruke
	movl $4, %eax
	movl $1, %ebx
	leal poruka, %ecx
	movl $poruka_len, %edx
	int $0x80

	#unos
	movl $3, %eax
	movl $0, %ebx
	leal unos, %ecx
	movl $unos_len, %edx
	int $0x80
	movl %eax, %edi
	subl $1, %edi #duzina unesenog stringa

	leal unos, %eax #baza za pocetak unosa
	leal unos, %ebx #baza za kraj unosa
	addl %edi, %ebx #pomerimo %ebx da pokazuje elemtn pre \n
	subl $1, %ebx
petlja:
	cmpl %eax, %ebx
	jle jeste_palindrom
	movb (%eax), %cl
	cmpb %cl, (%ebx)
	jnz nije_palindrom
	addl $1, %eax
	subl $1, %ebx
	jmp petlja
nije_palindrom: #ispisuje poruku ako nije palindrom
	movl $4, %eax
	movl $1, %ebx
	leal nijep, %ecx
	movl $nijep_len, %edx
	int $0x80

	movl $1, %ebx #postavlja se izlazni kod
	jmp kraj
jeste_palindrom: #ispisuje poruku ako jeste palindrom
	movl $4, %eax
	movl $1, %ebx
	leal jestep, %ecx
	movl $jestep_len, %edx
	int $0x80

	movl $0, %ebx #postavlja se izlazni kod
kraj:
	movl $1, %eax
	int $0x80
