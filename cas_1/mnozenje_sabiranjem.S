#program koji vrsi mnozenje putem sabiranja
#autor Dragoslav Tamindzija SV47

.section .data
.section .text
.globl main

main:
	movl $3, %eax
	movl $5, %ebx
	movl $0, %ecx #rez
	cmpl %eax, %ebx
	ja mnozenje_b
mnozenje_a:
	addl %eax, %ecx
	subl $1, %ebx
	je kraj
	jmp mnozenje_a
mnozenje_b:
	addl %ebx, %ecx
	subl $1, %eax
	je kraj
	jmp mnozenje_b
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
