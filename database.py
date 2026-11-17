import sqlite3

db = sqlite3.connect("music.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) ,
    artist VARCHAR(100) )
""")

cursor.execute("""INSERT INTO songs (name, artist) VALUES
    ("Janona", "Shahzoda"),
    ("Keragimsan", "Ulug'bek Rahmatullayev"),
    ("Qizg'aldog'im", "Yulduz Usmonova"),
    ("Yomg'ir", "Shohruhxon"),
    ("Sog'indim", "Sardor Rahimxon"),
    ("Hayot ayt", "Ozodbek Nazarbekov"),
    ("Aldamadim", "Ziyoda"),
    ("Xasta", "Konsta"),
    ("Million", "Jaloliddin Ahmadaliyev"),
    ("Layli", "Munisa Rizayeva"),
    ("Yurak", "Botir Qodirov")
""")
db.commit()