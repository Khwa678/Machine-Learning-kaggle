from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('regmodel.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html', prediction_text='')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect features from the form and convert to float
        features = [
            float(request.form['CRIM']),
            float(request.form['ZN']),
            float(request.form['INDUS']),
            float(request.form['CHAS']),
            float(request.form['NOX']),
            float(request.form['RM']),
            float(request.form['AGE']),
            float(request.form['DIS']),
            float(request.form['RAD']),
            float(request.form['TAX']),
            float(request.form['PTRATIO']),
            float(request.form['B']),
            float(request.form['LSTAT'])
        ]
        
        # Convert to numpy array for prediction
        final_features = np.array(features).reshape(1, -1)
        prediction = model.predict(final_features)[0]
        
        return render_template('home.html', prediction_text=f'Predicted Price: ${prediction:.2f}')
    
    except Exception as e:
        return render_template('home.html', prediction_text=f'Error: {e}')

if __name__ == "__main__":
    app.run(debug=True)
