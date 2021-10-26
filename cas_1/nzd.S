#program koji racuna nzd
#autor Dragoslav Tamindzija SV47

.section .data
.section .text
.global main

main:
	movl $12, %eax #prvi broj
	movl $8, %ebx #drugi broj

petlja:
	cmpl %eax, %ebx
	je kraj
	cmpl %eax, %ebx
	ja vece
	subl %ebx, %eax
	jmp petlja
vece:
	subl %eax, %ebx
	jmp petlja

kraj:
	movl $0, %eax
	movl $1, %ebx
	int $0x80
