from flask import Flask
import os

flaskPort = os.environ.get('PORT',5000)

app = Flask(__name__)

@app.route('/')
def func():
   return 'Hello on '+str(flaskPort)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=flaskPort)
