import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

data = load_breast_cancer()

x = pd.DataFrame(data.data, columns=data.feature_names)[[
    'mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness'
]]
y = data.target   

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train, y_train)

pickle.dump(model, open("model.pkl", "wb"))