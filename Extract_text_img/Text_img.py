from os import  read
import easyocr

#DEFINE O IDIOMA A SER USADO #
reader = easyocr.Reader(['pt'])

#CARREGA E FAZ A LEITURA DA IMAGEM #
results = reader.readtext('exemplo.png', paragraph=False)

print("\n\n")
#MOSTRA RESULTADOS #

for result in results:
    print(f'Texto: {result[1]}\n'
          f'Posição : {result[0]}\n')
