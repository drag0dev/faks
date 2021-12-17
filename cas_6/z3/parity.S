#potprogram koji racuna parity bit
#autor Dragoslav Tamindzija SV47/2021
#int SetParity(unsigned short int* v);
.section .text
.globl SetParity
SetParity:
	pushl %ebp
	movl %esp, %ebp

	movl 8(%ebp), %eax #pok na broj
	movl (%eax), %eax #broj prebacujemo u eax
	movl $0, %ecx #brojac jedinica
	movl $0, %edx #brojac pri prolasku kroz broj

petlja: #prolaz kroz broj bit po bit
	cmpl $15, %edx
	je izlaz

	shrl %eax
	jc jedinica #ako je shitovan bit 1

povratak:
	incl %edx
	jmp petlja

jedinica:
	incl %ecx
	jmp povratak

izlaz:
	movl 8(%ebp), %eax
	andl $0x7FFF, (%eax) #postavlja se dafult 0 nula za parity u broju
	movl $0, %eax #0 je default povratna vrednost
	testl $1, %ecx #ako je broj jedinica neparan skacemo na kraj
	je kraj
	movl 8(%ebp), %eax
	orl $0x8000, (%eax) #bit parnosti se stavlja na 1
	movl $1, %eax
kraj:
	movl %ebp, %esp
	popl %ebp
	ret
