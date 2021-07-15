#!/usr/bin/env python3

from datetime import datetime
from flask import Flask
import os


DAYONE = datetime(2019, 11, 1)

app = Flask(__name__)


@app.route("/")
def index():
    today = datetime.now()
    dayOnes = today - DAYONE
    return f"<h1>Day One {dayOnes.days}<br>Game on!</h1>"


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
