#izbacivanje razmaka sa kraja i pocetka
.section .data
string: .ascii "abcd   \0"
.section .text
.global main
main:
	movl $string, %eax #eax drzi adresa od strina
kraj_s: #petlja traiz \0 u stringu
	cmpb $0, (%eax)
	je razmak_kraj_s
	incl %eax
	jmp kraj_s
razmak_kraj_s: #petlja trazi zadnji ' '
	cmpb $' ', -1(%eax)
	jne izbaci
	decl %eax
	jmp razmak_kraj_s
izbaci: #stavlja \0 na mesto ' ' na kraju stringa
	movb $0, (%eax)
razmak_pocetak_s: #petlja proverava da li imamo ' ' na pocetku
	movl $string, %eax
	cmpb $' ', (%eax)
	jne kraj
brisanje_razmaka: #petlja koja ce pomeriti ceo string za jedan ulevo
	cmpb $0, (%eax) #ako smo dosli do \0 znaci da smo pomerili ceo string
	je razmak_pocetak_s
	movb 1(%eax), %dl #pomocna za zamenu
	movb %dl, (%eax)
	incl %eax
	jmp brisanje_razmaka
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
