import pandas as pd

class FeatureEngineer:
    def add_features(self, df):
        print("Adding engineered features...")
        df['like_rate'] = df['likes'] / (df['views'] + 1)
        df['dislike_rate'] = df['dislikes'] / (df['views'] + 1)
        df['comment_rate'] = df['comment_count'] / (df['views'] + 1)
        
        df['title_length'] = df['title'].apply(len)
        df['tag_count'] = df['tags'].apply(lambda x: len(x.split('|')))
        
        return df
