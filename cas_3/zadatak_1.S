#program koji sabira elemente podniza
#autor: Dragoslav Tamindzija SV47 2021
.section .data
NELEM=10
niz: .long 1,2,3,4,5,6,7,8,9,10
suma: .long 0
index_pocetak: .long 2
index_kraj: .long 6
.section .text
.global main

main:
	movl index_pocetak, %esi #index
	movl $0, %eax #suma
petlja:
	cmpl %esi, index_kraj
	je kraj
	addl niz(, %esi, 4), %eax
	incl %esi
	cmpl $NELEM, %esi
	jl petlja
kraj:
	movl %eax, suma
	movl $1, %eax
	movl $0, %ebx
	int $0x80
