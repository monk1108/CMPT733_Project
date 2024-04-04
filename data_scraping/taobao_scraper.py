# 参考：https://zhuanlan.zhihu.com/p/42053431
# https://darktiantian.github.io/%E8%AE%B0%E4%B8%80%E6%AC%A1%E6%B7%98%E5%AE%9D%E6%8E%A5%E5%8F%A3sign%E7%AD%BE%E5%90%8D%E7%A0%B4%E8%A7%A3/
# https://onejane.github.io/2021/04/25/JS%E9%80%86%E5%90%91%E4%B9%8B%E6%B7%98%E5%AE%9Dh5%E8%A7%86%E9%A2%91sign%E7%A0%B4%E8%A7%A3/#%E5%88%86%E6%9E%90
# https://zhuanlan.zhihu.com/p/655304909
# http://t.csdnimg.cn/EKgSr
# https://github.com/xzh0723/Taobao/tree/master
# http://t.csdnimg.cn/8umoV
# 设置了爬取20页
# 运行不了就说明cookie过期，重新设置

# 可视化：地图，

import urllib.request
import urllib.parse
import json
from openpyxl import Workbook
import requests
import csv
import time
import urllib.parse
from urllib.parse import urlencode
import os
import execjs
import re
import hashlib


def getPageResponse(product_name, page_num):
    appId = "34385"

    params = {
        "device": "HMA-AL00",
        "isBeta": "false",
        "grayHair": "false",
        "from": "nt_history",
        "brand": "HUAWEI",
        "info": "wifi",
        "index": "4",
        "rainbow": "",
        "schemaType": "auction",
        "elderHome": "false",
        "isEnterSrpSearch": "true",
        "newSearch": "false",
        "network": "wifi",
        "subtype": "",
        "hasPreposeFilter": "false",
        "prepositionVersion": "v2",
        "client_os": "Android",
        "gpsEnabled": "false",
        "searchDoorFrom": "srp",
        "debug_rerankNewOpenCard": "false",
        "homePageVersion": "v7",
        "searchElderHomeOpen": "false",
        "search_action": "initiative",
        "sugg": "_4_1",
        "sversion": "13.6",
        "style": "list",
        "ttid": "600000@taobao_pc_10.7.0",
        "needTabs": "true",
        "areaCode": "CN",
        "vm": "nw",
        "countryNum": "156",
        "m": "pc",
        "page": page_num,
        "n": 48,
        "q": product_name,
        "tab": "all",
        "pageSize": 48,
        "totalPage": 100,
        "totalResults": 4800,
        "sourceS": "0",
        "sort": "_coefp",
        "bcoffset": "",
        "ntoffset": "",
        "filterTag": "",
        "service": "",
        "prop": "",
        "loc": "",
        "start_price": None,
        "end_price": None,
        "startPrice": None,
        "endPrice": None,
        "itemIds": None,
        "p4pIds": None
    }

    json_string = json.dumps(params, separators=(',', ':'))

    # 将字典编码为 URL 查询字符串
    encoded_string = urllib.parse.quote(json_string).replace("%22", "%5C%22")
    encoded_string = "%7B%22appId%22%3A%22" + str(appId) + "%22%2C%22params%22%3A%22" + encoded_string + "%22%7D"

    # 将struct_time对象转换为时间戳
    timestamp = int(time.time()*1000)  # 乘以1000将秒转换为毫秒
    timestamp = str(timestamp)

    # TODO: 每次执行需要更新Cookie
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
        'Cookie': '_samesite_flag_=true; cookie2=1cf8793bd6d14ecb2f969f19939a1eea; t=f85510e5b3cee99c6121e9cc763e761a; _tb_token_=75de1b6e64eb3; cna=pO94G6uql0QCAW+6MVn3eVdx; lgc=tb1123273822; cancelledSubSites=empty; dnk=tb1123273822; tracknick=tb1123273822; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; havana_lgc2_0=eyJoaWQiOjIyMDE0ODAwMDE4NTcsInNnIjoiYTYwMmY1MzEyOGVjN2QyOWIxZGI2NjYxODU1NTFkOGMiLCJzaXRlIjowLCJ0b2tlbiI6IjFKOUFnRjRhdkE5YkVPYjNKbTBTTExRIn0; _hvn_lgc_=0; wk_cookie2=16f0a1f8cc08becb8961afd96f49b741; wk_unb=UUphy%2FZybz7dfg%2FuBA%3D%3D; xlly_s=1; 3PcFlag=1712114962275; sgcookie=E100pjnEJmXClTklhq4Aj92HODV3DmVJkgiqVIJhWqSx8nGWqdFXbkgdy1maxecKkfuQdjKL%2FrgG5j55HnWv1B0OGrUfBCJN97dLL7oWTzCxEvGRBPQF2Cyu%2BgvEOhyIGA9C; unb=2201480001857; uc1=pas=0&cookie15=V32FPkk%2Fw0dUvg%3D%3D&cookie14=UoYfoxyYSy7Ecw%3D%3D&cookie21=WqG3DMC9FxUx&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&existShop=false; uc3=nk2=F5REP75Lqi7aheXQ&vt3=F8dD3e86jvDTO1IK3Zk%3D&lg2=UIHiLt3xD8xYTw%3D%3D&id2=UUphy%2FZybz7dfg%2FuBA%3D%3D; csg=2fd303a9; cookie17=UUphy%2FZybz7dfg%2FuBA%3D%3D; skt=985ab4caa0808e65; existShop=MTcxMjExNDk2NQ%3D%3D; uc4=nk4=0%40FY4PbaqPAKnyDJ%2FDB4Eo%2FyA%2FadyD%2FaM%3D&id4=0%40U2grEJGNHK%2FDuijkypw0fbWiuFMGaK2e; _cc_=UtASsssmfA%3D%3D; _l_g_=Ug%3D%3D; sg=278; _nk_=tb1123273822; cookie1=BqsJtEybUwXw5GH4kbycHqs6Z34n%2Bu%2F5VVPttCcJtjk%3D; _uetsid=54f79f00f16a11eeb19815d152a86600; _uetvid=12c71e20d82c11eeb26cc5a92e3d05d3; mtop_partitioned_detect=1; _m_h5_tk=913be88daeac25ce65737c9069d994c7_1712189497866; _m_h5_tk_enc=4266d679a2837d24e047c427d369f6d6; tfstk=f_XJzwMtGr4lQPFhFgNcTA3Ibkq0ITIzraSsKeYoOZQAAED34LVepwLA8UAkFUDppMQF-wIU4HTCRwLhZS2G4gJedPvLIRjzhFOfHTpI-iaocpe0SR2GVgJedP4gYgUwbexHd3OSFmZvqH9IO3_BlIt6j49BdwsbDHtSPvGSN-9X43hEF0LnVeHd34GooP09lvMCF7RJWgcndv622QBCVEIR2tKJwFODyTH5FZjCETR4wb9Fm1QdONamZU19XZdGwPHRWa-CvH_8QcLfeMBvas0SNhpJyC6W1JDd2B1AHLX78fScDUO9nsV4rBvRy18wNSzVJiLlRTdjyrYhsiXWMNamHwRdOTvfFrwO4B6GBcdISFKnNoExTXRWmA3c6WmOib2MDFqmiXlein-vSoExTXRW0nLgmmGETIxV.; isg=BPn5leAtu-WMb2I4p84pKH4lCGXTBu24LzL5ixsudiCeohk0Y1TSiRD0JL5UGoXw',
        'Referer': 'https://s.taobao.com/',
        'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }

    cookie_token = re.search('_m_h5_tk=(.*?);', headers['Cookie']).group(1).split('_')[0]


    def get_sign(token, t, data):
        sign = token + "&" + t + "&" + '12574478' + "&" + data
        m = hashlib.md5()
        m.update(sign.encode('utf-8'))
        return m.hexdigest()

    data_dict = "{\"appId\":\"34385\",\"params\":\"{\\\"device\\\":\\\"HMA-AL00\\\",\\\"isBeta\\\":\\\"false\\\",\\\"grayHair\\\":\\\"false\\\",\\\"from\\\":\\\"nt_history\\\",\\\"brand\\\":\\\"HUAWEI\\\",\\\"info\\\":\\\"wifi\\\",\\\"index\\\":\\\"4\\\",\\\"rainbow\\\":\\\"\\\",\\\"schemaType\\\":\\\"auction\\\",\\\"elderHome\\\":\\\"false\\\",\\\"isEnterSrpSearch\\\":\\\"true\\\",\\\"newSearch\\\":\\\"false\\\",\\\"network\\\":\\\"wifi\\\",\\\"subtype\\\":\\\"\\\",\\\"hasPreposeFilter\\\":\\\"false\\\",\\\"prepositionVersion\\\":\\\"v2\\\",\\\"client_os\\\":\\\"Android\\\",\\\"gpsEnabled\\\":\\\"false\\\",\\\"searchDoorFrom\\\":\\\"srp\\\",\\\"debug_rerankNewOpenCard\\\":\\\"false\\\",\\\"homePageVersion\\\":\\\"v7\\\",\\\"searchElderHomeOpen\\\":\\\"false\\\",\\\"search_action\\\":\\\"initiative\\\",\\\"sugg\\\":\\\"_4_1\\\",\\\"sversion\\\":\\\"13.6\\\",\\\"style\\\":\\\"list\\\",\\\"ttid\\\":\\\"600000@taobao_pc_10.7.0\\\",\\\"needTabs\\\":\\\"true\\\",\\\"areaCode\\\":\\\"CN\\\",\\\"vm\\\":\\\"nw\\\",\\\"countryNum\\\":\\\"156\\\",\\\"m\\\":\\\"pc\\\",\\\"page\\\":\\\"" \
        + page_num + "\\\",\\\"n\\\":48,\\\"q\\\":\\\"" + \
        product_name + "\\\",\\\"tab\\\":\\\"all\\\",\\\"pageSize\\\":48,\\\"totalPage\\\":100,\\\"totalResults\\\":4800,\\\"sourceS\\\":\\\"0\\\",\\\"sort\\\":\\\"_coefp\\\",\\\"bcoffset\\\":\\\"\\\",\\\"ntoffset\\\":\\\"\\\",\\\"filterTag\\\":\\\"\\\",\\\"service\\\":\\\"\\\",\\\"prop\\\":\\\"\\\",\\\"loc\\\":\\\"\\\",\\\"start_price\\\":null,\\\"end_price\\\":null,\\\"startPrice\\\":null,\\\"endPrice\\\":null,\\\"itemIds\\\":null,\\\"p4pIds\\\":null}\"}"
    # timestamp = '1709365166304'
    sign = get_sign(cookie_token, timestamp, data_dict)

    url = 'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/?jsv=2.6.2&appKey=12574478&t=' + timestamp + '&sign=' + \
    sign + '&api=mtop.relationrecommend.WirelessRecommend.recommend&v=2.0&type=jsonp&dataType=jsonp&callback=mtopjsonp1&data={}'.format(encoded_string)

    # url_correct = 'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/?jsv=2.6.2&appKey=12574478&t=1709365166304&sign=69b84b2ba000f092d35e4ad639c80d1e&api=mtop.relationrecommend.WirelessRecommend.recommend&v=2.0&type=jsonp&dataType=jsonp&callback=mtopjsonp1&data=%7B%22appId%22%3A%2234385%22%2C%22params%22%3A%22%7B%5C%22device%5C%22%3A%5C%22HMA-AL00%5C%22%2C%5C%22isBeta%5C%22%3A%5C%22false%5C%22%2C%5C%22grayHair%5C%22%3A%5C%22false%5C%22%2C%5C%22from%5C%22%3A%5C%22nt_history%5C%22%2C%5C%22brand%5C%22%3A%5C%22HUAWEI%5C%22%2C%5C%22info%5C%22%3A%5C%22wifi%5C%22%2C%5C%22index%5C%22%3A%5C%224%5C%22%2C%5C%22rainbow%5C%22%3A%5C%22%5C%22%2C%5C%22schemaType%5C%22%3A%5C%22auction%5C%22%2C%5C%22elderHome%5C%22%3A%5C%22false%5C%22%2C%5C%22isEnterSrpSearch%5C%22%3A%5C%22true%5C%22%2C%5C%22newSearch%5C%22%3A%5C%22false%5C%22%2C%5C%22network%5C%22%3A%5C%22wifi%5C%22%2C%5C%22subtype%5C%22%3A%5C%22%5C%22%2C%5C%22hasPreposeFilter%5C%22%3A%5C%22false%5C%22%2C%5C%22prepositionVersion%5C%22%3A%5C%22v2%5C%22%2C%5C%22client_os%5C%22%3A%5C%22Android%5C%22%2C%5C%22gpsEnabled%5C%22%3A%5C%22false%5C%22%2C%5C%22searchDoorFrom%5C%22%3A%5C%22srp%5C%22%2C%5C%22debug_rerankNewOpenCard%5C%22%3A%5C%22false%5C%22%2C%5C%22homePageVersion%5C%22%3A%5C%22v7%5C%22%2C%5C%22searchElderHomeOpen%5C%22%3A%5C%22false%5C%22%2C%5C%22search_action%5C%22%3A%5C%22initiative%5C%22%2C%5C%22sugg%5C%22%3A%5C%22_4_1%5C%22%2C%5C%22sversion%5C%22%3A%5C%2213.6%5C%22%2C%5C%22style%5C%22%3A%5C%22list%5C%22%2C%5C%22ttid%5C%22%3A%5C%22600000%40taobao_pc_10.7.0%5C%22%2C%5C%22needTabs%5C%22%3A%5C%22true%5C%22%2C%5C%22areaCode%5C%22%3A%5C%22CN%5C%22%2C%5C%22vm%5C%22%3A%5C%22nw%5C%22%2C%5C%22countryNum%5C%22%3A%5C%22156%5C%22%2C%5C%22m%5C%22%3A%5C%22pc%5C%22%2C%5C%22page%5C%22%3A%5C%221%5C%22%2C%5C%22n%5C%22%3A48%2C%5C%22q%5C%22%3A%5C%22%25E5%25B0%258F%25E7%25B1%25B3%25E6%2589%258B%25E6%259C%25BA%5C%22%2C%5C%22tab%5C%22%3A%5C%22all%5C%22%2C%5C%22pageSize%5C%22%3A48%2C%5C%22totalPage%5C%22%3A100%2C%5C%22totalResults%5C%22%3A4800%2C%5C%22sourceS%5C%22%3A%5C%220%5C%22%2C%5C%22sort%5C%22%3A%5C%22_coefp%5C%22%2C%5C%22bcoffset%5C%22%3A%5C%22%5C%22%2C%5C%22ntoffset%5C%22%3A%5C%22%5C%22%2C%5C%22filterTag%5C%22%3A%5C%22%5C%22%2C%5C%22service%5C%22%3A%5C%22%5C%22%2C%5C%22prop%5C%22%3A%5C%22%5C%22%2C%5C%22loc%5C%22%3A%5C%22%5C%22%2C%5C%22start_price%5C%22%3Anull%2C%5C%22end_price%5C%22%3Anull%2C%5C%22startPrice%5C%22%3Anull%2C%5C%22endPrice%5C%22%3Anull%2C%5C%22itemIds%5C%22%3Anull%2C%5C%22p4pIds%5C%22%3Anull%7D%22%7D'

 
    # 包装url, headers
    request = urllib.request.Request(url=url, headers=headers)
    # 发送请求
    response = urllib.request.urlopen(request)
    # 读取结果n 
    content = response.read().decode('utf-8')
    print(content)
 

    # 去掉结果数据中前面的mtopjsonp2(
    a = content.replace("mtopjsonp2(", "")
    a = content.replace("mtopjsonp1(", "")

    # 去掉结果数据结尾的)
    b = a.replace(")", "")
 
    json_b = json.loads(b)
    return json_b


 
