from flask import Flask,render_template,request
import numpy as np
import pickle

model=pickle.load(open('Healthcare.pkl','rb'))

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def new():
    return render_template('new.html')

@app.route('/predict', methods=['POST','GET'] )
def predict():
    data1=float(request.form['a'])
    data2=float(request.form['b'])
    data3=float(request.form['c'])
    data4=float(request.form['d'])
    data5=float(request.form['e'])
    data6=float(request.form['f'])
    data7=float(request.form['g'])
    data8=float(request.form['h'])
    data9=float(request.form['i'])
    data10=float(request.form['j'])
    features=np.array([data1,data2,data3,data4,data5,data6,data7,data8,data9,data10])
    pred = model.predict([features])
    
    def statement():
        if pred == 0:
            return 'Result:- The model has predicted that you will not suffer from any cardic arresst but you should take care of your self.'
        elif pred == 1:
            return 'Result:- You should consult with doctor, The model has predicted that you will suffer form cardic arrest.'
    
    return render_template('new.html',statement=statement())


if __name__=='__main__':
    app.run()