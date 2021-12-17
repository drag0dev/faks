#unsigned int inter_to_oct_str(unsigned int broj, char* str, unsigned int duzina);
#autor: Dragoslav Tamindzija SV47/2021
.section .text
.globl inter_to_oct_str

inter_to_oct_str:
	pushl %ebp
	movl %esp, %ebp
	pushl %ebx

	movl 8(%ebp), %eax #eax ce biti broj
	movl 16(%ebp), %ecx #duzina buffera
	movl $8, %ebx #baza

	pushl $0 #\0 na stack
	decl %ecx #smanjimo duzina buffera za jedan zbog \0
	jz greska

petlja:
	test %ecx, %ecx #provera da li ima mesta u bufferu
	jz greska

	xorl %edx, %edx #edx = 0
	divl %ebx #abx/8

	addl $'0', %edx #na ostatak dodajemo 48
	pushl %edx #karakter se stavlja na stack 

	decl %ecx #umanjemo broj mesta

	testl %eax, %eax #provera da li smo dosli do kraja
	jz izlaz

	jmp petlja

izlaz: #popovanje sa stacka u string
	movl 12(%ebp), %ebx #ebx baza stringa
	movl 16(%ebp), %edx #duzina buffera
	subl %ecx, %edx #od duzine buffera oduzmemo koliko karaktera nije uneto
	movl $0, %eax #postavimo izlazni kod

ispis_u_string:
	popl (%ebx) #skidamo karakter sa stacka
	decl %edx #umanjemo broj karaktera koji treba da se skinu sa stacka
	jz kraj
	incl %ebx #pomeramo na sledeci karakter
	jmp ispis_u_string

greska: #u slucaju greske moraju se skinuti karakteri sa stacka
	movl 16(%ebp), %eax #eax je duzina buffera
	subl %ecx, %eax #eax sada drzi broj karaktera novog stringa

	movl $4, %ebx #mnozimo sa 4
	xorl %edx, %edx #edx na nulu
	mull %ebx # eax * ebx = broj bajtova koji treba da se skinu sa stacka

	addl %eax, %esp #sklanjaju se svi karakter sa stacka

	movl $1, %eax
kraj:
	popl %ebx
	movl %ebp, %esp
	popl %ebp
	ret
