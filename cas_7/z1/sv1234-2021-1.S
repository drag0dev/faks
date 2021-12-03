#autor: Dragoslav Tamindzija SV47/2021
#program enkodira uneti string cezarovim kodom
.section .data
prompt_1: .ascii "Unesite string: \0"
prompt_1_duzina = . - prompt_1
prompt_2: .ascii "Enkodovan string: \0"
prompt_2_duzina = . - prompt_2
str: .fill 51, 1, 0
.section .text
.globl main

main:
	#ispis prompt_1
	movl $4, %eax
	movl $1, %ebx
	movl $prompt_1, %ecx
	movl $prompt_1_duzina, %edx
	int $0x80

	#unos stringa
	movl $3, %eax
	movl $0, %ebx
	movl $str, %ecx
	movl $50, %edx
	int $0x80

	movl %eax, %esi #cuvamo koliko je slova uneseno u esi
	subl $1, %esi

	#ispis prompt_2
	movl $4, %eax
	movl $1, %ebx
	movl $prompt_2, %ecx
	movl $prompt_2_duzina, %edx
	int $0x80

	movl $1, %eax #eax ce biti broj
	movl $str, %ebx #ebx je baza unesenog stringa

veliko_slovo:
	cmpb $'A', (%ebx) #da li je slovo vece ili jedanko od A
	jnae malo_slovo

	cmpb $'Z', (%ebx) #da li je slovo manje ili jednako od Z
	jnbe malo_slovo

	subb $3, (%ebx) #ako je slovo veliko slovo pomeramo za tri unazad

	cmpb $'A', (%ebx) #proveravamo da li je dobijeni karakter jos uvek veliko slovo
	jnb petlja

	addb $26, (%ebx) #ako vise nije veliko slovo
	jmp petlja

malo_slovo:

	cmpb $'a', (%ebx) #da li je slovo vece ili jednako od a
	jnae petlja

	cmpb $'z', (%ebx) #da li je slovo manje ili jedanko od z
	jnbe petlja

	subb $3, (%ebx) #ako je slovo malo slovo pomeramo za tri unazad

	cmpb $'a', (%ebx) #provera da li je dobijen karakter jos uvek malo slovo
	jnb petlja

	addb $26, (%ebx) #ako nije malo slovo dodamo 26

petlja:
	cmpl %eax, %esi
	je ispis_novog_stringa
	incl %eax #uvecavamo brojac
	addl $1, %ebx #pomeramo na sledece slovo
	jmp veliko_slovo

ispis_novog_stringa:
	movl $4, %eax
	movl $1, %ebx
	movl $str, %ecx
	movl %esi, %edx #u esi se nalazi koliko je karaktera uneto
	int $0x80
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
