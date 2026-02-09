import pandas as pd
from .config import DATA_URL

class DataLoader:
    def load_data(self):
        print("Loading data from URL...")
        df = pd.read_csv(DATA_URL)
        return df

    def clean_data(self, df):
        print("Cleaning data...")
        df = df.drop_duplicates(subset=['video_id'])
        df = df.dropna()
        
        df['publish_time'] = pd.to_datetime(df['publish_time'])
        df['trending_date'] = pd.to_datetime(df['trending_date'], format='%y.%d.%m')
        
        return df
