# CMPT733 Project

## Project Overview

This project encompasses a comprehensive analysis of mobile phone data sourced from Taobao.com, China's largest e-commerce platform. It involves multiple components aimed at data extraction, visualization, predictive modeling, and a recommendation system.

## Project Architecture

The project is structured into five distinct parts:

- **Data Scraping**: 
  - Utilizes custom scraping scripts to gather data on mobile phones from Taobao.com over the past month.
  
- **Visualization**: 
  - Employs visualization techniques to present insights derived from the processed data. This includes visualizations of sales across different provinces, price ranges, and geographical maps.
  
- **Prediction**: 
  - Implements predictive modeling to identify underlying patterns within the product data. These patterns are then utilized to forecast the sales of specific products based on their features.
  
- **Recommendation System**: 
  - Develops a recommendation engine capable of suggesting the ten most similar mobile phones based on a user-selected item.

## Implementation Details

- **Data Scraping**: 
  1. Run `python data_scraping/taobao_scraper.py` to scrape raw data of the desired product. This script requires input such as the product name, start page, and end page.
  2. Execute `python data_scraping/data_cleaning.py` to clean and organize the scraped raw data, including standardizing product names, extracting sales data, and other relevant features.
  3. Utilize `python data_scraping/data_screening.py` to screen the cleaned data and remove outliers, ensuring data quality.
  4. Optionally merge search results of different products using `python data_scraping/join_table.py`.

- **Visualization**: 
  - Launch the visualization application using `python visualization/app.py`. The output will be accessible via a local web page.

- **Prediction**: 
  - Execute the code blocks within `prediction/graph_analysis.ipynb` to perform graph analysis and predictive modeling.

- **Recommendation System**: 
  1. Obtain recommendation results for a specific product by running `python recommendation/recommender.py`.
  2. Interact with the recommendation system using `python recommendation/app.py`. Input the product title and item ID to receive the top 10 related product recommendations.
