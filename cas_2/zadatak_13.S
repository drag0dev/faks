#program vrsi deljenje pomocu oduzimanja u dvostrukoj prezicnosti
#autor: Dragoslav Tamindzija SV24 2021
.section .data
a: .quad 16
b: .quad 3
rez: .long 0
greska: .byte 0
.section .text
.globl main

main:
	movl $0, %eax
	movl $0, %ebx
	movl $0, %ecx
	movl $0, %edx
	movl a, %eax
	movl a+4, %ebx
	movl b, %ecx
	movl b+4, %edx
priprema: #provera da li je a >= b
	cmpl %edx, %ebx
	jl kraj
	cmpl %ecx, %eax
	jl kraj
petlja:
	subl %ecx, %eax
	sbbl %edx, %ebx
	jc izlaz_greska
	addl $1, rez

provera_deljivosti:
	cmpl %edx, %ebx
	jl kraj
	cmpl %ecx, %eax
	jl kraj
	jmp petlja
izlaz_greska:
	movl $1, greska
	jmp kraj
kraj:
	movl $1, %eax
	int $0x80
