# Urban Crime Modeling and Prediction

This project analyzes socioeconomic factors associated with violent crime rates within urban communities using the Communities and Crime dataset from the UCI Machine Learning Repository. Five machine learning models were implemented to identify key predictors of violent crime and compare model performance.

The analysis focuses specifically on crime rates within predominatly urban communities

## Methods

Five modeling approaches were used to analyze the data:

**Linear Regression**  
Used as a baseline statistical model to estimate relationships between predictors and violent crime rates.

**Lasso Regression**  
Applies L1 regularization to reduce overfitting and perform automatic feature selection.

**Beta Regression**  
Used to model the already normalized dataset and discern which variables have the higest corrolation with crime rates.

**Decision Tree Classifier**  
Captures nonlinear relationships and interaction effects by splitting data into rule-based groups.

**Random Forest Classifier**  
Aggregates multiple decision trees to improve predictive accuracy and reduce variance.

## Model Evaluation

Classification models were then evaluated by compareing their accuracy, precision, recall, and F1 score

## Key Findings

Across multiple models, several variables consistently appeared as strong predictors of violent crime rates, including poverty, unemployment, education levels, housing instability, and family structure variables. These results suggest that socioeconomic conditions and community stability play a major role in explaining variation in violent crime rates across urban communities.

## Tools and Libraries

Python libraries used in this project include:

- pandas  
- numpy  
- matplotlib  
- seaborn  
- scikit-learn  
- statsmodels  

## Future Work

The methods used in this project can continously used to analyze new crime stasticts to compare with past data to identify new trends. The results of this project and future analyses can be used to better inform local authorities as to which policies would be the most effective at reducing crime rates. 

## Author

Tyler Crosbie  
M.S. Data Science  
University of California, Irvine
