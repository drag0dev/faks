#program koji racuna nzd samo se koriste promenljive
#autor: Dragoslav Tamindzija SV47

.section .data
a: .long 8
b: .long 12
rez: .long -1
.section .text
.global main

main:
	movl a, %eax
petlja:
	cmpl %eax, b
	je kraj
	cmpl %eax, b
	ja vece
	subl b, %eax
	jmp petlja
vece:
	subl %eax, b
	jmp petlja
kraj:
	movl %eax, a
	movl %eax, rez
	movl $1, %eax
	int $0x80
