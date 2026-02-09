<<<<<<< HEAD
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLOTS_DIR = os.path.join(BASE_DIR, 'plots')
MODELS_DIR = os.path.join(BASE_DIR, 'models')

os.makedirs(PLOTS_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)

DATA_URL = "https://raw.githubusercontent.com/talesmarra/youtube_data_analysis/master/data/USvideos.csv"

RANDOM_STATE = 42
TEST_SIZE = 0.2
=======
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLOTS_DIR = os.path.join(BASE_DIR, 'plots')
MODELS_DIR = os.path.join(BASE_DIR, 'models')

os.makedirs(PLOTS_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)

DATA_URL = "https://raw.githubusercontent.com/talesmarra/youtube_data_analysis/master/data/USvideos.csv"

RANDOM_STATE = 42
TEST_SIZE = 0.2
>>>>>>> 7ffa54c5391df4d08257f88f232dda529a6dfd62
