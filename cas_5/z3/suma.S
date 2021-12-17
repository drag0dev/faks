#program koji racunu sumu dva niza quadova
#autor Dragoslav Tamindzija SV47/2021
#int saberi_niz(long long *a, long long *b, long long *c, int n);

.section .text
.globl saberi_niz
saberi_niz:
	pushl %ebp
	movl %esp, %ebp

	pushl %ebx #cuvamo ebx
	pushl %edi #cuvamo edi

	movl 8(%ebp), %eax #eax baza niza a
	movl 12(%ebp), %ebx #ebx baza niza b
	movl 16(%ebp), %ecx #ecx baza niza c
	movl 20(%ebp), %edx #n odnosno brojac
	#edi ce se koristi kao pomocna

petlja:
	cmpl $0, %edx #provera da li smo prosli kroz n elem
	je izlaz_bez_greske

	#sabiranje nizi deo
	movl (%eax), %edi #nizi deo a u edi
	movl %edi, (%ecx) #nizi deo a u nizi deo c
	movl (%ebx), %edi #nizi deo b u edi
	addl %edi, (%ecx) #sabiraju se nizi delovi a i b i stavljaju u nizi deo c

	#sabiranje viseg dela kao nizi samo se gleda i carry
	movl 4(%eax), %edi
	movl %edi, 4(%ecx)
	movl 4(%ebx), %edi
	adcl %edi, 4(%ecx)
	jo izlaz_greska #jo jer je long signed

	addl $8, %eax
	addl $8, %ebx
	addl $8, %ecx
	subl $1, %edx
	jmp petlja

izlaz_bez_greske:
	movl $0, %eax
	jmp kraj

izlaz_greska:
	movl $1, %eax

kraj:
	popl %edi
	popl %ebx
	movl %ebp, %esp
	popl %ebp
	ret
