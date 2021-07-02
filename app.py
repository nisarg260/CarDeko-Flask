import modify
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)
picklee = pickle.load(open('rf_model.pkl', 'rb'))

companyy = ['Maruti', 'Hyundai', 'Ford', 'Mahindra', 'Tata', 'Renault',
       'Nissan', 'Mini', 'Mercedes-Benz', 'Toyota', 'Fiat', 'Volkswagen',
       'Honda', 'Chevrolet', 'Ambassador', 'Datsun', 'Kia', 'BMW',
       'Mitsubishi', 'Audi', 'Skoda', 'Land', 'Jaguar', 'Daewoo',
       'Bentley', 'MG', 'Isuzu', 'Porsche', 'Volvo', 'Lexus', 'Jeep',
       'Premier', 'Maserati', 'Force', 'Lamborghini', 'ISUZU', 'Ferrari',
       'OpelCorsa', 'Mercedes-AMG', 'DC', 'Rolls-Royce', 'Opel']
@app.route('/')
def home():
    return render_template('home.html', len = len(companyy), Company = companyy)

@app.route('/predict', methods=['POST'])
def value():
    year = 2021.0 - float(request.form['year'])
    seller_type = request.form['seller_type']
    km_driven = request.form['km_driven']
    owner_type = request.form['owner_type']
    fuel_type = request.form['fuel_type']
    transmission_type = request.form['transmission_type']
    seats =float(request.form['seats'])
    company = request.form['company']
    model = request.form['model'].capitalize()
    mileage = float(request.form['mileage'])
    engine = float(request.form['engine'])
    max_price = float(request.form['max_price']) / 100000
    min_price = float(request.form['min_price']) / 100000

    features = [year, seller_type, km_driven, owner_type, fuel_type, transmission_type, seats, company,
    model, mileage, engine, max_price, min_price]

   
    inputt = modify.convert(features)
    output = picklee.predict([inputt])
    ans = round(output[0]*100000)
    ans_1 = "Rs." + str(ans)
    
    # return str(output)
    return render_template('home.html', price = ans_1,len = len(companyy), Company = companyy)



if __name__ == '__main__':
	app.run(debug=True)