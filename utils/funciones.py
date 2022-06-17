from os import system

class Matematicas():

    def limpiaPantalla(self):
        system("clear")

    def creaMenu(self):
        return ["1. Numero primo.", "2. Factorial.", "3. Palindrome.", "4. Salir."]

    def numeroPrimo(self, numero):
        print("Numero Primo")
    
    def factorial(self):
        print("Factorial")

    def palindrome(self):
        print("Palindrome")
    
    def salir(self):
        print("Salir")