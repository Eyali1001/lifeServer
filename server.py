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

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/",methods=["POST"])
def insertintodb():
        db  = get_db()
	c = db.cursor()
	c.execute("UPDATE patients SET diagnosis=?,category=? WHERE patient_name=? ", 
	(request.form["d"],request.form['c'],request.form['u']))
	db.commit()
	return "Done."


@app.route("/signup",methods=['POST'])
def signup():
    db = get_db()
    c = db.cursor()
    if request.form['t'] == 'd':
        c.execute("INSERT INTO users (username,password,activechats,image) values (?,?,?,?)",
                  (request.form['u'],request.form['p'],",",request.form['b']))
        db.commit()
        return "Success"
    elif  request.form['t'] == 'p':
        c.execute("INSERT INTO patients (patient_name,password,image,age,gender) values (?,?,?,?,?)",
                  (request.form['u'],request.form['p'],request.form['b'],request.form['a'],request.form['g']))
        db.commit()
        
        return "Success"
    return "type error"

@app.route("/chat", methods=['POST'])
def updatechats():
    db = get_db()
    c = db.cursor()
    c.execute("SELECT activechats FROM users WHERE username=?",(request.form['du'],))
    data = c.fetchall()
    if request.form['pu'] in data.split(","):
        return "already chatting"
    else:
        c.execute("UPDATE users SET activechats=? WHERE username=?" ,
                  (data[0][0]+request.form['pu']+",",request.form['du']))
        db.commit()
        return "done"

@app.route("/chat/<du>",methods=['GET'])
def getchats(du):
    db = get_db()
    c = db.cursor()
    c.execute("SELECT activechats FROM users WHERE username=?",(du,))
    return c.fetchone()

@app.route("/signin",methods=['POST'])
def signin():
    db = get_db()
    c = db.cursor()

    c.execute("SELECT * FROM users WHERE username=?",(request.form['u'],))
    d = c.fetchall()
    print d
    if request.form['p'] == d[0][2]:
        return str(d[0][0])
    else:
        return "invalid"
    
        
    
@app.route("/<category>",methods=['GET'])
def getcategory(category):
	db  = get_db()
	c = db.cursor()
	c.execute("SELECT id,patient_name,image,diagnosis,gender,age,category FROM patients WHERE category=?",(category,))
	data = c.fetchall()
	response = []
	diclist = ['id','name','image','diagnosis','gender','age','category']
	for row in data:
                
		dic = {diclist[i]: row[i] for i in range(len(diclist))}
		response.append(dic)

	r = json.dumps(response)
	return r


app.config["DEBUG"]=True	
app.run()
