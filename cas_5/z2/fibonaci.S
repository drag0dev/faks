#potprogram fibonaci preko rekurzije
#autor Dragoslav Tamindzija SV47/2021
#unsigned int fibonaci(int n, int *g);

.section .text
.globl fibonaci

fibonaci:
	pushl %ebp
	movl %esp, %ebp

	movl 8(%ebp), %eax #uzimamo proslenjedno n
	cmpl $1, %eax #ako je n==1 ili ==0 skacemo na kraj
	jle kraj

	cmpl $1, 12(%ebp) #da li je doslo do greske
	je kraj

	#ako nije 1 ili 0 onda racunamo fibonaci(n-1)+fibonaci(n-2)
	#fibonaci(n-1)
	subl $1, %eax
	pushl 12(%ebp)
	pushl %eax
	call fibonaci
	addl $8, %esp

	pushl %eax #stavljamo fibonaci(n-1) rez u stack

	cmpl $1, 12(%ebp) #da li je doslo do greske
	je kraj

	#fibonaci(n-2)
	movl 8(%ebp), %eax
	subl $2, %eax
	pushl 12(%ebx)
	pushl %eax
	call fibonaci
	addl $8, %esp

	popl %edx #skidamo rez od fibonaci(n-1) sa stacka
	addl %edx, %eax #fibonaci(n-1) + fibonaci(n-2)
	jnc kraj
greska:
	movl $1, 12(%ebp)
kraj:
	movl %ebp, %esp
	popl %ebp
	ret
