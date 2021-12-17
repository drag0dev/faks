#program koji vrsi mnozenje preko sabiranja
#autor: Dragoslav Tamindzija SV47 2021
.section .data
a: .quad 20
b: .quad 4
greska: .byte 0
.section .text
.globl main

main:
	#provera da li je a vece od b
	movl a+4, %eax
	cmpl b+4, %eax
	jc priprema #ako je visi deo b veci od viseg dela a idemo u main
	ja zamena # ako je b manje od a vrsi se zamena
	movl a, %eax
	cmpl b, %eax
	jc priprema #ako je b vece idemo u main
zamena:
	movl a+4, %eax
	xchgl %eax, b+4
	movl %eax, a+4

	movl a, %eax
	xchgl %eax, b
	movl %eax, a
priprema:
	movl a, %eax
	movl $0, %ebx
	movl a+4, %ebx
	movl $0, %ecx # nizi deo rez
	movl $0, %edx # visi deo rez
petlja:
	addl b, %ecx
	adcl b+4, %edx
	jc greska_izlaz
brojac:
	subl $1, %eax
	sbbl $0, %ebx
	ja petlja
	cmpl $0, %eax
	je kraj
	ja petlja
greska_izlaz:
	incb greska
	jmp kraj
kraj:
	movl $1, %eax
	int $0x80
