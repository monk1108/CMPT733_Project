#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/26 14:48
# @Author : way
# @Site : 
# @Describe:

import json
import pandas as pd

class SourceDataDemo:

    def __init__(self):
        self.title = 'Mobile Phone Sales Within the Past Month in China'

        data_df1 = pd.read_csv('data/三星手机.csv')
        procity = data_df1['procity'].value_counts()
        data_df2 = pd.read_csv('data/小米手机.csv')
        procity = procity.add(data_df2['procity'].value_counts(), fill_value=0)
        data_df3 = pd.read_csv('data/华为手机.csv')
        procity = procity.add(data_df3['procity'].value_counts(), fill_value=0)
        data_df4 = pd.read_csv('data/iPhone.csv')
        procity = procity.add(data_df4['procity'].value_counts(), fill_value=0)
        data_df5 = pd.read_csv('data/oppo.csv')
        procity = procity.add(data_df5['procity'].value_counts(), fill_value=0)
        data_df6 = pd.read_csv('data/一加手机.csv')
        procity = procity.add(data_df6['procity'].value_counts(), fill_value=0)
        data_df7 = pd.read_csv('data/vivo.csv')
        procity = procity.add(data_df7['procity'].value_counts(), fill_value=0)
        # print(procity)


        
        # get the sum of selling phones in each brand
        # convert '31人付款' to 31
        data_df1['numeric_sales'] = data_df1['realSales'].str.extract('(\d+)(?:\+)?').astype(float)
        data_df2['numeric_sales'] = data_df2['realSales'].str.extract('(\d+)(?:\+)?').astype(float)
        data_df3['numeric_sales'] = data_df3['realSales'].str.extract('(\d+)(?:\+)?').astype(float)
        data_df4['numeric_sales'] = data_df4['realSales'].str.extract('(\d+)(?:\+)?').astype(float)
        data_df5['numeric_sales'] = data_df5['realSales'].str.extract('(\d+)(?:\+)?').astype(float)
        data_df6['numeric_sales'] = data_df6['realSales'].str.extract('(\d+)(?:\+)?').astype(float)
        data_df7['numeric_sales'] = data_df7['realSales'].str.extract('(\d+)(?:\+)?').astype(float)
        
        sales_samsung = data_df1['numeric_sales'].sum()
        sales_xiaomi = data_df2['numeric_sales'].sum()
        sales_huawei = data_df3['numeric_sales'].sum()
        sales_iphone = data_df4['numeric_sales'].sum()
        sales_oppo = data_df5['numeric_sales'].sum()
        sales_oneplus = data_df6['numeric_sales'].sum()
        sale_vivo = data_df7['numeric_sales'].sum()

        province_mapping = {'广东': 'Guangdong', '浙江': 'Zhejiang', '北京': 'Beijing', '上海': 'Shanghai', '江苏': 'Jiangsu', '河南': 'Henan',
                    '山东': 'Shandong', '四川': 'Sichuan', '湖北': 'Hubei', '香港': 'Hong Kong', '安徽': 'Anhui', '陕西': 'Shaanxi',
                    '广西': 'Guangxi', '河北': 'Hebei', '天津': 'Tianjin', '福建': 'Fujian', '辽宁': 'Liaoning', '江西': 'Jiangxi',
                    '湖南': 'Hunan', '重庆': 'Chongqing', '山西': 'Shanxi', '台湾': 'Taiwan'}

        city_mapping = {
            '深圳': 'Shenzhen', '东莞': 'Dongguan', '宁波': 'Ningbo', '广州': 'Guangzhou', '杭州': 'Hangzhou',
            '汕头': 'Shantou', '威海': 'Weihai', '温州': 'Wenzhou', '珠海': 'Zhuhai', '莆田': 'Putian',
            '嘉兴': 'Jiaxing', '合肥': 'Hefei', '阳江': 'Yangjiang', '香港岛': 'Hong Kong Island', '南京': 'Nanjing',
            '郑州': 'Zhengzhou', '台北': 'Taipei', '金华': 'Jinhua', '九龙': 'Kowloon', '河源': 'Heyuan',
            '成都': 'Chengdu', '青岛': 'Qingdao', '厦门': 'Xiamen', '揭阳': 'Jieyang', '长沙': 'Changsha',
            '惠州': 'Huizhou', '武汉': 'Wuhan', '三门峡': 'Sanmenxia', '大连': 'Dalian', '淮北': 'Huaibei',
            '汕尾': 'Shanwei', '石家庄': 'Shijiazhuang', '抚州': 'Fuzhou', '宜春': 'Yichun', '唐山': 'Tangshan',
            '西安': 'Xian', '江门': 'Jiangmen', '常州': 'Changzhou', '苏州': 'Suzhou', '佛山': 'Foshan',
            '茂名': 'Maoming', '济南': 'Jinan', '徐州': 'Xuzhou', '福州': 'Fuzhou', '襄阳': 'Xiangyang',
            '钦州': 'Qinzhou', '中山': 'Zhongshan', '宿迁': 'Suqian', '无锡': 'Wuxi', '湖州': 'Huzhou',
            '芜湖': 'Wuhu', '遂宁': 'Suining', '亳州': 'Bozhou', '宜宾': 'Yibin', '韶关': 'Shaoguan',
            '南昌': 'Nanchang', '滨州': 'Binzhou', '咸阳': 'Xianyang', '泉州': 'Quanzhou', '临沂': 'Linyi',
            '上饶': 'Shangrao', '太原': 'Taiyuan', '台州': 'Taizhou', '滁州': 'Chuzhou', '阜阳': 'Fuyang',
            '永州': 'Yongzhou', '张家口': 'Zhangjiakou', '盐城': 'Yancheng', '保定': 'Baoding', '淮南': 'Huainan',
            '济宁': 'Jining', '肇庆': 'Zhaoqing', '淄博': 'Zibo', '潮州': 'Chaozhou', '新界': 'New Territories',
            '南宁': 'Nanning', '赣州': 'Ganzhou', '北海': 'Beihai', '扬州': 'Yangzhou', '南平': 'Nanping'
        }

        # combine the cities within the same province
        province = procity.groupby(lambda x: x[:2]).sum()
        # sort from the highest to the lowest
        province = province.sort_values(ascending=False)
        province.index = province.index.map(province_mapping)

        merged_df = pd.concat([data_df1, data_df2, data_df3, data_df4, data_df5, data_df6, data_df7], axis=0)
        # 提取省份和市信息
        merged_df[['province', 'city']] = merged_df['procity'].str.split(' ', expand=True)
        merged_df2 = merged_df.copy()
        merged_df2['province'] = merged_df['province'].map(province_mapping)
        merged_df2['city'] = merged_df['city'].map(city_mapping)

        # 按照省份和市进行分组，并对销量进行求和，汇总各个品牌的销量
        result_df = merged_df.groupby(['city'])['numeric_sales'].sum().reset_index().sort_values('numeric_sales', ascending=False)       
        result_df2 = merged_df2.groupby(['city'])['numeric_sales'].sum().reset_index().sort_values('numeric_sales', ascending=False)


        total_sales = result_df['numeric_sales'].sum()
        product_num = len(merged_df)
        self.counter = {'name': 'Number of Mobile Phones', 'value': product_num}
        self.counter2 = {'name': 'Total Sales', 'value': total_sales}

        price_ranges = [0, 500, 1000, 2000, 5000, float('inf')]
        labels = ['0~500', '500~1000', '1000~2000', '2000~5000', 'Above 5000']
        # Create a new column for the price range
        merged_df['price_range'] = pd.cut(merged_df['price'], bins=price_ranges, labels=labels, right=False)

        # Group by the new price range column and calculate the sum of sales
        price_range = merged_df.groupby('price_range').sum()['numeric_sales']
        print(price_range)


        self.echart1_data = {
            'title': 'Sales of Each Brand in One Month',
            'data': [
                {"name": "Samsung", "value": sales_samsung},
                {"name": "Xiaomi", "value": sales_xiaomi},
                {"name": "Huawei", "value": sales_huawei},
                {"name": "iPhone", "value": sales_iphone},
                {"name": "oppo", "value": sales_oppo},
                {"name": "One Plus", "value": sales_oneplus},
                {"name": "vivo", "value": sale_vivo},
            ]
        }

        self.echart2_data = {
            'title': 'Number of Products Sold in Each Province',
            'data': [{'name': k, 'value': v} for k, v in province.items()][:6]

        }
        self.echarts3_1_data = {
            'title': '年龄分布',
            'data': [
                {"name": "0岁以下", "value": 47},
                {"name": "20-29岁", "value": 52},
                {"name": "30-39岁", "value": 90},
                {"name": "40-49岁", "value": 84},
                {"name": "50岁以上", "value": 99},
            ]
        }
        self.echarts3_2_data = {
            'title': '职业分布',
            'data': [
                {"name": "电子商务", "value": 10},
                {"name": "教育", "value": 20},
                {"name": "IT/互联网", "value": 20},
                {"name": "金融", "value": 30},
                {"name": "学生", "value": 40},
                {"name": "其他", "value": 50},
            ]
        }
        self.echarts3_3_data = {
            'title': '兴趣分布',
            'data': [
                {"name": "汽车", "value": 4},
                {"name": "旅游", "value": 5},
                {"name": "财经", "value": 9},
                {"name": "教育", "value": 8},
                {"name": "软件", "value": 9},
                {"name": "其他", "value": 9},
            ]
        }
        self.echart4_data = {
            'title': '时间趋势',
            'title': '',
            'data': [
                {"name": "安卓", "value": [3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 2, 4, 3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 4]},
                {"name": "IOS", "value": [5, 3, 5, 6, 1, 5, 3, 5, 6, 4, 6, 4, 8, 3, 5, 6, 1, 5, 3, 7, 2, 5, 8]},
            ],
            'xAxis': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '11', '12', '13', '14', '15', '16', '17',
                      '18', '19', '20', '21', '22', '23', '24'],
        }
        self.echart5_data = {
            'title': 'Top Sales of Each City',
            
            'data': [{'name': city, 'value': sales} for city, sales in zip(result_df2['city'], result_df2['numeric_sales'])][:6]
            
        }
        self.echart6_data = {
            'title': 'Mobile Phone Price Range Distribution',
            'data': [
                {"name": price_range.index[0], "value": price_range[0], "value2": 80000-price_range[0], "color": "01", "radius": ['59%', '70%']},
                {"name": price_range.index[1], "value": price_range[1], "value2": 80000-price_range[1], "color": "02", "radius": ['49%', '60%']},
                {"name": price_range.index[2], "value": price_range[2], "value2": 80000-price_range[2], "color": "03", "radius": ['39%', '50%']},
                {"name": price_range.index[3], "value": price_range[3], "value2": 80000-price_range[3], "color": "04", "radius": ['29%', '40%']},
                {"name": price_range.index[4], "value": price_range[4], "value2": 80000-price_range[4], "color": "05", "radius": ['20%', '30%']},
            ]
        }
        self.map_1_data = {
            'symbolSize': 800,
            'data': [{'name': city, 'value': sales} for city, sales in zip(result_df['city'], result_df['numeric_sales'])]
        }

    @property
    def echart1(self):
        data = self.echart1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echart2(self):
        data = self.echart2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echarts3_1(self):
        data = self.echarts3_1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_2(self):
        data = self.echarts3_2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_3(self):
        data = self.echarts3_3_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart


    @property
    def echart4(self):
        data = self.echart4_data
        echart = {
            'title': data.get('title'),
            'names': [i.get("name") for i in data.get('data')],
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart

    @property
    def echart5(self):
        data = self.echart5_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart6(self):
        data = self.echart6_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def map_1(self):
        data = self.map_1_data
        echart = {
            'symbolSize': data.get('symbolSize'),
            'data': data.get('data'),
        }
        return echart


class SourceData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        self.title = 'Mobile Phone Sales Within the Past Month in China'

class CorpData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        with open('corp.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        self.title = data.get('title')
        self.counter = data.get('counter')
        self.counter2 = data.get('counter2')
        self.echart1_data = data.get('echart1_data')
        self.echart2_data = data.get('echart2_data')
        self.echarts3_1_data = data.get('echarts3_1_data')
        self.echarts3_2_data = data.get('echarts3_2_data')
        self.echarts3_3_data = data.get('echarts3_3_data')
        self.echart4_data = data.get('echart4_data')
        self.echart5_data = data.get('echart5_data')
        self.echart6_data = data.get('echart6_data')
        self.map_1_data = data.get('map_1_data')

class JobData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        with open('job.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        self.title = data.get('title')
        self.counter = data.get('counter')
        self.counter2 = data.get('counter2')
        self.echart1_data = data.get('echart1_data')
        self.echart2_data = data.get('echart2_data')
        self.echarts3_1_data = data.get('echarts3_1_data')
        self.echarts3_2_data = data.get('echarts3_2_data')
        self.echarts3_3_data = data.get('echarts3_3_data')
        self.echart4_data = data.get('echart4_data')
        self.echart5_data = data.get('echart5_data')
        self.echart6_data = data.get('echart6_data')
        self.map_1_data = data.get('map_1_data')