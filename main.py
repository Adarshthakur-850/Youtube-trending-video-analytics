from src.data_loader import DataLoader
from src.preprocessing import Preprocessor
from src.feature_engineering import FeatureEngineer
from src.visualization import Visualizer
from src.model import ModelTrainer

def main():
    print("Starting YouTube Trending Video Analysis Pipeline...")
    
    # 1. Load Data
    loader = DataLoader()
    df = loader.load_data()
    df = loader.clean_data(df)
    
    # 2. Feature Engineering
    fe = FeatureEngineer()
    df = fe.add_features(df)
    
    # 3. Preprocessing
    pp = Preprocessor()
    df = pp.extract_time_features(df)
    df = pp.encode_categorical(df)
    
    # 4. Visualization
    viz = Visualizer()
    viz.plot_correlation_heatmap(df)
    viz.plot_views_distribution(df)
    viz.plot_top_categories(df)
    
    # 5. Modeling
    trainer = ModelTrainer()
    trainer.train_model(df)
    
    print("Pipeline completed successfully!")

if __name__ == "__main__":
    main()
