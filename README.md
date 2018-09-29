# myblog
Django demo project
==========================================================================
前端访问地址
http://127.0.0.1:8000/blog/index/
管理控制台地址
http://127.0.0.1:8000/admin/
admin/xiayang1
==========================================================================
以下为Django的说明
安装Django：
pip freeze //查看已安装的包
pip install Django==1.11.10 --proxy=proxy.jpn.hp.com:8080 //安装Django
python -m django --version //查看版本号
django-admin startproject myblog //创建工程
--------------------------------------------------------
Django project目录结构：
manage.py
    与项目进行交互的命令行工具集的入口
    项目管理器
    执行python manage.py来查看所有命令
wsgi.py
    WSGI(Python Web Server Gateway Interface)
    Python应用与Web服务器之间通信的接口
urls.py
    url配置文件
setting.py
    项目总配置
__init.py__
    声明模块的文件
    内容默认为空
--------------------------------------------------------
创建应用
manage.py同级目录
输入: python manage.py startapp blog

启动应用
python manage.py runserver
-------------------------------------------------------
Templates:
Django Template Language(DTL)
Jinja2
类似于jsp
--------------------------------------------------------
Models:
python manage.py makemigrations app名（可选）
你的Model会被扫描, 然后与migrations文件夹中以前的版本作比较, 然后生成本次迁移文件。
再执行python manage.py migrate
查看sql：python manage.py sqlmigrate blog 0001
--------------------------------------------------------
Admin:
Django自带的自动化数据管理界面，可以直接在Admin中管理数据库
admin/xiayang1
--------------------------------------------------------
Django Shell
django交互式界面
python manage.py shell
==========================================================================