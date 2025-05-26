# Task-1-Data-Cleaning
- Cleaned and preprocessed Titanic dataset including null handling, encoding, normalization, and outlier treatment.

- This repository contains the first task of the AI & ML Internship: Data Cleaning and Preprocessing using the Titanic Dataset. The goal is to prepare raw data for Machine Learning by performing essential preprocessing steps.

# Task Details

- Task Name: Task 1 - Data Cleaning & Preprocessing

- Conducted by: AI & ML Internship

- Objective: To clean raw Titanic dataset and make it suitable for ML models

- Tools Used: Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn

# Resource Used

Original Dataset - [Titanic-Dataset.csv](https://github.com/user-attachments/files/20443825/Titanic-Dataset.csv)

# Dataset Overview

- The Titanic dataset contains data of passengers who were on board the Titanic ship. It includes details like age, sex, fare, class, survival status, and more.

Columns in the Dataset:
- PassengerId, Survived (0 = No, 1 = Yes), Pclass (Ticket class: 1 = 1st, 2 = 2nd, 3 = 3rd), Name, Sex, Age, SibSp (Number of siblings/spouses aboard), Parch (Number of parents/children aboard), Ticket, Fare, Cabin, Embarked (Port of Embarkation: C = Cherbourg, Q = Queenstown, S = Southampton)

# Objectives

- Understand and explore the dataset.
- Handle missing values effectively.
- Encode categorical features for ML compatibility.
- Standardize numerical columns (Age, Fare).
- Visualize and remove outliers.
- Save the cleaned dataset for further use.

# Exploratory Data Analysis (EDA)
1. Missing Values:
- Filled Age with median.
- Filled Embarked with mode.
- Dropped Cabin due to high missingness.

2. Encoding:
- Applied Label Encoding to Sex.
- Applied One-Hot Encoding to Embarked.

3. Outliers:
- Detected and removed outliers using the IQR method for Age and Fare.

4. Standardization:
- Used StandardScaler to normalize Age and Fare.

# Insights
- Age and Fare contained significant outliers which were visualized using boxplots.
- Categorical values like Sex and Embarked were successfully encoded.
- Null values in critical features were handled to avoid bias.
- After preprocessing, the data is now ML-ready.

# Visualizations
- Boxplot- Age
