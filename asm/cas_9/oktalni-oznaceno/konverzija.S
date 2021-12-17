#potprogram za pretvaranje oznacenog oktalnog
#autor Dragoslav Tamindzija SV47/2021
#int oct_str_to_inter(char* str, unsigned int* greska);
.section .text
.globl oct_str_to_inter

oct_str_to_inter:
	pushl %ebp
	movl %esp, %ebp
	pushl %esi
	pushl %ebx	

	movl 12(%ebp), %edx
	movl $0, (%edx) #podesavanje greske na 0

	movl 8(%ebp), %esi # esi pok na str
	movl $0, %eax # eax rez
	movl $8, %ecx # ecx baza
	movl $0, %ebx

	cmpb $'+', (%esi)
	je znak
	cmpb $'-', (%esi)
	je znak
	jmp petlja

znak:
	addl $1, %esi

petlja:
	movb (%esi), %bl
	andb %bl, %bl
	jz izlaz

	cmpb $55, %bl #ako je broj manji od 0
	ja greska_karakter

	cmpb $48, %bl #ako je broj veci od 7
	jb greska_karakter	

	subb $'0', %bl
	movl $0, %edx
	mull %ecx
	jne greska

	addl %ebx, %eax
	jo greska
	addl $1, %esi
	jmp petlja 	

izlaz:
	cmpl %esi, 8(%ebp)
	jz grska

znak:
	cmpb $'-', (%esi)
	jnz kraj
	orl $0x8000, %eax #negativan broj
	jmp kraj

greska_karakter:
	movl 12(%ebp), %edx

greska_karakter:
	movl 12(%ebp), %edx
	movl $1, (%edx)
	jmp kraj

greska:
	movl 12(%ebp), %edx
	movl $2, (%edx)
kraj:
	popl %ebx
	popl %esi
	movl %ebp, %esp
	popl %ebp
	ret
