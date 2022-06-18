if __name__ == "__main__":
    string = input("Digite uma string para ser revertida: ")
    string = list(string)
    string_cpy = list(string)
    tam = len(string)
    for i in range(tam):
        string[i] = string_cpy[tam-(i+1)]
    string = ''.join(string)
    print(string)