import openai
import requests
import os
from io import BytesIO
from PIL import Image
def gerarImagem(prompt):
    openai.api_key = os.getenv('sua key da Openai')
    response = openai.Image.create(
        prompt = prompt,
        n = 1,
        size = '1024x1024',
        response_format = 'url'
    )
    image_url = response["data"][0]["url"]
    image_data = requests.get(image_url).content
    #CONVERTER IMAGUEM PARA OBJETO PILLOW IMAGE #
    image = Image.open(BytesIO(image_data))
    #EXIBIR IMAGEM #
    image.show()
gerarImagem('escreva o quer quiser para que a IA gere')
