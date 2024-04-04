from flask import Flask, render_template, request, jsonify
import pandas as pd
from KNN_recommender import Taobao_KNN_recommender
from naive_recommender import Content_recommender

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    name = data['itemName']
    id = int(data['itemId'])

    # Naive Recommender
    naive_test = Content_recommender()
    naive_result = naive_test.recommend(title=name)

    # KNN Recommender
    knn_test = Taobao_KNN_recommender()
    knn_result = knn_test.recommend(id, 10)

    # Combine results
    combined_result = pd.concat([naive_result, knn_result])
    combined_result = combined_result.sort_values(by='realSales', ascending=False)
    combined_result = combined_result.head(10)

    # Convert DataFrame to JSON
    combined_json = combined_result.to_json(orient='records')
    print(combined_result)
    # 转换标题中的特殊字符
    combined_result['title'] = combined_result['title'].str.replace('<span class=H>', '').str.replace('</span>', '')
    combined_result['auction'] = combined_result['auction'].apply(lambda x: f"<a href='https://{x}' target='_blank'>{x}</a>")

    # 将 DataFrame 转换为 HTML 表格
    html_table = combined_result.to_html(index=False, escape=False, classes='shop-table')
    print(html_table)

    return jsonify({'htmlTable': html_table})

if __name__ == '__main__':
    app.run(debug=True)
