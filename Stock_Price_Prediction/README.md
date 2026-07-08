# 📈 Stock Price Prediction & Analysis Dashboard

An interactive, AI-powered stock price prediction and trend analysis dashboard. This application utilizes a Deep Learning **LSTM (Long Short-Term Memory) Neural Network** built with TensorFlow/Keras to predict future stock prices based on historical time-series data. It features a Flask web dashboard that allows users to analyze any stock ticker using real-time data fetched from Yahoo Finance.

---

## 📑 Table of Contents
- [Overview](#-overview)
- [Project Structure](#-project-structure)
- [Key Features](#-key-features)
- [Model Architecture](#-model-architecture)
- [Quick Start](#-quick-start)
- [How to Run the Web App](#-how-to-run-the-web-app)
- [Jupyter Notebook Workstation](#-jupyter-notebook-workstation)
- [Screenshots & Visuals](#-screenshots--visuals)

---

## 🎯 Overview
Predicting stock market trends is a classic time-series forecasting problem. This project walks through the entire pipeline:
1. **Data Acquisition**: Fetching real-time and historical stock data directly via the Yahoo Finance API (`yfinance`).
2. **Data Processing**: Cleaning data, splitting train/test datasets, and normalizing values using `MinMaxScaler` (0 to 1 range).
3. **Model Development**: Training an LSTM recurrent neural network on historical data (specifically Google Stock Price records) to learn long-term sequences.
4. **Interactive Application**: Exposing the predictive model through a Flask backend, computing dynamic Technical Indicators (20, 50, 100, 200-day Exponential Moving Averages), generating charts, and presenting them on a modern web dashboard.

---

## 🏗️ Project Structure
```text
.
├── LICENSE                          # MIT License
├── OutPut.gif                       # Demonstration of the running dashboard
├── README.md                        # Project documentation (this file)
├── Dataset/
│   └── Data.md                      # Details about the dataset
├── Models/
│   ├── Stock_Price_Prediction.ipynb  # Jupyter Notebook for LSTM training and evaluation
│   └── stock_dl_model.h5            # Pre-trained TensorFlow LSTM model
└── Website/
    ├── app.py                       # Main Flask web application
    ├── requirements.txt             # Web application dependencies
    ├── stock_dl_model.h5            # Copy of the pre-trained LSTM model for deployment
    ├── Google_stock_data.csv        # Local cached dataset for testing
    ├── static/                      # Generated charts and client assets (CSS)
    └── templates/
        └── index.html               # Frontend dashboard template (Jinja2)
```

---

## ✨ Key Features
- 🔍 **Dynamic Symbol Search**: Analyze any global stock ticker supported by Yahoo Finance (e.g., `AAPL`, `MSFT`, `TSLA`, `BTC-USD`).
- 📊 **Descriptive Data Summary**: Displays statistics such as Mean, Standard Deviation, Min, Max, and Percentiles for the selected stock.
- 📈 **Exponential Moving Averages (EMA)**:
  - Generates charts showing 20-day & 50-day EMA trends (useful for short-term support/resistance).
  - Generates charts showing 100-day & 200-day EMA trends (useful for long-term trend analysis).
- 🤖 **Deep Learning Predictions**: Compares original closing prices vs LSTM-predicted prices on a visualization plot.
- 📥 **Dataset Export**: Download the extracted historical stock data directly as a `.csv` file.

---

## 🧠 Model Architecture
LSTMs are a special kind of Recurrent Neural Network (RNN) capable of learning long-term dependencies.
* **Input Window**: 100 timesteps (using the past 100 days of stock prices to predict the price of the next day).
* **Layers**: Stacked LSTM layers with dropout layers to prevent overfitting.
* **Loss Function**: Mean Squared Error (MSE) optimized using Adam.

---

## 🚀 Quick Start

### 1. Prerequisites
Make sure you have Python 3.9+ installed on your local machine.

### 2. Set Up a Virtual Environment
Navigate to the `Website` directory and set up a virtual environment:
```bash
cd Website
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

---

## 💻 How to Run the Web App
1. With the virtual environment active, run:
   ```bash
   python app.py
   ```
2. The web server starts on port `5052`. Open your browser and go to:
   ```text
   http://localhost:5052
   ```
3. Enter any stock symbol (e.g., `NVDA`) and submit to generate price predictions and trend lines.

---

## 📓 Jupyter Notebook Workstation
If you wish to re-train the LSTM model or run exploratory data analysis:
1. Open the notebook in `Models/Stock_Price_Prediction.ipynb`.
2. Follow the cells to download the Google stock dataset, define the LSTM architecture, train the model, and export the `.h5` file.
