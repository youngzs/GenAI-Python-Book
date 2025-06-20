# 第16章：Flask Web开发基础

> "Web开发就像经营一家咖啡厅，Flask是你的得力助手，帮你打造温馨舒适的数字空间。"

## 🎯 学习目标

通过本章学习，你将能够：

- 🏗️ **掌握Flask框架基础**：理解Web应用的工作原理，学会使用Flask构建Web应用
- 🛣️ **设计路由系统**：创建灵活的URL路由，处理不同类型的HTTP请求  
- 📝 **处理表单数据**：实现用户输入验证，管理会话状态
- 🗄️ **集成数据库**：使用SQLAlchemy进行数据建模和操作
- 🔌 **开发API接口**：构建RESTful API，实现前后端分离
- 🚀 **部署Web应用**：将应用部署到生产环境

## 🏪 "Web咖啡厅"比喻体系

在学习Flask之前，让我们建立一个有趣的比喻：

```
🏪 Flask应用 = 经营一家咖啡厅
├── 🍽️ 路由系统 = 菜单设计（客人看什么，点什么）
├── 👨‍🍳 视图函数 = 厨师团队（谁来做，怎么做）
├── 🍽️ 模板引擎 = 餐具摆盘（怎么呈现给客人）
├── 🛎️ 请求处理 = 服务员接单（理解客人需求）
├── 📦 数据库 = 厨房仓库（存储所有原料）
├── 🚚 API接口 = 外卖服务（远程提供服务）
└── 🏢 部署上线 = 连锁经营（规模化运营）
```

这个比喻将贯穿整个章节，让抽象的技术概念变得具体可感！

---

## 16.1 Flask框架入门 - "咖啡厅开张" ☕

> 万事开头难，但开一家咖啡厅其实很简单——你需要的只是一个地方、一份菜单、和一位厨师。

### 🎯 本节目标
- 理解Flask的基本概念和工作原理
- 学会创建第一个Flask应用
- 掌握路由系统和视图函数
- 了解模板引擎的使用方法

### 📚 理论基础：Flask是什么？

**Flask** 是一个轻量级的Python Web框架，它提供了构建Web应用所需的核心功能，同时保持简洁和灵活。

#### Flask的核心特点
```python
# Flask的设计哲学
"""
🎯 微框架 (Micro Framework)
   - 核心简单，功能通过扩展添加
   - 给开发者最大的自由度

🔧 WSGI兼容
   - 遵循Python Web服务器网关接口标准
   - 可以部署到各种Web服务器

📦 内置功能
   - 路由系统：URL到函数的映射
   - 模板引擎：Jinja2模板系统
   - 请求处理：HTTP请求和响应处理
   - 会话管理：用户状态保持

🧩 扩展生态
   - Flask-SQLAlchemy：数据库ORM
   - Flask-WTF：表单处理
   - Flask-Login：用户认证
   - Flask-Mail：邮件发送
"""
```

### 🛠️ 环境准备

#### 1. 安装Flask和相关依赖

```bash
# 创建虚拟环境
python -m venv flask_env
flask_env\Scripts\activate  # Windows
# source flask_env/bin/activate  # Linux/Mac

# 安装核心包
pip install Flask==2.3.3
pip install Flask-SQLAlchemy==3.0.5
pip install Flask-WTF==1.1.1
pip install Flask-Login==0.6.2
```

#### 2. 项目结构设计

```
my_coffee_shop/          # 我们的咖啡厅项目
├── app.py              # 主应用文件（咖啡厅管理中心）
├── config.py           # 配置文件（经营方针）
├── requirements.txt    # 依赖清单（供应商列表）
├── templates/          # 模板目录（餐具仓库）
│   ├── base.html      # 基础模板（标准餐具）
│   ├── index.html     # 首页模板（欢迎台布置）
│   └── about.html     # 关于页面（店铺介绍）
├── static/            # 静态文件（装饰用品）
│   ├── css/          # 样式文件（装修风格）
│   ├── js/           # JavaScript（智能设备）
│   └── images/       # 图片（装饰画）
└── models/            # 数据模型（仓库管理）
```

### 🚀 第一个Flask应用：Hello Coffee!

让我们从最简单的咖啡厅开始：

```python
# app.py - 咖啡厅的第一天营业
from flask import Flask

# 创建咖啡厅实例（开店！）
app = Flask(__name__)

# 设置咖啡厅的基本信息
app.config['SECRET_KEY'] = 'your-secret-key-here'  # 店铺密钥

@app.route('/')  # 菜单项：首页（欢迎光临）
def home():
    """首页视图函数 - 相当于门口的欢迎员"""
    return """
    <h1>🏪 欢迎来到我的咖啡厅！</h1>
    <p>☕ 这里有最香浓的咖啡和最温暖的服务</p>
    <a href="/menu">查看菜单</a> | 
    <a href="/about">关于我们</a>
    """

@app.route('/menu')  # 菜单项：菜单页面
def menu():
    """菜单视图函数 - 相当于菜单展示员"""
    menu_items = [
        "☕ 美式咖啡 - ¥25",
        "🥛 拿铁咖啡 - ¥30", 
        "🍰 提拉米苏 - ¥35",
        "🥪 三明治 - ¥20"
    ]
    
    menu_html = "<h1>📋 咖啡厅菜单</h1><ul>"
    for item in menu_items:
        menu_html += f"<li>{item}</li>"
    menu_html += "</ul><a href='/'>返回首页</a>"
    
    return menu_html

@app.route('/about')  # 菜单项：关于页面
def about():
    """关于页面视图函数 - 相当于店铺介绍员"""
    return """
    <h1>🏪 关于我们</h1>
    <p>我们是一家温馨的咖啡厅，致力于为每位客人提供最好的咖啡体验。</p>
    <p>📍 地址：Python街Flask大道16号</p>
    <p>⏰ 营业时间：9:00-21:00</p>
    <a href="/">返回首页</a>
    """

# 启动咖啡厅（开始营业！）
if __name__ == '__main__':
    print("🏪 咖啡厅正在开张...")
    print("🌐 请访问：http://127.0.0.1:5000")
    app.run(debug=True)  # debug=True 相当于"试营业模式"
```

#### 运行你的第一个咖啡厅

```bash
# 启动应用
python app.py

# 你会看到：
"""
🏪 咖啡厅正在开张...
🌐 请访问：http://127.0.0.1:5000
 * Running on http://127.0.0.1:5000
 * Debug mode: on
"""
```

打开浏览器访问 `http://127.0.0.1:5000`，你的第一家数字咖啡厅就开张了！

### 🛣️ 深入理解：路由系统

路由系统就像咖啡厅的菜单设计，决定了客人能点什么，以及每个订单由谁来处理。

#### 1. 基本路由语法

```python
@app.route('/路径')  # 装饰器：定义菜单项
def 视图函数名():    # 函数：指定处理的厨师
    return '响应内容'  # 返回：端给客人的东西
```

#### 2. 动态路由：个性化服务

```python
# 个性化欢迎 - 像咖啡师记住常客的名字
@app.route('/welcome/<name>')
def welcome_customer(name):
    """个性化欢迎函数"""
    return f"""
    <h1>🎉 欢迎 {name} 来到我们的咖啡厅！</h1>
    <p>很高兴再次见到您！</p>
    <a href="/">返回首页</a>
    """

# 订单详情 - 根据订单号查看详情
@app.route('/order/<int:order_id>')
def order_detail(order_id):
    """订单详情查看"""
    # 模拟订单数据
    orders = {
        1: {"item": "美式咖啡", "price": 25, "status": "制作中"},
        2: {"item": "拿铁咖啡", "price": 30, "status": "已完成"},
        3: {"item": "提拉米苏", "price": 35, "status": "已送达"}
    }
    
    order = orders.get(order_id)
    if order:
        return f"""
        <h1>📋 订单 #{order_id} 详情</h1>
        <p>商品：{order['item']}</p>
        <p>价格：¥{order['price']}</p>
        <p>状态：{order['status']}</p>
        <a href="/menu">继续点餐</a>
        """
    else:
        return f"<h1>❌ 订单 #{order_id} 不存在</h1><a href='/'>返回首页</a>"

# 分类菜单 - 按类别展示商品
@app.route('/category/<category>')
def show_category(category):
    """按分类显示商品"""
    categories = {
        'coffee': ['美式咖啡', '拿铁咖啡', '卡布奇诺'],
        'dessert': ['提拉米苏', '芝士蛋糕', '马卡龙'],
        'snack': ['三明治', '沙拉', '饼干']
    }
    
    items = categories.get(category, [])
    if items:
        items_html = "<ul>"
        for item in items:
            items_html += f"<li>{item}</li>"
        items_html += "</ul>"
        
        return f"""
        <h1>📂 {category.title()} 分类</h1>
        {items_html}
        <a href="/menu">查看完整菜单</a>
        """
    else:
        return f"<h1>❌ 分类 '{category}' 不存在</h1><a href='/menu'>查看菜单</a>"
```

#### 3. HTTP方法：不同的服务方式

```python
from flask import request

# 支持多种HTTP方法的路由
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """联系我们页面 - 支持查看和提交"""
    if request.method == 'GET':
        # GET请求：显示联系表单（客人想要联系表）
        return """
        <h1>📞 联系我们</h1>
        <form method="POST">
            <p>姓名：<input type="text" name="name" required></p>
            <p>邮箱：<input type="email" name="email" required></p>
            <p>消息：<textarea name="message" required></textarea></p>
            <p><button type="submit">发送消息</button></p>
        </form>
        <a href="/">返回首页</a>
        """
    else:
        # POST请求：处理表单提交（客人提交了联系信息）
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # 这里可以保存到数据库或发送邮件
        return f"""
        <h1>✅ 消息已收到！</h1>
        <p>感谢 {name} 的反馈！</p>
        <p>我们会尽快回复到 {email}</p>
        <a href="/">返回首页</a>
        """

# 仅支持POST的路由（比如订单提交）
@app.route('/submit_order', methods=['POST'])
def submit_order():
    """提交订单 - 只接受POST请求"""
    item = request.form.get('item')
    quantity = request.form.get('quantity', 1)
    
    return f"""
    <h1>✅ 订单已提交！</h1>
    <p>商品：{item}</p>
    <p>数量：{quantity}</p>
    <p>我们正在为您准备...</p>
    <a href="/menu">继续点餐</a>
    """
```

### 🍽️ 模板引擎：餐具与摆盘艺术

如果说路由是菜单，视图函数是厨师，那么模板就是餐具和摆盘——决定了美食如何优雅地呈现给客人。

#### 1. 为什么需要模板？

```python
# 不使用模板的问题（直接在视图函数中写HTML）
@app.route('/ugly_page')
def ugly_page():
    return """
    <html>
    <head><title>丑陋的页面</title></head>
    <body>
        <h1>这样写HTML很痛苦</h1>
        <p>代码混乱，难以维护</p>
        <p>没有复用性</p>
    </body>
    </html>
    """
    # 问题：HTML和Python代码混在一起，就像在厨房里摆盘一样混乱！
```

#### 2. Jinja2模板引擎基础

首先创建模板目录和基础模板：

```html
<!-- templates/base.html - 基础餐具模板 -->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}我的咖啡厅{% endblock %}</title>
    <style>
        /* 咖啡厅基础装修风格 */
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5dc;  /* 米色背景 */
            color: #4a4a4a;
        }
        
        .header {
            background-color: #8b4513;  /* 咖啡色 */
            color: white;
            padding: 1rem;
            text-align: center;
        }
        
        .nav {
            background-color: #deb887;  /* 浅咖啡色 */
            padding: 0.5rem;
            text-align: center;
        }
        
        .nav a {
            color: #4a4a4a;
            text-decoration: none;
            margin: 0 1rem;
            font-weight: bold;
        }
        
        .nav a:hover {
            color: #8b4513;
        }
        
        .container {
            max-width: 800px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        
        .footer {
            background-color: #8b4513;
            color: white;
            text-align: center;
            padding: 1rem;
            margin-top: 2rem;
        }
    </style>
</head>
<body>
    <!-- 咖啡厅顶部标识 -->
    <header class="header">
        <h1>☕ 我的温馨咖啡厅</h1>
        <p>品味生活，从一杯好咖啡开始</p>
    </header>
    
    <!-- 导航菜单 -->
    <nav class="nav">
        <a href="/">🏠 首页</a>
        <a href="/menu">📋 菜单</a>
        <a href="/about">ℹ️ 关于我们</a>
        <a href="/contact">📞 联系我们</a>
    </nav>
    
    <!-- 主要内容区域 -->
    <main class="container">
        {% block content %}
        <!-- 具体页面内容将在这里显示 -->
        {% endblock %}
    </main>
    
    <!-- 页脚信息 -->
    <footer class="footer">
        <p>&copy; 2024 我的咖啡厅 | 用Flask制作，用❤️调味</p>
    </footer>
</body>
</html>
```

