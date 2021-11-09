godina = -1
while godina <= 0:
    godina = eval(input("Unesite godinu: "))
if (godina%4==0 and godina%100!=0) or godina%400==0:
    print("Godina %d. je prestupna."% godina)
else:
    print("Godina %d. nije prestupna. " % godina)