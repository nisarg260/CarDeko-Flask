import pandas as pd


indexx = ['max_price', 'min_price', 'year', 'km_driven', 'seats',
       'mileage_kmpl', 'engine_cc', 'seller_type_Individual',
       'seller_type_Trustmark Dealer', 'owner_type_Second Owner',
       'owner_type_Third Owner', 'fuel_type_Diesel', 'fuel_type_Electric',
       'fuel_type_LPG', 'fuel_type_Petrol', 'transmission_type_Manual',
       'company_Audi', 'company_BMW', 'company_Bentley', 'company_Chevrolet',
       'company_DC', 'company_Daewoo', 'company_Datsun', 'company_Ferrari',
       'company_Fiat', 'company_Force', 'company_Ford', 'company_Honda',
       'company_Hyundai', 'company_ISUZU', 'company_Isuzu', 'company_Jaguar',
       'company_Jeep', 'company_Kia', 'company_Lamborghini', 'company_Land',
       'company_Lexus', 'company_MG', 'company_Mahindra', 'company_Maruti',
       'company_Maserati', 'company_Mercedes-AMG', 'company_Mercedes-Benz',
       'company_Mini', 'company_Mitsubishi', 'company_Nissan', 'company_Opel',
       'company_OpelCorsa', 'company_Porsche', 'company_Premier',
       'company_Renault', 'company_Rolls-Royce', 'company_Skoda',
       'company_Tata', 'company_Toyota', 'company_Volkswagen', 'company_Volvo',
       'model_1.4Gsi', 'model_1000', 'model_3', 'model_5', 'model_500',
       'model_6', 'model_7', 'model_800', 'model_A', 'model_A-Class',
       'model_A-Star', 'model_A3', 'model_A4', 'model_A5', 'model_A6',
       'model_A8', 'model_Abarth', 'model_Accent', 'model_Accord',
       'model_Alto', 'model_Altroz', 'model_Alturas', 'model_Amaze',
       'model_Ameo', 'model_Aria', 'model_Aspire', 'model_Aura',
       'model_Avanti', 'model_Aveo', 'model_Avigo', 'model_Avventura',
       'model_B', 'model_B-Class', 'model_BR-V', 'model_BRV', 'model_Baleno',
       'model_Beat', 'model_Beetle', 'model_Bolero', 'model_Bolt',
       'model_Boxster', 'model_Brio', 'model_C', 'model_C-Class',
       'model_CL-Class', 'model_CLA', 'model_CLK', 'model_CLS',
       'model_CLS-Class', 'model_CR', 'model_CR-V', 'model_Camry',
       'model_Captiva', 'model_Captur', 'model_Carnival', 'model_Cayenne',
       'model_Cayman', 'model_Cedia', 'model_Celerio', 'model_Ciaz',
       'model_City', 'model_Civic', 'model_Classic', 'model_Clubman',
       'model_Compass', 'model_Continental', 'model_Cooper', 'model_Corolla',
       'model_Corsa', 'model_Creta', 'model_CrossPolo', 'model_Cruze',
       'model_D-Max', 'model_Duster', 'model_Dzire', 'model_E',
       'model_E-Class', 'model_EON', 'model_ES', 'model_Ecosport',
       'model_Eeco', 'model_Elantra', 'model_Endeavour', 'model_Enjoy',
       'model_Ertiga', 'model_Escort', 'model_Esteem', 'model_Etios',
       'model_Evalia', 'model_F-PACE', 'model_F-Pace', 'model_F-TYPE',
       'model_Fabia', 'model_Fiesta', 'model_Figo', 'model_Fluence',
       'model_Fortuner', 'model_Freestyle', 'model_GL-Class', 'model_GLA',
       'model_GLC', 'model_GLE', 'model_GLS', 'model_GO', 'model_GTC4Lusso',
       'model_GTI', 'model_Gallardo', 'model_Getz', 'model_Ghibli',
       'model_Ghost', 'model_Glanza', 'model_Grand', 'model_Grande',
       'model_Gurkha', 'model_Gypsy', 'model_Harrier', 'model_Hector',
       'model_Hexa', 'model_Ignis', 'model_Ikon', 'model_Indica',
       'model_Indigo', 'model_Ingenio', 'model_Innova', 'model_Jazz',
       'model_Jeep', 'model_Jetta', 'model_KUV', 'model_KUV100', 'model_KWID',
       'model_Kicks', 'model_Kizashi', 'model_Kodiaq', 'model_Koleos',
       'model_Kona', 'model_Lancer', 'model_Land', 'model_Laura',
       'model_Linea', 'model_Lodgy', 'model_Logan', 'model_M', 'model_M-Class',
       'model_MU', 'model_MUX', 'model_Macan', 'model_Manza', 'model_Marazzo',
       'model_Matiz', 'model_Micra', 'model_Mobilio', 'model_Montero',
       'model_Mulsanne', 'model_Mustang', 'model_NX', 'model_Nano',
       'model_New', 'model_Nexon', 'model_NuvoSport', 'model_Octavia',
       'model_Omni', 'model_One', 'model_Optra', 'model_Outlander',
       'model_Pajero', 'model_Palio', 'model_Panamera', 'model_Passat',
       'model_Platinum', 'model_Polo', 'model_P6rius', 'model_Pulse',
       'model_Punto', 'model_Q3', 'model_Q5', 'model_Q7', 'model_Qualis',
       'model_Quanto', 'model_Quattroporte', 'model_R8', 'model_RX',
       'model_Rapid', 'model_RediGO', 'model_Renault', 'model_Rio',
       'model_Ritz', 'model_Rover', 'model_S', 'model_S-Class',
       'model_S-Cross', 'model_S-Presso', 'model_S4', 'model_S40', 'model_S5',
       'model_S60', 'model_S90', 'model_SLC', 'model_SLK', 'model_SX4',
       'model_Safari', 'model_Sail', 'model_Santa', 'model_Santro',
       'model_Scala', 'model_Scorpio', 'model_Seltos', 'model_Sierra',
       'model_Sonata', 'model_Sonet', 'model_Spark', 'model_Ssangyong',
       'model_Sumo', 'model_Sunny', 'model_Superb', 'model_Supro',
       'model_Swift', 'model_TT', 'model_TUV', 'model_Tavera', 'model_Teana',
       'model_Terracan', 'model_Terrano', 'model_Thar', 'model_Tiago',
       'model_Tigor', 'model_Tiguan', 'model_Trailblazer', 'model_Triber',
       'model_Tucson', 'model_V40', 'model_Vento', 'model_Venture',
       'model_Venue', 'model_Verito', 'model_Verna', 'model_Versa',
       'model_Vista', 'model_Vitara', 'model_WR-V', 'model_Wagon',
       'model_Winger', 'model_Wrangler', 'model_X-Trail', 'model_X1',
       'model_X3', 'model_X4', 'model_X5', 'model_X6', 'model_XC',
       'model_XC60', 'model_XC90', 'model_XE', 'model_XF', 'model_XJ',
       'model_XL6', 'model_XUV300', 'model_XUV500', 'model_Xcent',
       'model_Xenon', 'model_Xylo', 'model_Yaris', 'model_Yeti', 'model_Z4',
       'model_Zen', 'model_Zest', 'model_e2o', 'model_e2oPlus', 'model_i10',
       'model_i20', 'model_prado', 'model_redi-GO']
        
        
def convert(app):
        a = pd.Series(index=indexx)
        car = a.fillna(0)
        car['year'] = app[0]
        car['km_driven'] = app[2]
        car['seats'] = app[6]
        car['mileage_kmpl'] = app[9]
        car['engine_cc'] = app[10]
        car['max_price'] = app[11]
        car['min_price'] = app[12]
        reqire = ['seller_type_'+app[1], 'owner_type_'+app[3], 'fuel_type_'+app[4], 'transmission_type_'+app[5], 
                     'company_'+app[7], 'model_'+app[8]]
        
        for i in indexx:
            if i in reqire:
                car[i] = 1
        return car