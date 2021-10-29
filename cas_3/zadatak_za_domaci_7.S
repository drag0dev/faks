#sabiranje dva niza u dvostrukoj preciznosti
#autor Dragoslav Tamindzija SV47 2021
.section .data
NELEM = 5
a: .quad 0xFFFFFFFFFFFFFFFF, 0xFFFFFFFFFF, 0xFFFFFFFF
b: .quad 0xFFFFFFFFF, 0xFFFFFFFFFF, 0xFFFFFFFF
c: .fill 5,8,0
greska: .byte 0
.section .text
.global main
main:
	movl $0, %ebp #visi deo pri sabiranju
	movl $0, %esi #index
	movl $a, %eax #baza za niz a
	movl $b, %ebx #baza za niz b
	movl $c, %ecx #baza za niz c
petlja:
	movl $0, %ebp

	#sabiranje nizeg dela
	movl (%eax), %edx #prebacujemo nizi deo a
	addl (%ebx), %edx #dodajmo nizi deo b na a
	adcl $0, %ebp #ako imam carry prebacimo ga u ebp
	movl %edx, (%ecx) #prebacujem sabrano u c

	#sabiranje viseg dela
	movl 4(%eax), %edx
	addl 4(%ebx), %edx
	jc izlaz_greska #ako imamo carry na visem delu nastaje greska
	addl %ebp, %edx #ako smo imali carry u nizem delu
	movl %edx, 4(%ecx)

	#proveravamo da li smo dosli do kraja
	cmpl $NELEM-1, %esi
	je kraj

	incl %esi
	addl $8, %eax
	addl $8, %ebx
	addl $8, %ecx
	jmp petlja
izlaz_greska:
	movl $1, greska
	jmp kraj
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
