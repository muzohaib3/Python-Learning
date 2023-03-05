from flask import Flask, jsonify
import mysql.connector

# app = Flask(__name__)

# @app.route("/")
# def index():
#     cnx = mysql.connector.connect( user='root',password='',host='localhost',database='mydb')

#     cursor = cnx.cursor()
#     cursor.execute("SELECT * FROM customers")

#     results = cursor.fetchall()

#     cursor.close()
#     cnx.close()

#     return str(results)

# if __name__ == '__main__':
#     app.run()

app = Flask(__name__)

@app.route("/")
def index():
    cnx = mysql.connector.connect(
        user = "root",
        password = "",
        host = "localhost",
        database = "mydb"
    )
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM customers")

    results = cursor.fetchall()
    cursor.close()

    return str(results)

if __name__ == '__main__':
    app.run()

