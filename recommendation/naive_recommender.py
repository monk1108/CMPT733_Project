import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from bs4 import BeautifulSoup
import jieba
import numpy as np

class Content_recommender:
    def __init__(self):
        self.df = pd.read_csv('iPhone 15.csv')  # 修改CSV文件路径
        self.df.columns = ["shopTitle", "price", "title", "auction", "item_id", "realSales", "procity", "Trade-in", "Free Shipping Insurance", "Free Shipping", "Global Purchase", "Charity Goods", "CPU Model", "Camera Pixel", "Charging Power", "Screen Size", "Camera Number", "Highest Pixel"]


        self.df['title'] = self.df['title'].apply(lambda x: BeautifulSoup(x, "html.parser").get_text())

        self.tfidf = TfidfVectorizer(tokenizer=jieba.cut)
        self.df['title'] = self.df['title'].fillna('')
        tfidf_matrix = self.tfidf.fit_transform(self.df['title'])
        self.cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        self.indices = pd.Series(self.df.index, index=self.df['title']).drop_duplicates()

    def recommend(self, title):
        # Get the index of the item that matches the title
        idx = self.df[self.df['title'] == title].index

        # Get the pairwise similarity scores of all items with that item
        sim_scores = list(enumerate(self.cosine_sim[idx]))

        # Sort the items based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        scores_array = sim_scores[0][1]
        top_10_indices = np.argsort(scores_array)[-10:][::-1]

        # # Get the scores of the 10 most similar items
        # sim_scores = sim_scores[1:11]

        # # Get the item indices
        # item_indices = [i[0] for i in sim_scores]

        return self.df.iloc[top_10_indices]

