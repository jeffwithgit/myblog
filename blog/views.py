# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import unicode_literals

import base64
import json
from io import BytesIO

import matplotlib.pyplot as plt
from django.shortcuts import render
from pandas import DataFrame
import pandas as pd

from . import models


def image(request):
    # 这段正常画图
    plt.axis([0, 5, 0, 20])  # [xmin,xmax,ymin,ymax]对应轴的范围
    plt.title('My first plot')  # 图名
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')  # 图上的点,最后一个参数为显示的模式

    # 转成图片的步骤
    sio = BytesIO()
    plt.savefig(sio, format='png')
    image_data = base64.b64encode(sio.getvalue()).decode()
    plt.close()  # 记得关闭，不然画出来的图是重复的
    return render(request, 'blog/image.html', {'image_data': image_data})


def timezones(request):
    """
    Counting time zones with pandas
    """
    # 数据收集
    path = 'blog/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
    lines = open(path).readlines()
    records = [json.loads(line) for line in lines]

    frame = DataFrame(records)

    # 数据清洗
    clean_tz = frame['tz'].fillna('Missing')
    clean_tz[clean_tz == ''] = 'Unknown'

    # 绘制水平条状图
    tz_counts = clean_tz.value_counts()
    tz_counts[:10].plot(kind='barh', rot=0, title='Time Zone', figsize=(10, 4))

    # 转成图片的步骤
    sio = BytesIO()
    plt.savefig(sio, format='png')
    image_data = base64.b64encode(sio.getvalue()).decode()
    plt.close()  # 记得关闭，不然不同view画出来的图会相互影响
    return render(request, 'blog/timezones.html', {'image_data': image_data})


def devicetypes(request):
    """
    Counting device type with pandas
    """
    frame = pd.read_csv('blog/ch02/cmdb_201810051456.csv')  # 该csv文件为db导出

    # 数据清洗
    clean_dt = frame['device_type'].fillna('Missing')
    clean_dt[clean_dt == ''] = 'Unknown'

    # 绘制水平条状图
    dt_counts = clean_dt.value_counts()
    # print(dt_counts)
    dt_counts[:10].plot(kind='barh', rot=0, title='Device Type', figsize=(10, 4))

    # 转成图片的步骤
    sio = BytesIO()
    plt.savefig(sio, format='png')
    image_data = base64.b64encode(sio.getvalue()).decode()
    plt.close()  # 记得关闭，不然不同view画出来的图会相互影响
    return render(request, 'blog/devicetypes.html', {'image_data': image_data})


def index(request):
    articles = models.Article.objects.all()  # all的返回即为一个列表
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})


def edit_action(request):
    title = request.POST['title']
    content = request.POST['content']
    article_id = request.POST['article_id']

    if article_id == '0':
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})
        # return HttpResponseRedirect('index')  # 此处不是templates页面，而是url

    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/article_page.html', {'article': article})
