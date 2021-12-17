#potprogram koji generise bit masku
#autor: Dragoslav Tamindzija SV47/2021
#unsigned int maska(unsigned int n, unsigned int v);
.section .text
.globl maska
maska:
	pushl %ebp
	movl %esp, %ebp

	movl 8(%ebp), %eax #eax = n
	movl 12(%ebp), %edx #edx = v
	movl $1, %ecx # ecx je maska

	cmpl $1, %edx #zastita unosa
	ja kraj_greska

	cmpl $31, %eax #zastita unosa
	ja kraj_greska

petlja: #pomeramo jedinicu u maski na n-to mesto
	cmpl $0, %eax
	je provera_maske

	shll $1, %ecx
	decl %eax
	jmp petlja

provera_maske: #proverava se da li je potrebno negirati masku
	cmpl $0, %edx #ako je v=0 onda se negira
	je neg_maske

	movl %ecx, %eax
	jmp kraj

neg_maske:
	notl %ecx
	movl %ecx,%eax
	jmp kraj

kraj_greska:
	movl $0, %eax
kraj:
	movl %ebp, %esp
	popl %ebp
	ret