```html
<!-- templates/index.html - 首页模板 -->
{% extends "base.html" %}

{% block title %}首页 - 我的咖啡厅{% endblock %}

{% block content %}
<div style="text-align: center;">
    <h1>🎉 欢迎来到我们的咖啡厅！</h1>
    
    <div style="margin: 2rem 0;">
        <img src="https://via.placeholder.com/400x200/8b4513/ffffff?text=☕+Welcome" 
             alt="咖啡厅欢迎图" style="max-width: 100%; border-radius: 10px;">
    </div>
    
    <p style="font-size: 1.2rem; margin: 1.5rem 0;">
        在这里，每一杯咖啡都承载着我们的用心，每一个微笑都传递着温暖。
    </p>
    
    <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
        <a href="/menu" style="background-color: #8b4513; color: white; padding: 0.8rem 1.5rem; 
           text-decoration: none; border-radius: 5px; font-weight: bold;">
            📋 查看菜单
        </a>
        <a href="/about" style="background-color: #deb887; color: #4a4a4a; padding: 0.8rem 1.5rem; 
           text-decoration: none; border-radius: 5px; font-weight: bold;">
            ℹ️ 了解更多
        </a>
    </div>
    
    <!-- 今日推荐 -->
    <div style="margin-top: 3rem; padding: 1.5rem; background-color: white; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
        <h2>🌟 今日推荐</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="text-align: center; padding: 1rem;">
                <h3>☕ 招牌拿铁</h3>
                <p>香浓咖啡与丝滑牛奶的完美融合</p>
                <span style="color: #8b4513; font-weight: bold;">¥30</span>
            </div>
            <div style="text-align: center; padding: 1rem;">
                <h3>🍰 提拉米苏</h3>
                <p>意式经典甜品，入口即化</p>
                <span style="color: #8b4513; font-weight: bold;">¥35</span>
            </div>
            <div style="text-align: center; padding: 1rem;">
                <h3>🥪 俱乐部三明治</h3>
                <p>新鲜食材，营养丰富</p>
                <span style="color: #8b4513; font-weight: bold;">¥25</span>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

#### 3. 在视图函数中使用模板

```python
from flask import render_template

# 更新后的视图函数 - 使用模板
@app.route('/')
def home():
    """首页视图 - 使用模板渲染"""
    return render_template('index.html')

@app.route('/menu')
def menu():
    """菜单页面 - 传递数据到模板"""
    # 咖啡厅菜单数据（实际项目中来自数据库）
    menu_data = {
        'coffee': [
            {'name': '美式咖啡', 'price': 25, 'description': '经典黑咖啡，苦中带香'},
            {'name': '拿铁咖啡', 'price': 30, 'description': '咖啡与牛奶的完美融合'},
            {'name': '卡布奇诺', 'price': 28, 'description': '浓郁咖啡配奶泡'},
            {'name': '摩卡咖啡', 'price': 32, 'description': '咖啡巧克力双重享受'}
        ],
        'dessert': [
            {'name': '提拉米苏', 'price': 35, 'description': '意式经典甜品'},
            {'name': '芝士蛋糕', 'price': 30, 'description': '浓郁芝士香味'},
            {'name': '马卡龙', 'price': 8, 'description': '法式精致小点'}
        ],
        'snack': [
            {'name': '俱乐部三明治', 'price': 25, 'description': '多层丰富口感'},
            {'name': '凯撒沙拉', 'price': 22, 'description': '新鲜蔬菜健康选择'},
            {'name': '牛角包', 'price': 15, 'description': '法式酥脆面包'}
        ]
    }
    
    return render_template('menu.html', menu=menu_data)

@app.route('/about')
def about():
    """关于页面 - 传递店铺信息"""
    shop_info = {
        'name': '我的温馨咖啡厅',
        'address': 'Python街Flask大道16号',
        'phone': '400-FLASK-16',
        'hours': '周一至周日 9:00-21:00',
        'story': '我们的咖啡厅成立于2024年，致力于为每位客人提供最优质的咖啡体验。我们精选世界各地的优质咖啡豆，用心烘焙，用爱调制。',
        'features': [
            '☕ 精选咖啡豆，现场烘焙',
            '🍰 手工制作甜品',
            '📚 舒适阅读环境',
            '💻 免费WiFi',
            '🎵 轻松背景音乐'
        ]
    }
    
    return render_template('about.html', shop=shop_info)
```

对应的模板文件：

```html
<!-- templates/menu.html - 菜单页面模板 -->
{% extends "base.html" %}

{% block title %}菜单 - 我的咖啡厅{% endblock %}

{% block content %}
<h1 style="text-align: center; color: #8b4513;">📋 咖啡厅菜单</h1>

{% for category, items in menu.items() %}
<div style="margin: 2rem 0; padding: 1.5rem; background-color: white; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
    <h2 style="color: #8b4513; border-bottom: 2px solid #deb887; padding-bottom: 0.5rem;">
        {% if category == 'coffee' %}☕ 咖啡类
        {% elif category == 'dessert' %}🍰 甜品类
        {% else %}🥪 轻食类{% endif %}
    </h2>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem; margin-top: 1rem;">
        {% for item in items %}
        <div style="border: 1px solid #deb887; border-radius: 8px; padding: 1rem;">
            <h3 style="margin: 0 0 0.5rem 0; color: #8b4513;">{{ item.name }}</h3>
            <p style="margin: 0.5rem 0; color: #666; font-size: 0.9rem;">{{ item.description }}</p>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1rem;">
                <span style="font-size: 1.2rem; font-weight: bold; color: #8b4513;">¥{{ item.price }}</span>
                <button style="background-color: #8b4513; color: white; border: none; padding: 0.5rem 1rem; border-radius: 5px; cursor: pointer;">
                    加入订单
                </button>
            </div>
        </div>
        {% endfor %}
    </div>
</div>
{% endfor %}

<div style="text-align: center; margin-top: 2rem;">
    <p style="color: #666;">所有价格均为人民币，如有变动恕不另行通知</p>
    <a href="/" style="color: #8b4513; text-decoration: none;">← 返回首页</a>
</div>
{% endblock %}
```

### 🚀 实战项目：个人博客系统

现在让我们把学到的知识整合起来，创建一个完整的个人博客系统：

```python
# blog_app.py - 完整的博客应用
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-blog-secret-key'

# 模拟博客数据（实际项目中使用数据库）
blog_posts = [
    {
        'id': 1,
        'title': '我的第一篇博客',
        'content': '欢迎来到我的博客！这里我会分享我的学习心得和生活感悟。',
        'author': '博主',
        'date': datetime(2024, 1, 1),
        'tags': ['生活', '学习']
    },
    {
        'id': 2,
        'title': 'Flask学习笔记',
        'content': 'Flask是一个很棒的Python Web框架，轻量级但功能强大。',
        'author': '博主',
        'date': datetime(2024, 1, 15),
        'tags': ['技术', 'Python', 'Flask']
    }
]

@app.route('/')
def blog_home():
    """博客首页 - 显示所有文章"""
    return render_template('blog/index.html', posts=blog_posts)

@app.route('/post/<int:post_id>')
def blog_post(post_id):
    """文章详情页"""
    post = next((p for p in blog_posts if p['id'] == post_id), None)
    if post:
        return render_template('blog/post.html', post=post)
    else:
        return "文章不存在", 404

@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    """创建新文章"""
    if request.method == 'GET':
        return render_template('blog/new_post.html')
    else:
        # 处理表单提交
        title = request.form.get('title')
        content = request.form.get('content')
        tags = request.form.get('tags', '').split(',')
        
        # 创建新文章
        new_post = {
            'id': len(blog_posts) + 1,
            'title': title,
            'content': content,
            'author': '博主',
            'date': datetime.now(),
            'tags': [tag.strip() for tag in tags if tag.strip()]
        }
        
        blog_posts.append(new_post)
        return redirect(url_for('blog_home'))

@app.route('/about')
def blog_about():
    """关于页面"""
    return render_template('blog/about.html')

if __name__ == '__main__':
    app.run(debug=True)
