from flask import Flask
import Python_code.LeadsManager as LeadsManager

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return LeadsManager.Get()
