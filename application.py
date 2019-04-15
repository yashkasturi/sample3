from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from PIL import Image

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

@app.route('/index', methods=['GET', 'POST','REQUEST'])
def index1():
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
	return af(c,e)
def af(c,e):
	url = c
	try:
		resp = requests.get(url, stream=True).raw
	except requests.exceptions.RequestException as e:  
		sys.exit(1)
	try:
		img = Image.open(resp)
	except IOError:
		print("Unable to open image")
		sys.exit(1)
	img.save('static/images/after.jpg', 'jpeg')
	url = e
	try:
		resp = requests.get(url, stream=True).raw
	except requests.exceptions.RequestException as e:  
		sys.exit(1)
	try:
		img = Image.open(resp)
	except IOError:
		print("Unable to open image")
		sys.exit(1)
	img.save('static/images/before.jpg', 'jpeg')
	return render_template('final1.html')
