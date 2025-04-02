import os
import subprocess
import sys
import stat

VENV_DIR = "venv"

# Step 1: Create the virtual environment if it doesn't exist
if not os.path.exists(VENV_DIR):
    print("Creating virtual environment...")
    subprocess.run([sys.executable, "-m", "venv", VENV_DIR])

# Step 2: Ensure pip has execute permissions
pip_exec = os.path.join(VENV_DIR, "bin", "pip")
python_exec = os.path.join(VENV_DIR, "bin", "python")

# Fix permissions
if os.path.exists(pip_exec):
    os.chmod(pip_exec, stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR)

# Step 3: Install dependencies
print("Installing dependencies...")
subprocess.run([python_exec, "-m", "pip", "install", "--break-system-packages", "-r", "advanced_ai_project/requirements.txt"])

# Step 4: Import dependencies
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import psycopg2

# Step 5: Define database connection
def get_db_connection():
    return psycopg2.connect(
        dbname="mbarreras_db",
        user="mbarreras",
        password="B133eras",
        host="localhost",
        port="5432"
    )

# Step 6: Train the model
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
