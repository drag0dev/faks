#min i max niza
#autor: Dragoslav Tamindzija SV47 2021
.section .data
NELEM=10
niz: .long 14, 32, 5, 99, 91, 27, 66, 0, 8, 12
min_el: .long 0
max_el: .long 0
.section .text
.global main

main:
	movl $0, %esi #index
	movl niz, %eax #min
	movl niz, %ebx #max
petlja:
	movl niz(,%esi,4), %ecx
min: #proveravamo da li je elementi iz niza novi min
	cmpl %ecx, %eax
	jc max
	movl %ecx, %eax
max: #-||- max
	cmpl %ecx, %ebx
	jnc provera
	movl %ecx, %ebx
provera: #povecavamo index i proveravamo da li je kraj
	incl %esi
	cmpl $NELEM, %esi
	jne petlja
kraj:
	movl %eax, min_el
	movl %ebx, max_el
	movl $1, %eax
	movl $0, %ebx
	int $0x80
