import webbrowser
from threading import Timer
from flask import Flask, render_template, request, make_response
from flask_mysqldb import MySQL

app = Flask(__name__,template_folder='template')

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'ignition8.1goldtest'
app.config['MYSQL_HOST'] = 'localhost'
mysql = MySQL(app)

@app.route("/")
def home():
      cur = mysql.connection.cursor()
      cur.execute("SELECT * FROM tasks")
      mysql.connection.commit()
      data = cur.fetchall()
      return render_template('home.html', data=data)

def open_browser():
      webbrowser.open_new('http://127.0.0.1:2000/')

if __name__ == "__main__":
      Timer(1, open_browser).start();
      app.run(port=2000)


     