class Song:

    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artists_count = {}
    artist_count = artists_count

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, value):
        cls.genres.add(value)

    @classmethod
    def add_to_artists(cls, value):
        cls.artists.add(value)

    @classmethod
    def add_to_genre_count(cls, value):
        cls.genre_count[value] = cls.genre_count.get(value, 0) + 1

    @classmethod
    def add_to_artists_count(cls, value):
        cls.artists_count[value] = cls.artists_count.get(value, 0) + 1
        if cls.artist_count is not cls.artists_count:
            cls.artist_count[value] = cls.artist_count.get(value, 0) + 1

    add_to_artist = add_to_artists

    def __repr__(self):
        return f"{self.name}: {self.artist}. {self.genre}"
