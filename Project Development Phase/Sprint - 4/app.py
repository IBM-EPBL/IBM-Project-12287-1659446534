from flask import Flask,render_template, flash,redirect, url_for,request
import sqlite3 as sql

app = Flask(__name__)
app.secret_key="HIII"

@app.route("/")
def homepage():
	return render_template("homepage.html")
	
@app.route("/catalogue")                                      
def catalogue():
	return render_template("catalogue.html")


@app.route("/orderconfirmed")
def orderconfirmed():
   return render_template("orderconfirmed.html")

@app.route("/payment")
def payment():
   return render_template("payment.html")
 
@app.route("/registration_with_js_validation")
def registration_with_js_validation():
   return render_template("registration_with_js_validation.html")
 
@app.route("/registration")
def registration():
   return render_template("registration.html")
 
@app.route("/shoppingcart")
def shoppingcart():
   return render_template("shoppingcart.html")

@app.route("/contact")
def contact():
   return render_template("contact.html")

@app.route('/data',methods = ['POST', 'GET'])
def data():
   if request.method == 'POST':
      try:
         username = request.form['username']
         email = request.form['email']
         password = request.form['password']
          
         
         with sql.connect("student_database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (username,email,password) VALUES (?,?,?)",(username,email,password) )
            con.commit()
            msg = "Record successfully added!"
      except:
         con.rollback()
         msg = "error in insert operation" 
      
      finally:
        return render_template("List.html",msg = msg)
        con.close()     

@app.route('/list')
def list():
   con = sql.connect("student_database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   students = cur.fetchall()
   return render_template("List.html", students = students)

if __name__ == '__main__':
   app.run(debug = True)