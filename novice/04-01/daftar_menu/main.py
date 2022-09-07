from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = psycopg2.connect(
        host="localhost",
        database="menu",
        user="postgres",
        password="postgres")
    curs = conn.cursor()
    if request.method == "POST":
        hari = request.form.get("hari")
        sayur = request.form.get("sayur")
        lauk = request.form.get("lauk")
        buah = request.form.get("buah")
        query = f"insert into menu(hari, sayur, lauk, buah) values('{hari}', '{sayur}', '{lauk}', '{buah}')"
        curs.execute(query)
        conn.commit()
        print(request.method) 
    query = f"select * from menu" 
    curs.execute(query)
    data = curs.fetchall() 
    
    return render_template("index.html", context=data)

@app.route("/detail/<menu_id>")
def detail(menu_id):
    conn = psycopg2.connect(
        host="localhost",
        database="menu",
        user="postgres",
        password="postgres")

    curs = conn.cursor()
    query = f"select * from menu where id = {menu_id}"
    curs.execute(query)
    data = curs.fetchone()
    conn.commit()
    curs.close()
    conn.close()
    print (data)
    return render_template("detail.html", context=data)



@app.route("/delete/<menu_id>")
def delete(menu_id):
    conn = psycopg2.connect(
        host="localhost",
        database="menu",
        user="postgres",
        password="postgres")
    curs = conn.cursor()
    query = f"delete from menu where id = {menu_id}"
    curs.execute(query)
    conn.commit()
    curs.close()
    conn.close()
    return redirect("/")

@app.route("/update/<menu_id>", methods=["GET", "POST"])
def update(menu_id):
    conn = psycopg2.connect(
        host="localhost",
        database="menu",
        user="postgres",
        password="postgres")

    curs = conn.cursor()
    if request.method == "POST":
        hari = request.form.get("hari")
        sayur = request.form.get("sayur")
        lauk = request.form.get("lauk")
        buah = request.form.get("buah")
        query = f"update menu set hari ='{hari}', sayur = '{sayur}', lauk = '{lauk}', buah = '{buah}' where id = '{menu_id}'"
        curs.execute(query)
        conn.commit()
        return redirect("/")

    query = f"select * from menu where id = {menu_id}"
    curs.execute(query)
    data = curs.fetchone()
    curs.close()
    conn.close()
    return render_template("update.html", context = data)
    
if __name__ == "__main__":
        app.run()
