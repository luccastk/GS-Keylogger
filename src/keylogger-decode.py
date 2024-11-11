def openFile():
    fileFiltred = []
    try:
        file = input(str("Digite o nome do arquivo (com a extesão): "))
    
        with open(file, 'r') as f:
            for line in f.readlines()[2:]:        
                for l in line.split(" "):
                    if l != "\n":
                        fileFiltred.append(l.strip()) 
        return fileFiltred
    
    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado!")
    except Exception as e:
        print(f'Ocorreu um erro {e}')

phone_number = {
    2 : ("a", "b", "c"),
    3 : ("d", "e", "f"),
    4 : ("g", "h", "i"),
    5 : ("j", "k", "l"),
    6 : ("m", "n", "o"),
    7 : ("p", "q", "r", "s"),
    8 : ("t", "u", "v"),
    9 : ("w", "x", "y"),
    0 : ("o", "p", "r")
}            

def dataFiltred():
    dict_of_numbers = dict()
    resposta = ""
    
    for index, number in enumerate(openFile()):
        dict_of_numbers[index] = number

    for key, value in dict_of_numbers.items():
        pressionado = (len(value) - 1) % len(value)
        tecla = int(dict_of_numbers[key][0])

        resposta += "{flag}".format(flag = phone_number[tecla][pressionado])
    
    print("fiap{" + resposta + "}")
    
    
if __name__ == "__main__":
    dataFiltred()