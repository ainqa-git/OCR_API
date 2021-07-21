from flask import Flask, flash, redirect, render_template, request, session, abort
import camelot
import pandas as pd
import os
from flask_cors import CORS , cross_origin
from werkzeug.utils import secure_filename


CORS()

app = Flask(__name__)
app.secret_key = '12345678'
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/extract",methods=['GET', 'POST'])
def extract():
    
    file = request.files['file-upload']
    filename = secure_filename(file.filename)
    file.save(os.path.join(filename))
    tables = camelot.read_pdf(filename, flavor='stream')
    i = 0
    df1 = tables[i].df
    df1.to_csv('Table'+str(i)+'.csv')
    json_data = df1.to_json(orient='values')
    os.remove(filename)
    return json_data


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=5018,debug=True)
            

