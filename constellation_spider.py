# -*- coding: utf-8 -*- 
# @Time : 2019/5/22 下午7:59 
# @Author : Honay.King
# @File : spider.py
# @Software: PyCharm

import os
import requests
from lxml import etree
import pandas as pd


def get_urls():
    # ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座', '水瓶座', '双鱼座']
    Constel_list = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio',
                    'sagittarius', 'capricorn', 'aquarius', 'pisces']
    # 31天的月份
    lmonth_list = [1, 3, 5, 7, 8, 10, 12]
    # 30天的月份
    smonth_list = [4, 6, 9, 11]
    # 选定的年份：20140901 [2015, 2016, 2017, 2018, 2019]
    year_list = [2015, 2016, 2017, 2018, 2019]
    base_url = "http://www.xzw.com/fortune/"
    tmp_list = list()
    for year in year_list:
        if year == 2019:
            for i in range(4):
                if i < 9:
                    if i+1 in lmonth_list:
                        for d1 in range(31):
                            if d1 < 9:
                                tmp_list.append(str(year) + '0' + str(i + 1) + '0' + str(d1 + 1) + '.html')
                            else:
                                tmp_list.append(str(year) + '0' + str(i + 1) + str(d1 + 1) + '.html')
                    elif i+1 in smonth_list:
                        for d2 in range(30):
                            if d2 < 9:
                                tmp_list.append(str(year) + '0' + str(i + 1) + '0' + str(d2 + 1) + '.html')
                            else:
                                tmp_list.append(str(year) + '0' + str(i + 1) + str(d2 + 1) + '.html')
                    else:
                        for d3 in range(28):
                            if d3 < 9:
                                tmp_list.append(str(year) + '0' + str(i + 1) + '0' + str(d3 + 1) + '.html')
                            else:
                                tmp_list.append(str(year) + '0' + str(i + 1) + str(d3 + 1) + '.html')
                else:
                    if i+1 in lmonth_list:
                        for d1 in range(31):
                            if d1 < 9:
                                tmp_list.append(str(year) + str(i + 1) + '0' + str(d1 + 1) + '.html')
                            else:
                                tmp_list.append(str(year) + str(i + 1) + str(d1 + 1) + '.html')
                    elif i+1 in smonth_list:
                        for d2 in range(30):
                            if d2 < 9:
                                tmp_list.append(str(year) + str(i + 1) + '0' + str(d2 + 1) + '.html')
                            else:
                                tmp_list.append(str(year) + str(i + 1) + str(d2 + 1) + '.html')
                    else:
                        for d3 in range(28):
                            if d3 < 9:
                                tmp_list.append(str(year) + str(i + 1) + '0' + str(d3 + 1) + '.html')
                            else:
                                tmp_list.append(str(year) + str(i + 1) + str(d3 + 1) + '.html')
        else:
            for i in range(12):
                if i < 9:
                    if i+1 in lmonth_list:
                        for d1 in range(31):
                            if d1 < 9:
                                tmp_list.append(str(year) + '0' + str(i + 1) + '0' + str(d1 + 1) + '.html')
                            else:
                                tmp_list.append(str(year) + '0' + str(i + 1) + str(d1 + 1) + '.html')
                    elif i+1 in smonth_list:
                        for d2 in range(30):
                            if d2 < 9:
                                tmp_list.append(str(year) + '0' + str(i + 1) + '0' + str(d2 + 1) + '.html')
                            else:
                                tmp_list.append(str(year) + '0' + str(i + 1) + str(d2 + 1) + '.html')
                    else:
                        for d3 in range(28):
                            if d3 < 9:
                                tmp_list.append(str(year) + '0' + str(i + 1) + '0' + str(d3 + 1) + '.html')
                            else:
                                tmp_list.append(str(year) + '0' + str(i + 1) + str(d3 + 1) + '.html')
                else:
                    if i+1 in lmonth_list:
                        for d1 in range(31):
                            if d1 < 9:
                                tmp_list.append(str(year) + str(i + 1) + '0' + str(d1 + 1) + '.html')
                            else:
                                tmp_list.append(str(year) + str(i + 1) + str(d1 + 1) + '.html')
                    elif i+1 in smonth_list:
                        for d2 in range(30):
                            if d2 < 9:
                                tmp_list.append(str(year) + str(i + 1) + '0' + str(d2 + 1) + '.html')
                            else:
                                tmp_list.append(str(year) + str(i + 1) + str(d2 + 1) + '.html')
                    else:
                        for d3 in range(28):
                            if d3 < 9:
                                tmp_list.append(str(year) + str(i + 1) + '0' + str(d3 + 1) + '.html')
                            else:
                                tmp_list.append(str(year) + str(i + 1) + str(d3 + 1) + '.html')
    final_urls = list()
    for item in Constel_list:
        for html in tmp_list:
            final_urls.append(base_url + item + '/' + html)
    print('Urls Num Count:', len(final_urls))
    return final_urls


