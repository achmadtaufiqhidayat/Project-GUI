from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from werkzeug.security import check_password_hash, generate_password_hash
import urllib.request
from datetime import datetime
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
app = Flask(__name__)
#koneksi
app.secret_key = 'bebasapasaja'
app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] =''
app.config['MYSQL_DB'] ='imagesimilaarity'

mysql = MySQL(app)

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg" }

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
  return "." in filename and \
    filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/index", methods=["GET", "POST"])
def upload_files():
  if request.method == "POST":
    
    files = request.files.getlist("images")


    for file in files:
      if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        
         
    return redirect(url_for("index"))


@app.route("/index")
def uploaded_files():

  files = os.listdir(app.config["UPLOAD_FOLDER"])
  return "<br>".join(files)


           
           
#index
@app.route('/')
def index():
    if 'loggedin' in session:
        return render_template('index.html')
    flash('Harap Login dulu','danger')
    return redirect(url_for('login'))




#registrasi
@app.route('/register', methods=('GET','POST'))
def registrasi():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        level = request.form['level']

        #cek username atau email
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tbl_users WHERE username=%s OR email=%s',(username, email, ))
        akun = cursor.fetchone()
        if akun is None:
            cursor.execute('INSERT INTO tbl_users VALUES (NULL, %s, %s, %s, %s)', (username, email, generate_password_hash(password), level))
            mysql.connection.commit()
            flash('Registrasi Berhasil','success')
         
        else :
            flash('Username atau email sudah ada','danger')
            
    return render_template('register.html')

#login
@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        
        #cek data username
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tbl_users WHERE email=%s',(email, ))
        akun = cursor.fetchone()
        if akun is None:
            flash('Login Gagal, Cek Email Anda','danger')
        elif not check_password_hash(akun[3], password):
            flash('Login gagal, Cek Password Anda', 'danger')
        else:
            session['loggedin'] = True
            session['username'] = akun[1]
            session['level'] = akun[4]
            return redirect(url_for('index'))
    return render_template('login.html')




#logout
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    session.pop('level', None)
    
    return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True)