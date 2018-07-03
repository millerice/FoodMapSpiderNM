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
from queue import Queue
import threading

class CrawlBaiDuNuoMi(object):
	"""docstring for CrawlBaiDuNuoMi"""
	def __init__(self):
		self.conf=Config()  
		self.logger=self.conf.getLog()  
		self.start_url = "https://www.nuomi.com/changecity"
		self.session = requests.session()
		self.db = pymysql.connect("localhost","root","12345","map_food",charset="utf8")
		self.cursor = self.db.cursor()
		# self.url_queue = Queue()  #放url的队列
  #       self.html_str_queue = Queue()  #放响应的队列
  #       self.content_list_queue = Queue() #放提取的数据的队列
	
	def create_table(self):
		try:
			self.cursor.execute("DROP TABLE IF EXISTS food_data_test")
			sql = """CREATE TABLE food_data_test (
										address VARCHAR(300),
										shop_name VARCHAR(200),
										phone VARCHAR(60), 
										work_time VARCHAR(300),
										price VARCHAR(30),
										evaluate_num VARCHAR(50),
										good_level VARCHAR(50),
										commonly_level VARCHAR(50),
										bad_level VARCHAR(50),
										evaluate VARCHAR(50))"""
			self.cursor.execute(sql)
		except Exception as e:
			self.logger.exception('ERROR readFile:%s' %( str(e)))


	def crawl_city_url(self):
		# 创建数据表
		self.create_table()
		print("数据库创建成功")
		try:
			# 获取每个城市的url
			r = self.session.get("https://www.nuomi.com/changecity")
			r.encoding = 'utf-8'
			if r.ok:
				city_url_list = []
				city_url_li_list = pq(r.text).find('#J-city-list').find('li').find('ul').find('li')

				# print(city_url_li_list)
				for city_url in city_url_li_list:
					per_city_url = pq(city_url).find('a').attr('href')
					# print(per_city_url)
					per_city_url = "https:" + str(per_city_url) + "/326"
					city_url_list.append(per_city_url) 
				# print(len(city_url_list[1:]))
				# print(city_url_list)
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
				i = 435
				city_breakpoint_url_list = []
				while i < len(city_url_list):
					city_breakpoint_url_list.append(city_url_list[i])
					i += 1
				# print(city_breakpoint_url_list)

			self.crawl_food_list(city_breakpoint_url_list)
		except Exception as e:
			self.logger.exception('ERROR readFile:%s' %( str(e)))


	def crawl_food_list(self, city_breakpoint_url_list):
		# print(len(city_breakpoint_url_list))
		try:
			# 当程序无中断时执行
			for i in range(len(city_breakpoint_url_list)):
				print("正在爬取第"+ str(439-(len(city_breakpoint_url_list)-i)+1)+"个城市的数据")
				print("还剩"+str(len(city_breakpoint_url_list)-i)+"个城市的数据")
				daly_time = random.randint(1, 3)
				time.sleep(daly_time)

				# 代理IP池
				proxies_list = [{"http":"180.234.222.10:8080"},{"http":"177.126.81.62:20183"},{"http":"163.172.86.64:3128"},{"http":"50.233.137.33:80"},{"http":"91.201.68.141:8080"},{"http":"187.95.236.212:8080"},{"http":"101.51.138.3:8080"},{"http":"189.127.16.97:20183"},{"http":"194.190.17.23:8080"},{"http":"103.226.202.51:53281"},{"http":"78.111.92.59:8080"},{"http":"213.80.215.179:53281"},{"http":"114.215.174.227:8080"},{"http":"203.202.248.35:80"},{"http":"46.254.217.54:53281"},{"http":"94.242.59.245:10010"},{"http":"167.99.71.183:3128"},{"http":"80.211.148.100:8888"},{"http":"118.193.26.18:8080"},{"http":"207.154.194.13:80"},{"http":"89.169.205.18:53281"},{"http":"50.233.137.38:80"},{"http":"50.233.137.35:80"},{"http":"50.233.137.36:80"},{"http":"94.242.58.108:10010"},{"http":"47.89.10.103:80"},{"http":"39.106.160.36:3128"},{"http":"189.45.198.123:3128"},{"http":"50.233.137.38:80"},{"http":"50.233.137.37:80"},{"http":"50.233.137.34:80"},{"http":"50.233.137.35:80"},{"http":"47.89.10.103:80"},{"http":"94.242.58.108:10010"},{"http":"185.22.173.161:10010"},{"http":"186.96.112.63:80"},{"http":"114.215.95.188:3128"},{"http":"39.106.160.36:3128"},{"htpp":"109.236.89.153:1080"},{"htpp":"194.67.201.106:3128"},{"htpp":"161.139.222.254:9000"},{"htpp":"1.179.182.110:8088"},{"htpp":"212.237.61.17:8888"},{"htpp":"103.205.26.120:80"},{"htpp":"149.56.200.176:80"},{"htpp":"74.208.123.225:3128"},{"htpp":"35.194.75.101:80"},{"htpp":"80.211.50.116:3128"},{"htpp":"132.255.25.189:8080"},{"htpp":"201.63.154.170:20183"},{"htpp":"212.225.233.154:8080"},{"htpp":"121.254.214.219:80"},{"htpp":"65.61.106.141:8080"},{"htpp":"222.73.68.144:8090"},{"htpp":"179.108.43.10:20183"},{"htpp":"178.210.145.243:53281"},{"htpp":"150.242.180.151:80"},{"htpp":"189.51.98.214:20183"},{"htpp":"219.127.191.12:80"},{"htpp":"185.65.186.192:8080"},{"htpp":"52.44.15.0:3129"},{"htpp":"186.236.237.143:20183"},{"htpp":"54.208.37.230:3128"},{"htpp":"14.207.33.210:8080"},{"htpp":"52.87.106.125:3128"},{"htpp":"52.0.138.163:3128"},{"htpp":"183.89.8.249:8080"},{"htpp":"50.16.179.212:3128"}]
				
				f = requests.session()
				pro_cho = choice(proxies_list)
				print("使用的代理IP是"+ str(pro_cho))
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
				# print(per_food_detail_url)
				print('正在爬取路径为'+ per_food_detail_url +'的数据')
				self.craw_detail_information(per_food_detail_url)
		except Exception as e:
			self.logger.exception('ERROR readFile:%s' %( str(e)))

	def craw_detail_information(self, per_food_detail_url):
		try:
			# time.sleep(1)
			e = self.session.get(per_food_detail_url)
			e.encoding = 'utf-8'
			if e.ok:
				e_res = e.text
				address = pq(e_res).find('.shop-box').find('ul').find('li').eq(0).find('span').eq(1).text()
				print(address)
				shop_name = pq(e_res).find('.shop-box').find('h2').text()
				print(shop_name)
				phone = pq(e_res).find('.shop-box').find('ul').find('li').eq(1).find('p').text()
				print(phone)
				work_time = pq(e_res).find('.shop-box').find('ul').find('li').eq(2).find('p').text()
				# print(work_time)
				price = pq(e_res).find('.shop-box').find('p').find('span').eq(4).find('strong').text()
				print(price)
				evaluate_num = pq(e_res).find('.shop-box').find('p').find('span').eq(3).text()[1:-4]
				print(evaluate_num)
				good_level = pq(e_res).find('.level-detail').find('div').eq(0).find('span').eq(2).text()[:-1]
				print(good_level)
				commonly_level = pq(e_res).find('.level-detail').find('div').eq(1).find('span').eq(2).text()[:-1]
				print(commonly_level)
				bad_level = pq(e_res).find('.level-detail').find('div').eq(2).find('span').eq(2).text()[:-1]
				print(bad_level)
				evaluate = pq(e_res).find('.shop-box').find('p').find('span').eq(2).text()
				print(evaluate)
				if len(work_time) > 11 or len(work_time) < 9:
					work_time = "全天"
					print(work_time)
				else:
					work_time = work_time
					print(work_time)
				insert_food_data_test = ("INSERT INTO food_data_test(address,shop_name,phone,work_time,price,evaluate_num,good_level,commonly_level,bad_level,evaluate)" "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
				data_food_data_test = (address,shop_name,phone,work_time,price,evaluate_num,good_level,commonly_level,bad_level,evaluate)
				self.cursor.execute(insert_food_data_test, data_food_data_test)
				self.db.commit()
			# i += 1
		except Exception as e:
			self.logger.exception('ERROR readFile:%s' %( str(e)))


	# def run(self):
	# 	thread_list = []
 #        # 1.url_list
 #        self.crawl_city_url()
 #        t_url = threading.Thread(target=self.get_url_list)
 #        thread_list.append(t_url)




if __name__ == '__main__':
	cbdnm = CrawlBaiDuNuoMi()
	cbdnm.crawl_city_url()
	# cbdnm.crawl_breakpoint_city()
	# cbdnm.crawl_food_list()
	# cbdnm.craw_detail_information_url()
	# cbdnm.craw_detail_information()

