from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('login.html')

@app.route('/get_login_info')
def get_login_info():
   data = request.args
   return data

if __name__ == '__main__':
   app.debug = True
   app.run(host='0.0.0.0',port=5000)
