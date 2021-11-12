#program koji racunu sumu dva niza quadova
#autor Dragoslav Tamindzija SV47/2021
#int saberi_niz(long long *a, long long *b, long long *c, int n);

.section .text
.globl suma
suma:
	pushl %ebp
	movl %esp, %ebp

	pushl %ebx #cuvamo ebx
	pushl %edi #cuvamo edi

	movl 8(%ebp), %eax #eax niz a
	movl 12(%ebp), %ebx #ebx niz b
	movl 16(%ebp), %ecx #ecx niz c
	#edx pomocni

petalja:

	#place holder - ne uradjen zadatak
kraj:
	popl %edi
	popl %ebx
	movl %ebp, %esp
	popl %ebp
	ret
