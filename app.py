import mariadb
import dbcreds
import json
from flask import Flask

app = Flask(__name__)

conn = mariadb.connect(**dbcreds.conn_params)
cursor = conn.cursor()

def end_conn():
    if(cursor !=None):
        cursor.close()
    if(conn !=None):
        conn.close()



@app.get('/author')
def select_dogs():
    cursor.execute('CALL select_author()')
    results = cursor.fetchall()

    if(type(results) == list):
        rst_json = json.dumps(results, default=str)
        end_conn()
        return rst_json
    else:
        print("error")
        end_conn()

@app.get('/writen')
def select_cats():

    cursor.execute('CALL select_writen()')
    results = cursor.fetchall()

    if(type(results) == list):
        rst_json = json.dumps(results, default=str)
        end_conn()
        return rst_json
    else:
        print("error")
        end_conn()

@app.get('/popular')
def get_animals():

    cursor.execute('CALL select_popular()')
    results = cursor.fetchall()

    if(type(results) == list):
        rst_json = json.dumps(results, default=str)
        end_conn()
        return rst_json
    else:
        print("error")
        end_conn()


app.run(debug=True)