# try:
import psycopg2
conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="postgres")

# except Exception as e:
#     print(e)

curs = conn.cursor()
query = f"select * from siswa where nama='rohmah'"
curs.execute(query)
data = curs.fetchone()

print("nama:", data[0], "umur:", data[1])