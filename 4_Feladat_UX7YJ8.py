#4. Feladat: Pig Latin fordító

#Függvény
def pigLatinForm(text):             #Definiálunk egy függvényt
    pigText = ""                    #Létrehozunk egy segédstringet, ami később az output lesz
    text = text.lower()             #Kisbetűssé tesszük az egész szöveget, hogy ne legyenek benne össze-vissza nagybetűk (első karakterek)
    splitText = text.split(" ")     #Szóközönként felbontjuk a szöveget (szavak listájára)
    for i in splitText:             #Bejárjuk a szöveg szavainak listáját
        for j in range(1, len(i)):  #Az 1. betű kivételével végigmegyünk a szó elemein
            pigText += i[j]         #A segédstringet bővítjük a szavak betűivel (az első betű kivételével)
        pigText += i[0]             #Hozzáadjuk az eredeti 1. betűt minden szóból szavanként
        pigText += "ay"             #Hozzáadjuk az "ay" szócskát minden szóhoz
        pigText += " "              #Elválasztjuk szóközzel a szavakat
    return pigText.capitalize()     #A kapitalizált fordított szöveggel térünk vissza
#MAIN
def main():
    #print(pigLatinForm("The quick brown fox"))
    text = input("Írja be a fordítani kívánt szöveget: ")   #Bekérünk a felhasználótól egy szöveget
    print(pigLatinForm(text))  #Kiiratjuk a lefordított szöveget
main()