if __name__ == '__main__':
    product_name = input("请输入想爬取的商品名称：")
    start_page = int(input("开始页码："))
    end_page = int(input("结束页码："))
    
    # encode product_name in utf-8 format
    product_name_utf8 = urllib.parse.quote(product_name)    # e.g. 小米手机："%E5%B0%8F%E7%B1%B3%E6%89%8B%E6%9C%BA"
    # start_page = 1
    # end_page = 20
    data_list = []
    # procity: 省市 （e.g. 广东 深圳）
    fieldnames = ['shopTitle', 'price', 'title', 'auction', 'item_id', 'realSales', 'procity', 'Trade-in',
              'Free Shipping Insurance', 'Free Shipping', 'Global Purchase', 'Charity Goods',
              'CPU Model', 'Camera Pixel', 'Charging Power', 'Screen Size']
    csv_name = product_name + '.csv'

    with open(csv_name, 'w', newline='', encoding='utf-8') as csvfile:
        # Create a CSV writer
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Write the header
        writer.writeheader()

        for i in range(start_page, end_page + 1):
            print(f'正在爬取第{i}页')
            json_b = getPageResponse(product_name_utf8, str(i))

            products = json_b['data']['itemsArray']        

            # Write the product dictionaries as rows
            for product in products:
                auction = product['auctionURL'][2:]
                shopTitle = product['shopInfo']['title']
                price = product['priceWap']
                # priceWithRate = product['priceWithRate']
                title = product['title']
                item_id = product['item_id']
                realSales = product['realSales']
                procity = product['procity']


                if 'structuredUSPInfo' in product:
                    USPInfo = product['structuredUSPInfo']
                    property_dict = {
                        "CPU型号": "CPU Model",
                        "拍照像素": "Camera Pixel",
                        "充电功率": "Charging Power",
                        "屏幕尺寸": "Screen Size"
                    }
                    UPS_result = {}
                    # 遍历中英对照的属性字典
                    for property_name, translation in property_dict.items():
                        property_value = None
                        # 查找当前属性是否在USPInfo dataframe中
                        for info in USPInfo:
                            if info['propertyName'] == property_name:
                                property_value = info['propertyValueName']
                                break

                        # 将属性值添加到当前商品的结果字典中
                        UPS_result[translation] = property_value
                

                if 'icons' in product:
                    icons = product['icons']
                    icons_result = {}
                    keywords = {
                        "以旧换新": "Trade-in",
                        "赠运费险": "Free Shipping Insurance",
                        "包邮": "Free Shipping",
                        "全球购": "Global Purchase",
                        "公益宝贝": "Charity Goods"
                    }
                    # 遍历关键字
                    for keyword, keywordEng in keywords.items():
                        # 检查当前关键字是否在当前商品的icons dataframe中
                        found = False
                        for icon in icons:
                            if 'text' in icon and icon['text'] == keyword:
                                found = True
                                break
                        
                        # 将结果添加到当前商品的结果字典中
                        icons_result[keywordEng] = 1 if found else 0


                # write the features into a csv file
                writer.writerow({'shopTitle': shopTitle, 'price': price, 'title': title, 'auction': auction, 'item_id': item_id, \
                                 'realSales': realSales, 'procity': procity, 'Trade-in': icons_result['Trade-in'], \
                                'Free Shipping Insurance': icons_result['Free Shipping Insurance'], \
                                'Free Shipping': icons_result['Free Shipping'], \
                                'Global Purchase': icons_result['Global Purchase'], \
                                'Charity Goods': icons_result['Charity Goods'], \
                                'CPU Model': UPS_result['CPU Model'], \
                                'Camera Pixel': UPS_result['Camera Pixel'], \
                                'Charging Power': UPS_result['Charging Power'], \
                                'Screen Size': UPS_result['Screen Size']})

            # sleep 5 seconds
            time.sleep(5)