#sortiranje niza po abecedi
#autor: Dragoslav Tamindzija SV47 2021
.section .data
string: .ascii "ssfgeabbasss\0"
asc: .byte 0 #0 rastuce, 1 opadajuci
promena: .byte 0 #pomocna koja prati da li je bilo pomeranja
.section .text
.global main
main:
	movl $string, %eax #eax baza
	cmpb $0, string #provera da li je prazan string
	je kraj
petlja: #u petlji proveravamo da li je kraj i prebacujemo jedan el u registar
	incl %eax
	cmpb $0, (%eax)
	je provera_kraj
	movb -1(%eax), %bl
poredjenje: #proveravamo da li su dva elemnta < > ili =
	cmpb (%eax), %bl
	jc zamena_dsc #ako je slovo na visoj poziciji vece
	ja zamena_asc #ako je slovo na visoj poziciji manje
	jmp petlja
zamena_dsc: #zamena ako pravimo opadajuci
	cmpb $1, asc #proveravamo da li treba da se pravi opadajuci
	jne petlja
	xchgb %bl, (%eax) #zamena elemenata
	movb %bl, -1(%eax)
	movl $1, promena #nazancimo da je doslo do promene
	jmp petlja
zamena_asc: #zamena ako pravimo rastuci
	cmpb $0, asc #proveravamo da li treba da se pravi rastuci
	jne petlja
	xchgb %bl, (%eax) #zamena elemenata
	movb %bl, -1(%eax)
	movl $1, promena
	jmp petlja
provera_kraj: #gledamo da li je bilo promena pri zadnjem prolasku kroz string
	cmpl $0, promena
	je kraj
	movl $0, promena
	movl $string, %eax
	jmp petlja

kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
