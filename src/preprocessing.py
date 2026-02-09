import pandas as pd
from sklearn.preprocessing import LabelEncoder

class Preprocessor:
    def __init__(self):
        self.label_encoders = {}

    def extract_time_features(self, df):
        print("Extracting time features...")
        df['publish_hour'] = df['publish_time'].dt.hour
        df['publish_day'] = df['publish_time'].dt.day_name()
        df['publish_month'] = df['publish_time'].dt.month
        return df

    def encode_categorical(self, df):
        print("Encoding categorical features...")
        for col in ['category_id', 'publish_day']:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            self.label_encoders[col] = le
        return df
