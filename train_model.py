import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
data = pd.read_csv("dataset/student-dataset.csv")

# Display basic information
print("Dataset Preview:")
print(data.head())

print("\nColumns:")
print(data.columns)

print("\nMissing Values:")
print(data.isnull().sum())

# Convert Categorical Columns
data["InternetAvailable"] = data["InternetAvailable"].map({
    "No": 0,
    "Yes": 1
})

data["ParentEducation"] = data["ParentEducation"].map({
    "Primary": 0,
    "High School": 1,
    "Graduate": 2,
    "Post Graduate": 3
})

data["ExtracurricularActivities"] = data["ExtracurricularActivities"].map({
    "No": 0,
    "Yes": 1
})

data["FamilyIncome"] = data["FamilyIncome"].map({
    "Low": 0,
    "Medium": 1,
    "High": 2
})

# Features and Target
X = data[
    [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "Assignments",
        "InternetAvailable",
        "ParentEducation",
        "SleepHours",
        "ExtracurricularActivities",
        "DailyScreenTime",
        "FamilyIncome"
    ]
]

y = data["FinalScore"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Evaluation
print("\nModel Performance")
print("--------------------------")
print("Mean Absolute Error:", mean_absolute_error(y_test, predictions))
print("R² Score:", r2_score(y_test, predictions))

# Save Model
joblib.dump(model, "model.pkl")

print("\nModel trained successfully.")
print("model.pkl saved successfully.")