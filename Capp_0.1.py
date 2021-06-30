from bs4 import BeautifulSoup
import requests

def separar(string):
    string = string.split("</")
    string = str(string[0])
    string = string[5:]
    return string

def string_to_float(string):
    string = string.split(',')
    string = string[0] + '.' + string[1]
    string = float(string)
    return string

banco_de_dados = [['a',0,0],['a',0,0],['a',0,0],['a',0,0],['a',0,0],['a',0,0],['a',0,0],['a',0,0],['a',0,0]]
html = requests.get("https://www.infomoney.com.br/ferramentas/cambio/").content
soup = BeautifulSoup(html, 'html.parser')
body = soup.find('tbody')
bloco = body.findAll('tr')

for item in range(len(bloco)):
    texto = bloco[item]
    funil = texto.findAll('td')

    nome = str([funil[0]])
    nome = separar(nome)
    banco_de_dados[item][0] = nome

    preco_compra = str([funil[2]])
    preco_compra = separar(preco_compra)
    preco_compra = string_to_float(preco_compra)
    banco_de_dados[item][1] = preco_compra

    preco_venda = str([funil[3]])
    preco_venda = separar(preco_venda)
    preco_venda = string_to_float(preco_venda)
    banco_de_dados[item][2] = preco_venda

opcao = input("        | BEM VINDO AO CAPP |\n          | O QUE DESEJA? |\n             1 - Cotação\n             2 - Conversor\n             ")

if(opcao=='1'):
    opcao = input('                             1- Tabela inteira\n                             2- Moeda Especifica\n                             ')
    if(opcao=='1'):
        print('\n \n \n \n')
        for item in range(len(banco_de_dados)):
            print('\n\n-' + banco_de_dados[item][0].upper() +'-')
            print('\n Preço de compra: ' + str(banco_de_dados[item][1]))
            print('\n Preço de venda: ' + str(banco_de_dados[item][2]))

    elif(opcao=='2'):
        print('\n \n \n \n')
        opcao = input('        QUAL MOEDA GOSTARIA DE CONSULTAR?\n\n 1 - Peso Argentino\n 2 - Dólar Australiano\n 3 - Dólar Canadense\n 4 - Franco Suíço\n 5 - Dólar Comercial\n 6 - Dólar Turismo\n 7 - Euro\n 8 - Libra Esterlina\n 9 - Iene\n')
        if (opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5' and opcao != '6' and opcao != '7' and opcao != '8' and opcao != '9'):
            print('OPERAÇÃO INVÁLIDA')
        else:
            opcao = int(opcao)-1
            print('\n\n-' + banco_de_dados[opcao][0].upper() + '-')
            print('\n Preço de compra: ' + str(banco_de_dados[opcao][1]))
            print('\n Preço de venda: ' + str(banco_de_dados[opcao][2]))

    else:
        print('\n \n \n \n')
        print('OPERAÇÃO INVÁLIDA')

elif(opcao=='2'):
    print('\n \n \n \n')
    opcao = input('        QUAL MOEDA GOSTARIA DE CONVERTER?\n\n 1 - Peso Argentino\n 2 - Dólar Australiano\n 3 - Dólar Canadense\n 4 - Franco Suíço\n 5 - Dólar Comercial\n 6 - Dólar Turismo\n 7 - Euro\n 8 - Libra Esterlina\n 9 - Iene\n')
    if (opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5' and opcao != '6' and opcao != '7' and opcao != '8' and opcao != '9'):
        print('OPERAÇÃO INVÁLIDA')
    else:
        moeda = int(opcao) - 1
        opcao = input('        1 - Valor de compra\n        2 - Valor de venda\n        ')

        if(opcao!='1' and opcao!='2'):
            print('OPERAÇÃO INVÁLIDA')
        else:
            if (opcao == '1'):
                preco = banco_de_dados[moeda][1]
            elif (opcao == '2'):
                preco = banco_de_dados[moeda][2]
            opcao = input('                             1- Conversão ' + banco_de_dados[moeda][0] + ' - Real\n                             2- Conversão Real - '+ banco_de_dados[moeda][0]+'\n                             ')

            if(opcao=='1'):
                print('\n \n \n \n')
                moeda = input('QUANTO GOSTARIA DE CONVERTER PARA O REAL? \n')
                print('\nR$ ' + str(float(moeda)*preco))

            elif(opcao=='2'):
                print('\n \n \n \n')
                moeda = input('QUANTO GOSTARIA DE CONVERTER DE REAL PARA ' + banco_de_dados[moeda][0].upper() + '?\n')
                print('\nVocê terá: ' + str(float(moeda) / preco))

            else:
                print('OPERAÇÃO INVÁLIDA')
else:
    print('OPERAÇÃO INVÁLIDA')










