# import sqlite3

# from config import CONN, CURSOR
from config import CURSOR
from song import CURSOR

# CONN = sqlite3.connect("db/music.db")
# CURSOR = CONN.cursor()


class Song:
    # The __init__ method creates a new instance of the song class,
    # a new Python object.
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """

        CURSOR.execute(sql)

    # The save() method takes the attributes that characterize
    # a given song and saves them in a new row of the songs
    # table in our database.

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.album))

        self.id = CURSOR.execute("SELECT last_insert_row id() FROM songs").fetchone([0])

    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song
