from flask import Flask, render_template, request
import numpy as np   
import pickle

app = Flask(__name__)


model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get the 5 key features from form
    features = [
        float(request.form["mean_radius"]),
        float(request.form["mean_texture"]),
        float(request.form["mean_perimeter"]),
        float(request.form["mean_area"]),
        float(request.form["mean_smoothness"])
    ]
    
    # Convert to array
    import numpy as np
    final = np.array(features).reshape(1, -1)
    
    # Predict using model
    prediction = model.predict(final)
    output = "Benign" if prediction[0] == 1 else "Malignant"
    
    return render_template("index.html", prediction=f"Prediction: {output}")

if __name__ == '__main__':
    app.run(debug=True)