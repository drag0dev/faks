#program koji racuna prvih n
#autor Dragoslav Tamindzija SV47

.section .data
.section .text
.global main

main:
	movl $6, %eax #postavljamo n
	movl $0, %ebx #ovaj registar ce drzati zbir

sabiranje:
	addl %eax, %ebx
	subl $1, %eax
	je kraj
	jmp sabiranje

kraj:
	movl $0, %eax
	movl $1, %ebx
	int $0x80
