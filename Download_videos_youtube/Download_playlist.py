from pytube import Playlist

playlist = Playlist(input("Informe o link da playlist que vc deseja baixar:"))
path = input('Destino do download: ')

print(f'Iniciando o download dos videos da playlist: {playlist.title}\n')

for indece, video in enumerate(playlist.videos):
    print(f'Baixando video{indece +1}{len(playlist)}')
    video.streams.first().download(path)

print('Todos ps videos foram baixados ')