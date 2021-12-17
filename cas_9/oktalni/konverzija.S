#potprogram za konvertovanje stringa u oktalni broj
#autor Dragoslav Tamindzija SV47/2021
#unsigned int oct_str_to_inter(char* str, unsigned int* greska);
.section .text
.globl oct_str_to_inter

oct_str_to_inter:
	pushl %ebp
	movl %esp, %ebp
	pushl %esi

	movl 8(%ebp), %esi # esi = str

	movl $0, %eax # eax rezultat
	movl $8, %ecx # ecx baza
	movl $0, %edx # pomocna	
petlja:
	movb (%esi), %dl
	andb %dl, %dl
	jz izlaz
	subb $'0', %dl
	mull %ecx
	addl %edx, %eax
	addl $1, %esi
	jmp petlja

izlaz:
	movl $0, 12(%ebp)
	cmpl %esi, 8(%ebp)
	je greska
	jmp kraj

greska:
	movl $1, %edx

kraj:
	popl %esi
	movl %ebp, %esp
	popl %ebp
	ret
