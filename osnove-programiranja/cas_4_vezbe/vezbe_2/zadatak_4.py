# convert.py
# Konverzija temperature iz Celzijusa u Farenhajte

print("Program pretvara prikazuje tabelu stepeni celzijusa u poredjenju sa stepenima farenhajta od 0 do 100 stepeni.")

celsius = 0

print("Celzijus\tFarenhajt")
for i in range(11):
    fahrenheit = 9/5 * celsius + 32
    print(celsius,"\t\t",fahrenheit)
    celsius = celsius + 10
