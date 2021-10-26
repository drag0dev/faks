.section .data
a: .quad 4
b: .quad 20
greska: .byte 0
.section .text
.global main

priprema:
	#proverava se da li je a veci od b
	movl a+4, %eax
	cmpl b+4, %eax
	je main #ako su jednaki skoci na main
	jc main #ako je b vece od a skoci na main
	movl a, %eax
	cmpl b, %eax
	jc main

	#dalje cemo zameniti vrednosti a i b
	movl a+4, %eax
	xchgl %eax,b+4
	movl %eax, a+4

	movl a, %eax
	xchg %eax, b
	movl %eax, a
main:
	movl $0, %eax
	movl $0, %ebx
	movl $0, %ecx
 	movl $0, %edx

	movl a, %eax #nizi deo a
	movl a+4, %ecx #visi deo a
petlja:
	#ebx donji deo rez, edx gornji deo
	addl b, %ebx
	adcl b+4, %edx
	jc greska_izlaz
	cmpl $0, %eax
	ja manji_deo
	je veci_deo
manji_deo:
	subl $1, %eax
	jmp petlja
veci_deo:
	cmpl $0, %ecx
	je kraj
	subl $1, %ecx
	je kraj
	jmp petlja
greska_izlaz:
	incb greska
	jmp kraj
kraj:
	movl $1, %eax
	int $0x80
