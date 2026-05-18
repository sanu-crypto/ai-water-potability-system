# 💧 Water Potability Prediction using Machine Learning

A Machine Learning based web application that predicts whether water is safe for drinking using water quality parameters.  
This project uses a Random Forest Classifier along with Data Cleaning, Feature Engineering, KNN Imputation, and SMOTE balancing techniques.

---

# 🚀 Project Overview

The Water Potability Prediction System helps determine whether water is potable (safe for drinking) based on different chemical properties of water.

The project includes:

- Data Cleaning
- Missing Value Handling
- Feature Engineering
- SMOTE for Class Balancing
- Random Forest Machine Learning Model
- Streamlit Web Application
- Probability-based Prediction Output

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Random Forest Classifier
- KNN Imputer
- SMOTE (Imbalanced Learning)

---

# 📊 Input Features

The model uses the following water quality parameters:

| Feature | Description |
|---|---|
| pH | Acidic/Basic nature of water |
| Hardness | Mineral concentration |
| Solids | Total dissolved solids |
| Chloramines | Chloramine level |
| Sulfate | Sulfate concentration |
| Conductivity | Electrical conductivity |
| Organic Carbon | Organic carbon content |
| Trihalomethanes | Chemical compounds in water |
| Turbidity | Water clarity |

---

# ⚙️ Machine Learning Workflow

## 1️⃣ Data Loading
The dataset is loaded using Pandas.

## 2️⃣ Data Cleaning
- Removed duplicate values
- Checked missing values

## 3️⃣ Missing Value Handling
Used **KNN Imputer** to fill missing values intelligently.

## 4️⃣ Feature Engineering
Created additional features:

- ph_Hardness
- Solids_Conductivity
- Chloramines_Turbidity
- Organic_Trihalo

## 5️⃣ Train-Test Split
Dataset split into training and testing sets.

## 6️⃣ Class Imbalance Handling
Applied **SMOTE** to balance potable and non-potable classes.

## 7️⃣ Model Training
Used **Random Forest Classifier** with optimized parameters.

## 8️⃣ Model Evaluation
Evaluated using:

- Accuracy Score
- Classification Report
- Confusion Matrix

## 9️⃣ Model Saving
Saved:
- Trained model
- KNN Imputer
- Feature column names

using Pickle files.

---

# 🧠 Model Used

## Random Forest Classifier

### Parameters Used:

```python
RandomForestClassifier(
    n_estimators=600,
    max_depth=25,
    min_samples_split=2,
    min_samples_leaf=1,
    max_features="sqrt",
    class_weight="balanced_subsample",
    random_state=42,
    n_jobs=-1
)
```

---

# 📁 Project Structure

```text
water-potability-prediction/
│
├── app.py
├── model_training.py
├── water_potability.csv
├── water_potability_rf_model.pkl
├── water_potability_imputer.pkl
├── water_potability_columns.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ▶️ How To Run The Project

## Step 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/water-potability-prediction.git
```

---

## Step 2️⃣ Open Project Folder

```bash
cd water-potability-prediction
```

---

## Step 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## Step 4️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

# 💻 Streamlit Web Application

The Streamlit application allows users to:

- Enter water quality values
- Predict water potability
- View prediction probabilities
- Get instant results

---

# 📈 Prediction Output

The app predicts:

✅ Water is Safe for Drinking

or

❌ Water is Not Safe for Drinking

along with prediction probabilities.

---

# 📦 requirements.txt

```txt
streamlit
numpy
pandas
scikit-learn
imbalanced-learn
```

---

# 📌 Key Features

- Interactive Web Interface
- Real-time Prediction
- Feature Engineering
- Missing Value Handling
- Class Balancing using SMOTE
- Probability-Based Results
- Clean and User-Friendly Design

---

# 🔮 Future Enhancements

- Deploy on Streamlit Cloud
- Add Data Visualization Dashboard
- Use Deep Learning Models
- Add Water Quality Report Generation
- Mobile Friendly UI
- API Integration

---

# 📷 Sample Workflow

1. User enters water quality parameters
2. Data preprocessing applied
3. Feature engineering performed
4. Random Forest model predicts result
5. Streamlit displays prediction

---

# 👨‍💻 Author

## Sayan Das

Final Year B.E. Student – Artificial Intelligence & Data Science

---

# ⭐ GitHub Repository

If you like this project, give it a ⭐ on :contentReference[oaicite:0]{index=0}
