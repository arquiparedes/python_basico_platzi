def run():
    word = input("Introduzca un Palindromo: ")
    palindrome = word.lower()
    palindrome = palindrome.replace(" " , "")
    reverse_palindrome = palindrome[::-1]

    if palindrome == reverse_palindrome:
        print("Su busqueda: " + word + ", sí es un palíndromo")
    else:
        print("Su busqueda: " + word + ", no es un palíndromo")


if __name__ == "__main__":
    run()