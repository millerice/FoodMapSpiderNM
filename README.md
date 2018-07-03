# 基于python实现对百度糯米中有关美食的数据进行爬取，并使用echarts将抓取的数据进行展示
## 环境依赖
1.lxml<br>
2.xpath<br>
3.pyquery<br>
4.bs4<br>
5.etree<br>
6.re<br>
## 运行方法
pip 安装依赖<br> 
$pip install -r requirments.txt<br> 
## 运行爬虫程序
$python craw_baidunuomi.py<br>
![](https://github.com/Maxwellwk/FoodMapSpiderNM/blob/master/image/(CXPL~TMSS%24FVDI_L)PXQ3D.png)  
## 爬取的美食数据量在9万左右
![](https://github.com/Maxwellwk/FoodMapSpiderNM/blob/master/image/K%5D50N1X(AMAZ%5DNPLB7E%25BKV.jpg)
## 数据爬取流程
先获取所有城市的URL地址并将其放入列表中，然后每从列表中取一个城市的url地址就获取其城市的所有美食数据，拼接地址、翻页等。在爬取过程中用到了IP代理池，每次都会确定使用的ip，若ip失效，则替换掉，从断点处继续爬取。并将爬到的数据保存在mysql数据库中。
## 将爬取的数据进行展示
### 热力图展示
![]()
