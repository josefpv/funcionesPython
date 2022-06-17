from os import system
import math

class Matematicas():

    def limpiaPantalla(self):
        system("clear")

    def creaMenu(self):
        return ["1. Numero primo.", "2. Factorial.", "3. Palindrome.", "4. Salir."]

    def numeroPrimo(self, numero):
        
        divisores = 0
        for n in range(1, numero + 1):
            if numero % n == 0:
                divisores += 1

        if divisores > 2:
            return False
        
        return True
    
    def factorial(self, numero):
        return math.factorial(numero)

    def palindrome(self):
        print("Palindrome")
    
    def salir(self):
        print("Salir")