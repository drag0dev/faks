#autor Dragoslav Tamindzija
#ubacivanje stringa posle svake 3 reci
.section .data
upis_prompt: .ascii "Unesite string: "
upis_prompt_len = . - upis_prompt

rez_prompt: .ascii "Tekst sa ubacenim stringom: "
rez_prompt_len = . - rez_prompt

dodatni_str: .ascii "o00o \0"
dodatni_str_len = . - dodatni_str - 1 # ne treba nam null u ispisu 

ulazni_str: .fill 1001, 1, 0 # 1000 karaktera + null

novi_red: .fill 1,1,10

.section .text
.globl main
main:
	# poruka za upis stringa
	movl $4, %eax
	movl $1, %ebx
	movl $upis_prompt, %ecx
	movl $upis_prompt_len, %edx
	int $0x80

	# upis stringa
	movl $3, %eax
	movl $0, %ebx
	movl $ulazni_str, %ecx
	movl $1000, %edx
	int $0x80

	# ispis poruke za rezultat
	movl $4, %eax
	movl $1, %ebx
	movl $rez_prompt, %ecx
	movl $rez_prompt_len, %edx
	int $0x80

	xorl %esi, %esi # broj razmaka
	xorl %edi, %edi # edi broj karaktera za ispis dela unetog stringa
	movl $ulazni_str, %ecx # ecx pokazivac na uneti string

petlja:
	cmpb $10, (%ecx)
	jz ispis
	cmpb $0, (%ecx)
	jz ispis

	addl $1, %edi
	addl $1, %ecx
	cmpb $' ', -1(%ecx)
	jnz petlja
	addl $1, %esi
	cmpl $3, %esi
	jz ispis
	jmp petlja
	
ispis:
	push %ecx # cuva se adresa gde se stalo
	subl %edi, %ecx # vracamo na pocetak dela

ispis_dela:
	# ispis dela unetog stringa
	movl $4, %eax
	movl $1, %ebx
	movl %edi, %edx
	int $0x80

ispis_dodatnog:
	cmpl $3, %esi
	jnz kraj_ispisa
	# ispis stringa koji se dodaje
	movl $4, %eax
	movl $1, %ebx
	movl $dodatni_str, %ecx
	movl $dodatni_str_len, %edx
	int $0x80

kraj_ispisa:
	popl %ecx # vraca se adresa gde se stalo
	xorl %edi, %edi
	xorl %esi, %esi
	cmpb $0, (%ecx)
	jz kraj
	cmpb $10, (%ecx)
	jz kraj
	jmp petlja
kraj:
	# ispis \n na kraju
	movl $4, %eax
	movl $1, %ebx
	movl $novi_red, %ecx
	movl $1, %edx
	int $0x80

	movl $1, %eax
	movl $0, %ebx
	int $0x80
