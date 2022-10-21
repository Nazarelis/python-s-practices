def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabraInvert = palabra [::-1]
    print(palabra)
    print(palabraInvert)
    if palabra == palabraInvert:
        return True
    else:
        return False
    
    
    

def recorrer():
    palabra = input("Escribe una palabra o frase: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")
        
recorrer()