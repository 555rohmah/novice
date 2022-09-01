try:
    import psycopg2
    conn = psycopg2.connect(
            host="localhost",
            database="contoh",
            user="postgres",
            password="postgres")

    curs = conn.cursor()

    namaLama = "hana"
    namaBaru = "hani"
    umurBaru = 10
    query = f"update siswa set nama='{namaBaru} ', umur={umurBaru} where nama='{namaLama}' "
    
    curs.execute(query)
    conn.commit()
    print("data berhasil diupdate")
except Exception as e:
    print(e)