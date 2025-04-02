import os
import subprocess
import sys

# Step 1: Create and activate virtual environment
VENV_DIR = "venv"

if not os.path.exists(VENV_DIR):
    print("Creating virtual environment...")
    subprocess.run([sys.executable, "-m", "venv", VENV_DIR])

# Activate virtual environment
activate_script = os.path.join(VENV_DIR, "bin", "activate_this.py")
exec(open(activate_script).read(), {'__file__': activate_script})

# Step 2: Install dependencies
print("Installing dependencies...")
subprocess.run([f"{VENV_DIR}/bin/pip", "install", "--break-system-packages", "pandas", "psycopg2", "matplotlib", "scikit-learn", "joblib"])

# Step 3: Import required libraries
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import psycopg2

# Step 4: Define database connection
def get_db_connection():
    return psycopg2.connect(
        dbname="mbarreras_db",
        user="your_user",
        password="your_password",
        host="localhost",
        port="5432"
    )

# Step 5: Train the model
def train_model():
    conn = get_db_connection()
    df = pd.read_sql("SELECT * FROM customer", conn)
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
