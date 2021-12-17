#potprogram za pravljenje quad maske
#autor: Dragoslav Tamindzija SV47/2021
#unsigned long long maska64(unsigned int n, unsigned int v);
.section .text
.globl maska64
maska64:
	pushl %ebp
	movl %esp, %ebp
	pushl %ebx
	pushl %esi

	movl 8(%ebp), %eax #eax = n
	movl 12(%ebp), %edx #edx = v
	movl $1, %ecx #ecx je 32obitni deo maske
	movl $0, %ebx #ako je ebx = 0, ecx je nizi deo
	movl $0, %esi #pomocni default deo

	cmpl $63, %eax #zastita unosa
	ja kraj_greska

	cmpl $1, %edx #zastita unosa
	ja kraj_greska

petlja: #shiftuje jedinicu u ecx
	cmpl $0, %eax
	je izlaz
	shll $1, %ecx
	jc prelaz_visi_deo #ako predjemo prvih 32 bita
brojac:
	decl %eax
	jmp petlja

prelaz_visi_deo: #ebx=1 i restuje se ecx
	movl $1, %ebx #naznacimo da smo dosli u visi deo
	movl $1, %ecx #resetujemo masku na 0....1
	jmp brojac

izlaz: #proverava se da li se maska treba negirati
	cmpl $0, %edx #ako nije v=1
	je negiran_izlaz
	jmp visi_nizi_deo_izlaz
negiran_izlaz: #negiraju se visi i nizi deo bez obzira na ebx
	notl %esi
	notl %ecx
visi_nizi_deo_izlaz: #da li imamo 32 ili 64 bita povratnu vrednost
	cmpl $1, %ebx
	je izlaz_visi_deo #ako imamo visi deo
	movl %esi, %edx #ako nemamo visi deo, visi deo je default
	movl %ecx, %eax #nizi deo u eax
	jmp kraj
izlaz_visi_deo:
	movl %ecx, %edx #visi deo je u edx
	movl %esi, %eax #nizi deo je default
	jmp kraj

kraj_greska:
	movl $0, %edx #visi deo 0
	movl $0, %eax #nizi deo 0
kraj:
	popl %esi
	popl %ebx
	movl %ebp, %esp
	popl %ebp
	ret
