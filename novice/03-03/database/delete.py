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
    query = f"delete from siswa where nama='{nama}' "
    
    curs.execute(query)
    conn.commit()
    print("data berhasil dihapus")
except Exception as e:
    print(e)