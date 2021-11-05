.section .data
str_unos:   .ascii "Unesite string:\0"
str_unos_len = . -str_unos -1

str_ispis:  .ascii "\nObrnuti redosled:\n\0"
str_ispis_len = . -str_unos -1

broj_stringova = 10

matrica: .fill broj_stringova*20, 1, 42 #blok u memoriji u kome su stringovi
str_matrica_len = 20 #duzina po stringu zajedno sa \n

duzina_stringova: .fill broj_stringova,4,0 #niz koji cuva duzinu svakog unesenog stringa

poslednji_element_matrica= matrica + broj_stringova * str_matrica_len
poslednji_element_duzina= duzina_stringova + broj_stringova * 4
.section .text
.global main
main:
	leal matrica, %edi #edi baza za matricu
	leal duzina_stringova, %esi #baza za duzuni stringova
	movl $0, %ebp #brojac
petlja:
	cmpl $broj_stringova, %ebp #proveravamo da li smo uneli sve stringove
	je priprema

	#ispis poruke za unos
	movl $4, %eax
	movl $1, %ebx
	leal str_unos, %ecx
	movl $str_unos_len, %edx
	int $0x80

	#unos
	movl $3, %eax
	movl $0, %ebx
	movl %edi, %ecx #dajemo adresu matrice
	movl $str_matrica_len, %edx #uzimamo n karaktera zajedno sa \n
	int $0x80
	movl %eax, (%esi) #duzinu unesenog stringa pisemo u niz duzina

	addl $str_matrica_len, %edi #pomeramo na sledeci string u matrici
	addl $4, %esi #pomeramo na slededcu duzinu u nizu
	addl $1, %ebp #uvecavamo pokazivac
	jmp petlja

priprema:
	leal matrica, %edi
	movl $poslednji_element_matrica, %edi #edi ce imati adresu poslednjeg stringa

	leal duzina_stringova, %esi
	movl $poslednji_element_duzina, %esi #esi ce imati adresu poslednjeg elementa niza duzina

	movl $0, %ebp

	#ispis - obrnuti redosled
	movl $4, %eax
	movl $1, %ebx
	leal str_ispis, %ecx
	movl $str_matrica_len, %edx
	int $0x80

ispis:
	cmpl $broj_stringova, %ebp #proveravamo da li smo ispisali stringova
	jg kraj

	movl $4, %eax
	movl $1, %ebx
	movl %edi, %ecx #adresa zadnjeg el u nizu
	movl (%esi), %edx #vrednost koja govori duzinu stringa
	int $0x80

	addl $1, %ebp #uvecavamo brojac
	subl $str_matrica_len, %edi #idemo jedan string unazad u matrici
	subl $4, %esi #idemeo jedan el niza unazad
	jmp ispis
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
