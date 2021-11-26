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

spoljasnja_petlja: #prolazimo kroz izvorni i ciljni

	movl 16(%ebp), %ecx
	addl $1, %eax
	addl $1, %ebx

	cmpb $0, (%eax)
	je kraj

unutrasnja_petlja: #prolazimo kroz str enkodovati
	movb (%eax), %dl
	cmpb %dl, (%ecx)
	je promena

	addl $1, %ecx
	cmpb $0, (%ecx)
	je spoljasnja_petlja
	jmp unutrasnja_petlja
promena:
	incl %esi
	movb (%ebx), %dl
	movb %dl, (%ecx) #zamenjujemo ciljni u enkodovati
	addl $1, %ecx
	cmpb $0, (%ecx)
	je spoljasnja_petlja
	jmp unutrasnja_petlja

kraj:
	movl %esi, %eax
	popl %esi
	popl %ebx
	movl %ebp, %esp
	popl %ebp
	ret
