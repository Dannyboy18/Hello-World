import os
from flask import Flask
app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')
def hello_world(name="World"):
    return 'Hello, {}!'.format(name)

if __name__ == "__main__":
  port = int(os.getenv("PORT", 8080))
  app.run(host='0.0.0.0', port=port)