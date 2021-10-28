#program koji racuna formulu a=2*b+c/3 sa duplom preciznoscu
#autor: Dragoslav Tamindzija SV47 2021
.section .data
a: .quad 0
b: .quad 0xAFF0000
c: .quad 0xAFF0000
brojac: .byte 0
greska: .byte 0
.section .text
.global main
main:
	movl b, %eax
	movl b+4, %ebx
	movl c, %ecx
	movl c+4, %edx
mnozenje:
	addl %eax,a
	adcl %ebx,a+4
	addl $1, brojac
	jc greska_izlaz
	cmpl $2, brojac
	jnz mnozenje

	#ako smo pomnozili, resetujemo brojac i proveravamo deljenje
	movl $0, brojac
	cmpl $3, %ecx
	jge deljenje
	cmpl $0, %edx
	jg deljenje
	jmp kraj #ako je c < 3 skacemo na kraj
deljenje:
	addl $1, a
	adcl $0, a+4
	jc greska_izlaz
	subl $3, %ecx
	sbbl $0, %edx
	cmpl $3, %ecx
	jge deljenje
	cmpl $0, %edx
	jg deljenje
	jmp kraj
greska_izlaz:
	movl $1, greska
	jmp kraj

kraj:
	movl $1, %eax
	int $0x80
