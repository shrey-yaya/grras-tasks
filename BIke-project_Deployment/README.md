# 🏍️ Used Bike Price Prediction (Deployment)

A machine learning-powered web application that predicts the resale price of used bikes based on features like kilometers driven, ownership status, age, power, and brand name. The app is built with a Flask backend, scikit-learn random forest model, and a responsive web dashboard.

---

## 📑 Table of Contents
- [Overview](#-overview)
- [Project Structure](#-project-structure)
- [Technical Details & Model](#-technical-details--model)
- [Quick Start](#-quick-start)
- [How to Use](#-how-to-use)
- [Deployment Guide](#-deployment-guide)
  - [Deployment on AWS EC2 (Directly)](#1-deployment-on-aws-ec2-directly)
  - [Deployment using Docker](#2-deployment-using-docker)
  - [Deployment via CI/CD (AWS Elastic Beanstalk)](#3-deployment-via-cicd-aws-elastic-beanstalk)

---

## 🎯 Overview
This project provides a complete end-to-end pipeline for predicting used bike prices:
1. **Model Development**: Jupyter Notebook (`Bike_notebook.ipynb`) used for data cleaning, exploratory data analysis (EDA), feature engineering, model training, and evaluation.
2. **Model Serialization**: The trained Random Forest Regressor is serialized as `updated_model.lb` using the `joblib` library.
3. **Web Server**: A lightweight Flask server (`application.py`) that loads the model, exposes API endpoints, and serves a user interface.
4. **Web UI**: A clean dashboard built with HTML/CSS where users can input bike features and get predicted prices instantly.

---

## 🏗️ Project Structure
```text
.
├── application.py         # Main Flask server
├── Bike_notebook.ipynb    # Jupyter Notebook for EDA & model training
├── Used_Bikes.csv         # Raw dataset containing historical bike listings
├── updated_model.lb       # Trained Random Forest model (Joblib format)
├── rf_model.lb            # Original trained Random Forest model
├── requirements.txt       # Project dependencies (Flask, scikit-learn, etc.)
├── deploy_commands.txt    # Helper guide for deployment commands
├── templates/             
│   └── index.html         # HTML template for the web interface
└── static/                # Static assets (CSS, JS, images)
```

---

## 🤖 Technical Details & Model

### Features Utilized for Prediction:
* **Kilometers Driven (`Kms_Driven`)**: Total distance the bike has traveled.
* **Owner (`owner`)**: Number of previous owners (e.g. First Owner, Second Owner).
* **Age (`age`)**: Age of the bike in years.
* **Power (`power`)**: Engine displacement in CC (Cubic Centimeters).
* **Brand (`brand_name`)**: Categorical feature representing the bike manufacturer, mapped internally as follows:
  1. Royal Enfield
  2. KTM
  3. Bajaj
  4. Harley
  5. Yamaha
  6. Honda
  7. Suzuki
  8. TVS
  9. Kawasaki
  10. Hyosung
  11. Benelli
  12. Mahindra
  13. Triumph
  14. Ducati
  15. BMW

### Machine Learning Algorithm:
* **Random Forest Regressor** trained on the `Used_Bikes.csv` dataset. The model captures non-linear relationships between bike attributes and their resale values, providing robust predictions.

---

## 🚀 Quick Start

### 1. Prerequisites
Make sure you have Python 3.8+ installed.

### 2. Set Up a Virtual Environment
```bash
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python application.py
```
The application will start on `http://localhost:5050` by default.

---

## 💻 How to Use
1. Open your browser and navigate to `http://localhost:5050`.
2. Fill out the form with the bike details:
   - **Kilometers Driven** (e.g., `12000`)
   - **Owner Type** (e.g., `1` for First Owner, `2` for Second Owner, etc.)
   - **Age** (e.g., `3`)
   - **Power (CC)** (e.g., `150`)
   - **Brand** (Select from Royal Enfield, KTM, Bajaj, Yamaha, Honda, etc.)
3. Click **Predict** to receive the estimated price instantly on the page.

---

## ☁️ Deployment Guide

### 1. Deployment on AWS EC2 (Directly)
1. **Launch EC2 Instance**: Set up an Ubuntu instance with appropriate Security Groups (allow TCP inbound on port `5050`).
2. **SSH Key Setup**:
   ```bash
   ssh-keygen -t rsa -b 4096
   cat ~/.ssh/id_rsa.pub
   # Copy public key and add it to your GitHub account under SSH Keys
   ```
3. **Clone the Repository**:
   ```bash
   git clone <repo_url>
   cd Bike_project
   ```
4. **Install Dependencies**:
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install python3-pip python3-venv -y
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
5. **Run in Background** using `screen` to keep the application active:
   ```bash
   screen -S deploy-session
   python application.py
   ```
   Press `Ctrl + A` then `D` to detach. To re-attach, run `screen -r deploy-session`.

### 2. Deployment using Docker
1. **Install Docker on Host**:
   ```bash
   sudo apt install docker.io -y
   ```
2. **Create a `Dockerfile`** (if not already present):
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY . /app
   RUN pip install --no-cache-dir -r requirements.txt
   EXPOSE 5050
   CMD ["python", "application.py"]
   ```
3. **Build and Run the Container**:
   ```bash
   docker build -t bike-price-predictor .
   docker run -d -p 5050:5050 bike-price-predictor
   ```

### 3. Deployment via CI/CD (AWS Elastic Beanstalk)
1. Launch an EBS environment configured with the Python platform.
2. Set up AWS CodePipeline connected to your GitHub repository.
3. Configure `.ebextensions/python.config` to launch your Flask application (`application.py`).
4. Push updates to your GitHub branch to trigger automatic deployment.
