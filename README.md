# 🎓 Student Score Prediction  

📖 A machine learning project to predict **student exam scores** based on study hours and related features.  
This project demonstrates data preprocessing, training regression models, evaluating performance, and visualizing results.  

---

## 🚀 Features  
- Load and preprocess student dataset  
- Apply **Linear Regression** and **Polynomial Regression**  
- Compare model performance using evaluation metrics  
- Visualize:  
  - Data distributions & correlations  
  - Regression line & polynomial curve fit  
  - Model predictions vs actual scores  
- Clean and well-documented code with explanations  

---

## 📊 Dataset  
- Input features such as: **study hours, attendance, etc.**  
- Target variable: **student exam scores**  
- Preprocessed to remove duplicates & handle missing values  

---

## ⚙️ Getting Started  

### ✅ Prerequisites  
- Python 3.7 or later  
- pip or other package manager
- ## 🧠 Models Used  

### 1️⃣ Linear Regression  
- Fits a straight line to predict scores based on features.  
- Provides baseline performance.  

### 2️⃣ Polynomial Regression  
- Captures non-linear relationships between features and scores.  
- Improves prediction accuracy over simple linear regression.  

---

## 📈 Performance  

The models were evaluated using:  
- **R² Score**  
- **Mean Squared Error (MSE)**  
- **Mean Absolute Error (MAE)**  

✅ **Polynomial Regression outperformed Linear Regression** in capturing non-linear patterns and gave better accuracy.  

---

## 🔍 Example Prediction  

Input: `Study Hours = 7`  

- **Linear Regression Prediction:** 65  
- **Polynomial Regression Prediction:** 70  
- **Actual Score:** 72  


### 🔧 Installation  
Clone the repository:  
```bash
git clone https://github.com/your-username/student-score-prediction.git
cd student-score-prediction
