import sys
from PIL import Image

obrazek_sciezka = input("Podaj sciezke: ")
obrazek = Image.open(obrazek_sciezka)

szerokosc, wysokosc = obrazek.size
proporcje = wysokosc/szerokosc
szerokosc = 120
wysokosc = szerokosc*proporcje*0.55
obrazek = obrazek.resize((szerokosc, int(wysokosc)))

obrazek = obrazek.convert("L")

piksele = obrazek.getdata()

#znaczki = ['@', 'G', 'K', 'M', 'I', 'L', '?', '/', '!', ':', '.']
znaczki = ['.', ':', '!', '/', '?', 'L', 'I', 'M', 'K', 'G', '@']
#znaczki = ["B","S","#","&","@","$","%","*","!",":","."]
ciag_znaczkow = [znaczki[x//25] for x in piksele]
ciag_znaczkow = ''.join(ciag_znaczkow)


dl = len(ciag_znaczkow)
obrazek_ascii = [ciag_znaczkow[y:y+szerokosc] for y in range(0,dl,szerokosc)]
obrazek_ascii = '\n'.join(obrazek_ascii)
print(obrazek_ascii)

with open('wynik.txt', 'w') as wynik:
    wynik.write(obrazek_ascii)
