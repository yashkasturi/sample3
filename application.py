from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from PIL import Image
import requests
import imgsave
import imgsave1

app = Flask(__name__)

@app.route('/')
def page1():
    return render_template('mangrove_Index.html')

app.config['MYSQL_HOST'] = 'db4free.net'
app.config['MYSQL_USER'] = 'mangroveteam'
app.config['MYSQL_PASSWORD'] = 'mangroveteam'
app.config['MYSQL_DB'] = 'mangrove'

mysql = MySQL(app)

@app.route('/index.html', methods=['GET', 'POST'])
def page2():
	if request.method == "POST":
		  details = request.form
		  pathname1 = details['pathname']
		  #cur = mysql.connection.cursor()
		  #cur.execute("SELECT before_url from image WHERE pathname='{}'".format(pathname1))
		  #mysql.connection.commit()
		  #result=cur.fetchall()
		  #for i in result:
		  #	print(i)    
		  #cur.close()
		  cur1 = mysql.connection.cursor()
		  cur1.execute("UPDATE imginput SET p_name='{}' where id=1".format(pathname1))
		  mysql.connection.commit()
		  result1=cur1.fetchall()
		  for x in result1:
		    print(x)    
		  cur1.close()
		  print (pathname1)
		  #return pathname1
	return render_template('index.html')

@app.route('/index', methods=['GET', 'POST','REQUEST'])
def page3():
	if request.method == "REQUEST" or "POST":
		cur = mysql.connection.cursor()
		cur.execute("SELECT p_name from imginput WHERE id=1")
		mysql.connection.commit()
		result=cur.fetchone()
		a = result
		for i in result:
			print(i)    
		cur.close()
		cur2 = mysql.connection.cursor()
		cur2.execute("SELECT before_url from image WHERE pathname='{}'".format(result[0]))
		mysql.connection.commit()
		result2=cur2.fetchone()
		b=result2
	        #return render_template('final.html', a=b[0])
		cur3 = mysql.connection.cursor()
		cur3.execute("SELECT after_url from image WHERE pathname='{}'".format(result[0]))
		mysql.connection.commit()
		result3=cur3.fetchone()
		d=result3
	#return render_template('final.html', a=b[0])
	c=b[0]
	e=d[0]
	imgsave.af(c,e)
	return render_template('final1.html')


