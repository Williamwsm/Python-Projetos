from PIL import Image

# CARREGA A IMAGEM#
image_file = Image.open(r".\colorida.png")

#CONVERTE A IMAGEM PARA PRETO E BRANCO #
image_file = image_file.convert('L')

# SALVA A IMAGEM EM PRETO E BRANCO#
image_file.save(r".\preta-e-branca.png")