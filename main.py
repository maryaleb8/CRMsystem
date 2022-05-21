#!/usr/bin/python3
import sqlite3
from flask import Flask

conn = sqlite3.connect('otbor4.s3db', check_same_thread=False)
cur = conn.cursor()

# creating table
#
# cur.execute("""CREATE TABLE t1 (
#     --name TEXT,
#     --address TEXT,
#     --number INT,
#     order_id INT,
#     --sum INT,
#     status TEXT
# )""")


def add_order(cur, order_id, status):
    # inp = input("input = ")
    # a = inp.split(" ")[0]
    # b = inp.split(" ")[1]
    # cur.execute('INSERT INTO t1(a, b) VALUES (?, ?);', (a, b))
    cur.execute("INSERT INTO t1(order_id, status) VALUES ('?', '?');", (order_id, status))
    conn.commit()


def delete_order(cur, b):
    cur.execute("DELETE FROM t1 WHERE b=?;", (b))
    conn.commit()


def update_order(cur, b, new):
    cur.execute("UPDATE t1 SET a = ? where b = ?", (new, b))
    conn.commit()


def see_order(cur):
    cur.execute("SELECT * FROM t1;")
    all_results = cur.fetchall()
    return all_results


from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/all_orders", methods=['GET'])
def index():
    try:
        print(see_order(cur))
        resp = {'data': []}
        for order in see_order(cur):
            resp['data'].append({'order_id': order[0], 'order': order[1]})
        print(resp)
        return jsonify(resp)
    except Exception:
        return 'error'


@app.route("/add_new_order", methods=['POST'])
def add_new_order():
    order_id = request.form.get('order_id')
    status = request.form.get('status')
    add_order(cur, order_id, status)
    return 'ok'


@app.route('/admin', methods=['GET'])
def admin_page():
    return open('admin.html', 'r', encoding='utf-8').read()




if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
