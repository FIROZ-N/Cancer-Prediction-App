🩺 Breast Cancer Prediction App

A machine learning-powered web app that predicts whether a breast tumor is Benign or Malignant based on five key diagnostic features from the Breast Cancer Wisconsin Dataset.
Built using Python, Flask, Streamlit, and scikit-learn.

🔍 Overview

This project demonstrates how to build a simple end-to-end ML application:

Train a classification model on medical data.

Save the trained model using pickle.

Deploy it using Flask (for a web form interface).

Build an interactive version using Streamlit.

🧠 Features Used

We selected 5 key predictive features for simplicity and speed:

Mean Radius

Mean Texture

Mean Perimeter

Mean Area

Mean Smoothness

⚙️ Tech Stack

Python 3.x

Flask — Backend web framework

Streamlit — Data web app framework

scikit-learn — Model training and prediction

pandas, numpy, pickle — Data handling & storage

🧩 Project Structure
breast_cancer_prediction/
│
├── train_model.py          # Train & save ML model
├── model.pkl               # Saved trained model
├── app.py                  # Flask app
├── app_streamlit.py        # Streamlit app
├── templates/
│   └── index.html          # Flask front-end template
├── requirements.txt        # Required dependencies
└── README.md               # Project documentation

🏗️ Setup & Run
1️⃣ Clone the Repository
git clone https://github.com/your-username/breast-cancer-prediction.git
cd breast-cancer-prediction

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Train the Model
python train_model.py

4️⃣ Run Flask App
python app.py


Visit: http://127.0.0.1:5000

5️⃣ Run Streamlit App
streamlit run app_streamlit.py

📊 Model Information

Dataset: Breast Cancer Wisconsin (from sklearn.datasets)

Algorithm: Random Forest Classifier

Accuracy: ~96–98% on test data

🧾 Example Output

Input:
Mean Radius = 14.5
Mean Texture = 20.1
Mean Perimeter = 95.3
Mean Area = 600.5
Mean Smoothness = 0.1

Prediction:
✅ Benign

👨‍💻 Author

FIROZ MUHAMMED N
BSc Computer Science | Machine Learning & Web Developer

🪪 License

This project is licensed under the MIT License — you’re free to use, modify, and distribute it.

🌟 Star the Repo

If you like this project, don’t forget to ⭐ it on GitHub to support future development!
