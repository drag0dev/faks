#a=b na n
#n puta cemo vrsiti mnozenje samog sebe
#autor: Dragoslav Tamindzija SV47 2021
.section .data
greska: .byte 0
a: .quad 0
b: .quad 5
n: .long 3
.section .text
.globl main
main:
	movl b, %eax
	movl b+4, %ebx
	subl $1, n
priprema:
	movl b, %ecx # brojac za mnozenje
	movl b+4, %edx # -||-
petlja_mnozenja:
	addl %eax, a
	adcl %ebx, a+4
	jc greska_izlaz

	subl $1, %ecx
	sbbl $0, %edx
	cmpl $0, %ecx
	jnz petlja_mnozenja
	cmpl $0, %edx
	jnz petlja_mnozenja
brojac:
	subl $1, n
	jz kraj
	movl a, %eax
	movl a+4, %ebx
	movl $0, a
	movl $0, a+4
	jmp priprema
greska_izlaz:
	movl $1, greska
kraj:
	movl $0, %eax
	int $0x80
