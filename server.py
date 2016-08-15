from flask import Flask, request,g
import sqlite3
import json


app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
		print "initialized"
		db = g._database = sqlite3.connect("database.db")
	
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route("/",methods=["POST"])
def insertintodb():
	db  = get_db()
	c = db.cursor()
	c.execute("INSERT INTO patients (patient_name,diagnosis,gender,age,category) values (?,?,?,?,?)", 
	(request.form["n"],request.form["d"],request.form["g"],request.form['a'],request.form['c']))
	db.commit()
	return "Done."
	
@app.route("/<category>",methods=['GET'])
def getcategory(category):
	db  = get_db()
	c = db.cursor()
	c.execute("SELECT * FROM patients WHERE category=?",(category,))
	data = c.fetchall()
	response = []
	diclist = ['id','name','diagnosis','gender','age','category']
	for row in data:
		dic = {diclist[i]: str(row[i]) for i in range(len(diclist))}
		response.append(dic)
	r = json.dumps(response)
	return r
	

with app.app_context():
	init_db()
	
app.run()