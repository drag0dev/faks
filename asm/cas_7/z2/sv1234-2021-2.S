#autor: Dragoslav Tamindzija SV47/2021
#int encode(char* izvorni, char* ciljni, char* enkodovati);
.section .text
.globl encode

encode:
	pushl %ebp
	movl %esp, %ebp
	pushl %ebx #ebx se cuva na stacku
	pushl %esi

	movl $0, %esi

	movl 8(%ebp), %eax #eax je baza izvorni
	movl 12(%ebp), %ebx #ebx je baza ciljni
	movl 16(%ebp), %ecx #ecx je baza enkodovati
	#edx ce se koristi kao pomocna

	jmp unutrasnja_petlja

spoljasnja_petlja: #prolazimo kroz svaki karakter iz enkodovati

	addl $1, %ecx
	movl 8(%ebp), %eax
	movl 12(%ebp), %ebx

	cmpb $0, (%ecx)
	je kraj

unutrasnja_petlja: #prolazimo kroz izvorni i ciljni
	movb (%eax), %dl
	cmpb %dl, (%ecx)
	je promena
	addl $1, %eax
	addl $1, %ebx
	cmpb $0, (%eax)
	je spoljasnja_petlja
	jmp unutrasnja_petlja

promena: #ako se nadje slovo iz enkodovani u izvornom
	incl %esi
	movb (%ebx), %dl
	movb %dl, (%ecx) #zamenjujemo ciljni u enkodovati
	jmp spoljasnja_petlja

kraj:
	movl %esi, %eax
	popl %esi
	popl %ebx
	movl %ebp, %esp
	popl %ebp
	ret
