from  pytube import YouTube

#DIGITE O LINK E O LOCAL NA QUAL DESEJA SALVAR O VIDEO#
link = input('Digite o link do video que deseja baixar: ')
path = input('Digite onde voce  deseja salvar o video: ')
yt = YouTube(link)

#MOSTRA OS DETALHES DO VIDEO#
print("Titulo ", yt.title)
print("Numero de views: ", yt.views)
print("Tamanho do video: ", yt.length," segundos")
print("Avaliação do video: ",yt.rating)

#USA A MAIOR RESOLUÇAO#
ys= yt.streams.get_highest_resolution()

#COMEÇA O DOWNLOAD DO VIDEO#
print('Baixando....')
ys.download(path)
print("Download completo")