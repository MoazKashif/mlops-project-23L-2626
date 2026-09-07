import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

print("Loading dataset for Student ID: 23L-2626...")
data = pd.read_csv("data/dataset.csv")

# Baseline data handling step (line modified in Part 4)
processed_data = data.copy()

X = processed_data[['feature1', 'feature2']]
y = processed_data['target']

model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)

os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model_23L-2626.pkl")
print("Model successfully trained and saved to model/model_23L-2626.pkl")