from flask import Flask, render_template, request
#from flask import redirect, request, jsonify, Response,render_template,url_for
import sqlite3 
conn=sqlite3.connect('database.db')
c=conn.cursor()
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='item' ''')
if (c.fetchone()[0]==1) :
    
    print('TABLE EXIST !')
    
else :
    print('TABLE NOT EXIST !')
    sql ='''CREATE TABLE item(
    item_name text,
    price text
    )'''
    c.execute(sql)
    c.execute('''INSERT INTO item
    (item_name,price) VALUES
    ('BLANKET',750)''')
    conn.commit()
app = Flask(__name__)
@app.route('/')
def home():
   return render_template('home.html')

@app.route('/new_item')
def new_item():
   return render_template('item.html')

@app.route('/additem',methods=['POST','GET'])
def additem():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         pr = request.form['pr']
         
         with sqlite3.connect("database.db") as con:
            c = con.cursor()
            
            #conn.execute('INSERT INTO item (item_name,price)',VALUES (?,?),(nm,pr) )
            #c.execute("""insert into item(nm , pr)
            #values (?,?)""",(nm,pr)) 
            c.execute("INSERT INTO item(item_name, price) VALUES('{}', '{}')".format(nm,pr))
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sqlite3.connect("database.db")
   con.row_factory = sqlite3.Row
   
   c = con.cursor()
   c.execute("select * from item")
   rows = c.fetchall()
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)