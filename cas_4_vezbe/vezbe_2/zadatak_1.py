# convert.py
# Konverzija temperature iz Celzijusa u Farenhajte
print("Program pretvara zadatu temperaturu u stepenima celzijusa u stepen farenhajta.")
celsius = eval(input("Unesite temperaturu u C >> "))
fahrenheit = 9/5 * celsius + 32
print("Temperatura je", fahrenheit, "stepeni Farenhajta.")
