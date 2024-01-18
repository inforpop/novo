from flask import Flask
import os
app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))
@app.route('/')
def index():
    return 'Web App with Python Flask!'

app.run(debug=True, port=33507)
