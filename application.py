from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/')
def css():
    return render_template('mangrove_Index.html')

app.config['MYSQL_HOST'] = 'db4free.net'
app.config['MYSQL_USER'] = 'mangroveteam'
app.config['MYSQL_PASSWORD'] = 'mangroveteam'
app.config['MYSQL_DB'] = 'mangrove'

mysql = MySQL(app)

@app.route('/index.html', methods=['GET', 'POST'])
def index():
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
