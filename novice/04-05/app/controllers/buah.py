import psycopg2
from flask import request, render_template, redirect

def index():
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="postgres")
    curs = conn.cursor()
    if request.method == "POST":
        nama = request.form.get("nama")
        detail = request.form.get("detail")
        query = f"insert into buah(nama, detail) values('{nama}', '{detail}')"
        curs.execute(query)
        conn.commit()

    print(request.method) 
    query = f"select * from buah" 
    curs.execute(query)
    data = curs.fetchall() 
    # data = ["apel", "pear", "anggur"] 
    #     print(20*"=")
    #     print(nama)
    #     print(detail)
    #     print(20*"=")
    # print(request.method)
    # print(20*"=")
    # print(request.form)
    # print(request.form.get("nama"))
    # print(request.form.get("detail"))
    # print(20*"=")
    # data = ["aku", "kamu", "dia"]
    return render_template("index.html", context=data)

def delete(buah_id):
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="postgres")
    curs = conn.cursor()
    query = f"delete from buah where id = {buah_id}"
    curs.execute(query)
    conn.commit()
    curs.close()
    conn.close()
    return redirect("/")

def update(buah_id):
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="postgres")

    curs = conn.cursor()
    if request.method == "POST":
       nama = request.form.get("nama")
       detail = request.form.get("detail")
       query = f"update buah set nama ='{nama}', detail = '{detail}' where id = {buah_id}"
       curs.execute(query)
       conn.commit()
       return redirect("/")

    query = f"select * from buah where id = {buah_id}"
    curs.execute(query)
    data = curs.fetchone()
    curs.close()
    conn.close()
    return render_template("update.html", context = data)
    
if __name__ == "__main__":
        app.run()