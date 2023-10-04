import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import numpy as np
import streamlit as st

model=pd.read_csv(r'C:\Users\yuvan\Downloads\project\data\full-data.csv')



TargetVariable=['Value']
Predictors=['RAA', 'Wins', 'EFscore', 'Salary']
X=model[Predictors].values
Y=model[TargetVariable].values
X_train_val, X_test, y_train_val, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.25, random_state=0)

imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
imputer.fit(X[:, :])
X[:, :] = imputer.transform(X[:, :])



xgb_model = XGBRegressor()
xgb_model.fit(X_train_val, y_train_val)

st.title('IPL PLAYER VALUE PREDICTOR')
RAA=st.number_input("RAA")
Wins=st.number_input("Wins(1 to 100%)")
EFscore=st.number_input("EFscore(-1 to 1)")
Salary=st.number_input("Salary")
data = {'RAA': RAA,
                'Wins': Wins,
                'EFscore': EFscore,
                'Salary': Salary
                }
features = pd.DataFrame(data, index=[0])
inputfe=features
if st.button("Predict"): 
        prediction = xgb_model.predict(inputfe)
        st.header('Prediction of Value (in currency)')
        st.write(prediction)
        st.write('---')


