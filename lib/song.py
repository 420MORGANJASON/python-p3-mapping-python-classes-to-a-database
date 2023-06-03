# import sqlite3

# # from config import CONN, CURSOR
# from config import CURSOR
# from song import CURSOR

# # CONN = sqlite3.connect("db/music.db")
# # CURSOR = CONN.cursor()


# class Song:
#     # The __init__ method creates a new instance of the song class,
#     # a new Python object.

#     all = []
#     def __init__(self, name, album):
#         self.id = None
#         self.name = name
#         self.album = album

#     @classmethod
#     def create_table(self):
#         sql = """
#             CREATE TABLE IF NOT EXISTS songs (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT,
#                 album TEXT
#             )
#         """

#         CURSOR.execute(sql)

#     # The save() method takes the attributes that characterize
#     # a given song and saves them in a new row of the songs
#     # table in our database.

#     def save(self):
#         sql = """
#             INSERT INTO songs (name, album)
#             VALUES (?, ?)
#         """

#         CURSOR.execute(sql, (self.name, self.album))

#         self.id = CURSOR.execute("SELECT last_insert_row id() FROM songs").fetchone([0])

#     @classmethod
#     def create(cls, name, album):
#         song = Song(name, album)
#         song.save()
#         return song

#     @classmethod
#     def new_from_db(cls, row):
#         song = cls(row[1], row[2])
#         song.id = row[0]

#     @classmethod
#     def all(cls):
#         sql = """
#             SELECT *
#             FROM songs
#         """


#     all = CURSOR.execute(sql).fetchall()


#     @classmethod
#     def get_all(cls):
#         sql = """
#             SELECT *
#             FROM songs
#         """

#     all = CURSOR.execute(sql).fetchall()

#     cls.all = [cls.new_from_db(row) for row in all]
import sqlite3
from config import CURSOR


class Song:
    all = []  # List to store all song instances

    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.album))

        # Fetch the last inserted row id
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song

    @classmethod
    def new_from_db(cls, row):
        song = cls(row[1], row[2])
        song.id = row[0]
        return song

    @classmethod
    def all(cls):
        sql = """
            SELECT *
            FROM songs
        """
        all_songs = CURSOR.execute(sql).fetchall()
        cls.all = [cls.new_from_db(row) for row in all_songs]
        return cls.all
