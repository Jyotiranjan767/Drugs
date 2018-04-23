from flask import Flask, render_template,flash, redirect, url_for,request,logging,session
# from data1 import articles
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField, PasswordField,validators
from passlib.hash import sha256_crypt
from functools import wraps
# import sys
# print(sys.path)
# sys.path.append('C:\\Users\\luckie\\Desktop\\flask_app\\templates')


# artic = articles()
app = Flask(__name__)
#config mysql
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='myflaskapp'
app.config['MYSQL_CURSORCLASS']='DictCursor'

#init mysql
mysql = MySQL(app) 
# app.debug =True
#check if user logged in
def is_logged_in(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('Unauthorized attempt, please login','danger')
			return redirect(url_for('login'))
	return wrap
@app.route('/')
def index():
	# return "myself"
	return render_template('home1.html')

@app.route('/about')
def about():
	return render_template('about.html')
@app.route('/articles')
@is_logged_in
def article():
	#create a connection
	cur = mysql.connection.cursor()
	result  = cur.execute("SELECT * from articles ")
	articles = cur.fetchall()

	if result > 0:
		return render_template('article.html', articles= articles)
	else:
		msg = 'No article is found'
		return render_template('article.html', msg= msg)

	return render_template('article.html',  articles = artic)
@app.route('/ids/<string:id>')
def ids(id):
	#create a connection
	cur = mysql.connection.cursor()
	result  = cur.execute("SELECT * from articles WHERE id = %s", [id])
	articles = cur.fetchone()
	return render_template('ids.html', article = articles)

class RegisterForm(Form):
	name = StringField('Name', [validators.Length(min=1, max = 50)])
	username=StringField("UserName",[validators.Length(min= 4, max = 20)])
	email = StringField('Email', [validators.Length(min =6,max= 50)])
	password = PasswordField('Password',
		[validators.DataRequired(),
		validators.EqualTo('confirm',message = "password do not match ")
			])
	confirm = PasswordField("Confirm Password")

@app.route('/register', methods = ["GET","POST"])
def register():
	form = RegisterForm(request.form)
	if(request.method == "POST" and form.validate()):
		name = form.name.data
		email  = form.email.data
		username = form.username.data
		password  = sha256_crypt.encrypt(str(form.password.data))
		#create a cursor
		cur = mysql.connection.cursor()
		infos=[]
		#infos = cur.fetchall()
		# for infos['name'] in infos.values():
			# if(infos['name'] != name):
		cur.execute("INSERT INTO users (name,email,userName,password)VALUES (%s, %s, %s, %s)",(name,email,username,password))
			# else:
				# redirect(url_for('home1.html'))
				# cur.close()
		#commit to db
		mysql.connection.commit()
		#close connection
		cur.close()
		flash('you are now registered to HOomestead 2 and can login','success')
		return redirect(url_for('index'))
	return render_template('register.html', form = form)
@app.route('/login',methods = ["GET","POST"])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password_candidate = request.form['password']

		cur = mysql.connection.cursor()
		result = cur.execute("SELECT * FROM users WHERE userName = %s ", [username])
		if result > 0:
			data = cur.fetchone()
			password = data['password']

			#compare passwords
			if sha256_crypt.verify(password_candidate, password):
				# app.logger.info('PASSWORD MATCHED')
				#passed
				session['logged_in'] = True
				session['username'] = username
				flash('you are now logged in','success')
				return redirect(url_for('dashboard'))  
			else:
				error = "invalid login"
				render_template('login.html', error=error)
			#close connection
			cur.close()
		else:
			error = 'Username not found'
			return render_template('login.html', error=error)
	return render_template('login.html')


@app.route('/logout')
def logout():
	session.clear()
	flash('you are now logged out , and please log in to continue ','success')
	return redirect(url_for('login'))
	# return render_template('login.html') # it does not help in logging in 
@app.route('/dashboard')
@is_logged_in
def dashboard():
	#create a connection
	cur = mysql.connection.cursor()
	result  = cur.execute("SELECT * from articles ")
	articles = cur.fetchall()

	if result > 0:
		return render_template('dashboard.html', article= articles)
	else:
		msg = 'No article is found'
		return render_template('dashboard.html', msg= msg)
	#close connection
	cur.close()
	# return render_template('article.html', articles = artic)
#article form class
class ArticleForm(Form):
	title = StringField('Title', [validators.length(min = 1, max = 200)])
	body = TextAreaField('Body',[validators.length(min = 30)])

#add article
@app.route('/add_article',methods = ['GET','POST'])
@is_logged_in
def add_article():
	form = ArticleForm(request.form)
	if request.method == 'POST' and form.validate():
		title = form.title.data
		body = form.body.data
		#create cursor
		cur = mysql.connection.cursor()
		cur.execute("ALTER TABLE articles AUTO_INCREMENT = 1")
		cur.execute("INSERT INTO articles (title, body, author) VALUES (%s, %s, %s)",(title, body, session['username']))
		#commit to db
		mysql.connection.commit()
		#close connection
		cur.close()

		flash('Article created','success')
		return redirect(url_for('dashboard'))
	return render_template('add_article.html',form = form)
#edit article
@app.route('/edit_article/<string:id>', methods =['GET', 'POST'])
@is_logged_in
def edit_article(id):
	cur = mysql.connection.cursor()
	result = cur.execute("SELECT * FROM articles WHERE id = %s",[id])
	article = cur.fetchone()
	#get form
	form = ArticleForm(request.form)
	form.title.data = article['title']
	form.body.data= article['body']
	if request.method == 'POST' and form.validate():
		title =request.form['title']
		body = request.form['body']
		cur = mysql.connection.cursor()
		cur.execute('UPDATE articles SET title = %s, body = %s where id = %s ',(title, body,id))
		mysql.connection.commit()
		cur.close()

		flash('Article updated ','success')
		return redirect(url_for('dashboard'))
	return render_template('edit_article.html',form = form)
@app.route('/delete_article/<string:id>',methods = ['POST'])
@is_logged_in
def delete_article(id):
	cur = mysql.connection.cursor()
	cur.execute("delete from articles where id = %s",[id])

	mysql.connection.commit()
	cur.close()
	flash('Article deleted','success')
	return redirect(url_for('dashboard'))
if __name__ =='__main__':
	app.secret_key= 'jyotiLuckie143'
	app.run(debug= True)