from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.methods == 'POST':
        return login()

        from    
if __name__ =="__main__":
    app.run()


Create = POST
Read = GET
Update = PUT
Delete = DELETE

