from flask import Flask
import LeadsManager

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return LeadsManager.Get()
