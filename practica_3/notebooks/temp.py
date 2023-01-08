# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import plotly.express as px
from scipy.stats import pearsonr
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import scipy.stats as stats
from scipy.stats import chi2_contingency
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import joblib
import geopandas
from textblob import Word
import nltk
nltk.download('stopwords')# preprocessing text
nltk.download('wordnet')
import string
import re # regular expression
from textblob import TextBlob
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')