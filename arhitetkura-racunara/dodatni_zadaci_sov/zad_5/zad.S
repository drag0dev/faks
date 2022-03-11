# autor Dragoslav Tamindzija
# procenat ocena
.section .data
unos_str: .ascii "Unesi broj ocena "
unos_str_len = . - unos_str

dve_tacke: .ascii ": "
novi_red: .ascii "\n"
taraba: .ascii "#"
procenat: .ascii "%"
space: .ascii " "

izlaz_str: .ascii "Procenat ocena " 
izlaz_str_len= . - izlaz_str

ulazni_str: .fill 21, 1, 0 # 20 karaktera + null

niz_ocena: .fill 5, 4, 0 # 5 long ocena

greska_flag: .long 0
pomocni_string: .fill 21, 1, 0 # 20 karaktera + 0
pomocni_broj: .long 0

greska_str: .ascii "Greska kod operanda!\n"
greska_str_len = . - greska_str

ukupno_ocena: .long 0

.section .text
.globl main
.globl str_to_int
.globl int_to_str
.globl unos_ocene

# potprogram pretvara iz stringa u int
# broj, *izlazni_str, *broj_karaktera
#-----------------------------------------------
int_to_str:
	pushl %ebp
	movl %esp, %ebp
	pushl %ebx

	pushl $10 #baza
	movl 8(%ebp), %eax # broj
	xorl %ebx, %ebx
	movl 12(%ebp), %ecx # pok na izlazni string

int_to_str_petlja:
	xorl %edx, %edx
	divl -8(%ebp)

	addb $'0', %dl

	movb %dl, (%ecx)

	addl $1, %ecx
	addl $1, %ebx
	andl %eax, %eax
	jnz int_to_str_petlja

	subl $1, %ecx
	movl 12(%ebp), %eax	
	xorl %edx, %edx
	pushl %ebx

	cmpl %eax, %ecx
	jbe int_to_str_kraj
	
invert_str:
	movb (%eax), %dl
	movb (%ecx), %bl
	movb %dl, (%ecx)
	movb %bl, (%eax)
	addl $1, %eax
	subl $1, %ecx
	cmpl %eax, %ecx
	jbe int_to_str_kraj
	jmp invert_str

int_to_str_kraj:
	movl 16(%ebp), %eax
	popl (%eax)
	popl %eax

	popl %ebx
	movl %ebp, %esp
	popl %ebp
	ret
#-----------------------------------------------

# potprogram pretvara string u int
# *ulazni_str, *greska
#----------------------------------------------
str_to_int:
	pushl %ebp
	movl %esp, %ebp

	movl 12(%ebp), %eax
	movl $0, (%eax)

	xorl %eax, %eax
	movl $10, %ebx
	movl 8(%ebp), %ecx

str_to_int_petlja:
	xorl %edx, %edx
	mull %ebx

	cmpl $0, %edx
	jnz greska

	xorl %edx, %edx
	movb (%ecx), %dl

	cmpb $'0', %dl
	jb greska

	cmpb $'9', %dl
	ja greska

	subb $'0', %dl

	addl %edx, %eax
	jc greska

	addl $1, %ecx

	cmpb $0, (%ecx)
	jz str_to_int_kraj
	cmpb $10, (%ecx)
	jz str_to_int_kraj
	jmp str_to_int_petlja 

greska:
	movl 12(%ebp), %eax
	movl $1, (%eax)

str_to_int_kraj:
	movl %ebp, %esp
	popl %ebp
	ret
#-----------------------------------------------

main:
	movl $niz_ocena, %esi # esi je pokazivac na niz ocena
	movl $6, %edi # ocena

