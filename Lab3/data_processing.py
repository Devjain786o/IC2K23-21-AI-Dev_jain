
"""
Data Preprocessing and Exploratory Data Analysis
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split


project_root = Path(__file__).resolve().parent.parent
output_dir = Path(__file__).resolve().parent / "outputs"
output_dir.mkdir(parents=True, exist_ok=True)


# 1. Performing NumPy operations
arr = np.array([10, 20, 30, 40, 50])

print("NUMPY OPERATIONS")
print("-" * 35)

print("Array:", arr)
print("Average:", arr.mean())
print("Highest Value:", arr.max())
print("Lowest Value:", arr.min())


# 2. Reading the dataset
data = pd.read_csv(
    project_root / "dataset" / "student.csv",
    sep="|",
    skiprows=[1],
    skipfooter=1,
    usecols=range(1, 7),
    skipinitialspace=True,
    na_values=["—", "NA", "N/A"],
    engine="python",
)
data.columns = data.columns.str.strip()
for column in data.select_dtypes(include=["object", "string"]).columns:
    data[column] = data[column].str.strip()

for column in ["CGPA", "Internships"]:
    data[column] = pd.to_numeric(data[column], errors="coerce")

print("\nORIGINAL DATA")
print(data.head())

print("\nDATASET DETAILS")
data.info()

# 3. Performing exploratory data analysis
print("\nTOTAL ROWS AND COLUMNS:", data.shape)

print("\nDATA DESCRIPTION")
print(data.describe())

print("\nCHECKING NULL VALUES")
print(data.isna().sum())

print("\nPLACEMENT DETAILS")
print(data["Placement"].value_counts())


# 4. Creating visualizations

plt.figure(figsize=(6, 4))
sns.countplot(x="Placement", data=data)
plt.title("Student Placement Distribution")
plt.savefig(output_dir / "placement_distribution.png")
plt.close()

plt.figure(figsize=(6, 4))
sns.histplot(data["CGPA"], bins=6, kde=True)
plt.title("CGPA Distribution")
plt.savefig(output_dir / "cgpa_distribution.png")
plt.close()


# 5. Filling missing values

data["CGPA"] = data["CGPA"].fillna(data["CGPA"].median())

data["Internships"] = data["Internships"].fillna(
    data["Internships"].median()
)

for col in ["Gender", "Course"]:
    data[col] = data[col].fillna(data[col].mode()[0])

print("\nNULL VALUES AFTER PREPROCESSING")
print(data.isnull().sum())


# 6. Removing unwanted column
data = data.drop(columns=["Student_ID"])


# 7. Converting categorical data into numerical form

label_encoder = LabelEncoder()

categorical_columns = ["Gender", "Course", "Placement"]

for col in categorical_columns:
    data[col] = label_encoder.fit_transform(data[col])

print("\nDATA AFTER LABEL ENCODING")
print(data.head())


# 8. Selecting important features

features = data.drop(columns=["Placement"])
target = data["Placement"]

feature_selector = SelectKBest(score_func=chi2, k=3)

selected_data = feature_selector.fit_transform(features, target)

important_features = features.columns[
    feature_selector.get_support()
]

print("\nIMPORTANT FEATURES")
print(list(important_features))


# 9. Splitting data into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(
    selected_data,
    target,
    test_size=0.25,
    random_state=42,
    stratify=target
)

print("\nTRAINING SET SIZE:", X_train.shape)
print("TESTING SET SIZE:", X_test.shape)


# 10. Saving the processed dataset

data.to_csv(
    output_dir / "cleaned_dataset.csv",
    index=False
)

print("\nProcessed dataset saved successfully!")
print("DATA PREPROCESSING AND EDA COMPLETED!")
