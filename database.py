import sqlite3

db = sqlite3.connect("music.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) ,
    artist VARCHAR(100),
    minut INTEGER,
    hajmi INTEGER
    )
""")

cursor.execute("""INSERT INTO songs (name, artist, minutes, hajmi) VALUES
    ("Janona", "Shahzoda", 4, 5),
    ("Keragimsan", "Ulug'bek Rahmatullayev", 5, 6),
    ("Keragimsan", "Ulug'bek Rahmatullayev", 5, 6),
    ("Qizg'aldog'im", "Yulduz Usmonova", 4, 5),
    ("Yomg'ir", "Shohruhxon", 5, 6),
    ("Sog'indim", "Sardor Rahimxon", 4, 5),
    ("Hayot ayt", "Ozodbek Nazarbekov", 5, 6),
    ("Aldamadim", "Ziyoda", 4, 5),
    ("Xasta", "Konsta", 5, 6),
    ("Million", "Jaloliddin Ahmadaliyev", 4, 5),
    ("Layli", "Munisa Rizayeva", 5, 6),
    ("Yurak", "Botir Qodirov", 4, 5)
""")
db.commit()