import database

while True:
    print("\n===== QO'SHIQLAR RO'YXATI =====")
    print("1. Qo'shiq qo'shish")
    print("2. Qo'shiqlarni ko'rish")
    print("3. Qo'shiq o'chirish")
    print("0. Chiqish")

    tanlov = input("Tanlang: ")

    if tanlov == "1":
        name = input("Qo'shiq nomi: ")
        artist = input("Ijodkor: ")

        database.cursor.execute(
            "INSERT INTO songs (name, artist) VALUES (?, ?)",
            (name, artist)
        )
        database.db.commit()

        print("Qo'shiq qo'shildi!")

    elif tanlov == "2":
        database.cursor.execute("SELECT * FROM songs")
        songs = database.cursor.fetchall()

        for song in songs:
            print(f"ID: {song[0]} | Nomi: {song[1]} | Ijodkor: {song[2]}")

    elif tanlov == "3":
        song_id = input("O'chirish uchun ID kiriting: ")

        if song_id.isdigit():
            database.cursor.execute(
                "DELETE FROM songs WHERE id = ?",
                (int(song_id),)
            )
            database.db.commit()

            # if database.cursor.rowcount:
            #     print("Qo'shiq o'chirildi!")
            # else:
            #     print("Bunday ID mavjud emas!")
        else:
            print("ID -> raqam bo'lishi kerak!")

    elif tanlov == "0":
        print("Dastur tugadi!")
        break

    else:
        print("Noto'g'ri tanlov!")

database.cursor.close()
database.db.close()