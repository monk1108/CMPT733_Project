# CMPT733_Project

## Project Architecture
The project is made up of 5 parts:
- **Data Scraping**: scrape data from taobao.com
- **Visualization**: visualize the processed data
- **Prediction**: find data's inner pattern, and predict the sales of a product based on its features
- **Recommendation System**: recommend 10 most similar products based on one selected item

## Implementation Details
- **Data Scraping**: 
    1. Scrape raw data of the product you're interested in: `python taobao_scraper.py`. You need to enter the product name, start page and end page.
    2. Clean raw data to make product name, sales and other features organized: `python data_cleaning.py`.
    3. Screen data and drop outliers: `python data_screening.py`.
    4. Join search results of different products if you want: `python join_table.py`.
- **Visualization**: `python app.py` and the result will be available as a local web page.
- **Prediction**: run code blocks of `graph_analysis.ipynb`.
- **Recommendation System**: 
    1. To get recommendation results of a certain product, `python recommender.py`.
    2. To interact with the recomendation system, `python app.py`. Entering the product title and item id, you can get the top 10 related product recommendations.