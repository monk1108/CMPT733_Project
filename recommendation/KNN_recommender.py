import pandas as pd
from surprise import Reader, Dataset
from surprise import KNNBaseline
from surprise import KNNWithMeans
from surprise import KNNBasic


class Taobao_KNN_recommender:
    def __init__(self, mode=0):
        self.index = pd.read_csv('iPhone 15.csv')  # Load Taobao iPhone 15 products dataset
        self.reader = Reader(rating_scale=(0, None))  # Define rating scale according to 'realSales'
        self.ratings = self.index[['item_id', 'realSales']].copy()  # Use 'item_id' and 'realSales' as ratings
        self.ratings['userId'] = 1  # Dummy userId, as we're not dealing with users here
        data = Dataset.load_from_df(self.ratings[['userId', 'item_id', 'realSales']], self.reader)  # Load data
        trainset = data.build_full_trainset()
        sim_options = {'name': 'pearson_baseline', 'user_based': False}
        if mode == 0:
            self.algo = KNNBaseline(sim_options=sim_options)
        elif mode == 1:
            self.algo = KNNWithMeans(sim_options=sim_options)
        elif mode == 2:
            self.algo = KNNBasic(sim_options=sim_options)
        else:
            exit(0)

        self.algo.fit(trainset)

    def get_similar_products(self, item_id, num=10):
        item_inner_id = self.algo.trainset.to_inner_iid(item_id)
        item_neighbors = self.algo.get_neighbors(item_inner_id, k=num)
        item_neighbors = [self.algo.trainset.to_raw_iid(inner_id) for inner_id in item_neighbors]
        return item_neighbors

    def recommend(self, item_id, num=10):
        item_similar = self.get_similar_products(item_id, num)
        recommending = []
        
        # return the items whose item_id is in item_similar
        for i in item_similar:
            recommending.append(self.index[self.index['item_id'] == i])
        return pd.concat(recommending)



