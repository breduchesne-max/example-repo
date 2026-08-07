'''design a class called Album that contains
album_name - stores the name of the album
number_of_songs - stores the number of songs in the album
album_artist - stores the name of the artist
a __str__ method that returns a string that represents the Album objectin the following format:
(album_name, album_artist, number_of_songs)'''

class Album:
    def __init__(self, album_name, album_artist, number_of_songs):
        self.album_name = album_name
        self.album_artist = album_artist
        self.number_of_songs = number_of_songs

    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"

albums1 = [
  Album("Abbey Road", "The Beatles", 17),
  Album("Thriller", "Michael Jackson", 9),
  Album("Back in Black", "AC/DC", 10),
  Album("Rumours", "Fleetwood Mac", 11),
  Album("Hotel California", "Eagles", 12)
]

for album in albums1:
  print(album)

#print out the albums by by nymber of songs
print("\n=====Sorting Albums by Number of Songs=====")

albums1.sort(key=lambda x: x.number_of_songs)

for album in albums1:
  print(album)

#switch out pos 1 with pos 2 from albums1 and print out
print("\n=====Switching Albums=====")
albums1[1], albums1[2] = albums1[2], albums1[1]
for album in albums1:
  print(album)

#create a new list album2, print
print("\n=====Creating a New List of Albums=====")
albums2 = [
  Album('Blood on the Tracks', 'Bob Dylan', 11),
  Album('Purple Rain', 'Prince', 9),
  Album('London Calling', 'The Clash', 19),
  Album('Kid A', 'Radiohead', 10),
  Album('Read My Mind', 'Reba McEntire', 10)
]

for album in albums2:
  print(album)

#combine the two lists and print out the combined list
print("\n=====Combining the Two Lists of Albums=====")
albums2.extend(albums1)

for album in albums2:
  print(album)

# Add two Pink/Britney albums to albums2
print("\n=====Adding Two New Albums=====")
albums2.append(Album('Dark Side of the Moon', 'Pink Floyd', 9))
albums2.append(Album('Oops!... I Did It Again', 'Britney Spears', 12))

for album in albums2:
  print(album)

#sort albums alphabetically in albums2 by album name and print out the sorted list
print("\n=====Sorting Albums Alphabetically by Album Name=====")
albums2.sort(key=lambda x: x.album_name)
for album in albums2:
  print(album)


#search for the album "Dark side of the Moon" in albums2 and print out the index of the album in albums2 list
print("\n=====Searching for an Album=====")
def search_album(album_name, albums):
    for index, album in enumerate(albums):
        if album.album_name == album_name:
            return index
    return None

index = search_album("Dark Side of the Moon", albums2)
if index is not None:
    print(f"Album found at index: {index}")
else:
    print("Album not found")