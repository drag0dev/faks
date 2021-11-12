#program racuna n-ti element fibonacijevog niza
#autor Dragoslav Tamindzija SV47

.section .data
.section .text
.globl main

main:
	movl $10, %eax #n-ti element
	movl $1, %ebx #prvi sabirak
	movl $1, %ecx #drugi sabirak
	movl $0, %edx #pomocna

	cmpl $2, %eax
	je kraj
	cmpl $1, %eax
	je kraj
	cmp $0, %eax
	je kraj

	subl $2, %eax
niz:
	movl %ecx, %edx
	addl %ebx, %ecx
	movl %edx, %ebx
	subl $1, %eax
	je kraj
	jmp niz
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80

