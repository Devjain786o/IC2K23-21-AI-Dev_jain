# Lab 3 – Data Preprocessing and Exploratory Data Analysis

## Aim
To study and implement data preprocessing techniques using NumPy, Pandas, Matplotlib, Seaborn, and Scikit-learn.

## Problem Statement
To analyze a student placement dataset and perform data cleaning, missing value treatment, label encoding, feature selection, and data visualization.

## Operations Performed

1. Numerical operations using NumPy.
2. Dataset loading using Pandas.
3. Exploratory Data Analysis (EDA).
4. Data cleaning and preprocessing.
5. Handling missing values.
6. Label Encoding of categorical data.
7. Feature selection using SelectKBest.
8. Splitting data into training and testing sets.
9. Data visualization using graphs.

## Libraries Used
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

## Algorithm

1. Import all required Python libraries.
2. Load the student placement dataset.
3. Display the dataset using `head()`, `info()`, and `describe()`.
4. Check the dataset for missing values.
5. Replace missing numerical values with their median.
6. Replace missing categorical values with their mode.
7. Convert categorical columns into numerical values using Label Encoding.
8. Select important features using SelectKBest.
9. Divide the dataset into training and testing sets.
10. Generate visualizations and save the processed dataset.

## Results
The student placement dataset was successfully loaded and analyzed. Missing values were handled, categorical columns were converted into numerical values, important features were selected, and the dataset was divided into training and testing sets.

## Output Files
1. `placement_distribution.png`
2. `cgpa_distribution.png`
3. `cleaned_dataset.csv`

## Performance Analysis
This lab focuses on data preprocessing and exploratory analysis rather than training a prediction model. Therefore, classification metrics such as accuracy, precision, recall, and F1-score are not applicable.

## Learning Outcomes

1. Learned numerical operations using NumPy.
2. Understood data handling using Pandas.
3. Practised Exploratory Data Analysis.
4. Learned different methods of handling missing values.
5. Understood Label Encoding and feature selection.
6. Learned to create data visualizations.
7. Understood the process of train-test splitting.

## Conclusion
The lab work demonstrated how raw datasets can be cleaned, analyzed, transformed, and prepared for machine learning applications. It provided practical knowledge of data preprocessing, exploratory data analysis, feature selection, and visualization techniques.