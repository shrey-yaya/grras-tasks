import pickle
import pandas as pd

with open("resume_model.pkl", "rb") as file:
    model = pickle.load(file)

def predict_resume(skills_count):

    if skills_count >= 5:
        return 1   # Selected
    else:
        return 0   # Rejected