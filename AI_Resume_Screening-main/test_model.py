import pickle
import pandas as pd

# Load saved model
with open("resume_model.pkl", "rb") as file:
    model = pickle.load(file)

# Sample candidate
sample = pd.DataFrame({
    "Experience (Years)": [5],
    "Education": [2],
    "Job Role": [3],
    "Projects Count": [8],
    "Skills Count": [6]
})

prediction = model.predict(sample)

print("Prediction:", prediction)