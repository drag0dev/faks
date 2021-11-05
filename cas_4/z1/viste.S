.section .data
poruka1: .ascii "Unesite ime i prezime: \0"
poruka1_len = . - poruka1 -1
poruka2: .ascii "Vi ste: \0"
poruka2_len = . - poruka2 -1
imeprez: .fill 50,1,42
imeprez_len = . - imeprez
.section .text
.global main

main:
	#ispis poruka1
	movl $4, %eax
	movl $1, %ebx
	leal poruka1, %ecx
	movl $poruka1_len, %edx
	int $0x80

	#unos
	movl $3, %eax
	movl $0, %ebx
	leal imeprez, %ecx
	movl $imeprez_len, %edx
	int $0x80
	subl $1, %eax
	movl %eax, %edi

	movl $imeprez, %eax #baza %eax
petlja:
	addl $1, %eax
	cmpb $10, -1(%eax) #==\n
	je ispis
	cmpb $97, -1(%eax)
	jc petlja
	subl $32, -1(%eax)
	jmp petlja
ispis:
	#ispis poruka2
	movl $4, %eax
	movl $1, %ebx
	leal poruka2, %ecx
	movl $poruka2_len, %edx
	int $0x80

	#ispis ime i prezime
	movl $4, %eax
	movl $1, %ebx
	leal imeprez, %ecx
	movl %edi, %edx
	int $0x80

kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
