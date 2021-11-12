.section .data
a: .long 0x12345678
.section .text
.globl main

main:
	movb a, %ah
	movb a+1, %al
	movb a+2, %bh
	movb a+3, %bl
kraj:
	movl $1, %eax
	int $0x80
