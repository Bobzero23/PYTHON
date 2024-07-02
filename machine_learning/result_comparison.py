import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

# Define the original data
data = np.array([
    [1400, 100, 450],
    [1500, 120, 460],
    [1600, 130, 470],
    [1700, 140, 480],
    [1800, 150, 490],
    [1900, 160, 500],
    [2000, 170, 510],
    [2100, 180, 520],
    [2200, 190, 530],
    [2300, 200, 540]
])

# Define feature and target variables
X = data[:, :2]  # Weight and Horsepower
y = data[:, 2]  # Torque

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define normalization methods
scalers = {
    'Original': None,
    'Min-Max Scaling': MinMaxScaler(),
    'Z-score Normalization': StandardScaler(),
    'Robust Scaling': RobustScaler()
}

# Initialize results dictionary
results = {}


# Function to train and evaluate models
def evaluate_model(name, X_train, X_test):
    models = {
        'KNN': KNeighborsClassifier(n_neighbors=3),
        'SVM': SVC(kernel='linear'),
        'Random Forest': RandomForestClassifier(n_estimators=10, random_state=42)
    }

    model_results = {}
    for model_name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        model_results[model_name] = {
            'Accuracy': accuracy_score(y_test, y_pred),
            'Precision': precision_score(y_test, y_pred, average='weighted', zero_division=1),
            'Recall': recall_score(y_test, y_pred, average='weighted', zero_division=1),
            'F1 Score': f1_score(y_test, y_pred, average='weighted', zero_division=1)
        }
    return model_results


# Evaluate models with each normalization method
for name, scaler in scalers.items():
    if scaler:
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
    else:
        X_train_scaled = X_train
        X_test_scaled = X_test

    results[name] = evaluate_model(name, X_train_scaled, X_test_scaled)

# Print results
for method, metrics in results.items():
    print(f"Results for {method}:")
    for model, model_metrics in metrics.items():
        print(f"  {model}:")
        for metric, value in model_metrics.items():
            print(f"    {metric}: {value:.2f}")
    print()

