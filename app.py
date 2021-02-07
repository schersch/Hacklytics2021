from flask import Flask, jsonify, request, render_template, flash, redirect, url_for, send_from_directory, send_file
import os
import pandas as pd
import numpy as np
import shapefile
import matplotlib.pyplot as plt
import json

app = Flask(__name__)
app.secret_key = os.urandom(24)

shape = shapefile.Reader("NRI_Shapefile_Counties.shp")

data = pd.read_csv('data.csv')

def countyPrinter(stcofip):
    for i in range(len(shape)):
        if shape.record(i)['STCOFIPS'] == stcofip:
            shapeRec = shape.shapeRecord(i)
            break

    listx = []
    listy = []

    for x,y in shapeRec.shape.points:
        listx.append(x)
        listy.append(y)

    fig, ax = plt.subplots()
    plt.plot(listx, listy)

    fig.patch.set_visible(False)
    ax.axis('off')
    imgpath = os.path.join('static', stcofip+'.png')
    plt.savefig(imgpath)


def riskAssesor(stcofip):
    coData = {}
    if not os.path.isfile(os.path.join('static', stcofip+'.png')):
        countyPrinter(stcofip)
    coData['countyImg'] = stcofip+'.png'
    coData['riskLevel'] = data[data['COMBOFIPS']==int(stcofip)]['RISK_RATNG'].values[0]
    #webOut = json.dumps(coData, indent = 4)
    return coData

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['GET', 'POST'])
def result():   
    if request.method == 'POST':
        if 'stcofips' not in request.form:
            flash('No stcofips entered')
            return redirect(request.url)
        stcofips = request.form['stcofips']
        coData = riskAssesor(stcofips)
        return render_template('result.html', riskLevel=coData['riskLevel'], countyImg=coData['countyImg'])

if(__name__ == '__main__'):
    app.run()