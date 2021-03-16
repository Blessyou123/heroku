from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
  return 'Name: Edrian Arcayan Course and Year: BSIT-2'
