import webbrowser
from threading import Timer
from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route("/")
def hello():
      app.config['MYSQL_HOST'] = 'localhost'
      app.config['MYSQL_USER'] = 'root'
      app.config['MYSQL_PASSWORD'] = 'root'
      app.config['MYSQL_DB'] = 'ignition8.1goldtest'
 
      mysql = MySQL(app)
      cursor = mysql.connection.cursor()
      cursor.execute(''' SELECT * FROM tasks''')
      mysql.connection.commit()
      cursor.close()
      return render_template('Home.html')

def open_browser():
      webbrowser.open_new('http://127.0.0.1:2000/')

if __name__ == "__main__":
      Timer(1, open_browser).start();
      app.run(port=2000)


     