import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os
from .config import MODELS_DIR, RANDOM_STATE, TEST_SIZE

class ModelTrainer:
    def train_model(self, df):
        print("Training model...")
        
        # Define features and target
        # We'll use a subset of features for demonstration
        features = ['likes', 'dislikes', 'comment_count', 'title_length', 'tag_count', 'publish_hour', 'category_id']
        target = 'views'
        
        # Ensure only numeric columns are used (just in case)
        X = df[features]
        y = df[target]
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE)
        
        # Initialize and train model
        model = RandomForestRegressor(n_estimators=100, random_state=RANDOM_STATE, n_jobs=-1)
        model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        print(f"Model Performance:")
        print(f"MSE: {mse:.2f}")
        print(f"R2 Score: {r2:.4f}")
        
        # Save model
        model_path = os.path.join(MODELS_DIR, 'random_forest_model.pkl')
        joblib.dump(model, model_path)
        print(f"Model saved to {model_path}")
        
        return model, r2
