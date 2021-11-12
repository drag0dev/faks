#potprogram koji racuna n-ti element fib niza
#autor Dragoslav Tamindzija SV47/2021
#int fibonaci(int n, unsigned int* rez);

.section .text
.globl fibonaci
fibonaci:
	pushl %ebp
	movl %esp, %ebp

	pushl %ebx

	movl $1, %eax
	movl $1, %ebx
	movl 8(%ebp), %ecx #ecx je brojac

	cmpl $2, %ecx
	jle kraj

	subl $2, %ecx #posto se u registrima nalaze 1. i 2. element

petlja:
	cmpl $0, %ecx
	je izlaz_bez_greske

	movl %ebx, %edx #edx pomocna

	addl %eax, %ebx
	jc izlaz_greska

	movl %edx, %eax
	subl $1, %ecx #brojac se umanjuje
	jmp petlja

izlaz_greska:
	movl $1, %eax
	jmp kraj

izlaz_bez_greske:
	movl $0, %eax

kraj:
	movl 12(%ebp), %edx #adresa rez
	movl %ebx, (%edx)
	popl %ebx #vracamo ebx

	movl %ebp, %esp
	popl %ebp
	ret
