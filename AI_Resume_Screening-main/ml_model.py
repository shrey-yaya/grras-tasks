import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("AI_Resume_Screening-selected-columns.csv")

# Feature Engineering
df["Skills Count"] = df["Skills"].apply(
    lambda x: len(str(x).split(","))
)

# Label Encoding
le = LabelEncoder()

df["Education"] = le.fit_transform(df["Education"])
df["Job Role"] = le.fit_transform(df["Job Role"])
df["Recruiter Decision"] = le.fit_transform(df["Recruiter Decision"])

# Features (X)
X = df[
    [
        "Experience (Years)",
        "Education",
        "Job Role",
        "Projects Count",
        "Skills Count"
    ]
]

# Target (y)
y = df["Recruiter Decision"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Logistic Regression Model
model = LogisticRegression()

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# Classification Report
report = classification_report(y_test, y_pred)

print("\nClassification Report:")
print(report)
# Save model
with open("resume_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel saved successfully!")
