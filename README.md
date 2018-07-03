# 基于python实现对百度糯米中有关美食的数据进行爬取，并使用echarts将抓取的数据进行展示
* 代码中还存在很多问题，非常欢迎各位大佬们能给出改进意见！
## 使用本程序前需要先配置系统的环境
* 配置的系统环境如下：<br>
* 本系统使用的是Python3.4和Django1.8.2<br>
* 用到的编译器是Sublime和Pycharm<br>
* 用到的数据库是Mysql5.6,<br>
* 用到的数据库管理工具是Navicat.<br>
## 需要先开启爬虫程序进行数据的采集
* 首先执行的程序是crawl_baidunuomi.py<br>
* 或者执行crawl_baidunuomi_toal.py<br>
## 开启美食地图系统
* 使用Pycharm打开美食地图系统，然后执行python manager.py runserver 即可打开程序<br>
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
对路径稍作修改可以爬取其他类型的数据（酒店、机票、旅游等）<br>
![](https://github.com/Maxwellwk/FoodMapSpiderNM/blob/master/image/data.jpg)
## 数据爬取流程
先获取所有城市的URL地址并将其放入列表中，然后每从列表中取一个城市的url地址就获取其城市的所有美食数据，拼接地址、翻页等。在爬取过程中用到了IP代理池，每次都会确定使用的ip，若ip失效，则替换掉，从断点处继续爬取。并将爬到的数据保存在mysql数据库中。
## 将爬取的数据进行展示
### 热力图展示
![](https://github.com/Maxwellwk/FoodMapSpiderNM/blob/master/image/%E5%9B%BE%E7%89%877.png)
### 美食地图主页展示
![](https://github.com/Maxwellwk/FoodMapSpiderNM/blob/master/image/%E5%9B%BE%E7%89%8713.png)
### 美食数据云图展示
![](https://github.com/Maxwellwk/FoodMapSpiderNM/blob/master/image/%E5%9B%BE%E7%89%879.png)
### 美食数据饼状图展示
![](https://github.com/Maxwellwk/FoodMapSpiderNM/blob/master/image/%E5%9B%BE%E7%89%8710.png)
### 美食地图详细数据展示
![](https://github.com/Maxwellwk/FoodMapSpiderNM/blob/master/image/%E5%9B%BE%E7%89%8711.png)

注：由于各种原因，数据包不能上传需要的私聊我！<br>
