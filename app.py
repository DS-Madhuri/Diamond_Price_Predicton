from flask import Flask, request, jsonify, render_template, redirect, url_for
from utils import DiamondPrice
import config
import traceback

app = Flask(__name__)

@app.route('/Diamond_price')
def home1():
    
    return render_template('index.html')

@app.route('/predict', methods = ['GET', 'POST'])
def predict():

    if request.method == 'GET':
        print("+"*50)
        data = request.args.get
        print("Data :",data)

        carat=float(data('carat'))
        cut = data('cut')
        color= data('color')
        clarity = data('clarity')
        depth = float(data('depth'))
        table = float(data('table'))
        x = float(data('x'))
        y = float(data('y'))
        z = float(data('z'))

        Obj = DiamondPrice(carat,cut,color,clarity,depth,table,x,y,z)
        pred_price = Obj.get_predicted_price()    

        return render_template('form.html', prediction = pred_price)
           

    elif request.method == 'POST':
        print("*"*40)
        data = request.form.get
        print("Data :",data)

        carat=float(data('carat'))
        cut = data('cut')
        color= data('color')
        clarity = data('clarity')
        depth = float(data('depth'))
        table = float(data('table'))
        x = float(data('x'))
        y = float(data('y'))
        z = float(data('z'))

        Obj = DiamondPrice(carat,cut,color,clarity,depth,table,x,y,z)
        pred_price = Obj.get_predicted_price()    

        return render_template('form.html', prediction = pred_price)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 8080, debug=False)
