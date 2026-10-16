<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=180&section=header&text=Retail%20Sales%20Forecasting&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Predict%20daily%20store%20sales%20with%20machine%20learning&descAlignY=60&descSize=18" width="100%"/>
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=36BCF7&center=true&vCenter=true&width=600&lines=54+stores+%C2%B7+33+product+families;ARIMA+%C2%B7+Prophet+%C2%B7+XGBoost+%C2%B7+LSTM;Tracked+with+MLflow;Live+Streamlit+dashboard" alt="Typing SVG"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/XGBoost-EC6B23?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white"/>
</p>

## What is this?

A supermarket chain needs to know **how much it will sell** to order the right amount of stock.

We used the data of **Corporación Favorita**, a big grocery chain in Ecuador, from the [Kaggle Store Sales competition](https://www.kaggle.com/c/store-sales-time-series-forecasting). We trained several models to predict **daily sales** for each store and product family.

## How it works

```mermaid
flowchart LR
    A[Raw sales data] --> B[Clean + add features<br/>date, holidays, promotions, oil price]
    B --> C[EDA]
    C --> D[Train models<br/>ARIMA · Prophet · XGBoost · LSTM]
    D --> E[MLflow tracking]
    E --> F[Best model → Streamlit app]
```

## Models we tried

| Model | Notebook |
|-------|----------|
| ARIMA + Prophet | `models/Arima&prophet_model.ipynb` |
| XGBoost ✅ used in the app | `models/XGboost_model.ipynb` |
| LSTM | `models/lstm-model (1).ipynb` |
| K-Means (store clusters) | `models/K-MeansModel.ipynb` |

## The app

The Streamlit app has 5 pages:

| Page | What you can do |
|------|-----------------|
| 🏠 **Home** | Project overview |
| 🔎 **Data Filtering** | Search and filter the data |
| 📊 **Data Analysis** | Interactive charts: sales by month, day, promotions and transactions |
| 🔮 **Data Prediction** | Pick a store, date and cluster and get the predicted sales from XGBoost |
| 🧪 **MLflow** | Train the model again and log the run in MLflow |

## How to run

```bash
pip install -r requirements.txt
streamlit run main.py
```

To see the MLflow runs:

```bash
mlflow ui
```

Then open http://localhost:5000

## Files

```
├── main.py              # app menu
├── Home.py              # home page
├── Filtering.py         # data filtering page
├── Analysis.py          # charts page
├── Prediction.py        # prediction page (XGBoost)
├── ML_Flow.py           # MLflow training page
├── models/              # notebooks for each model
├── new_model (1).pkl    # trained XGBoost model
└── subset_data.csv      # sample data for the app
```

## Team

Built as a team project at the **Digital Egypt Pioneers Initiative (DEPI)**:

- [Emad Mostafa](https://github.com/3madMostafa)
- [Abdelrahman Zahran](https://github.com/AbdoZahran)
- [Omar Sahwan](https://github.com/OmarSahwan)
- [heka2002](https://github.com/heka2002)

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,50:203a43,100:0f2027&height=100&section=footer" width="100%"/>
</p>
