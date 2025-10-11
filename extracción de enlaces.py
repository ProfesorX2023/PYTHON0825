from pytube import Playlist

# URL de tu playlist
url = "https://www.youtube.com/playlist?list=PLrvCjcrXXKGYa7az6vx6bsuuhhelwNTji"

# Crear objeto Playlist
playlist = Playlist(url)


# Extraer enlaces de cada video
for video_url in playlist.video_urls:
    print(video_url)
