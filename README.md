# Human Survival Status Prediction after Heart Attack using ML

[Heart Attack]([[https://example.com/path/to/heart-attack-image.png](https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMyocardial_infarction&psig=AOvVaw26xebCvHNUKH6kePOm_A8i&ust=1690182286575000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCJD4_fmhpIADFQAAAAAdAAAAABAE)](https://www.istockphoto.com/photo/heart-attack-concept-gm1128931450-298046977))

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Web App](#web-app)

## Introduction

The Human Survival Status Prediction after Heart Attack using ML project is a machine learning-based application that aims to predict the survival status of patients who have experienced a heart attack. It utilizes a dataset containing various medical features of patients and their corresponding survival outcomes to build and evaluate a predictive model.

This README provides an overview of the project, instructions for setting up the environment, guidelines for model training, and information on how to contribute.

## Dataset

The dataset used for training and evaluation can be found at [([https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data])
- It contains the following columns:

- `anaemia`: Decrease of red blood cells or hemoglobin (boolean)
- `Creatinine_phosphokinase`: Level of the CPK enzyme in the blood (mcg/L)
- `diabetes`: If the patient has diabetes (boolean)
- `ejection_fraction`: Percentage of blood leaving the heart at each contraction (percentage)
- `high_blood_pressure`: If the patient has hypertension (boolean)
- `platelets`: Platelets in the blood (kiloplatelets/mL)
- `serum_creatinine`: Level of serum creatinine in the blood (mg/dL)
- `erum_sodium`: Level of serum sodium in the blood (mEq/L)
- `Sex`: Woman or man (boolean)
- `Death Event`: Survived or not survived (boolean)
  
## Installation

1. Clone the repository:

```bash
git clone https://github.com/Surendradhaka123/Human-Survival-Status-Predictor-using-ML.git
cd Human-Survival-Status-Predictor-using-ML
```

2. Set up a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To use the trained model for predicting survival status after a heart attack, follow these steps:

1. Ensure you have installed the required dependencies as mentioned in the [Installation](#installation) section.

2. Prepare your data in the same format as the dataset used for training.

3. Load the trained model:

```python
import joblib

# Load the model from file
model = joblib.load("model.pkl")
```

4. Preprocess your data to make predictions:

```python
# Assuming 'data' is a pandas DataFrame containing your data
predictions = model.predict(data)
```

5. `predictions` will now contain the predicted survival status for each entry in your dataset.

   ## Web App

   I have developed a web app for this model, where you can directly enter the required value and get the prediction. I have made this app using Streamlit and deployed it on Streamlit Cloud.

   You can check out this app by folllowing the link. [web app](https://surendradhaka123-ml-projects-app-k56xaz.streamlit.app/)

---

We hope this README helps you understand the Human Survival Status Prediction after Heart Attack using ML project. If you have any questions or need further assistance, please don't hesitate to reach out.

Thank you for using our project!
