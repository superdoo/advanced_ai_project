
#Trains a logistic regression model for churn prediction.

import pandas as pd
import joblib
import psycopg2
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from db_connector import get_db_connection






def train_model():
    conn = get_db_connection()
    df = pd.read_sql("SELECT * FROM customers", conn)
    conn.close()
    
    X = df[['age', 'income', 'account_balance']]
    y = df['churn']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    joblib.dump(model, "model.pkl")
    print("Model trained and saved.")

if __name__ == "__main__":
    train_model()