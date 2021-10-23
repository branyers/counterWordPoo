from collections import Counter


class CounterWord:

    def __init__(self, nameFile, limite):
        self.nameFile = nameFile
        self.limite = limite

    def frecuencywordonfile(self):
        try:
            file = open(f"{self.nameFile}.txt")
            for word in file:
                palabras = word.split()
                return Counter(palabras).most_common(self.limite)

        except FileNotFoundError:
            print("El archivo no fue encontrado")


class SonCounter(CounterWord):
    def __init__(self,nameFile,limite):
        CounterWord.__init__(self, nameFile, limite)




sonCounter = SonCounter("holaMundo",5)
print(sonCounter.frecuencywordonfile())