petlja_upis:
	pushl $pomocni_broj
	pushl $pomocni_string
	pushl %edi
	call int_to_str
	addl $12, %esp

	# ispis poruke za upis
	movl $4, %eax
	movl $1, %ebx
	movl $unos_str, %ecx
	movl $unos_str_len, %edx
	int $0x80

	# ispis ocene
	movl $4, %eax
	movl $1, %ebx
	movl $pomocni_string, %ecx
	movl pomocni_broj, %edx	
	int $0x80

	# ispis dve tacke
	movl $4, %eax
	movl $1, %ebx
	movl $dve_tacke, %ecx
	movl $2, %edx
	int $0x80

	# unos ocene
	movl $3, %eax
	movl $0, %ebx
	movl $pomocni_string, %ecx
	movl $20, %edx
	int $0x80

	movl $pomocni_string, %eax
	cmpb $10, (%eax)
	jz greska_operand

	pushl $greska_flag
	pushl $pomocni_string
	call str_to_int
	addl $8, %esp

	cmpl $0, greska_flag	
	jnz greska_operand

	movl %eax, (%esi)
	addl $4, %esi
	addl $1, %edi
	cmpl $11, %edi
	jb petlja_upis

	
	movl $niz_ocena, %esi
	movl $0, %eax
sabiranje_broja_ocena:
	movl (%esi), %edi
	addl %edi, ukupno_ocena
	addl $1, %eax
	addl $4, %esi
	cmpl $5, %eax
	jnz sabiranje_broja_ocena

	movl $niz_ocena, %esi # esi pok na niz ocena
	movl $6, %edi # broj ocene

ispis_procenata:
	cmpl $11, %edi
	jz kraj
	movl $100, %ebx
	movl (%esi), %eax
	addl $4, %esi
	mull %ebx # broj * 100
	
	xorl %edx, %edx
	movl ukupno_ocena, %ecx # edx ukupan broj ocena
	divl %ecx # broj*100 / ukupan_broj_ocena

	pushl %eax

	# ispis izlazne poruke
	movl $4, %eax
	movl $1, %ebx
	movl $izlaz_str, %ecx
	movl $izlaz_str_len, %edx
	int $0x80

	# pretvaranje ocene u str
	pushl $pomocni_broj
	pushl $pomocni_string
	pushl %edi
	call int_to_str
	add $12, %esp

	# ispis ocene
	movl $4, %eax
	movl $1, %ebx
	movl $pomocni_string, %ecx
	movl pomocni_broj, %edx
	int $0x80

	# ispis dve tacke
	movl $4, %eax
	movl $1, %ebx
	movl $dve_tacke, %ecx
	movl $2, %edx
	int $0x80

	popl %ebx
	pushl $pomocni_broj
	pushl $pomocni_string
	pushl %ebx
	call int_to_str
	add $12, %esp

	pushl %ebx

	# ispis procenta
	movl $4, %eax
	movl $1, %ebx
	movl $pomocni_string, %ecx
	movl pomocni_broj, %edx
	int $0x80

	# ispis %
	movl $4, %eax
	movl $1, %ebx
	movl $procenat, %ecx
	movl $1, %edx
	int $0x80

	addl $1, %edi

	# ispis razmaka
	movl $4, %eax
	movl $1, %ebx
	movl $space, %ecx
	movl $1, %edx
	int $0x80

	popl %eax
	cmpl $10, %eax
	jb novi_red_ispis

ispis_taraba:
	pushl %eax
	# ispis tarabe
	movl $4, %eax
	movl $1, %ebx
	movl $taraba, %ecx
	movl $1, %edx
	int $0x80

	popl %eax
	subl $10, %eax
	cmpl $10, %eax
	jge ispis_taraba

novi_red_ispis:
	#ispis \n
	movl $4, %eax
	movl $1, %ebx
	movl $novi_red, %ecx
	movl $1, %edx
	int $0x80
	jmp ispis_procenata
	
greska_operand:
	# ispis poruke za gresku
	movl $4, %eax
	movl $1, %ebx
	movl $greska_str, %ecx
	movl $greska_str_len, %edx	
	int $0x80

kraj:
	movl $1, %eax
	int $0x80
