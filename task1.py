# Titanic Dataset - Data Cleaning, Preprocessing, and Outlier Removal

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Step 1: Load the dataset
data = pd.read_csv('Titanic-Dataset.csv')

# Step 2: Show basic info
print("Before Cleaning:")
print(data.info())
print("\nMissing values:\n", data.isnull().sum())

# Step 3: Handle missing values
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop(columns=['Cabin'], inplace=True)

# Step 4: Encode categorical data
label = LabelEncoder()
data['Sex'] = label.fit_transform(data['Sex'])  # Male=1, Female=0
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# Step 5: Visualize outliers using boxplots
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
sns.boxplot(y=data['Age'])
plt.title('Boxplot - Age')
plt.subplot(1, 2, 2)
sns.boxplot(y=data['Fare'])
plt.title('Boxplot - Fare')
plt.tight_layout()
plt.show()

# Step 6: Remove outliers using IQR method
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return df[(df[column] >= lower) & (df[column] <= upper)]

data = remove_outliers(data, 'Age')
data = remove_outliers(data, 'Fare')

# Step 7: Normalize/standardize numeric data
scaler = StandardScaler()
data[['Age', 'Fare']] = scaler.fit_transform(data[['Age', 'Fare']])

# Step 8: Final dataset info
print("\nAfter Cleaning & Removing Outliers:")
print(data.info())
print("\nCleaned Data Sample:\n", data.head())

# Step 9: Save cleaned data
data.to_csv('Cleaned_Titanic.csv', index=False)