```

对应的模板文件：

```html
<!-- templates/blog/base.html - 博客基础模板 -->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}我的个人博客{% endblock %}</title>
    <style>
        body {
            font-family: 'Georgia', serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f8f9fa;
            color: #333;
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem 0;
            text-align: center;
        }
        
        .nav {
            background-color: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            padding: 1rem 0;
        }
        
        .nav-container {
            max-width: 800px;
            margin: 0 auto;
            display: flex;
            justify-content: center;
            gap: 2rem;
        }
        
        .nav a {
            color: #333;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s;
        }
        
        .nav a:hover {
            color: #667eea;
        }
        
        .container {
            max-width: 800px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        
        .footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 2rem 0;
            margin-top: 4rem;
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>📝 我的个人博客</h1>
        <p>记录生活，分享思考</p>
    </header>
    
    <nav class="nav">
        <div class="nav-container">
            <a href="/">🏠 首页</a>
            <a href="/new_post">✍️ 写文章</a>
            <a href="/about">👤 关于我</a>
        </div>
    </nav>
    
    <main class="container">
        {% block content %}{% endblock %}
    </main>
    
    <footer class="footer">
        <p>&copy; 2024 我的个人博客 | 用Flask构建，用心维护</p>
    </footer>
</body>
</html>
```

### 📝 本节小结

通过"咖啡厅开张"这一节，我们学会了：

1. **Flask基础概念**：理解了微框架的设计理念
2. **路由系统**：学会了静态路由、动态路由和HTTP方法
3. **模板引擎**：掌握了Jinja2的基本语法和模板继承
4. **项目实战**：完成了从简单页面到博客系统的完整开发

**核心要点回顾**：
- 🏪 Flask应用就像咖啡厅，需要菜单（路由）、厨师（视图函数）、餐具（模板）
- 🛣️ 路由系统负责URL到函数的映射，支持动态参数和多种HTTP方法
- 🍽️ 模板引擎分离了展示逻辑和业务逻辑，提高代码可维护性
- 🚀 实际项目中要合理组织代码结构，使用模板继承提高复用性

**下一节预告**：在16.2节"顾客点餐服务"中，我们将学习如何处理用户输入、验证表单数据、管理用户会话，让我们的咖啡厅能够真正为客人提供个性化服务！ 

---

## 16.2 请求处理与表单 - "顾客点餐服务" 🛎️

> 一家咖啡厅的成功不仅在于好的咖啡，更在于优质的服务。服务员要能听懂客人的需求，准确记录订单，还要记住常客的喜好。

### 🎯 本节目标
- 掌握HTTP请求的处理方法
- 学会创建和验证HTML表单
- 理解会话管理和用户状态保持
- 实现用户注册和登录系统

### 📚 理论基础：HTTP请求处理

在Web开发中，客户端（浏览器）和服务器之间通过HTTP协议进行通信，就像客人和服务员之间的对话。

#### HTTP请求的组成部分

```python
"""
HTTP请求 = 客人的完整订单
├── 请求方法 (GET/POST/PUT/DELETE) = 服务类型（查看菜单/下订单/修改订单/取消订单）
├── 请求头 (Headers) = 客人的基本信息（语言偏好、设备类型等）
├── 请求参数 (Query Parameters) = 具体要求（不加糖、少冰等）
└── 请求体 (Request Body) = 详细订单内容（表单数据、JSON数据等）
"""
```

### 🛎️ Flask中的请求处理

#### 1. 获取请求数据

```python
from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-for-sessions'

@app.route('/order_info')
def show_request_info():
    """展示请求信息 - 像服务员了解客人需求"""
    info = {
        'method': request.method,           # 请求方法
        'url': request.url,                # 完整URL
        'path': request.path,              # 路径部分
        'args': dict(request.args),        # URL参数
        'form': dict(request.form),        # 表单数据
        'headers': dict(request.headers),   # 请求头
        'remote_addr': request.remote_addr, # 客户端IP
        'user_agent': request.user_agent.string  # 浏览器信息
    }
    
    return f"""
    <h1>📋 请求信息详情</h1>
    <h2>基本信息</h2>
    <p><strong>请求方法:</strong> {info['method']}</p>
    <p><strong>请求URL:</strong> {info['url']}</p>
    <p><strong>客户端IP:</strong> {info['remote_addr']}</p>
    
    <h2>URL参数 (Query Parameters)</h2>
    <pre>{info['args']}</pre>
    
    <h2>表单数据</h2>
    <pre>{info['form']}</pre>
    
    <a href="/">返回首页</a>
    """

# 测试URL: /order_info?drink=coffee&size=large&sugar=no
```

#### 2. 处理不同类型的请求参数

```python
@app.route('/search')
def search_menu():
    """菜单搜索功能 - 根据客人需求筛选"""
    # 获取URL参数 (Query Parameters)
    keyword = request.args.get('q', '')           # 搜索关键词
    category = request.args.get('category', 'all') # 分类筛选
    min_price = request.args.get('min_price', 0, type=int)  # 最低价格
    max_price = request.args.get('max_price', 100, type=int) # 最高价格
    
    # 模拟菜单数据
    menu_items = [
        {'name': '美式咖啡', 'category': 'coffee', 'price': 25},
        {'name': '拿铁咖啡', 'category': 'coffee', 'price': 30},
        {'name': '提拉米苏', 'category': 'dessert', 'price': 35},
        {'name': '三明治', 'category': 'snack', 'price': 20}
    ]
    
    # 根据条件筛选
    filtered_items = []
    for item in menu_items:
        # 关键词匹配
        if keyword and keyword.lower() not in item['name'].lower():
            continue
        # 分类筛选
        if category != 'all' and item['category'] != category:
            continue
        # 价格范围
        if not (min_price <= item['price'] <= max_price):
            continue
        
        filtered_items.append(item)
    
    # 构建结果HTML
    result_html = f"<h1>🔍 搜索结果</h1>"
    result_html += f"<p>关键词: '{keyword}' | 分类: {category} | 价格: ¥{min_price}-{max_price}</p>"
    
    if filtered_items:
        result_html += "<ul>"
        for item in filtered_items:
            result_html += f"<li>{item['name']} - {item['category']} - ¥{item['price']}</li>"
        result_html += "</ul>"
    else:
        result_html += "<p>❌ 没有找到符合条件的商品</p>"
    
    result_html += """
    <form method="GET" action="/search">
        <p>
            关键词: <input type="text" name="q" value="">
            分类: <select name="category">
                <option value="all">全部</option>
                <option value="coffee">咖啡</option>
                <option value="dessert">甜品</option>
                <option value="snack">轻食</option>
            </select>
        </p>
        <p>
            价格范围: ¥<input type="number" name="min_price" value="0" min="0"> - 
                     ¥<input type="number" name="max_price" value="100" min="0">
        </p>
        <p><button type="submit">🔍 搜索</button></p>
    </form>
    <a href="/">返回首页</a>
    """
    
    return result_html
```

### 📝 HTML表单处理

表单是客人向咖啡厅下订单的主要方式，我们需要仔细处理每一个细节。

#### 1. 基础表单创建和处理

```python
@app.route('/order', methods=['GET', 'POST'])
def place_order():
    """下订单功能 - 完整的点餐流程"""
    if request.method == 'GET':
        # 显示订单表单
        return render_template('order_form.html')
    else:
        # 处理订单提交
        # 获取表单数据
        customer_name = request.form.get('customer_name')
        drink = request.form.get('drink')
        size = request.form.get('size')
        sugar = request.form.get('sugar')
        milk = request.form.get('milk')
        special_requests = request.form.get('special_requests', '')
        
        # 基础验证
        errors = []
        if not customer_name:
            errors.append("请填写客人姓名")
        if not drink:
            errors.append("请选择饮品")
        if not size:
            errors.append("请选择杯型")
            
        if errors:
            # 有错误，重新显示表单
            return render_template('order_form.html', 
                                 errors=errors,
                                 form_data=request.form)
        
        # 计算价格
        prices = {
            'americano': {'small': 20, 'medium': 25, 'large': 30},
            'latte': {'small': 25, 'medium': 30, 'large': 35},
            'cappuccino': {'small': 23, 'medium': 28, 'large': 33}
        }
        
        total_price = prices.get(drink, {}).get(size, 0)
        
        # 生成订单号
        import time
        order_id = f"ORD{int(time.time())}"
        
        # 保存订单（实际项目中保存到数据库）
        order = {
            'id': order_id,
            'customer_name': customer_name,
            'drink': drink,
            'size': size,
            'sugar': sugar,
            'milk': milk,
            'special_requests': special_requests,
            'total_price': total_price,
            'status': '制作中',
            'order_time': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # 使用flash消息显示成功信息
        flash(f'订单 {order_id} 已成功提交！', 'success')
        
        return render_template('order_success.html', order=order)

# 对应的模板文件
```

```html
<!-- templates/order_form.html - 订单表单模板 -->
{% extends "base.html" %}

{% block title %}下订单 - 我的咖啡厅{% endblock %}

{% block content %}
<div style="max-width: 600px; margin: 0 auto;">
    <h1 style="text-align: center; color: #8b4513;">📝 客人订单</h1>
    
    <!-- 显示错误信息 -->
    {% if errors %}
    <div style="background-color: #ffe6e6; border: 1px solid #ff9999; padding: 1rem; border-radius: 5px; margin-bottom: 1rem;">
        <h3 style="color: #cc0000; margin: 0 0 0.5rem 0;">❌ 请修正以下错误：</h3>
        <ul style="margin: 0; color: #cc0000;">
            {% for error in errors %}
            <li>{{ error }}</li>
            {% endfor %}
        </ul>
    </div>
    {% endif %}
    
    <!-- 显示flash消息 -->
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
            <div style="background-color: {% if category == 'success' %}#e6ffe6{% else %}#ffe6e6{% endif %}; 
                        border: 1px solid {% if category == 'success' %}#99ff99{% else %}#ff9999{% endif %}; 
                        padding: 1rem; border-radius: 5px; margin-bottom: 1rem;">
                <p style="margin: 0; color: {% if category == 'success' %}#006600{% else %}#cc0000{% endif %};">
                    {{ message }}
                </p>
            </div>
            {% endfor %}
        {% endif %}
    {% endwith %}
    
    <form method="POST" style="background-color: white; padding: 2rem; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
        <!-- 客人信息 -->
        <div style="margin-bottom: 1.5rem;">
            <label style="display: block; font-weight: bold; margin-bottom: 0.5rem;">👤 客人姓名:</label>
            <input type="text" name="customer_name" 
                   value="{{ form_data.customer_name if form_data else '' }}"
                   style="width: 100%; padding: 0.8rem; border: 1px solid #ddd; border-radius: 5px; font-size: 1rem;"
                   placeholder="请输入您的姓名" required>
        </div>
        
        <!-- 饮品选择 -->
        <div style="margin-bottom: 1.5rem;">
            <label style="display: block; font-weight: bold; margin-bottom: 0.5rem;">☕ 选择饮品:</label>
            <select name="drink" style="width: 100%; padding: 0.8rem; border: 1px solid #ddd; border-radius: 5px; font-size: 1rem;" required>
                <option value="">请选择饮品</option>
                <option value="americano" {% if form_data and form_data.drink == 'americano' %}selected{% endif %}>美式咖啡</option>
                <option value="latte" {% if form_data and form_data.drink == 'latte' %}selected{% endif %}>拿铁咖啡</option>
                <option value="cappuccino" {% if form_data and form_data.drink == 'cappuccino' %}selected{% endif %}>卡布奇诺</option>
            </select>
        </div>
        
        <!-- 杯型选择 -->
        <div style="margin-bottom: 1.5rem;">
            <label style="display: block; font-weight: bold; margin-bottom: 0.5rem;">📏 选择杯型:</label>
            <div style="display: flex; gap: 1rem;">
                <label style="display: flex; align-items: center; cursor: pointer;">
                    <input type="radio" name="size" value="small" 
                           {% if form_data and form_data.size == 'small' %}checked{% endif %}
                           style="margin-right: 0.5rem;">
                    小杯 (+¥0)
                </label>
                <label style="display: flex; align-items: center; cursor: pointer;">
                    <input type="radio" name="size" value="medium" 
                           {% if form_data and form_data.size == 'medium' %}checked{% endif %}
                           style="margin-right: 0.5rem;">
                    中杯 (+¥5)
                </label>
                <label style="display: flex; align-items: center; cursor: pointer;">
                    <input type="radio" name="size" value="large" 
                           {% if form_data and form_data.size == 'large' %}checked{% endif %}
                           style="margin-right: 0.5rem;">
                    大杯 (+¥10)
                </label>
            </div>
        </div>
        
        <!-- 糖分选择 -->
        <div style="margin-bottom: 1.5rem;">
            <label style="display: block; font-weight: bold; margin-bottom: 0.5rem;">🍯 糖分要求:</label>
            <select name="sugar" style="width: 100%; padding: 0.8rem; border: 1px solid #ddd; border-radius: 5px; font-size: 1rem;">
                <option value="normal" {% if form_data and form_data.sugar == 'normal' %}selected{% endif %}>正常糖</option>
                <option value="less" {% if form_data and form_data.sugar == 'less' %}selected{% endif %}>少糖</option>
                <option value="none" {% if form_data and form_data.sugar == 'none' %}selected{% endif %}>无糖</option>
                <option value="extra" {% if form_data and form_data.sugar == 'extra' %}selected{% endif %}>多糖</option>
            </select>
        </div>
        
        <!-- 奶制品选择 -->
        <div style="margin-bottom: 1.5rem;">
            <label style="display: block; font-weight: bold; margin-bottom: 0.5rem;">🥛 奶制品选择:</label>
            <div style="display: flex; flex-wrap: wrap; gap: 1rem;">
                <label style="display: flex; align-items: center; cursor: pointer;">
                    <input type="checkbox" name="milk" value="whole_milk" 
                           {% if form_data and 'whole_milk' in form_data.getlist('milk') %}checked{% endif %}
                           style="margin-right: 0.5rem;">
                    全脂牛奶
                </label>
                <label style="display: flex; align-items: center; cursor: pointer;">
                    <input type="checkbox" name="milk" value="skim_milk" 
                           {% if form_data and 'skim_milk' in form_data.getlist('milk') %}checked{% endif %}
                           style="margin-right: 0.5rem;">
                    脱脂牛奶
                </label>
                <label style="display: flex; align-items: center; cursor: pointer;">
                    <input type="checkbox" name="milk" value="soy_milk" 
                           {% if form_data and 'soy_milk' in form_data.getlist('milk') %}checked{% endif %}
                           style="margin-right: 0.5rem;">
                    豆奶
                </label>
                <label style="display: flex; align-items: center; cursor: pointer;">
                    <input type="checkbox" name="milk" value="oat_milk" 
                           {% if form_data and 'oat_milk' in form_data.getlist('milk') %}checked{% endif %}
                           style="margin-right: 0.5rem;">
                    燕麦奶
                </label>
            </div>
        </div>
        
        <!-- 特殊要求 -->
        <div style="margin-bottom: 1.5rem;">
            <label style="display: block; font-weight: bold; margin-bottom: 0.5rem;">📝 特殊要求:</label>
            <textarea name="special_requests" 
                      style="width: 100%; padding: 0.8rem; border: 1px solid #ddd; border-radius: 5px; font-size: 1rem; min-height: 80px;"
                      placeholder="如有特殊要求请在此说明...">{{ form_data.special_requests if form_data else '' }}</textarea>
        </div>
        
        <!-- 提交按钮 -->
        <div style="text-align: center;">
            <button type="submit" style="background-color: #8b4513; color: white; border: none; padding: 1rem 2rem; border-radius: 5px; font-size: 1.1rem; cursor: pointer; font-weight: bold;">
                🛎️ 提交订单
            </button>
        </div>
    </form>
    
    <div style="text-align: center; margin-top: 1rem;">
        <a href="/" style="color: #8b4513; text-decoration: none;">← 返回首页</a>
    </div>
</div>
{% endblock %}
```

### 🎫 会话管理：记住常客喜好

会话（Session）就像咖啡厅的会员卡系统，让我们能够记住每位客人的偏好和历史订单。

#### 1. Flask Session基础

```python
from flask import session

@app.route('/set_preference', methods=['POST'])
def set_preference():
    """设置客人偏好 - 像办理会员卡"""
    # 从表单获取偏好设置
    favorite_drink = request.form.get('favorite_drink')
    favorite_size = request.form.get('favorite_size')
    sugar_level = request.form.get('sugar_level')
    
    # 保存到会话中
    session['favorite_drink'] = favorite_drink
    session['favorite_size'] = favorite_size
    session['sugar_level'] = sugar_level
    session['customer_name'] = request.form.get('customer_name')
    
    flash('偏好设置已保存！下次点餐会为您自动填充', 'success')
    return redirect(url_for('order_with_preference'))

@app.route('/order_with_preference')
def order_with_preference():
    """智能订单表单 - 根据会员偏好预填充"""
    # 从会话中获取偏好
    preferences = {
        'customer_name': session.get('customer_name', ''),
        'favorite_drink': session.get('favorite_drink', ''),
        'favorite_size': session.get('favorite_size', ''),
        'sugar_level': session.get('sugar_level', 'normal')
    }
    
    return render_template('smart_order_form.html', preferences=preferences)

@app.route('/clear_session')
def clear_session():
    """清除会话 - 像注销会员卡"""
    session.clear()
    flash('会话已清除，偏好设置已重置', 'info')
    return redirect(url_for('home'))

@app.route('/view_session')
def view_session():
    """查看当前会话内容 - 调试用"""
    return f"""
    <h1>🎫 当前会话信息</h1>
    <pre>{dict(session)}</pre>
    <a href="/clear_session">清除会话</a> | 
    <a href="/">返回首页</a>
    """
```

#### 2. 购物车功能实现

```python
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    """添加商品到购物车"""
    item_name = request.form.get('item_name')
    item_price = float(request.form.get('item_price', 0))
    quantity = int(request.form.get('quantity', 1))
    
    # 初始化购物车（如果不存在）
    if 'cart' not in session:
        session['cart'] = []
    
    # 检查商品是否已在购物车中
    cart = session['cart']
    found = False
    for item in cart:
        if item['name'] == item_name:
            item['quantity'] += quantity
            found = True
            break
    
    if not found:
        cart.append({
            'name': item_name,
            'price': item_price,
            'quantity': quantity
        })
    
    session['cart'] = cart  # 更新会话
    flash(f'已将 {item_name} x{quantity} 添加到购物车', 'success')
    return redirect(url_for('view_cart'))

@app.route('/cart')
def view_cart():
    """查看购物车"""
    cart = session.get('cart', [])
    total = sum(item['price'] * item['quantity'] for item in cart)
    
    return render_template('cart.html', cart=cart, total=total)

@app.route('/remove_from_cart/<int:item_index>')
def remove_from_cart(item_index):
    """从购物车移除商品"""
    cart = session.get('cart', [])
    if 0 <= item_index < len(cart):
        removed_item = cart.pop(item_index)
        session['cart'] = cart
        flash(f'已从购物车移除 {removed_item["name"]}', 'info')
    
    return redirect(url_for('view_cart'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    """结账流程"""
    cart = session.get('cart', [])
    if not cart:
        flash('购物车为空，无法结账', 'warning')
        return redirect(url_for('menu'))
    
    if request.method == 'GET':
        total = sum(item['price'] * item['quantity'] for item in cart)
        return render_template('checkout.html', cart=cart, total=total)
    else:
        # 处理结账
        customer_name = request.form.get('customer_name')
        phone = request.form.get('phone')
        
        # 生成订单
        import time
        order_id = f"ORD{int(time.time())}"
        
        # 清空购物车
        session.pop('cart', None)
        
        flash(f'订单 {order_id} 已成功提交！我们会尽快为您准备', 'success')
        return redirect(url_for('home'))
```

### 👤 用户认证系统

现在让我们实现一个完整的用户注册和登录系统：

```python
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

# 模拟用户数据库（实际项目中使用真实数据库）
users_db = {}

def login_required(f):
    """登录验证装饰器"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('请先登录', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/register', methods=['GET', 'POST'])
def register():
    """用户注册"""
    if request.method == 'GET':
        return render_template('auth/register.html')
    
    # 处理注册表单
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    
    # 验证输入
    errors = []
    if not username or len(username) < 3:
        errors.append('用户名至少需要3个字符')
    if not email or '@' not in email:
        errors.append('请输入有效的邮箱地址')
    if not password or len(password) < 6:
        errors.append('密码至少需要6个字符')
    if password != confirm_password:
        errors.append('两次输入的密码不一致')
    
    if errors:
        return render_template('auth/register.html', errors=errors, form_data=request.form)
    
    # 创建用户
    user_id = len(users_db) + 1
    users_db[username] = {
        'id': user_id,
        'username': username,
        'email': email,
        'password_hash': generate_password_hash(password),
        'created_at': datetime.now(),
        'last_login': None,
        'profile': {
            'full_name': '',
            'phone': '',
            'birthday': '',
            'favorite_drink': '',
            'dietary_restrictions': []
        },
        'order_history': [],
        'loyalty_points': 0
    }
    
    flash('注册成功！请登录', 'success')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """用户登录"""
    if request.method == 'GET':
        return render_template('auth/login.html')
    
    username = request.form.get('username')
    password = request.form.get('password')
    
    # 验证用户
    user = users_db.get(username)
    if user and check_password_hash(user['password_hash'], password):
        # 登录成功
        session['user_id'] = user['id']
        session['username'] = username
        
        flash(f'欢迎回来，{username}！', 'success')
        
        # 重定向到原来想访问的页面
        next_page = request.args.get('next')
        return redirect(next_page or url_for('home'))
    else:
        flash('用户名或密码错误', 'error')
        return render_template('auth/login.html', form_data=request.form)

@app.route('/logout')
def logout():
    """用户登出"""
    username = session.get('username', '访客')
    session.clear()
    flash(f'再见，{username}！', 'info')
    return redirect(url_for('home'))

@app.route('/profile')
@login_required
def profile():
    """用户个人资料"""
    username = session.get('username')
    user = users_db.get(username)
    
    if user:
        return render_template('auth/profile.html', user=user)
    else:
        flash('用户信息不存在', 'error')
        return redirect(url_for('logout'))

@app.route('/update_profile', methods=['POST'])
@login_required
def update_profile():
    """更新个人资料"""
    username = session.get('username')
    user = users_db.get(username)
    
    if user:
        # 更新邮箱
        new_email = request.form.get('email')
        if new_email and '@' in new_email:
            user['email'] = new_email
            flash('个人资料已更新', 'success')
        else:
            flash('请输入有效的邮箱地址', 'error')
    
    return redirect(url_for('profile'))
```

对应的认证模板：

```html
<!-- templates/auth/register.html - 注册页面 -->
{% extends "base.html" %}

{% block title %}用户注册 - 我的咖啡厅{% endblock %}

{% block content %}
<div style="max-width: 400px; margin: 0 auto;">
    <h1 style="text-align: center; color: #8b4513;">👤 用户注册</h1>
    
    {% if errors %}
    <div style="background-color: #ffe6e6; border: 1px solid #ff9999; padding: 1rem; border-radius: 5px; margin-bottom: 1rem;">
        <ul style="margin: 0; color: #cc0000;">
            {% for error in errors %}
            <li>{{ error }}</li>
            {% endfor %}
        </ul>
    </div>
    {% endif %}
    
    <form method="POST" style="background-color: white; padding: 2rem; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
        <div style="margin-bottom: 1rem;">
            <label style="display: block; font-weight: bold; margin-bottom: 0.5rem;">用户名:</label>
            <input type="text" name="username" 
                   value="{{ form_data.username if form_data else '' }}"
                   style="width: 100%; padding: 0.8rem; border: 1px solid #ddd; border-radius: 5px;"
                   placeholder="请输入用户名" required>
        </div>
        
        <div style="margin-bottom: 1rem;">
            <label style="display: block; font-weight: bold; margin-bottom: 0.5rem;">邮箱:</label>
            <input type="email" name="email" 
                   value="{{ form_data.email if form_data else '' }}"
                   style="width: 100%; padding: 0.8rem; border: 1px solid #ddd; border-radius: 5px;"
                   placeholder="请输入邮箱地址" required>
        </div>
        
        <div style="margin-bottom: 1rem;">
            <label style="display: block; font-weight: bold; margin-bottom: 0.5rem;">密码:</label>
            <input type="password" name="password" 
                   style="width: 100%; padding: 0.8rem; border: 1px solid #ddd; border-radius: 5px;"
                   placeholder="请输入密码" required>
        </div>
        
        <div style="margin-bottom: 1.5rem;">
            <label style="display: block; font-weight: bold; margin-bottom: 0.5rem;">确认密码:</label>
            <input type="password" name="confirm_password" 
                   style="width: 100%; padding: 0.8rem; border: 1px solid #ddd; border-radius: 5px;"
                   placeholder="请再次输入密码" required>
        </div>
        
        <button type="submit" style="width: 100%; background-color: #8b4513; color: white; border: none; padding: 1rem; border-radius: 5px; font-size: 1.1rem; cursor: pointer;">
            📝 注册账户
        </button>
    </form>
    
    <div style="text-align: center; margin-top: 1rem;">
        <p>已有账户？<a href="/login" style="color: #8b4513;">立即登录</a></p>
        <a href="/" style="color: #8b4513; text-decoration: none;">← 返回首页</a>
    </div>
</div>
{% endblock %}
```

### 🚀 实战项目：用户管理系统

让我们整合所有学到的知识，创建一个完整的用户管理系统：

```python
# user_management_app.py - 完整的用户管理系统
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from datetime import datetime
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-user-management-secret-key'

# 模拟数据存储
users_db = {}
user_sessions = {}

class UserManager:
    """用户管理类 - 咖啡厅会员管理系统"""
    
    @staticmethod
    def create_user(username, email, password):
        """创建新用户"""
        if username in users_db:
            return False, "用户名已存在"
        
        user_id = len(users_db) + 1
        users_db[username] = {
            'id': user_id,
            'username': username,
            'email': email,
            'password_hash': generate_password_hash(password),
            'created_at': datetime.now(),
            'last_login': None,
            'profile': {
                'full_name': '',
                'phone': '',
                'birthday': '',
                'favorite_drink': '',
                'dietary_restrictions': []
            },
            'order_history': [],
            'loyalty_points': 0
        }
        return True, "用户创建成功"
    
    @staticmethod
    def authenticate_user(username, password):
        """验证用户"""
        user = users_db.get(username)
        if user and check_password_hash(user['password_hash'], password):
            user['last_login'] = datetime.now()
            return True, user
        return False, None
    
    @staticmethod
    def get_user(username):
        """获取用户信息"""
        return users_db.get(username)
    
    @staticmethod
    def update_profile(username, profile_data):
        """更新用户资料"""
        user = users_db.get(username)
        if user:
            user['profile'].update(profile_data)
            return True
        return False

def login_required(f):
    """登录验证装饰器"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('请先登录访问此页面', 'warning')
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    """首页"""
    user = None
    if 'username' in session:
        user = UserManager.get_user(session['username'])
    
    return render_template('user_system/home.html', user=user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """用户注册"""
    if request.method == 'GET':
        return render_template('user_system/register.html')
    
    # 获取表单数据
    username = request.form.get('username', '').strip()
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '')
    confirm_password = request.form.get('confirm_password', '')
    
    # 验证输入
    errors = []
    if not username or len(username) < 3:
        errors.append('用户名至少需要3个字符')
    if not email or '@' not in email:
        errors.append('请输入有效的邮箱地址')
    if not password or len(password) < 6:
        errors.append('密码至少需要6个字符')
    
    if errors:
        return render_template('user_system/register.html', errors=errors, form_data=request.form)
    
    # 创建用户
    success, message = UserManager.create_user(username, email, password)
    if success:
        flash('注册成功！请登录您的账户', 'success')
        return redirect(url_for('login'))
    else:
        return render_template('user_system/register.html', errors=[message], form_data=request.form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """用户登录"""
    if request.method == 'GET':
        return render_template('user_system/login.html')
    
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '')
    
    success, user = UserManager.authenticate_user(username, password)
    if success:
        session['user_id'] = user['id']
        session['username'] = username
        
        flash(f'欢迎回来，{username}！', 'success')
        
        # 重定向到原来想访问的页面
        next_page = request.args.get('next')
        return redirect(next_page or url_for('dashboard'))
    else:
        flash('用户名或密码错误', 'error')
        return render_template('user_system/login.html', form_data=request.form)

@app.route('/logout')
def logout():
    """用户登出"""
    username = session.get('username', '访客')
    session.clear()
    flash(f'再见，{username}！期待您的下次光临', 'info')
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    """用户仪表板"""
    username = session.get('username')
    user = UserManager.get_user(username)
    
    # 统计信息
    stats = {
        'total_orders': len(user['order_history']),
        'loyalty_points': user['loyalty_points'],
        'member_since': user['created_at'].strftime('%Y年%m月'),
        'last_login': user['last_login'].strftime('%Y-%m-%d %H:%M') if user['last_login'] else '首次登录'
    }
    
    return render_template('user_system/dashboard.html', user=user, stats=stats)

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    """个人资料管理"""
    username = session.get('username')
    user = UserManager.get_user(username)
    
    if request.method == 'GET':
        return render_template('user_system/profile.html', user=user)
    
    # 更新资料
    profile_data = {
        'full_name': request.form.get('full_name', ''),
        'phone': request.form.get('phone', ''),
        'birthday': request.form.get('birthday', ''),
        'favorite_drink': request.form.get('favorite_drink', ''),
        'dietary_restrictions': request.form.getlist('dietary_restrictions')
    }
    
    if UserManager.update_profile(username, profile_data):
        flash('个人资料已成功更新', 'success')
    else:
        flash('更新失败，请重试', 'error')
    
    return redirect(url_for('profile'))

if __name__ == '__main__':
    # 创建一些测试用户
    UserManager.create_user('admin', 'admin@coffee.com', 'admin123')
    UserManager.create_user('demo', 'demo@coffee.com', 'demo123')
    
    app.run(debug=True)
```

### 📝 本节小结

通过"顾客点餐服务"这一节，我们深入学习了：

1. **HTTP请求处理**：掌握了GET/POST请求的区别和处理方法
2. **表单数据处理**：学会了表单验证、错误处理和数据回填
3. **会话管理**：理解了Session的工作原理和应用场景
4. **用户认证系统**：实现了完整的注册、登录、登出功能
5. **购物车功能**：掌握了复杂状态管理的实现方法

**核心要点回顾**：
- 🛎️ HTTP请求处理要区分不同的请求方法和数据来源
- 📝 表单验证是确保数据质量的重要环节
- 🎫 Session让Web应用能够记住用户状态
- 👤 用户认证是Web应用安全的基础
- 🛒 购物车等功能展示了会话管理的实际应用

**下一节预告**：在16.3节"厨房管理系统"中，我们将学习数据库集成，使用Flask-SQLAlchemy进行数据建模和持久化存储，让我们的咖啡厅拥有真正的"记忆"！ 

---

## 16.3 数据库集成 - "厨房管理系统" 🗄️

> 一家好的咖啡厅需要井井有条的厨房管理——知道有什么原料，存放在哪里，什么时候用完需要补货。

### 🎯 本节目标
- 掌握Flask-SQLAlchemy的配置和使用
- 学会设计数据模型和关系映射
- 理解数据库迁移和版本管理
- 实现完整的CRUD操作

### 📚 理论基础：为什么需要数据库？

在前面的学习中，我们使用内存字典来存储数据，但这有明显的局限性：

```python
# 内存存储的问题
users_db = {}  # 重启应用后数据丢失
shopping_cart = {}  # 无法处理并发访问
menu_items = []  # 数据结构简单，难以建立关系

# 数据库存储的优势
"""
🔒 数据持久化：应用重启后数据不丢失
🔄 并发安全：多用户同时访问不会冲突
🔍 高效查询：支持复杂的查询和索引
📊 数据关系：支持表之间的关联关系
🛡️ 事务支持：保证数据操作的一致性
📈 扩展性：支持大量数据的存储和查询
"""
```

### 🏗️ Flask-SQLAlchemy配置

#### 1. 安装和基本配置

```python
# config.py - 咖啡厅的经营配置
import os
from datetime import timedelta

class Config:
    """咖啡厅基础配置"""
    # 安全密钥（店铺保险箱密码）
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'coffee-shop-secret-key-2024'
    
    # 数据库配置（厨房仓库位置）
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///coffee_shop.db'  # SQLite数据库文件
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 关闭修改跟踪（节省资源）
    
    # 会话配置（客户记忆时间）
    PERMANENT_SESSION_LIFETIME = timedelta(hours=2)  # 会话2小时过期
    
    # 分页配置（菜单每页显示数量）
    POSTS_PER_PAGE = 10
    
    # 上传文件配置（店铺装饰图片）
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB最大文件大小
    UPLOAD_FOLDER = 'static/uploads'

class DevelopmentConfig(Config):
    """开发环境配置（试营业阶段）"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///coffee_shop_dev.db'

class ProductionConfig(Config):
    """生产环境配置（正式营业阶段）"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///coffee_shop_prod.db'

# 配置字典（不同经营模式）
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
```

#### 2. 应用初始化

```python
# app.py - 咖啡厅主应用
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

# 创建扩展实例（准备厨房设备）
db = SQLAlchemy()  # 数据库管理器（智能仓库系统）
migrate = Migrate()  # 数据库迁移工具（仓库改造工具）

def create_app(config_name='default'):
    """应用工厂函数 - 咖啡厅建设蓝图"""
    app = Flask(__name__)
    
    # 加载配置（按照经营方针设置）
    app.config.from_object(config[config_name])
    
    # 初始化扩展（安装厨房设备）
    db.init_app(app)
    migrate.init_app(app, db)
    
    # 注册蓝图（组织各个部门）
    from routes import main_bp
    app.register_blueprint(main_bp)
    
    return app

# 创建应用实例
app = create_app()
```

### 🗃️ 数据模型设计：咖啡厅的"仓库清单"

让我们设计一个完整的咖啡厅数据模型：

```python
# models.py - 咖啡厅数据模型
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    """用户模型 - 咖啡厅会员档案"""
    __tablename__ = 'users'
    
    # 基本信息（会员基础档案）
    id = db.Column(db.Integer, primary_key=True, comment='用户ID')
    username = db.Column(db.String(80), unique=True, nullable=False, comment='用户名')
    email = db.Column(db.String(120), unique=True, nullable=False, comment='邮箱')
    password_hash = db.Column(db.String(255), nullable=False, comment='密码哈希')
    
    # 个人资料（详细会员信息）
    full_name = db.Column(db.String(100), comment='真实姓名')
    phone = db.Column(db.String(20), comment='电话号码')
    birthday = db.Column(db.Date, comment='生日')
    avatar = db.Column(db.String(200), comment='头像URL')
    
    # 偏好设置（个性化服务记录）
    favorite_drink = db.Column(db.String(50), comment='最爱饮品')
    dietary_restrictions = db.Column(db.Text, comment='饮食限制（JSON格式）')
    
    # 系统信息（管理数据）
    created_at = db.Column(db.DateTime, default=datetime.utcnow, comment='注册时间')
    last_login = db.Column(db.DateTime, comment='最后登录时间')
    is_active = db.Column(db.Boolean, default=True, comment='账户状态')
    loyalty_points = db.Column(db.Integer, default=0, comment='积分余额')
    
    # 关系映射（会员关联的订单）
    orders = db.relationship('Order', backref='customer', lazy='dynamic', 
                           cascade='all, delete-orphan')
    
    def set_password(self, password):
        """设置密码（加密存储）"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """验证密码"""
        return check_password_hash(self.password_hash, password)
    
    def add_points(self, points):
        """增加积分（消费奖励）"""
        self.loyalty_points += points
        db.session.commit()
    
    def use_points(self, points):
        """使用积分（积分兑换）"""
        if self.loyalty_points >= points:
            self.loyalty_points -= points
            db.session.commit()
            return True
        return False
    
    def __repr__(self):
        return f'<User {self.username}>'

class Category(db.Model):
    """商品分类模型 - 菜单分类"""
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True, comment='分类ID')
    name = db.Column(db.String(50), unique=True, nullable=False, comment='分类名称')
    description = db.Column(db.Text, comment='分类描述')
    icon = db.Column(db.String(50), comment='分类图标')
    sort_order = db.Column(db.Integer, default=0, comment='排序顺序')
    is_active = db.Column(db.Boolean, default=True, comment='是否启用')
    
    # 关系映射（分类下的商品）
    products = db.relationship('Product', backref='category', lazy='dynamic')
    
    def __repr__(self):
        return f'<Category {self.name}>'

class Product(db.Model):
    """商品模型 - 咖啡厅菜单项目"""
    __tablename__ = 'products'
    
    # 基本信息
    id = db.Column(db.Integer, primary_key=True, comment='商品ID')
    name = db.Column(db.String(100), nullable=False, comment='商品名称')
    description = db.Column(db.Text, comment='商品描述')
    price = db.Column(db.Numeric(8, 2), nullable=False, comment='价格')
    cost = db.Column(db.Numeric(8, 2), comment='成本价')
    
    # 商品属性
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), 
                          nullable=False, comment='分类ID')
    image_url = db.Column(db.String(200), comment='商品图片')
    preparation_time = db.Column(db.Integer, default=5, comment='制作时间（分钟）')
    calories = db.Column(db.Integer, comment='卡路里')
    
    # 库存管理
    stock_quantity = db.Column(db.Integer, default=0, comment='库存数量')
    min_stock_level = db.Column(db.Integer, default=10, comment='最低库存警戒线')
    
    # 状态管理
    is_available = db.Column(db.Boolean, default=True, comment='是否可售')
    is_featured = db.Column(db.Boolean, default=False, comment='是否推荐')
    created_at = db.Column(db.DateTime, default=datetime.utcnow, comment='创建时间')
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, 
                          onupdate=datetime.utcnow, comment='更新时间')
    
    # 关系映射
    order_items = db.relationship('OrderItem', backref='product', lazy='dynamic')
    
    @property
    def is_low_stock(self):
        """检查是否库存不足"""
        return self.stock_quantity <= self.min_stock_level
    
    def update_stock(self, quantity_sold):
        """更新库存（销售后减少）"""
        self.stock_quantity -= quantity_sold
        if self.stock_quantity < 0:
            self.stock_quantity = 0
        db.session.commit()
    
    def restock(self, quantity):
        """补充库存"""
        self.stock_quantity += quantity
        db.session.commit()
    
    def __repr__(self):
        return f'<Product {self.name}>'

class Order(db.Model):
    """订单模型 - 客户订单记录"""
    __tablename__ = 'orders'
    
    # 订单基本信息
    id = db.Column(db.Integer, primary_key=True, comment='订单ID')
    order_number = db.Column(db.String(20), unique=True, nullable=False, comment='订单号')
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'), 
                          nullable=False, comment='客户ID')
    
    # 订单状态
    status = db.Column(db.String(20), default='pending', comment='订单状态')
    # pending: 待处理, confirmed: 已确认, preparing: 制作中, 
    # ready: 待取餐, completed: 已完成, cancelled: 已取消
    
    # 金额信息
    subtotal = db.Column(db.Numeric(8, 2), nullable=False, comment='小计')
    tax_amount = db.Column(db.Numeric(8, 2), default=0, comment='税费')
    discount_amount = db.Column(db.Numeric(8, 2), default=0, comment='折扣金额')
    total_amount = db.Column(db.Numeric(8, 2), nullable=False, comment='总金额')
    points_used = db.Column(db.Integer, default=0, comment='使用积分')
    points_earned = db.Column(db.Integer, default=0, comment='获得积分')
    
    # 时间信息
    created_at = db.Column(db.DateTime, default=datetime.utcnow, comment='下单时间')
    confirmed_at = db.Column(db.DateTime, comment='确认时间')
    completed_at = db.Column(db.DateTime, comment='完成时间')
    estimated_ready_time = db.Column(db.DateTime, comment='预计完成时间')
    
    # 订单备注
    notes = db.Column(db.Text, comment='订单备注')
    
    # 关系映射
    items = db.relationship('OrderItem', backref='order', lazy='dynamic',
                          cascade='all, delete-orphan')
    
    def generate_order_number(self):
        """生成订单号"""
        from datetime import datetime
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        self.order_number = f'CF{timestamp}{self.id:04d}'
    
    def calculate_total(self):
        """计算订单总金额"""
        self.subtotal = sum(item.subtotal for item in self.items)
        self.tax_amount = self.subtotal * 0.1  # 10%税率
        self.total_amount = self.subtotal + self.tax_amount - self.discount_amount
        
        # 计算积分奖励（每消费1元获得1积分）
        self.points_earned = int(self.total_amount)
    
    def apply_discount(self, discount_percent):
        """应用折扣"""
        self.discount_amount = self.subtotal * (discount_percent / 100)
        self.calculate_total()
    
    def __repr__(self):
        return f'<Order {self.order_number}>'

class OrderItem(db.Model):
    """订单项目模型 - 订单中的具体商品"""
    __tablename__ = 'order_items'
    
    id = db.Column(db.Integer, primary_key=True, comment='订单项ID')
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), 
                        nullable=False, comment='订单ID')
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), 
                          nullable=False, comment='商品ID')
    
    # 商品信息（下单时的快照）
    product_name = db.Column(db.String(100), nullable=False, comment='商品名称')
    unit_price = db.Column(db.Numeric(8, 2), nullable=False, comment='单价')
    quantity = db.Column(db.Integer, nullable=False, comment='数量')
    subtotal = db.Column(db.Numeric(8, 2), nullable=False, comment='小计')
    
    # 定制选项
    customizations = db.Column(db.Text, comment='定制选项（JSON格式）')
    special_instructions = db.Column(db.Text, comment='特殊要求')
    
    def calculate_subtotal(self):
        """计算小计"""
        self.subtotal = self.unit_price * self.quantity
    
    def __repr__(self):
        return f'<OrderItem {self.product_name} x{self.quantity}>'
```

### 🔧 数据库操作：厨房管理实战

#### 1. 数据库初始化和迁移

```python
# manage.py - 数据库管理脚本
from flask import Flask
from flask_migrate import Migrate, init, migrate, upgrade
from app import create_app
from models import db, User, Category, Product, Order, OrderItem

app = create_app()
migrate = Migrate(app, db)

@app.cli.command()
def init_db():
    """初始化数据库（建设厨房仓库）"""
    db.create_all()
    print("✅ 数据库初始化完成！")

@app.cli.command()
def seed_db():
    """填充测试数据（准备基础原料）"""
    # 创建分类
    categories_data = [
        {'name': '咖啡类', 'description': '各种精品咖啡', 'icon': '☕'},
        {'name': '茶饮类', 'description': '传统茶饮和花茶', 'icon': '🍵'},
        {'name': '甜品类', 'description': '精美甜点和蛋糕', 'icon': '🍰'},
        {'name': '轻食类', 'description': '三明治和沙拉', 'icon': '🥪'},
    ]
    
    for cat_data in categories_data:
        category = Category(**cat_data)
        db.session.add(category)
    
    db.session.commit()
    
    # 创建商品
    products_data = [
        # 咖啡类
        {'name': '美式咖啡', 'description': '经典黑咖啡，香浓醇厚', 'price': 25.00, 'category_id': 1, 'stock_quantity': 100},
        {'name': '拿铁咖啡', 'description': '咖啡与牛奶的完美融合', 'price': 30.00, 'category_id': 1, 'stock_quantity': 100},
        {'name': '卡布奇诺', 'description': '浓郁咖啡配奶泡', 'price': 28.00, 'category_id': 1, 'stock_quantity': 100},
        
        # 茶饮类
        {'name': '柠檬蜂蜜茶', 'description': '清香柠檬配天然蜂蜜', 'price': 22.00, 'category_id': 2, 'stock_quantity': 80},
        {'name': '茉莉花茶', 'description': '传统茉莉花茶，清香淡雅', 'price': 20.00, 'category_id': 2, 'stock_quantity': 80},
        
        # 甜品类
        {'name': '提拉米苏', 'description': '意式经典甜品', 'price': 35.00, 'category_id': 3, 'stock_quantity': 20},
        {'name': '芝士蛋糕', 'description': '浓郁芝士香味', 'price': 32.00, 'category_id': 3, 'stock_quantity': 20},
        
        # 轻食类
        {'name': '火腿三明治', 'description': '新鲜火腿配蔬菜', 'price': 18.00, 'category_id': 4, 'stock_quantity': 50},
        {'name': '凯撒沙拉', 'description': '经典凯撒沙拉', 'price': 25.00, 'category_id': 4, 'stock_quantity': 30},
    ]
    
    for prod_data in products_data:
        product = Product(**prod_data)
        db.session.add(product)
    
    # 创建管理员用户
    admin = User(
        username='admin',
        email='admin@coffee.com',
        full_name='咖啡厅管理员',
        is_active=True
    )
    admin.set_password('admin123')
    db.session.add(admin)
    
    # 创建测试用户
    demo_user = User(
        username='demo',
        email='demo@coffee.com',
        full_name='演示用户',
        favorite_drink='拿铁咖啡',
        loyalty_points=100
    )
    demo_user.set_password('demo123')
    db.session.add(demo_user)
    
    db.session.commit()
    print("✅ 测试数据填充完成！")

if __name__ == '__main__':
    app.run()
```

#### 2. 数据操作服务类

```python
# services.py - 业务逻辑服务
from models import db, User, Category, Product, Order, OrderItem
from datetime import datetime, timedelta
from sqlalchemy import func

class ProductService:
    """商品管理服务 - 菜单管理员"""
    
    @staticmethod
    def get_all_products(category_id=None, available_only=True):
        """获取所有商品（按分类筛选）"""
        query = Product.query
        
        if category_id:
            query = query.filter_by(category_id=category_id)
        
        if available_only:
            query = query.filter_by(is_available=True)
        
        return query.order_by(Product.name).all()
    
    @staticmethod
    def get_featured_products():
        """获取推荐商品"""
        return Product.query.filter_by(is_featured=True, is_available=True).all()
    
    @staticmethod
    def get_low_stock_products():
        """获取库存不足的商品"""
        return Product.query.filter(
            Product.stock_quantity <= Product.min_stock_level
        ).all()
    
    @staticmethod
    def search_products(keyword):
        """搜索商品"""
        return Product.query.filter(
            Product.name.contains(keyword) | 
            Product.description.contains(keyword)
        ).filter_by(is_available=True).all()
    
    @staticmethod
    def update_product_stock(product_id, new_quantity):
        """更新商品库存"""
        product = Product.query.get(product_id)
        if product:
            product.stock_quantity = new_quantity
            db.session.commit()
            return True
        return False

class OrderService:
    """订单管理服务 - 订单处理员"""
    
    @staticmethod
    def create_order(customer_id, items_data, notes=None):
        """创建新订单"""
        try:
            # 创建订单
            order = Order(
                customer_id=customer_id,
                status='pending',
                notes=notes,
                subtotal=0,
                total_amount=0
            )
            db.session.add(order)
            db.session.flush()  # 获取订单ID
            
            # 生成订单号
            order.generate_order_number()
            
            # 添加订单项目
            for item_data in items_data:
                product = Product.query.get(item_data['product_id'])
                if not product or not product.is_available:
                    raise ValueError(f"商品 {product.name if product else '未知'} 不可用")
                
                if product.stock_quantity < item_data['quantity']:
                    raise ValueError(f"商品 {product.name} 库存不足")
                
                order_item = OrderItem(
                    order_id=order.id,
                    product_id=product.id,
                    product_name=product.name,
                    unit_price=product.price,
                    quantity=item_data['quantity'],
                    customizations=item_data.get('customizations'),
                    special_instructions=item_data.get('special_instructions')
                )
                order_item.calculate_subtotal()
                db.session.add(order_item)
                
                # 减少库存
                product.update_stock(item_data['quantity'])
            
            # 计算订单总金额
            order.calculate_total()
            
            # 设置预计完成时间
            total_prep_time = sum(
                item.product.preparation_time * item.quantity 
                for item in order.items
            )
            order.estimated_ready_time = datetime.utcnow() + timedelta(minutes=total_prep_time)
            
            db.session.commit()
            return order
            
        except Exception as e:
            db.session.rollback()
            raise e
    
    @staticmethod
    def get_user_orders(user_id, limit=10):
        """获取用户订单历史"""
        return Order.query.filter_by(customer_id=user_id)\
                         .order_by(Order.created_at.desc())\
                         .limit(limit).all()
    
    @staticmethod
    def update_order_status(order_id, new_status):
        """更新订单状态"""
        order = Order.query.get(order_id)
        if order:
            order.status = new_status
            
            if new_status == 'confirmed':
                order.confirmed_at = datetime.utcnow()
            elif new_status == 'completed':
                order.completed_at = datetime.utcnow()
                # 给用户增加积分
                user = order.customer
                user.add_points(order.points_earned)
            
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def get_daily_sales_report(date=None):
        """获取日销售报告"""
        if not date:
            date = datetime.utcnow().date()
        
        # 当日订单统计
        orders = Order.query.filter(
            func.date(Order.created_at) == date,
            Order.status != 'cancelled'
        ).all()
        
        total_orders = len(orders)
        total_revenue = sum(order.total_amount for order in orders)
        
        # 热销商品统计
        popular_products = db.session.query(
            OrderItem.product_name,
            func.sum(OrderItem.quantity).label('total_sold'),
            func.sum(OrderItem.subtotal).label('total_revenue')
        ).join(Order).filter(
            func.date(Order.created_at) == date,
            Order.status != 'cancelled'
        ).group_by(OrderItem.product_name)\
         .order_by(func.sum(OrderItem.quantity).desc())\
         .limit(5).all()
        
        return {
            'date': date,
            'total_orders': total_orders,
            'total_revenue': float(total_revenue) if total_revenue else 0,
            'popular_products': [
                {
                    'name': item[0],
                    'quantity_sold': item[1],
                    'revenue': float(item[2])
                }
                for item in popular_products
            ]
        }

class UserService:
    """用户管理服务 - 会员管理员"""
    
    @staticmethod
    def get_user_profile(user_id):
        """获取用户完整资料"""
        user = User.query.get(user_id)
        if user:
            # 计算用户统计信息
            total_orders = Order.query.filter_by(customer_id=user_id).count()
            total_spent = db.session.query(func.sum(Order.total_amount))\
                                   .filter_by(customer_id=user_id)\
                                   .scalar() or 0
            
            return {
                'user': user,
                'stats': {
                    'total_orders': total_orders,
                    'total_spent': float(total_spent),
                    'loyalty_points': user.loyalty_points,
                    'member_since': user.created_at.strftime('%Y年%m月')
                }
            }
        return None
    
    @staticmethod
    def update_user_preferences(user_id, preferences):
        """更新用户偏好设置"""
        user = User.query.get(user_id)
        if user:
            user.favorite_drink = preferences.get('favorite_drink', user.favorite_drink)
            user.dietary_restrictions = preferences.get('dietary_restrictions', user.dietary_restrictions)
            db.session.commit()
            return True
        return False
```

### 📱 实战项目：任务管理系统

让我们创建一个完整的咖啡厅管理系统：

```python
# routes.py - 路由处理
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask import session
from models import db, User, Category, Product, Order
from services import ProductService, OrderService, UserService
from datetime import datetime

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """首页 - 咖啡厅欢迎页"""
    featured_products = ProductService.get_featured_products()
    categories = Category.query.filter_by(is_active=True).all()
    
    return render_template('index.html', 
                         featured_products=featured_products,
                         categories=categories)

@main_bp.route('/menu')
@main_bp.route('/menu/<int:category_id>')
def menu(category_id=None):
    """菜单页面"""
    categories = Category.query.filter_by(is_active=True).all()
    products = ProductService.get_all_products(category_id=category_id)
    
    current_category = None
    if category_id:
        current_category = Category.query.get(category_id)
    
    return render_template('menu.html',
                         products=products,
                         categories=categories,
                         current_category=current_category)

@main_bp.route('/product/<int:product_id>')
def product_detail(product_id):
    """商品详情页"""
    product = Product.query.get_or_404(product_id)
    related_products = ProductService.get_all_products(
        category_id=product.category_id
    )[:4]  # 推荐4个相关商品
    
    return render_template('product_detail.html',
                         product=product,
                         related_products=related_products)

@main_bp.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    """添加到购物车"""
    if 'cart' not in session:
        session['cart'] = []
    
    product_id = int(request.form.get('product_id'))
    quantity = int(request.form.get('quantity', 1))
    
    product = Product.query.get(product_id)
    if not product or not product.is_available:
        flash('商品不可用', 'error')
        return redirect(url_for('main.menu'))
    
    if product.stock_quantity < quantity:
        flash('库存不足', 'error')
        return redirect(url_for('main.product_detail', product_id=product_id))
    
    # 检查购物车中是否已有该商品
    cart_item = None
    for item in session['cart']:
        if item['product_id'] == product_id:
            cart_item = item
            break
    
    if cart_item:
        cart_item['quantity'] += quantity
    else:
        session['cart'].append({
            'product_id': product_id,
            'product_name': product.name,
            'unit_price': float(product.price),
            'quantity': quantity,
            'subtotal': float(product.price * quantity)
        })
    
    session.modified = True
    flash(f'{product.name} 已添加到购物车', 'success')
    return redirect(url_for('main.menu'))

@main_bp.route('/cart')
def view_cart():
    """查看购物车"""
    cart = session.get('cart', [])
    
    # 重新计算小计（防止价格变动）
    for item in cart:
        product = Product.query.get(item['product_id'])
        if product:
            item['unit_price'] = float(product.price)
            item['subtotal'] = item['unit_price'] * item['quantity']
    
    total = sum(item['subtotal'] for item in cart)
    
    return render_template('cart.html', cart=cart, total=total)

@main_bp.route('/checkout', methods=['GET', 'POST'])
def checkout():
    """结账"""
    if 'user_id' not in session:
        flash('请先登录', 'warning')
        return redirect(url_for('auth.login'))
    
    cart = session.get('cart', [])
    if not cart:
        flash('购物车为空', 'warning')
        return redirect(url_for('main.menu'))
    
    if request.method == 'GET':
        total = sum(item['subtotal'] for item in cart)
        return render_template('checkout.html', cart=cart, total=total)
    
    # 处理订单提交
    try:
        items_data = [
            {
                'product_id': item['product_id'],
                'quantity': item['quantity'],
                'special_instructions': request.form.get(f'instructions_{item["product_id"]}', '')
            }
            for item in cart
        ]
        
        order = OrderService.create_order(
            customer_id=session['user_id'],
            items_data=items_data,
            notes=request.form.get('order_notes', '')
        )
        
        # 清空购物车
        session.pop('cart', None)
        
        flash(f'订单 {order.order_number} 创建成功！', 'success')
        return redirect(url_for('main.order_detail', order_id=order.id))
        
    except Exception as e:
        flash(f'订单创建失败：{str(e)}', 'error')
        return redirect(url_for('main.checkout'))

@main_bp.route('/orders')
def my_orders():
    """我的订单"""
    if 'user_id' not in session:
        flash('请先登录', 'warning')
        return redirect(url_for('auth.login'))
    
    orders = OrderService.get_user_orders(session['user_id'])
    return render_template('my_orders.html', orders=orders)

@main_bp.route('/order/<int:order_id>')
def order_detail(order_id):
    """订单详情"""
    order = Order.query.get_or_404(order_id)
    
    # 检查权限（只能查看自己的订单）
    if 'user_id' not in session or order.customer_id != session['user_id']:
        flash('无权访问此订单', 'error')
        return redirect(url_for('main.index'))
    
    return render_template('order_detail.html', order=order)

@main_bp.route('/admin/dashboard')
def admin_dashboard():
    """管理员仪表板"""
    # 简单的权限检查（实际项目中应该更完善）
    if 'user_id' not in session:
        flash('请先登录', 'warning')
        return redirect(url_for('auth.login'))
    
    # 获取今日销售报告
    today_report = OrderService.get_daily_sales_report()
    
    # 获取库存不足的商品
    low_stock_products = ProductService.get_low_stock_products()
    
    # 获取待处理订单
    pending_orders = Order.query.filter_by(status='pending').count()
    
    return render_template('admin/dashboard.html',
                         today_report=today_report,
                         low_stock_products=low_stock_products,
                         pending_orders=pending_orders)

@main_bp.route('/admin/products')
def admin_products():
    """商品管理"""
    products = Product.query.all()
    categories = Category.query.all()
    
    return render_template('admin/products.html',
                         products=products,
                         categories=categories)

@main_bp.route('/admin/orders')
def admin_orders():
    """订单管理"""
    status = request.args.get('status', 'all')
    
    query = Order.query
    if status != 'all':
        query = query.filter_by(status=status)
    
    orders = query.order_by(Order.created_at.desc()).all()
    
    return render_template('admin/orders.html',
                         orders=orders,
                         current_status=status)

@main_bp.route('/api/update_order_status', methods=['POST'])
def update_order_status():
    """更新订单状态 API"""
    order_id = request.json.get('order_id')
    new_status = request.json.get('status')
    
    if OrderService.update_order_status(order_id, new_status):
        return jsonify({'success': True, 'message': '状态更新成功'})
    else:
        return jsonify({'success': False, 'message': '更新失败'}), 400
```

### 📝 本节小结

通过"厨房管理系统"这一节，我们深入学习了：

1. **Flask-SQLAlchemy配置**：掌握了数据库连接和配置管理
2. **数据模型设计**：学会了设计复杂的关系型数据模型
3. **数据库迁移**：理解了数据库版本管理的重要性
4. **业务逻辑分层**：实现了Service层来处理复杂的业务逻辑
5. **CRUD操作**：掌握了完整的数据库增删改查操作

**核心要点回顾**：
- 🗄️ 数据库让Web应用拥有了"记忆"能力
- 🔗 关系映射让不同数据表之间建立了有意义的联系
- 🛠️ Service层让业务逻辑更加清晰和可维护
- 📊 数据模型设计要考虑实际业务需求和扩展性
- 🔄 数据库迁移是生产环境中不可缺少的工具

**下一节预告**：在16.4节"外卖服务"中，我们将学习API开发和部署，构建RESTful API接口，实现前后端分离架构！

---

## 16.4 API开发与部署 - "外卖服务" 🚚

> 现代咖啡厅不仅要有舒适的堂食环境，还要提供便捷的外卖服务。API就是我们的"外卖平台"，让其他应用也能享受我们的服务。

### 🎯 本节目标
- 理解RESTful API设计原则
- 学会构建JSON API接口
- 掌握API文档和测试方法
- 了解Web应用部署流程

### 📚 理论基础：什么是API？

**API（Application Programming Interface）** 就像咖啡厅的外卖服务：

```python
# API的比喻理解
"""
🏪 传统服务 = 堂食
   - 客人来店里，面对面点餐
   - 直接在店内享用食物
   - 服务员直接沟通

🚚 API服务 = 外卖
   - 通过电话/App远程点餐
   - 食物打包配送到指定地点
   - 标准化的订单格式和流程
"""
```

#### RESTful API设计原则

```python
# REST (Representational State Transfer) 设计原则
"""
📋 资源导向 (Resource-Oriented)
   - 每个URL代表一种资源
   - GET /api/products - 获取商品列表
   - GET /api/products/1 - 获取特定商品

🔧 HTTP方法语义化
   - GET: 获取资源（查看菜单）
   - POST: 创建资源（下新订单）
   - PUT: 更新资源（修改订单）
   - DELETE: 删除资源（取消订单）

📦 统一的数据格式
   - 请求和响应都使用JSON格式
   - 标准化的错误码和消息

🔄 无状态设计
   - 每个请求都包含完整信息
   - 服务器不保存客户端状态
"""
```

### 🛠️ API开发实战

#### 1. API蓝图设计

```python
# api.py - API路由蓝图
from flask import Blueprint, request, jsonify, session
from flask_restful import Api, Resource
from models import db, Product, Category, Order, User
from services import ProductService, OrderService, UserService
from functools import wraps
import jwt
from datetime import datetime, timedelta

# 创建API蓝图（外卖服务部门）
api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

def token_required(f):
    """API认证装饰器（外卖身份验证）"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': '缺少认证令牌', 'code': 401}), 401
        
        try:
            # 移除 "Bearer " 前缀
            if token.startswith('Bearer '):
                token = token[7:]
            
            # 解码JWT令牌
            data = jwt.decode(token, 'your-secret-key', algorithms=['HS256'])
            current_user_id = data['user_id']
            
        except jwt.ExpiredSignatureError:
            return jsonify({'error': '令牌已过期', 'code': 401}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': '无效令牌', 'code': 401}), 401
        
        return f(current_user_id, *args, **kwargs)
    return decorated

# 标准API响应格式
def api_response(data=None, message='操作成功', code=200, success=True):
    """标准化API响应格式"""
    response = {
        'success': success,
        'code': code,
        'message': message,
        'timestamp': datetime.utcnow().isoformat(),
        'data': data
    }
    return jsonify(response), code

def api_error(message='操作失败', code=400, details=None):
    """标准化API错误响应"""
    response = {
        'success': False,
        'code': code,
        'message': message,
        'timestamp': datetime.utcnow().isoformat(),
        'details': details
    }
    return jsonify(response), code

@api_bp.route('/auth/login', methods=['POST'])
def api_login():
    """API登录（获取外卖服务授权）"""
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return api_error('用户名和密码不能为空', 400)
        
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            # 生成JWT令牌
            token_payload = {
                'user_id': user.id,
                'username': user.username,
                'exp': datetime.utcnow() + timedelta(hours=24)  # 24小时过期
            }
            token = jwt.encode(token_payload, 'your-secret-key', algorithm='HS256')
            
            # 更新最后登录时间
            user.last_login = datetime.utcnow()
            db.session.commit()
            
            return api_response({
                'token': token,
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'full_name': user.full_name,
                    'loyalty_points': user.loyalty_points
                }
            }, '登录成功')
        else:
            return api_error('用户名或密码错误', 401)
            
    except Exception as e:
        return api_error(f'登录失败: {str(e)}', 500)

@api_bp.route('/products', methods=['GET'])
def get_products():
    """获取商品列表（外卖菜单）"""
    try:
        # 获取查询参数
        category_id = request.args.get('category_id', type=int)
        featured_only = request.args.get('featured', 'false').lower() == 'true'
        search = request.args.get('search', '').strip()
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        
        # 构建查询
        query = Product.query.filter_by(is_available=True)
        
        if category_id:
            query = query.filter_by(category_id=category_id)
        
        if featured_only:
            query = query.filter_by(is_featured=True)
        
        if search:
            query = query.filter(
                Product.name.contains(search) | 
                Product.description.contains(search)
            )
        
        # 分页
        pagination = query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        products_data = []
        for product in pagination.items:
            products_data.append({
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': float(product.price),
                'category': {
                    'id': product.category.id,
                    'name': product.category.name
                },
                'image_url': product.image_url,
                'preparation_time': product.preparation_time,
                'calories': product.calories,
                'is_featured': product.is_featured,
                'stock_quantity': product.stock_quantity,
                'is_low_stock': product.is_low_stock
            })
        
        return api_response({
            'products': products_data,
            'pagination': {
                'page': page,
                'pages': pagination.pages,
                'per_page': per_page,
                'total': pagination.total,
                'has_next': pagination.has_next,
                'has_prev': pagination.has_prev
            }
        })
        
    except Exception as e:
        return api_error(f'获取商品列表失败: {str(e)}', 500)

@api_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """获取单个商品详情"""
    try:
        product = Product.query.get(product_id)
        if not product:
            return api_error('商品不存在', 404)
        
        product_data = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': float(product.price),
            'category': {
                'id': product.category.id,
                'name': product.category.name,
                'description': product.category.description
            },
            'image_url': product.image_url,
            'preparation_time': product.preparation_time,
            'calories': product.calories,
            'is_featured': product.is_featured,
            'stock_quantity': product.stock_quantity,
            'is_available': product.is_available,
            'created_at': product.created_at.isoformat(),
            'updated_at': product.updated_at.isoformat()
        }
        
        return api_response(product_data)
        
    except Exception as e:
        return api_error(f'获取商品详情失败: {str(e)}', 500)

@api_bp.route('/categories', methods=['GET'])
def get_categories():
    """获取商品分类列表"""
    try:
        categories = Category.query.filter_by(is_active=True).order_by(Category.sort_order).all()
        
        categories_data = []
        for category in categories:
            categories_data.append({
                'id': category.id,
                'name': category.name,
                'description': category.description,
                'icon': category.icon,
                'product_count': category.products.filter_by(is_available=True).count()
            })
        
        return api_response(categories_data)
        
    except Exception as e:
        return api_error(f'获取分类列表失败: {str(e)}', 500)

@api_bp.route('/orders', methods=['POST'])
@token_required
def create_order(current_user_id):
    """创建订单（外卖下单）"""
    try:
        data = request.get_json()
        
        # 验证必需字段
        if 'items' not in data or not data['items']:
            return api_error('订单项目不能为空', 400)
        
        # 构建订单项目数据
        items_data = []
        for item in data['items']:
            if 'product_id' not in item or 'quantity' not in item:
                return api_error('订单项目缺少必需字段', 400)
            
            items_data.append({
                'product_id': item['product_id'],
                'quantity': item['quantity'],
                'customizations': item.get('customizations'),
                'special_instructions': item.get('special_instructions', '')
            })
        
        # 创建订单
        order = OrderService.create_order(
            customer_id=current_user_id,
            items_data=items_data,
            notes=data.get('notes', '')
        )
        
        # 返回订单信息
        order_data = {
            'id': order.id,
            'order_number': order.order_number,
            'status': order.status,
            'subtotal': float(order.subtotal),
            'tax_amount': float(order.tax_amount),
            'total_amount': float(order.total_amount),
            'estimated_ready_time': order.estimated_ready_time.isoformat() if order.estimated_ready_time else None,
            'created_at': order.created_at.isoformat(),
            'items': [
                {
                    'product_name': item.product_name,
                    'quantity': item.quantity,
                    'unit_price': float(item.unit_price),
                    'subtotal': float(item.subtotal),
                    'special_instructions': item.special_instructions
                }
                for item in order.items
            ]
        }
        
        return api_response(order_data, '订单创建成功', 201)
        
    except ValueError as e:
        return api_error(str(e), 400)
    except Exception as e:
        return api_error(f'创建订单失败: {str(e)}', 500)

@api_bp.route('/orders', methods=['GET'])
@token_required
def get_user_orders(current_user_id):
    """获取用户订单列表"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        status = request.args.get('status')
        
        query = Order.query.filter_by(customer_id=current_user_id)
        
        if status:
            query = query.filter_by(status=status)
        
        pagination = query.order_by(Order.created_at.desc()).paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        orders_data = []
        for order in pagination.items:
            orders_data.append({
                'id': order.id,
                'order_number': order.order_number,
                'status': order.status,
                'total_amount': float(order.total_amount),
                'created_at': order.created_at.isoformat(),
                'estimated_ready_time': order.estimated_ready_time.isoformat() if order.estimated_ready_time else None,
                'items_count': order.items.count()
            })
        
        return api_response({
            'orders': orders_data,
            'pagination': {
                'page': page,
                'pages': pagination.pages,
                'per_page': per_page,
                'total': pagination.total
            }
        })
        
    except Exception as e:
        return api_error(f'获取订单列表失败: {str(e)}', 500)

@api_bp.route('/orders/<int:order_id>', methods=['GET'])
@token_required
def get_order_detail(current_user_id, order_id):
    """获取订单详情"""
    try:
        order = Order.query.get(order_id)
        if not order:
            return api_error('订单不存在', 404)
        
        # 检查权限
        if order.customer_id != current_user_id:
            return api_error('无权访问此订单', 403)
        
        order_data = {
            'id': order.id,
            'order_number': order.order_number,
            'status': order.status,
            'subtotal': float(order.subtotal),
            'tax_amount': float(order.tax_amount),
            'discount_amount': float(order.discount_amount),
            'total_amount': float(order.total_amount),
            'points_used': order.points_used,
            'points_earned': order.points_earned,
            'notes': order.notes,
            'created_at': order.created_at.isoformat(),
            'confirmed_at': order.confirmed_at.isoformat() if order.confirmed_at else None,
            'completed_at': order.completed_at.isoformat() if order.completed_at else None,
            'estimated_ready_time': order.estimated_ready_time.isoformat() if order.estimated_ready_time else None,
            'items': [
                {
                    'id': item.id,
                    'product_name': item.product_name,
                    'unit_price': float(item.unit_price),
                    'quantity': item.quantity,
                    'subtotal': float(item.subtotal),
                    'customizations': item.customizations,
                    'special_instructions': item.special_instructions
                }
                for item in order.items
            ]
        }
        
        return api_response(order_data)
        
    except Exception as e:
        return api_error(f'获取订单详情失败: {str(e)}', 500)

@api_bp.route('/user/profile', methods=['GET'])
@token_required
def get_user_profile(current_user_id):
    """获取用户资料"""
    try:
        profile_data = UserService.get_user_profile(current_user_id)
        if not profile_data:
            return api_error('用户不存在', 404)
        
        user = profile_data['user']
        stats = profile_data['stats']
        
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'full_name': user.full_name,
            'phone': user.phone,
            'birthday': user.birthday.isoformat() if user.birthday else None,
            'avatar': user.avatar,
            'favorite_drink': user.favorite_drink,
            'loyalty_points': user.loyalty_points,
            'created_at': user.created_at.isoformat(),
            'last_login': user.last_login.isoformat() if user.last_login else None,
            'stats': stats
        }
        
        return api_response(user_data)
        
    except Exception as e:
        return api_error(f'获取用户资料失败: {str(e)}', 500)

# 错误处理
@api_bp.errorhandler(404)
def api_not_found(error):
    return api_error('API接口不存在', 404)

@api_bp.errorhandler(405)
def api_method_not_allowed(error):
    return api_error('HTTP方法不被允许', 405)

@api_bp.errorhandler(500)
def api_internal_error(error):
    return api_error('服务器内部错误', 500)
```

#### 2. API测试工具

```python
# test_api.py - API测试脚本
import requests
import json
from datetime import datetime

class CoffeeShopAPITester:
    """咖啡厅API测试工具"""
    
    def __init__(self, base_url='http://127.0.0.1:5000/api/v1'):
        self.base_url = base_url
        self.token = None
        self.session = requests.Session()
    
    def login(self, username='demo', password='demo123'):
        """登录获取令牌"""
        url = f'{self.base_url}/auth/login'
        data = {
            'username': username,
            'password': password
        }
        
        response = self.session.post(url, json=data)
        result = response.json()
        
        if result['success']:
            self.token = result['data']['token']
            self.session.headers.update({
                'Authorization': f'Bearer {self.token}'
            })
            print(f"✅ 登录成功: {result['data']['user']['username']}")
            return True
        else:
            print(f"❌ 登录失败: {result['message']}")
            return False
    
    def test_get_products(self):
        """测试获取商品列表"""
        print("\n🧪 测试: 获取商品列表")
        
        url = f'{self.base_url}/products'
        response = self.session.get(url)
        result = response.json()
        
        if result['success']:
            products = result['data']['products']
            print(f"✅ 获取到 {len(products)} 个商品")
            for product in products[:3]:  # 显示前3个
                print(f"   - {product['name']}: ¥{product['price']}")
        else:
            print(f"❌ 获取失败: {result['message']}")
    
    def test_get_categories(self):
        """测试获取分类列表"""
        print("\n🧪 测试: 获取分类列表")
        
        url = f'{self.base_url}/categories'
        response = self.session.get(url)
        result = response.json()
        
        if result['success']:
            categories = result['data']
            print(f"✅ 获取到 {len(categories)} 个分类")
            for category in categories:
                print(f"   - {category['name']}: {category['product_count']} 个商品")
        else:
            print(f"❌ 获取失败: {result['message']}")
    
    def test_create_order(self):
        """测试创建订单"""
        print("\n🧪 测试: 创建订单")
        
        if not self.token:
            print("❌ 需要先登录")
            return
        
        url = f'{self.base_url}/orders'
        data = {
            'items': [
                {
                    'product_id': 1,  # 美式咖啡
                    'quantity': 2,
                    'special_instructions': '少糖'
                },
                {
                    'product_id': 6,  # 提拉米苏
                    'quantity': 1
                }
            ],
            'notes': 'API测试订单'
        }
        
        response = self.session.post(url, json=data)
        result = response.json()
        
        if result['success']:
            order = result['data']
            print(f"✅ 订单创建成功: {order['order_number']}")
            print(f"   总金额: ¥{order['total_amount']}")
            print(f"   预计完成时间: {order['estimated_ready_time']}")
            return order['id']
        else:
            print(f"❌ 创建失败: {result['message']}")
            return None
    
    def test_get_orders(self):
        """测试获取订单列表"""
        print("\n🧪 测试: 获取订单列表")
        
        if not self.token:
            print("❌ 需要先登录")
            return
        
        url = f'{self.base_url}/orders'
        response = self.session.get(url)
        result = response.json()
        
        if result['success']:
            orders = result['data']['orders']
            print(f"✅ 获取到 {len(orders)} 个订单")
            for order in orders[:3]:  # 显示前3个
                print(f"   - {order['order_number']}: ¥{order['total_amount']} ({order['status']})")
        else:
            print(f"❌ 获取失败: {result['message']}")
    
    def test_get_profile(self):
        """测试获取用户资料"""
        print("\n🧪 测试: 获取用户资料")
        
        if not self.token:
            print("❌ 需要先登录")
            return
        
        url = f'{self.base_url}/user/profile'
        response = self.session.get(url)
        result = response.json()
        
        if result['success']:
            user = result['data']
            print(f"✅ 用户资料获取成功")
            print(f"   用户名: {user['username']}")
            print(f"   积分: {user['loyalty_points']}")
            print(f"   总订单数: {user['stats']['total_orders']}")
            print(f"   总消费: ¥{user['stats']['total_spent']}")
        else:
            print(f"❌ 获取失败: {result['message']}")
    
    def run_all_tests(self):
        """运行所有测试"""
        print("🚀 开始API测试...")
        print("=" * 50)
        
        # 1. 登录
        if not self.login():
            return
        
        # 2. 测试各个接口
        self.test_get_categories()
        self.test_get_products()
        self.test_get_profile()
        order_id = self.test_create_order()
        self.test_get_orders()
        
        print("\n" + "=" * 50)
        print("🎉 API测试完成！")

# 运行测试
if __name__ == '__main__':
    tester = CoffeeShopAPITester()
    tester.run_all_tests()
```

### 🚀 应用部署

#### 1. 生产环境配置

```python
# wsgi.py - WSGI入口文件
from app import create_app
import os

# 根据环境变量选择配置
config_name = os.environ.get('FLASK_ENV', 'production')
app = create_app(config_name)

if __name__ == "__main__":
    app.run()
```

```python
# requirements.txt - 生产环境依赖
Flask==2.3.3
Flask-SQLAlchemy==3.0.5
Flask-Migrate==4.0.5
Flask-WTF==1.1.1
Flask-Login==0.6.2
Flask-RESTful==0.3.10
PyJWT==2.8.0
Werkzeug==2.3.7
gunicorn==21.2.0  # WSGI服务器
python-dotenv==1.0.0  # 环境变量管理
```

```bash
# .env - 环境变量配置文件
FLASK_ENV=production
SECRET_KEY=your-super-secret-key-here
DATABASE_URL=sqlite:///coffee_shop_prod.db

# 如果使用PostgreSQL
# DATABASE_URL=postgresql://username:password@localhost/coffee_shop

# 如果使用MySQL
# DATABASE_URL=mysql://username:password@localhost/coffee_shop
```

#### 2. Docker部署

```dockerfile
# Dockerfile - 容器化配置
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 设置环境变量
ENV FLASK_ENV=production
ENV PYTHONPATH=/app

# 暴露端口
EXPOSE 5000

# 启动命令
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "wsgi:app"]
```

```yaml
# docker-compose.yml - 多容器编排
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - DATABASE_URL=postgresql://postgres:password@db:5432/coffee_shop
    depends_on:
      - db
    volumes:
      - ./static/uploads:/app/static/uploads

  db:
    image: postgres:13
    environment:
      - POSTGRES_DB=coffee_shop
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./static:/var/www/static
    depends_on:
      - web

volumes:
  postgres_data:
```

#### 3. 部署脚本

```bash
#!/bin/bash
# deploy.sh - 一键部署脚本

echo "🚀 开始部署咖啡厅应用..."

# 1. 拉取最新代码
echo "📥 拉取最新代码..."
git pull origin main

# 2. 构建Docker镜像
echo "🔨 构建Docker镜像..."
docker-compose build

# 3. 停止旧容器
echo "⏹️ 停止旧容器..."
docker-compose down

# 4. 启动新容器
echo "▶️ 启动新容器..."
docker-compose up -d

# 5. 运行数据库迁移
echo "🗄️ 运行数据库迁移..."
docker-compose exec web flask db upgrade

# 6. 检查服务状态
echo "🔍 检查服务状态..."
docker-compose ps

echo "✅ 部署完成！"
echo "🌐 应用访问地址: http://localhost"
echo "📊 API文档地址: http://localhost/api/v1/docs"
```

### 📚 API文档生成

```python
# docs.py - API文档生成
from flask import Blueprint, render_template_string

docs_bp = Blueprint('docs', __name__)

@docs_bp.route('/api/v1/docs')
def api_docs():
    """API文档页面"""
    
    api_doc_template = """
<!DOCTYPE html>
<html>
<head>
    <title>咖啡厅API文档</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; }
        .endpoint { border: 1px solid #ddd; margin: 10px 0; padding: 15px; border-radius: 5px; }
        .method { display: inline-block; padding: 4px 8px; border-radius: 3px; color: white; font-weight: bold; }
        .get { background: #61affe; }
        .post { background: #49cc90; }
        .put { background: #fca130; }
        .delete { background: #f93e3e; }
        .code { background: #f8f8f8; padding: 10px; border-radius: 3px; overflow-x: auto; }
        pre { margin: 0; }
    </style>
</head>
<body>
    <h1>🏪 咖啡厅API文档</h1>
    <p>欢迎使用咖啡厅外卖服务API！</p>
    
    <h2>🔐 认证</h2>
    <div class="endpoint">
        <h3><span class="method post">POST</span> /api/v1/auth/login</h3>
        <p>用户登录获取访问令牌</p>
        <h4>请求体:</h4>
        <div class="code">
            <pre>{
  "username": "demo",
  "password": "demo123"
}</pre>
        </div>
        <h4>响应:</h4>
        <div class="code">
            <pre>{
  "success": true,
  "data": {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "user": {
      "id": 1,
      "username": "demo",
      "email": "demo@coffee.com"
    }
  }
}</pre>
        </div>
    </div>
    
    <h2>📋 商品管理</h2>
    <div class="endpoint">
        <h3><span class="method get">GET</span> /api/v1/products</h3>
        <p>获取商品列表</p>
        <h4>查询参数:</h4>
        <ul>
            <li><code>category_id</code> - 分类ID</li>
            <li><code>featured</code> - 是否只返回推荐商品</li>
            <li><code>search</code> - 搜索关键词</li>
            <li><code>page</code> - 页码</li>
            <li><code>per_page</code> - 每页数量</li>
        </ul>
    </div>
    
    <div class="endpoint">
        <h3><span class="method get">GET</span> /api/v1/products/{id}</h3>
        <p>获取商品详情</p>
    </div>
    
    <div class="endpoint">
        <h3><span class="method get">GET</span> /api/v1/categories</h3>
        <p>获取商品分类列表</p>
    </div>
    
    <h2>🛒 订单管理</h2>
    <div class="endpoint">
        <h3><span class="method post">POST</span> /api/v1/orders</h3>
        <p>创建新订单 <strong>(需要认证)</strong></p>
        <h4>请求头:</h4>
        <div class="code">
            <pre>Authorization: Bearer {token}</pre>
        </div>
        <h4>请求体:</h4>
        <div class="code">
            <pre>{
  "items": [
    {
      "product_id": 1,
      "quantity": 2,
      "special_instructions": "少糖"
    }
  ],
  "notes": "请快点制作"
}</pre>
        </div>
    </div>
    
    <div class="endpoint">
        <h3><span class="method get">GET</span> /api/v1/orders</h3>
        <p>获取用户订单列表 <strong>(需要认证)</strong></p>
    </div>
    
    <div class="endpoint">
        <h3><span class="method get">GET</span> /api/v1/orders/{id}</h3>
        <p>获取订单详情 <strong>(需要认证)</strong></p>
    </div>
    
    <h2>👤 用户管理</h2>
    <div class="endpoint">
        <h3><span class="method get">GET</span> /api/v1/user/profile</h3>
        <p>获取用户资料 <strong>(需要认证)</strong></p>
    </div>
    
    <h2>📝 响应格式</h2>
    <p>所有API响应都遵循统一格式:</p>
    <div class="code">
        <pre>{
  "success": true,
  "code": 200,
  "message": "操作成功",
  "timestamp": "2024-01-01T12:00:00.000000",
  "data": { ... }
}</pre>
    </div>
    
    <h2>❌ 错误代码</h2>
    <ul>
        <li><code>400</code> - 请求参数错误</li>
        <li><code>401</code> - 未认证或令牌无效</li>
        <li><code>403</code> - 无权限访问</li>
        <li><code>404</code> - 资源不存在</li>
        <li><code>500</code> - 服务器内部错误</li>
    </ul>
    
    <hr>
    <p><small>© 2024 咖啡厅外卖服务 API v1.0</small></p>
</body>
</html>
    """
    
    return render_template_string(api_doc_template)
```

### 📝 本节小结

通过"外卖服务"这一节，我们全面学习了：

1. **RESTful API设计**：掌握了标准的API设计原则和最佳实践
2. **JSON数据处理**：学会了处理JSON请求和响应
3. **JWT认证机制**：实现了基于令牌的API认证系统
4. **API测试方法**：编写了完整的API测试套件
5. **应用部署方案**：了解了从开发到生产的完整部署流程

**核心要点回顾**：
- 🚚 API让Web应用具备了"外卖服务"能力
- 📋 RESTful设计让API接口标准化和易于理解
- 🔐 JWT认证提供了安全可靠的身份验证机制
- 🧪 API测试确保了接口的可靠性和稳定性
- 🚀 容器化部署简化了应用的发布和维护

---

## 🎓 第16章总结

恭喜你完成了Flask Web开发基础的学习！让我们回顾一下"Web咖啡厅"的完整建设历程：

### 🏗️ 建设历程回顾

1. **16.1 咖啡厅开张** ☕
   - 学会了Flask基础和路由系统
   - 掌握了模板引擎和静态文件处理
   - 建立了第一个Web应用

2. **16.2 顾客点餐服务** 🛎️
   - 深入理解了HTTP请求处理
   - 实现了完整的用户认证系统
   - 掌握了表单处理和会话管理

3. **16.3 厨房管理系统** 🗄️
   - 学会了数据库集成和模型设计
   - 实现了复杂的业务逻辑处理
   - 掌握了数据持久化和关系映射

4. **16.4 外卖服务** 🚚
   - 构建了标准的RESTful API
   - 实现了JWT认证和权限控制
   - 学会了应用部署和容器化

### 🎯 核心技能掌握

通过本章学习，你已经掌握了：

- ✅ **Flask框架核心概念**：路由、视图、模板、蓝图
- ✅ **Web开发基础技能**：HTTP协议、表单处理、会话管理
- ✅ **数据库集成应用**：SQLAlchemy ORM、数据建模、迁移
- ✅ **API开发能力**：RESTful设计、JSON处理、认证授权
- ✅ **项目部署经验**：容器化、环境配置、生产部署

### 🚀 进阶学习方向

完成了基础学习后，你可以继续探索：

1. **前端集成**：学习React/Vue.js与Flask API的集成
2. **微服务架构**：将单体应用拆分为多个服务
3. **性能优化**：缓存、数据库优化、负载均衡
4. **安全强化**：HTTPS、CSRF保护、输入验证
5. **监控运维**：日志管理、性能监控、错误追踪

### 💡 项目实践建议

1. **扩展咖啡厅功能**：
   - 添加商品评价系统
   - 实现优惠券和促销活动
   - 增加实时订单状态推送
   - 开发移动端应用

2. **应用到其他领域**：
   - 在线书店管理系统
   - 学生成绩管理系统
   - 企业内部办公系统
   - 个人博客和作品展示

记住，**实践是最好的老师**！现在就开始动手构建属于你自己的Web应用吧！

---

*"每一杯完美的咖啡都需要精心调制，每一个优秀的Web应用也需要细致打磨。愿你在Flask的世界里，调制出属于自己的完美应用！"* ☕✨