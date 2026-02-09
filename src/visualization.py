import matplotlib.pyplot as plt
import seaborn as sns
import os
from .config import PLOTS_DIR

class Visualizer:
    def plot_correlation_heatmap(self, df):
        print("Generating correlation heatmap...")
        plt.figure(figsize=(10, 8))
        # Select numeric columns only
        numeric_df = df.select_dtypes(include=['float64', 'int64'])
        corr = numeric_df.corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Correlation Heatmap')
        plt.tight_layout()
        plt.savefig(os.path.join(PLOTS_DIR, 'correlation_heatmap.png'))
        plt.close()

    def plot_views_distribution(self, df):
        print("Generating views distribution plot...")
        plt.figure(figsize=(10, 6))
        sns.histplot(df['views'], bins=50, log_scale=True)
        plt.title('Distribution of Views (Log Scale)')
        plt.xlabel('Views')
        plt.ylabel('Count')
        plt.tight_layout()
        plt.savefig(os.path.join(PLOTS_DIR, 'views_distribution.png'))
        plt.close()

    def plot_top_categories(self, df):
        print("Generating top categories plot...")
        plt.figure(figsize=(12, 6))
        # Assuming category_id is encoded, we might want to map it back if we had the map, 
        # but for now we plot the encoded id or whatever is available.
        top_cats = df['category_id'].value_counts().head(10)
        sns.barplot(x=top_cats.index, y=top_cats.values)
        plt.title('Top 10 Trending Categories (by ID)')
        plt.xlabel('Category ID')
        plt.ylabel('Number of Videos')
        plt.tight_layout()
        plt.savefig(os.path.join(PLOTS_DIR, 'top_categories.png'))
        plt.close()