def get_info(urls):
    constellation_list = list()
    for url in urls:
        info = {}
        html = requests.get(url).text
        s = etree.HTML(html)
        print(url)
        stop_list = ["http://www.xzw.com/fortune/cancer/20150802.html"]
        if url == stop_list:
            print('[WARNING] The Cur Url: {} is NOT GOOD!'.format(url))
            continue
        if s.xpath('//*[@id="view"]/div[2]/div[3]/div[2]/p[2]/span/text()') == []:
            print('[WARNING] The Cur Url: {} is NOT GOOD!'.format(url))
            continue
        whole = s.xpath('//*[@id="view"]/div[2]/dl/dd/ul/li[1]/span/em')[0].attrib.get('style')
        whole_star = ''.join(list(filter(lambda x: x.isdigit(), whole)))
        love = s.xpath('//*[@id="view"]/div[2]/dl/dd/ul/li[2]/span/em')[0].attrib.get('style')
        love_star = ''.join(list(filter(lambda x: x.isdigit(), love)))
        career = s.xpath('//*[@id="view"]/div[2]/dl/dd/ul/li[3]/span/em')[0].attrib.get('style')
        career_star = ''.join(list(filter(lambda x: x.isdigit(), career)))
        wealth = s.xpath('//*[@id="view"]/div[2]/dl/dd/ul/li[4]/span/em')[0].attrib.get('style')
        wealth_star = ''.join(list(filter(lambda x: x.isdigit(), wealth)))

        constellation = s.xpath('//*[@id="view"]/div[2]/dl/dd/h4/text()')[0]
        time_cur = s.xpath('//*[@id="view"]/div[2]/dl/dd/h4/small/text()')[0]
        health_point = s.xpath('//*[@id="view"]/div[2]/dl/dd/ul/li[5]/text()')[0]
        discuss_point = s.xpath('//*[@id="view"]/div[2]/dl/dd/ul/li[6]/text()')[0]
        daily_message = s.xpath('//*[@id="view"]/div[2]/dl/dd/ul/li[10]/text()')[0]
        whole_analysis = s.xpath('//*[@id="view"]/div[2]/div[3]/div[2]/p[1]/span/text()')[0]
        love_analysis = s.xpath('//*[@id="view"]/div[2]/div[3]/div[2]/p[2]/span/text()')[0]
        wealth_analysis = s.xpath('//*[@id="view"]/div[2]/div[3]/div[2]/p[4]/span/text()')[0]
        career_analysis = s.xpath('//*[@id="view"]/div[2]/div[3]/div[2]/p[3]/span/text()')[0]
        health_analysis = s.xpath('//*[@id="view"]/div[2]/div[3]/div[2]/p[5]/span/text()')[0]

        if (love_star and wealth_star and career_star and health_point and discuss_point and daily_message
                and whole_analysis and love_analysis and wealth_analysis and career_analysis and health_analysis):
            info['星座*'] = constellation
            info['时间*'] = time_cur
            info['爱情运势*'] = love_star
            info['财富运势*'] = wealth_star
            info['事业学业*'] = career_star
            info['综合运势*'] = whole_star
            info['商谈指数'] = discuss_point
            info['健康指数'] = health_point
            info['每日短评'] = daily_message
            info['综合运势分析'] = whole_analysis
            info['事业学业分析'] = career_analysis
            info['爱情运势分析'] = love_analysis
            info['财富运势分析'] = wealth_analysis
            info['健康运势分析'] = health_analysis
            constellation_list.append(info)
    data = pd.DataFrame(constellation_list)
    data.to_csv('./constellation.csv', mode='w', index_label='ID')


def resave_csv(source_csv, target_csv):
    if not os.path.exists(source_csv):
        print('[ERROR] resave_csv failed! | The parameter: {}'.format(source_csv))
        return False
    source_data = pd.read_csv(source_csv, low_memory=False)
    source_data.to_csv(target_csv, mode='a', encoding='gb18030', index=False)


if __name__ == "__main__":
    # 开始爬取数据
    # get_info(get_urls())
    # 将爬取数据进行备份
    source_csv = r'./constellation.csv'
    target_csv = r'./constellation_base.csv'
    resave_csv(source_csv, target_csv)

    exit(0)
