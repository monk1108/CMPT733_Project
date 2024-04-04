import pandas as pd
from KNN_recommender import Taobao_KNN_recommender
from naive_recommender import Content_recommender

name = '新款Apple/苹果 iPhone 15 Plus 国行5G手机原封原装正品6.7英寸'
id = 739450006268


# naive
test = Content_recommender()
naive_result = test.recommend(title=name)
# # Return the top 10 most similar items, with their whole information like title, price, etc.
# # write to csv file
# naive_path = 'naive_result.csv'
# naive_result.to_csv(naive_path, index=False)

# KNN
test = Taobao_KNN_recommender()
knn_result = test.recommend(id, 10)  # Pass an item_id to get recommendations
# # save to csv file
# knn_path = 'KNN_result.csv'
# result_df = pd.DataFrame(knn_result, columns=['title'])
# result_df.to_csv(knn_path, index=False)

# combine naive_result and knn_result
# sort by realSales, from high to low
# select the top 10 results and save to a csv file
combined_result = pd.concat([naive_result, knn_result])
combined_result = combined_result.sort_values(by='realSales', ascending=False)
combined_result = combined_result.head(10)
combined_path = 'combined_result.csv'
combined_result.to_csv(combined_path, index=False)
