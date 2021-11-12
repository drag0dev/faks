#fibonaci sa dvostrukom preciznoscu
#autor: Dragoslav Tamindzija SV4 2021
.section .data
greska: .byte 0
n: .quad 15
.section .text
.globl main
main:
	movl $1, %eax
	movl $0, %ebx
	movl $1, %ecx
	movl $0, %edx
	#za pomocni koristi se edi i esi
petlja:
	movl %ecx, %edi
	movl %edx, %esi
	addl %eax, %ecx
	adcl %ebx, %edx
	jc greska_izlaz
	movl %edi, %eax
	movl %esi, %ebx
	subl $1, n
	sbbl $0, n+4
	cmpl $0, n
	jnz petlja
	cmpl $0, n+4
	jnz petlja
	jmp kraj
greska_izlaz:
	movl $1, greska
kraj:
	movl $1,%eax
	int $0x80
