# -*- coding: utf-8 -*-
__author__ = 'wankgai'  
from test_log import Config 
import requests
from urllib import request
import json
from lxml import etree
from pyquery import PyQuery as pq
from random import choice
import time
import random
import re
import math
import pymysql

class CrawlBaiDuNuoMi(object):
	"""docstring for CrawlBaiDuNuoMi"""
	def __init__(self):
		self.conf=Config()  
		self.logger=self.conf.getLog()  
		self.start_url = "https://www.nuomi.com/changecity"
		self.session = requests.session()
		self.db = pymysql.connect("localhost","root","12345","map_food",charset="utf8")
		self.cursor = self.db.cursor()
	
	def create_table(self):
		try:
			self.cursor.execute("DROP TABLE IF EXISTS food_toal_information")
			sql = """CREATE TABLE food_toal_information (
										address VARCHAR(300),
										shop_name VARCHAR(200),
										price VARCHAR(30),
										sale VARCHAR(50),
										evaluate_num VARCHAR(50),
										evaluate VARCHAR(50))"""
			self.cursor.execute(sql)
		except Exception as e:
			self.logger.exception('ERROR readFile:%s' %( str(e)))


	def crawl_city_url(self):
		# 创建数据表
		self.create_table()
		try:
			# 获取每个城市的url
			r = self.session.get("https://www.nuomi.com/changecity")
			r.encoding = 'utf-8'
			if r.ok:
				city_url_list = []
				city_url_li_list = pq(r.text).find('#J-city-list').find('li').find('ul').find('li')
				for city_url in city_url_li_list:
					per_city_url = pq(city_url).find('a').attr('href')
					per_city_url = "https:" + str(per_city_url) + "/326"
					city_url_list.append(per_city_url) 
			self.crawl_food_list(city_url_list)
		except Exception as e:
			self.logger.exception('ERROR readFile:%s' %( str(e)))
			

	# 爬取数据中断时开启
	def crawl_breakpoint_city(self):
		try:
			# 获取每个城市的url
			r = self.session.get("https://www.nuomi.com/changecity")
			r.encoding = 'utf-8'
			if r.ok:
				city_url_list = []
				city_url_li_list = pq(r.text).find('#J-city-list').find('li').find('ul').find('li')
				for city_url in city_url_li_list:
					per_city_url = pq(city_url).find('a').attr('href')
					per_city_url = "https:" + str(per_city_url) + "/326"
					city_url_list.append(per_city_url) 
				# print(city_url_list)
				i = 433
				city_breakpoint_url_list = []
				while i < len(city_url_list):
					city_breakpoint_url_list.append(city_url_list[i])
					i += 1
				# print(city_breakpoint_url_list)
 

			self.crawl_food_list(city_breakpoint_url_list)
		except Exception as e:
			self.logger.exception('ERROR readFile:%s' %( str(e)))


	def crawl_food_list(self, city_breakpoint_url_list):
		print(len(city_breakpoint_url_list))
		try:
			for i in range(len(city_breakpoint_url_list)):
				print("正在爬取第"+ str(439-(len(city_breakpoint_url_list)-i)+1)+"个城市的数据")
				print("还剩"+str(len(city_breakpoint_url_list)-i)+"个城市的数据")
				daly_time = random.randint(1, 3)
				time.sleep(daly_time)

				# 代理IP池
				# proxies_list = [{"http":"203.174.10.222:80"},{"http":"34.213.199.191:80"},{"http":"50.233.137.36:80"},{"http":"47.89.10.103:80"},{"http":"217.23.69.198:3128"},{"http":"94.242.58.108:10010"},{"http":"185.22.173.161:10010"},{"http":"119.28.50.37:82"},{"http":"101.50.1.2:80"},{"http":"94.242.58.14:10010"},{"http":"94.242.58.142:10010"},{"http":"122.72.18.34:80"}]
				proxies_list = [{"http":"180.234.222.10:8080"},{"http":"177.126.81.62:20183"},{"http":"163.172.220.221:8888"},{"http":"163.172.86.64:3128"},{"http":"50.233.137.33:80"},{"http":"177.69.8.170:3128"},{"http":"91.201.68.141:8080"},{"http":"187.95.236.212:8080"},{"http":"101.51.138.3:8080"},{"http":"124.205.191.106:8181"},{"http":"189.127.16.97:20183"},{"http":"194.190.17.23:8080"},{"http":"84.21.227.187:8080"},{"http":"103.226.202.51:53281"},{"http":"78.111.92.59:8080"},{"http":"213.80.215.179:53281"},{"http":"114.215.174.227:8080"},{"http":"51.15.101.16:3128"},{"http":"203.202.248.35:80"},{"http":"46.254.217.54:53281"},{"http":"94.242.59.245:10010"},{"http":"167.99.71.183:3128"},{"http":"80.211.148.100:8888"},{"http":"118.193.26.18:8080"},{"http":"207.154.194.13:80"},{"http":"42.115.91.82:52225"},{"http":"89.169.205.18:53281"},{"http":"175.181.40.61:8080"},{"http":"50.233.137.38:80"},{"http":"50.233.137.35:80"},{"http":"50.233.137.36:80"},{"http":"94.242.58.108:10010"},{"http":"47.89.10.103:80"},{"http":"39.106.160.36:3128"},{"http":"189.45.198.123:3128"},{"http":"50.233.137.38:80"},{"http":"50.233.137.37:80"},{"http":"50.233.137.34:80"},{"http":"50.233.137.35:80"},{"http":"47.89.10.103:80"},{"http":"94.242.58.108:10010"},{"http":"185.22.173.161:10010"},{"http":"167.99.235.248:3128"},{"http":"186.96.112.63:80"},{"http":"114.215.95.188:3128"},{"http":"39.106.160.36:3128"},{"htpp":"109.236.89.153:1080"},{"htpp":"194.67.201.106:3128"},{"htpp":"161.139.222.254:9000"},{"htpp":"1.179.182.110:8088"},{"htpp":"212.237.61.17:8888"},{"htpp":"103.205.26.120:80"},{"htpp":"149.56.200.176:80"},{"htpp":"74.208.123.225:3128"},{"htpp":"35.194.75.101:80"},{"htpp":"80.211.50.116:3128"},{"htpp":"132.255.25.189:8080"},{"htpp":"201.63.154.170:20183"},{"htpp":"212.225.233.154:8080"},{"htpp":"121.254.214.219:80"},{"htpp":"65.61.106.141:8080"},{"htpp":"222.73.68.144:8090"},{"htpp":"179.108.43.10:20183"},{"htpp":"178.210.145.243:53281"},{"htpp":"150.242.180.151:80"},{"htpp":"189.51.98.214:20183"},{"htpp":"219.127.191.12:80"},{"htpp":"185.65.186.192:8080"},{"htpp":"52.44.15.0:3129"},{"htpp":"186.236.237.143:20183"},{"htpp":"54.208.37.230:3128"},{"htpp":"14.207.33.210:8080"},{"htpp":"52.87.106.125:3128"},{"htpp":"52.0.138.163:3128"},{"htpp":"183.89.8.249:8080"},{"htpp":"50.16.179.212:3128"}]
				
				f = requests.session()
				pro_cho = choice(proxies_list)
				print(pro_cho)
				f.proxies= pro_cho

				f = (f.get(city_breakpoint_url_list[i]))

				# f = self.session.get(city_breakpoint_url_list[i])
				f.encoding = 'utf-8'
				if f.ok:
					f_res = f.text
					totle_num = pq(f_res).find('.pager-info').find('span').eq(0).text()
					print(totle_num)

					if totle_num is '':
						print('此城市无美食数据')
						continue
					else:
						num = math.ceil(int(totle_num)/25)
						print('此城市共有'+str(num)+'页数据')

					for n in range(num):
						page_url = city_breakpoint_url_list[i] + '-page' + str(n+1) + '?#j-sort-bar'
						print(page_url)
						daly_time = random.randint(1, 3)
						time.sleep(daly_time)
						c = self.session.get(page_url,
							headers = {
										'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
										'Accept-Encoding': 'gzip, deflate, br',
										'Accept-Language': 'zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
										'Connection': 'keep-alive',
										# 'Cookie': 'access_log=6517b284e5fd1420bb2353f12ad58157; BAIDUID=A4D7DB31CE60C69A0F56DE463269D3CC:FG=1; flag=101; visited=6094886; visitedRight=6094886; gpsGot=0; channel_webapp=webapp; Hm_lvt_a028c07bf31ffce4b2d21dd85b0b8907=1526460597,1526462697,1526462700,1526517984; PHPSESSID=6atobmcoadrkajnli8uv3uaqp1; NUOMI_MEISHI_MORE_AB=unfold; areaCode=1300030000; domainUrl=as; SID=937_918_931_935_953_955_957_959_961_963; shop_visited=2592924%2C54631949%2C3692957%2C1718230; Hm_lpvt_a028c07bf31ffce4b2d21dd85b0b8907=1526537473; channel=zhifang_other%7C%7Ct10_qd_pc',
										# 'Host': 'as.nuomi.com',
										'Upgrade-Insecure-Requests': '1',
										'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
							})
						c.encoding = 'utf-8'
						if c.ok:
							res_resout = c.text
							# print(res_resout)
							if num < 2:
								food_totle1 = int(totle_num)
								self.loop_ergodic(food_totle1, res_resout)	
							else:
								if num/(n+1) != 1:
									food_totle2 = 25
									self.loop_ergodic(food_totle2, res_resout)				
								else:
									food_totle3 = int(totle_num) - (num-1)*25
									self.loop_ergodic(food_totle3, res_resout)
					
		except Exception as e:
			self.logger.exception('ERROR readFile:%s' %( str(e)))

	def loop_ergodic(self, totle_demo, res_resout):
		try:
			food_detail_url_list = pq(res_resout).find('.shop-infoo-list-ul').find('li')
			print('本页有'+str(totle_demo)+'条数据')
			daly_time = random.randint(1, 3)
			time.sleep(daly_time)
			for food_detail_url in food_detail_url_list:
				per_food_detail_url = pq(food_detail_url).find('a').attr('href')
				per_food_detail_url = "https:" + per_food_detail_url
				print('正在爬取路径为'+ per_food_detail_url +'的数据')
				self.craw_detail_information(per_food_detail_url)
		except Exception as e:
			self.logger.exception('ERROR readFile:%s' %( str(e)))

	def craw_detail_information(self, per_food_detail_url):
	# def craw_detail_information(self):
		try:
			# time.sleep(1)
			e = self.session.get(per_food_detail_url)
			# e = self.session.get("https://www.nuomi.com/shop/161247")

			e.encoding = 'utf-8'
			if e.ok:
				e_res = e.text
				address = pq(e_res).find('.shop-box').find('ul').find('li').eq(0).find('span').eq(1).text()
				print(address)
				shop_name = pq(e_res).find('.shop-box').find('h2').text()
				print(shop_name)
				price = pq(e_res).find('.shop-box').find('p').find('span').eq(4).find('strong').text()
				print(price)
				sale = pq(e_res).find('.shop-current').find('.col-wrap')
				value = 0
				for per_sale in sale:
					detail_sale = pq(per_sale).find('div').eq(1).find('p').eq(-1).text()[2:]
					value = value + int(detail_sale)
				sale = str(value)
				print(sale)
				evaluate_num = pq(e_res).find('.shop-box').find('p').find('span').eq(3).text()[1:-4]
				print(evaluate_num)
				evaluate = pq(e_res).find('.shop-box').find('p').find('span').eq(2).text()
				print(evaluate)
				
				insert_food_toal_information = ("INSERT INTO food_toal_information(address,shop_name,price,sale,evaluate_num,evaluate)" "VALUES(%s,%s,%s,%s,%s,%s)")
				data_food_toal_information = (address,shop_name,price,sale,evaluate_num,evaluate)
				self.cursor.execute(insert_food_toal_information, data_food_toal_information)
				self.db.commit()
			
		except Exception as e:
			self.logger.exception('ERROR readFile:%s' %( str(e)))

if __name__ == '__main__':
	cbdnm = CrawlBaiDuNuoMi()
	# cbdnm.crawl_city_url()
	cbdnm.crawl_breakpoint_city()
	# cbdnm.crawl_food_list()
	# cbdnm.craw_detail_information_url()
	# cbdnm.craw_detail_information()

