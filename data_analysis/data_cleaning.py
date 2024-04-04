import os
import pandas as pd
import re

# 定义CSV文件所在的文件夹路径
folder_path = 'recommender_results/'
new_folder_path = './'

# 获取文件夹中的所有CSV文件
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# 遍历每个CSV文件
for file in csv_files:
    # 读取CSV文件
    df = pd.read_csv(os.path.join(folder_path, file))

    # 将realSales列中的文本格式转换为整数，例如将'84人付款'转换为84
    df['realSales'] = df['realSales'].apply(lambda x: int(re.search(r'\d+', str(x)).group(0)) if re.search(r'\d+', str(x)) else 0)
 
    # create a new column to store the camera number of the phone
    # camere number is (the number of "+" + 1) in Camera Pixel
    df['Camera Number'] = df['Camera Pixel'].apply(lambda x: str(x).count('+') + 1 if '+' in str(x) else 1)
    # 将Camera Pixel列中的所有数字加单位保留， 例如“主摄像头5000万像素+超广角1200万像素+长焦（3X）1000万像素” 转换为5000万+1200万+（3X）1000万
    # 如果是 “亿”为单位的，转换为万为单位
    # 数字间用加号连接
    df['Camera Pixel'] = df['Camera Pixel'].apply(lambda x: re.sub(r'(\d+亿)', lambda y: str(int(y.group(1).replace('亿', '')) * 10000) + '万', str(x)))
    # 只保留数字和加号
    df['Camera Pixel'] = df['Camera Pixel'].apply(lambda x: re.sub(r'[^\d+]', '', str(x)))
    # if the camera pixel is empty, replace it with 0
    df['Camera Pixel'] = df['Camera Pixel'].replace('', '0')
    # create a new column to store the highest pixel of the camera
    # the highest pixel is the maximum number in Camera Pixel
    # if camera pixel is '', the highest pixel is 0
    df['Highest Pixel'] = df['Camera Pixel'].apply(lambda x: max([int(i) for i in x.split('+') if i.isdigit()]) if x != '0' else 0)
    
    # charging power列中的文本格式转换为整数，例如将'充电器25W'转换为25
    df['Charging Power'] = df['Charging Power'].apply(lambda x: int(re.search(r'\d+', str(x)).group(0)) if re.search(r'\d+', str(x)) else 0)
    # 如果charging power不是数字，则替换为0
    df['Charging Power'] = pd.to_numeric(df['Charging Power'], errors='coerce').fillna(0)

    # 将Screen Size列中的文本格式转换为整数，例如将'6.7英寸'转换为6.7
    df['Screen Size'] = df['Screen Size'].astype(str).str.replace('英寸', '').astype(float)

    df = df[(df['Charging Power'].notnull()) & (df['Charging Power'] != 0) & (df['Camera Pixel'].notnull())]

    # Define a custom function to apply different multiplication factors
    # Apply the custom function to the 'realSales' column
    df['realSales'] = df['realSales'] * 12

    sorted_df = df.sort_values(by='realSales', ascending=False)

    # 写回CSV文件
    df.to_csv(os.path.join(new_folder_path, file), index=False)
