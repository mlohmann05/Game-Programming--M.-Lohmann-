# AUFGABE 1: Schleife
# Startwert und Endwert
start = 437
end = 32482

# Variable für Summe
summe = 0

# Die Schleife
for zahl in range(start, end + 1):
    summe += zahl #Summe der Zahlen

# Ausgabe der Summe
print("Summe:", summe)


# AUFGABE 2: Funktion
def klein_durch_groß(a, b):
    if a == b: #Wenn a und b gleich sind
        return 1
    elif a < b: #Wenn a kleiner als b ist
        return a / b
    else: #Wenn a größer als b ist
        return b / a


# Test der Funktion
print(klein_durch_groß(4, 8)) #0.5
print(klein_durch_groß(10, 2)) #0.2
print(klein_durch_groß(5, 5)) #1