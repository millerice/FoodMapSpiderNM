from django.db import models

# Create your models here.
# 定义默认表
class food_table(models.Model):
    time_data = models.DateField() #日期
    province_name = models.CharField(max_length=60)#省名
    food_name = models.CharField(max_length=60)  # 食物名
    food_num = models.IntegerField(default=0) #食物数量

class food_table(models.Model):
    time_data = models.DateField() #日期
    province_name = models.CharField(max_length=60)#省名

#定义food_province表
class food_province(models.Model):
    time_data = models.DateField()  # 日期
    province_name = models.CharField(max_length=60)  # 省名
    tian_num = models.IntegerField(default=0)  # 食物数量
    huo_num = models.IntegerField(default=0)  # 食物数量
    xiao_num = models.IntegerField(default=0)  # 食物数量
    xi_num = models.IntegerField(default=0)  # 食物数量


class food_type(models.Model):
    food_name = models.CharField(max_length=60)  # 食物名

class nuomi_information_new(models.Model):
    address = models.CharField(max_length=300)
    shop_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=60)
    work_time = models.CharField(max_length=300)
    price = models.CharField(max_length=30)
    evaluate_num = models.CharField(max_length=50)
    good_level = models.CharField(max_length=50)
    commonly_level = models.CharField(max_length=50)
    bad_level = models.CharField(max_length=50)
    evaluate = models.CharField(max_length=50)

class AreaInfo(models.Model):
    atitle = models.CharField(verbose_name='名称', max_length=30)  # 名称
    aParent = models.ForeignKey('self', verbose_name='父级名称', null=True, blank=True)  # 父级
    def __str__(self):
        return self.atitle
    def title(self):
        return self.atitle
    title.admin_order_field = 'atitle'
    title.short_description = '地区名称'

class food_evaluate(models.Model):
    evaluate = models.CharField(max_length=50)

class food_toal_information(models.Model):
    address = models.CharField(max_length=300)
    shop_name = models.CharField(max_length=200)
    price = models.CharField(max_length=30)
    sale = models.CharField(max_length=50)
    evaluate_num = models.CharField(max_length=50)
    evaluate = models.CharField(max_length=50)

class food_hotmap_table(models.Model):
    city_name = models.CharField(max_length=200)
    food_num = models.CharField(max_length=50)

