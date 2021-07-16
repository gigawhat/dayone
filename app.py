#!/usr/bin/env python3

from datetime import datetime
from flask import Flask, render_template
from flask_compress import Compress
import os


DAYONE = datetime(2019, 11, 1)

app = Flask(__name__)
Compress(app)


@app.route("/")
def index():
    return render_template('index.html', day=(datetime.now() - DAYONE).days)


if __name__ == '__main__':
    debug = True if os.getenv('DEBUG').lower() == 'true' else False
    app.run(debug=debug, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
