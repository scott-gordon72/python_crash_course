albums = []

while True:
    name = input("What is the artist's name: ")
    print("Type 'q' to quit.")
    if name == 'q':
        break
    title = input("What is the album's title: ")
    print("Type 'q' to quit.")
    if title == 'q':
        break

    def make_album(artist_name, album_title):
        album = {artist_name.title(): album_title.title()}
        albums.append(album)
        return albums

    album = make_album(name, title)
print(albums)
