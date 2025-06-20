# 第15章：Pandas数据分析

> 🎯 **学习目标**  
> 通过本章学习，你将掌握Python数据分析利器Pandas的核心功能，学会处理真实世界的数据分析任务，为成为数据分析师打下坚实基础。

## 📖 本章导读

在现代数据驱动的世界中，数据分析能力已成为各行各业的核心技能。无论是商业决策、科学研究，还是日常工作，我们都需要从海量数据中提取有价值的信息。

**为什么学习Pandas？**
- 🏭 **数据工厂的管理者**：Pandas就像一个智能化的数据工厂，能够高效处理各种"原料"（数据）
- 📊 **数据科学的基石**：90%的数据科学工作都离不开Pandas
- 🚀 **职场竞争力**：掌握Pandas是数据分析岗位的必备技能
- 🎯 **解决实际问题**：从学生成绩分析到企业销售报表，无所不能

**本章知识地图**：
```mermaid
mindmap
  root((Pandas数据分析))
    数据结构
      Series(一维数据)
      DataFrame(二维表格)
      Index(索引系统)
    数据输入输出
      文件读取(CSV/Excel/JSON)
      数据库连接
      网络数据获取
    数据清洗
      缺失值处理
      重复数据处理
      数据类型转换
    数据分析
      描述性统计
      分组聚合
      数据透视表
      可视化展示
```

## 15.1 Pandas基础与数据结构

### 🏭 数据工厂的原料仓库

想象一下，你是一家现代化数据工厂的管理者。工厂里有两种主要的原料仓库：

- **Series仓库**：专门存储单一类型的产品，如"所有学生的数学成绩"
- **DataFrame仓库**：存储多种相关产品，如"学生信息表（姓名、年龄、各科成绩）"

### 15.1.1 Pandas简介与环境准备

Pandas（Panel Data Analysis）是基于NumPy构建的数据分析库，提供了高性能、易用的数据结构和数据分析工具。

```python
# 安装Pandas（如果还未安装）
# pip install pandas matplotlib seaborn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 设置显示选项
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 20)

print("Pandas版本:", pd.__version__)
print("数据工厂已准备就绪！🏭")
```

### 15.1.2 Series：单一产品线的数据容器

Series是Pandas中的一维数据结构，类似于带标签的数组。

```python
# === Series创建方法 ===

# 方法1：从列表创建
students_math_scores = pd.Series([85, 92, 78, 96, 88], 
                                name='数学成绩')
print("📊 学生数学成绩：")
print(students_math_scores)
print()

# 方法2：从字典创建（自动生成索引）
student_scores = pd.Series({
    '张三': 85,
    '李四': 92, 
    '王五': 78,
    '赵六': 96,
    '钱七': 88
}, name='数学成绩')

print("📋 带姓名的成绩单：")
print(student_scores)
print()

# 方法3：指定索引
ages = pd.Series([18, 19, 18, 20, 19], 
                index=['张三', '李四', '王五', '赵六', '钱七'],
                name='年龄')
print("👥 学生年龄信息：")
print(ages)
print()

# === Series基本属性 ===
print("=== Series基本信息 ===")
print(f"数据类型: {student_scores.dtype}")
print(f"数据长度: {len(student_scores)}")
print(f"索引: {student_scores.index.tolist()}")
print(f"数值: {student_scores.values}")
print(f"名称: {student_scores.name}")
```

#### Series的核心操作

```python
# === 数据访问 ===
print("=== 数据访问方式 ===")

# 按索引访问
print(f"张三的成绩: {student_scores['张三']}")
print(f"李四的成绩: {student_scores.loc['李四']}")

# 按位置访问
print(f"第一个学生成绩: {student_scores.iloc[0]}")
print(f"前三个学生成绩:\n{student_scores.iloc[:3]}")

# 条件筛选
high_scores = student_scores[student_scores >= 90]
print(f"\n优秀学生(≥90分):\n{high_scores}")

# === 数据修改 ===
print("\n=== 数据修改 ===")
student_scores_copy = student_scores.copy()
student_scores_copy['张三'] = 90  # 修改单个值
print(f"张三成绩修改后: {student_scores_copy['张三']}")

# 批量修改
student_scores_copy[student_scores_copy < 80] += 5  # 低分加5分
print(f"低分提升后:\n{student_scores_copy}")

# === 数学运算 ===
print("\n=== 数学运算 ===")
print(f"平均分: {student_scores.mean():.2f}")
print(f"最高分: {student_scores.max()}")
print(f"最低分: {student_scores.min()}")
print(f"标准差: {student_scores.std():.2f}")

# 成绩加权（期末成绩占70%）
final_scores = student_scores * 0.7
print(f"\n期末成绩(70%权重):\n{final_scores}")
```

### 15.1.3 DataFrame：多产品线的数据管理系统

DataFrame是Pandas的核心数据结构，可以理解为带标签的二维表格。

```python
# === DataFrame创建方法 ===

# 方法1：从字典创建
student_data = {
    '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
    '年龄': [18, 19, 18, 20, 19],
    '性别': ['男', '女', '男', '女', '男'],
    '数学': [85, 92, 78, 96, 88],
    '语文': [88, 85, 92, 89, 87],
    '英语': [82, 94, 85, 93, 90]
}

df_students = pd.DataFrame(student_data)
print("📊 学生信息表：")
print(df_students)
print()

# 方法2：从嵌套列表创建
data_matrix = [
    ['张三', 18, '男', 85, 88, 82],
    ['李四', 19, '女', 92, 85, 94],
    ['王五', 18, '男', 78, 92, 85],
    ['赵六', 20, '女', 96, 89, 93],
    ['钱七', 19, '男', 88, 87, 90]
]

df_from_list = pd.DataFrame(data_matrix, 
                           columns=['姓名', '年龄', '性别', '数学', '语文', '英语'])
print("📋 从列表创建的DataFrame：")
print(df_from_list.head(3))  # 显示前3行
print()

# === DataFrame基本信息 ===
print("=== DataFrame基本信息 ===")
print(f"形状 (行数, 列数): {df_students.shape}")
print(f"列名: {df_students.columns.tolist()}")
print(f"索引: {df_students.index.tolist()}")
print(f"数据类型:\n{df_students.dtypes}")
print()

# 详细信息
print("=== 详细信息 ===")
print(df_students.info())
print()

# 描述性统计
print("=== 数值列描述性统计 ===")
print(df_students.describe())
```

#### DataFrame的数据访问

```python
# === 列操作 ===
print("=== 列操作 ===")

# 选择单列（返回Series）
math_scores = df_students['数学']
print(f"数学成绩列:\n{math_scores}")
print(f"类型: {type(math_scores)}")
print()

# 选择多列（返回DataFrame）
score_columns = df_students[['姓名', '数学', '语文', '英语']]
print("成绩相关列:")
print(score_columns)
print()

# === 行操作 ===
print("=== 行操作 ===")

# 按位置选择行
first_student = df_students.iloc[0]  # 第一行
print(f"第一个学生信息:\n{first_student}")
print()

# 按索引选择行
student_info = df_students.loc[0]  # 索引为0的行
print(f"索引0的学生信息:\n{student_info}")
print()

# 选择多行
first_three = df_students.iloc[:3]  # 前三行
print("前三个学生:")
print(first_three)
print()

# === 条件筛选 ===
print("=== 条件筛选 ===")

# 单条件筛选
high_math = df_students[df_students['数学'] >= 90]
print("数学成绩优秀的学生:")
print(high_math)
print()

# 多条件筛选
excellent_students = df_students[
    (df_students['数学'] >= 85) & 
    (df_students['语文'] >= 85)
]
print("数学和语文都优秀的学生:")
print(excellent_students)
print()

# 字符串条件
male_students = df_students[df_students['性别'] == '男']
print("男学生信息:")
print(male_students)
```

### 15.1.4 索引系统：仓库的货架编号

索引是Pandas的核心概念，就像仓库中的货架编号系统。

```python
# === 设置索引 ===
print("=== 索引操作 ===")

# 将姓名设为索引
df_indexed = df_students.set_index('姓名')
print("以姓名为索引的DataFrame:")
print(df_indexed)
print()

# 重置索引
df_reset = df_indexed.reset_index()
print("重置索引后:")
print(df_reset.head(3))
print()

# === 多层索引 ===
print("=== 多层索引示例 ===")

# 创建多层索引数据
multi_data = {
    '成绩': [85, 88, 82, 92, 85, 94, 78, 92, 85],
    '学期': ['第一学期', '第一学期', '第一学期', '第二学期', '第二学期', '第二学期', '第三学期', '第三学期', '第三学期']
}

multi_index = pd.MultiIndex.from_tuples([
    ('张三', '数学'), ('张三', '语文'), ('张三', '英语'),
    ('李四', '数学'), ('李四', '语文'), ('李四', '英语'),
    ('王五', '数学'), ('王五', '语文'), ('王五', '英语')
], names=['学生', '科目'])

df_multi = pd.DataFrame(multi_data, index=multi_index)
print("多层索引DataFrame:")
print(df_multi)
print()

# 多层索引访问
print("张三的所有成绩:")
print(df_multi.loc['张三'])
print()

print("所有学生的数学成绩:")
print(df_multi.loc[(slice(None), '数学'), :])
```

### 🎯 实践项目：学生成绩管理系统

让我们创建一个完整的学生成绩管理系统，展示Pandas基础功能的综合应用。

```python
class StudentGradeManager:
    """学生成绩管理系统
    
    这个系统模拟了一个数据工厂的完整流程：
    - 原料入库：录入学生信息和成绩
    - 质量检查：数据验证和清洗
    - 生产加工：成绩计算和统计
    - 产品包装：报表生成和可视化
    """
    
    def __init__(self):
        self.students_df = pd.DataFrame()
        self.subjects = ['数学', '语文', '英语', '物理', '化学']
        
    def add_student(self, name, age, gender, scores):
        """添加学生信息"""
        if len(scores) != len(self.subjects):
            raise ValueError(f"成绩数量必须为{len(self.subjects)}个")
            
        student_data = {
            '姓名': name,
            '年龄': age,
            '性别': gender
        }
        
        # 添加各科成绩
        for subject, score in zip(self.subjects, scores):
            student_data[subject] = score
            
        # 转换为DataFrame并添加到主表
        new_student = pd.DataFrame([student_data])
        self.students_df = pd.concat([self.students_df, new_student], 
                                   ignore_index=True)
        
        print(f"✅ 学生 {name} 信息已录入")
        
    def batch_add_students(self, students_list):
        """批量添加学生"""
        for student in students_list:
            self.add_student(*student)
            
    def calculate_total_average(self):
        """计算总分和平均分"""
        # 计算总分
        self.students_df['总分'] = self.students_df[self.subjects].sum(axis=1)
        
        # 计算平均分
        self.students_df['平均分'] = self.students_df[self.subjects].mean(axis=1)
        
        print("✅ 总分和平均分计算完成")
        
    def get_rank(self):
        """计算排名"""
        self.students_df['排名'] = self.students_df['总分'].rank(
            method='min', ascending=False).astype(int)
        
        print("✅ 排名计算完成")
        
    def get_statistics(self):
        """获取统计信息"""
        stats = {
            '学生总数': len(self.students_df),
            '男生人数': len(self.students_df[self.students_df['性别'] == '男']),
            '女生人数': len(self.students_df[self.students_df['性别'] == '女']),
            '平均年龄': self.students_df['年龄'].mean(),
            '总分最高': self.students_df['总分'].max(),
            '总分最低': self.students_df['总分'].min(),
            '班级平均分': self.students_df['平均分'].mean()
        }
        
        return stats
        
    def get_subject_analysis(self):
        """各科成绩分析"""
        subject_stats = {}
        
        for subject in self.subjects:
            subject_stats[subject] = {
                '平均分': self.students_df[subject].mean(),
                '最高分': self.students_df[subject].max(),
                '最低分': self.students_df[subject].min(),
                '标准差': self.students_df[subject].std(),
                '及格率': (self.students_df[subject] >= 60).mean() * 100
            }
            
        return subject_stats
        
    def find_excellent_students(self, threshold=85):
        """查找优秀学生（平均分超过阈值）"""
        excellent = self.students_df[
            self.students_df['平均分'] >= threshold
        ].sort_values('平均分', ascending=False)
        
        return excellent
        
    def generate_report(self):
        """生成完整报告"""
        print("=" * 50)
        print("📊 学生成绩管理系统报告")
        print("=" * 50)
        
        # 基本统计
        stats = self.get_statistics()
        print("\n📈 基本统计信息:")
        for key, value in stats.items():
            if isinstance(value, float):
                print(f"  {key}: {value:.2f}")
            else:
                print(f"  {key}: {value}")
                
        # 各科分析
        print("\n📚 各科成绩分析:")
        subject_stats = self.get_subject_analysis()
        for subject, stats in subject_stats.items():
            print(f"\n  {subject}:")
            for key, value in stats.items():
                print(f"    {key}: {value:.2f}")
                
        # 优秀学生
        print("\n🏆 优秀学生名单 (平均分≥85):")
        excellent = self.find_excellent_students()
        if not excellent.empty:
            print(excellent[['姓名', '平均分', '排名']].to_string(index=False))
        else:
            print("  暂无优秀学生")
            
        # 完整成绩单
        print("\n📋 完整成绩单:")
        display_df = self.students_df.sort_values('排名')
        print(display_df.to_string(index=False))

# === 使用示例 ===
if __name__ == "__main__":
    # 创建成绩管理系统
    grade_manager = StudentGradeManager()
    
    # 示例学生数据
    students_data = [
        ('张三', 18, '男', [85, 88, 82, 90, 87]),
        ('李四', 19, '女', [92, 85, 94, 88, 91]),
        ('王五', 18, '男', [78, 92, 85, 82, 79]),
        ('赵六', 20, '女', [96, 89, 93, 95, 94]),
        ('钱七', 19, '男', [88, 87, 90, 85, 89]),
        ('孙八', 18, '女', [83, 91, 87, 89, 85]),
        ('周九', 19, '男', [90, 84, 88, 92, 86]),
        ('吴十', 18, '女', [87, 93, 91, 88, 92])
    ]
    
    # 批量添加学生
    print("🏭 数据工厂开始运作...")
    grade_manager.batch_add_students(students_data)
    
    # 计算总分和平均分
    grade_manager.calculate_total_average()
    
    # 计算排名
    grade_manager.get_rank()
    
    # 生成报告
    grade_manager.generate_report()
    
    print("\n🎉 学生成绩管理系统演示完成！")
```

### 💡 核心概念总结

1. **Series**：一维标签数组，适合存储单一类型的数据
2. **DataFrame**：二维标签表格，Pandas的核心数据结构
3. **Index**：行和列的标签系统，支持快速数据访问
4. **数据访问**：支持标签访问（.loc）和位置访问（.iloc）
5. **条件筛选**：使用布尔索引进行数据过滤

通过"数据工厂"的比喻，我们了解了Pandas的基本数据结构。接下来，让我们学习如何将各种"原料"（数据文件）导入到我们的工厂中。

---

## 15.2 数据读取与输入输出

### 🚛 数据工厂的进货与出货系统

在真实的数据分析工作中，数据很少是直接在代码中创建的。就像工厂需要从不同供应商采购原料一样，我们需要从各种数据源读取数据：CSV文件、Excel表格、数据库、网络API等。

同样，处理完的数据也需要"出货"——保存为文件、写入数据库或发送给其他系统。

### 15.2.1 文件读取：从仓库提取原料

#### CSV文件读取

CSV（Comma-Separated Values）是最常见的数据交换格式。

```python
# === CSV文件读取 ===
import pandas as pd
import numpy as np
from io import StringIO

# 模拟CSV文件内容
csv_content = """
姓名,年龄,性别,部门,薪资,入职日期
张三,28,男,技术部,15000,2020-03-15
李四,32,女,市场部,18000,2019-07-22
王五,25,男,技术部,12000,2021-01-10
赵六,29,女,人事部,14000,2020-11-05
钱七,35,男,销售部,20000,2018-05-30
孙八,26,女,技术部,13000,2021-08-18
"""

# 从字符串读取（模拟文件读取）
df_employees = pd.read_csv(StringIO(csv_content.strip()))
print("📊 员工信息表：")
print(df_employees)
print()

# === 常用读取参数 ===
# 指定编码（处理中文）
# df = pd.read_csv('employees.csv', encoding='utf-8')

# 指定分隔符
# df = pd.read_csv('data.txt', sep='\t')  # Tab分隔

# 跳过行
# df = pd.read_csv('data.csv', skiprows=2)  # 跳过前2行

# 指定列名
# df = pd.read_csv('data.csv', names=['col1', 'col2', 'col3'])

# 指定数据类型
dtype_dict = {
    '年龄': 'int64',
    '薪资': 'float64'
}
df_typed = pd.read_csv(StringIO(csv_content.strip()), dtype=dtype_dict)
print("指定数据类型后的DataFrame:")
print(df_typed.dtypes)
print()
```

#### Excel文件读取

```python
# === Excel文件读取示例 ===
# 注意：实际使用需要安装 openpyxl 或 xlrd
# pip install openpyxl

# 模拟Excel数据读取
excel_data = {
    'Sheet1': {
        '产品名称': ['笔记本电脑', '台式机', '平板电脑', '智能手机'],
        '销量': [150, 80, 200, 500],
        '单价': [5000, 3000, 2000, 1500],
        '库存': [50, 30, 100, 200]
    },
    'Sheet2': {
        '月份': ['1月', '2月', '3月', '4月'],
        '收入': [500000, 600000, 750000, 800000],
        '支出': [300000, 350000, 400000, 450000]
    }
}

# 模拟读取Excel的第一个工作表
df_products = pd.DataFrame(excel_data['Sheet1'])
print("📱 产品销售数据：")
print(df_products)
print()

# 模拟读取Excel的第二个工作表
df_finance = pd.DataFrame(excel_data['Sheet2'])
print("💰 财务数据：")
print(df_finance)
print()

# === Excel读取的实际代码示例 ===
print("Excel读取代码示例：")
print("""
# 读取Excel文件
df = pd.read_excel('sales_data.xlsx')

# 读取指定工作表
df = pd.read_excel('sales_data.xlsx', sheet_name='Sheet2')

# 读取多个工作表
dfs = pd.read_excel('sales_data.xlsx', sheet_name=['Sheet1', 'Sheet2'])

# 读取所有工作表
all_sheets = pd.read_excel('sales_data.xlsx', sheet_name=None)
""")
```

#### JSON文件读取

```python
# === JSON文件读取 ===
import json

# 模拟JSON数据
json_data = '''
[
    {
        "用户ID": "U001",
        "姓名": "张三",
        "年龄": 25,
        "爱好": ["编程", "阅读", "游泳"],
        "地址": {
            "省份": "北京",
            "城市": "北京市",
            "区域": "朝阳区"
        }
    },
    {
        "用户ID": "U002", 
        "姓名": "李四",
        "年龄": 30,
        "爱好": ["音乐", "旅行"],
        "地址": {
            "省份": "上海",
            "城市": "上海市",
            "区域": "浦东新区"
        }
    }
]
'''

# 从JSON字符串读取
df_users = pd.read_json(json_data)
print("👥 用户信息（JSON格式）：")
print(df_users)
print()

# 处理嵌套JSON数据
df_normalized = pd.json_normalize(json.loads(json_data))
print("📋 标准化后的用户信息：")
print(df_normalized)
```

### 15.2.2 数据库连接：从数据仓库提取

```python
# === 数据库连接示例 ===
import sqlite3

# 创建内存数据库演示
conn = sqlite3.connect(':memory:')

# 创建示例表
create_table_sql = '''
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade REAL,
    class_name TEXT
)
'''

conn.execute(create_table_sql)

# 插入示例数据
students_data = [
    (1, '张三', 18, 85.5, '高三1班'),
    (2, '李四', 17, 92.0, '高二3班'),
    (3, '王五', 18, 78.5, '高三2班'),
    (4, '赵六', 16, 88.0, '高一1班')
]

conn.executemany(
    'INSERT INTO students VALUES (?, ?, ?, ?, ?)', 
    students_data
)
conn.commit()

# 使用Pandas读取数据库
df_from_db = pd.read_sql_query(
    "SELECT * FROM students WHERE grade >= 80", 
    conn
)

print("📚 从数据库读取的学生信息：")
print(df_from_db)
print()

# 关闭连接
conn.close()

# === 实际数据库连接代码示例 ===
print("实际数据库连接代码：")
print("""
# MySQL连接示例
import pymysql
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://user:password@host:port/database')
df = pd.read_sql('SELECT * FROM table_name', engine)

# PostgreSQL连接示例
import psycopg2
engine = create_engine('postgresql://user:password@host:port/database')
df = pd.read_sql('SELECT * FROM table_name', engine)
""")
```

### 15.2.3 网络数据获取：在线原料采购

```python
# === 网络数据获取示例 ===
import requests
from io import StringIO

# 模拟API响应数据
api_response_data = '''
{
    "status": "success",
    "data": [
        {"date": "2025-01-01", "temperature": 15.2, "humidity": 65},
        {"date": "2025-01-02", "temperature": 18.5, "humidity": 70},
        {"date": "2025-01-03", "temperature": 12.8, "humidity": 80},
        {"date": "2025-01-04", "temperature": 20.1, "humidity": 55}
    ]
}
'''

# 解析API数据
import json
api_data = json.loads(api_response_data)
df_weather = pd.DataFrame(api_data['data'])
df_weather['date'] = pd.to_datetime(df_weather['date'])

print("🌤️ 天气数据（来自API）：")
print(df_weather)
print()

# === 网络CSV读取示例 ===
# 模拟网络CSV数据
network_csv = '''
股票代码,股票名称,当前价格,涨跌幅
000001,平安银行,12.50,+2.3%
000002,万科A,18.20,-1.5%
600036,招商银行,45.80,+0.8%
600519,贵州茅台,1680.00,+1.2%
'''

df_stocks = pd.read_csv(StringIO(network_csv))
print("📈 股票数据（网络CSV）：")
print(df_stocks)
print()

print("网络数据获取代码示例：")
print("""
# 从网络URL读取CSV
df = pd.read_csv('https://example.com/data.csv')

# 使用requests获取API数据
import requests
response = requests.get('https://api.example.com/data')
data = response.json()
df = pd.DataFrame(data)

# 带认证的API请求
headers = {'Authorization': 'Bearer your_token'}
response = requests.get('https://api.example.com/data', headers=headers)
""")
```

### 15.2.4 数据导出：成品出货系统

```python
# === 数据导出示例 ===

# 准备示例数据
export_data = {
    '产品名称': ['产品A', '产品B', '产品C', '产品D'],
    '销量': [100, 150, 80, 200],
    '收入': [50000, 75000, 40000, 100000],
    '利润率': [0.2, 0.25, 0.15, 0.3]
}
df_export = pd.DataFrame(export_data)

print("📦 准备导出的数据：")
print(df_export)
print()

# === CSV导出 ===
# df_export.to_csv('products.csv', index=False, encoding='utf-8')
print("CSV导出代码：")
print("df.to_csv('products.csv', index=False, encoding='utf-8')")
print()

# === Excel导出 ===
# df_export.to_excel('products.xlsx', index=False, sheet_name='产品数据')
print("Excel导出代码：")
print("df.to_excel('products.xlsx', index=False, sheet_name='产品数据')")
print()

# === JSON导出 ===
json_output = df_export.to_json(orient='records', force_ascii=False, indent=2)
print("JSON导出结果：")
print(json_output)
print()

# === 数据库导出 ===
print("数据库导出代码示例：")
print("""
# 导出到SQLite
df.to_sql('table_name', conn, if_exists='replace', index=False)

# 导出到MySQL
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://user:password@host/db')
df.to_sql('table_name', engine, if_exists='append', index=False)
""")
```

### 🎯 实践项目：多源数据整合分析器

让我们创建一个能够处理多种数据源的整合分析器：

```python
class MultiSourceDataAnalyzer:
    """多源数据整合分析器
    
    模拟数据工厂的完整供应链管理：
    - 多渠道采购：从不同数据源获取数据
    - 质量检验：数据格式验证和清洗
    - 统一加工：数据标准化处理
    - 综合分析：跨数据源的关联分析
    - 报告输出：多格式结果导出
    """
    
    def __init__(self):
        self.data_sources = {}
        self.processed_data = {}
        
    def load_csv_data(self, name, csv_content, **kwargs):
        """加载CSV数据"""
        try:
            df = pd.read_csv(StringIO(csv_content.strip()), **kwargs)
            self.data_sources[name] = {
                'data': df,
                'source_type': 'CSV',
                'load_time': pd.Timestamp.now()
            }
            print(f"✅ CSV数据源 '{name}' 加载成功，共 {len(df)} 条记录")
            return True
        except Exception as e:
            print(f"❌ CSV数据源 '{name}' 加载失败: {e}")
            return False
            
    def load_json_data(self, name, json_content):
        """加载JSON数据"""
        try:
            data = json.loads(json_content)
            df = pd.DataFrame(data)
            self.data_sources[name] = {
                'data': df,
                'source_type': 'JSON',
                'load_time': pd.Timestamp.now()
            }
            print(f"✅ JSON数据源 '{name}' 加载成功，共 {len(df)} 条记录")
            return True
        except Exception as e:
            print(f"❌ JSON数据源 '{name}' 加载失败: {e}")
            return False
            
    def load_dict_data(self, name, dict_data):
        """加载字典数据"""
        try:
            df = pd.DataFrame(dict_data)
            self.data_sources[name] = {
                'data': df,
                'source_type': 'Dictionary',
                'load_time': pd.Timestamp.now()
            }
            print(f"✅ 字典数据源 '{name}' 加载成功，共 {len(df)} 条记录")
            return True
        except Exception as e:
            print(f"❌ 字典数据源 '{name}' 加载失败: {e}")
            return False
            
    def show_data_sources(self):
        """显示所有数据源信息"""
        print("\n📊 数据源概览：")
        print("-" * 60)
        
        for name, info in self.data_sources.items():
            df = info['data']
            print(f"数据源: {name}")
            print(f"  类型: {info['source_type']}")
            print(f"  形状: {df.shape}")
            print(f"  列名: {list(df.columns)}")
            print(f"  加载时间: {info['load_time']}")
            print()
            
    def merge_data_sources(self, source1, source2, on_column, how='inner', result_name=None):
        """合并两个数据源"""
        if source1 not in self.data_sources or source2 not in self.data_sources:
            print("❌ 指定的数据源不存在")
            return False
            
        try:
            df1 = self.data_sources[source1]['data']
            df2 = self.data_sources[source2]['data']
            
            merged_df = pd.merge(df1, df2, on=on_column, how=how)
            
            if result_name is None:
                result_name = f"{source1}_{source2}_merged"
                
            self.processed_data[result_name] = merged_df
            print(f"✅ 数据源合并成功，结果保存为 '{result_name}'，共 {len(merged_df)} 条记录")
            return True
            
        except Exception as e:
            print(f"❌ 数据源合并失败: {e}")
            return False
            
    def analyze_data(self, data_name):
        """分析指定数据"""
        if data_name in self.data_sources:
            df = self.data_sources[data_name]['data']
        elif data_name in self.processed_data:
            df = self.processed_data[data_name]
        else:
            print(f"❌ 数据 '{data_name}' 不存在")
            return
            
        print(f"\n📈 数据分析报告：{data_name}")
        print("=" * 50)
        
        # 基本信息
        print(f"数据形状: {df.shape}")
        print(f"内存使用: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")
        print()
        
        # 数值列统计
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            print("📊 数值列描述性统计:")
            print(df[numeric_cols].describe())
            print()
            
        # 文本列统计
        text_cols = df.select_dtypes(include=['object']).columns
        if len(text_cols) > 0:
            print("📝 文本列信息:")
            for col in text_cols:
                unique_count = df[col].nunique()
                print(f"  {col}: {unique_count} 个唯一值")
            print()
            
        # 缺失值检查
        missing_data = df.isnull().sum()
        if missing_data.sum() > 0:
            print("⚠️ 缺失值情况:")
            print(missing_data[missing_data > 0])
        else:
            print("✅ 无缺失值")
            
    def export_data(self, data_name, format_type='csv', filename=None):
        """导出数据"""
        if data_name in self.data_sources:
            df = self.data_sources[data_name]['data']
        elif data_name in self.processed_data:
            df = self.processed_data[data_name]
        else:
            print(f"❌ 数据 '{data_name}' 不存在")
            return False
            
        if filename is None:
            filename = f"{data_name}_export"
            
        try:
            if format_type.lower() == 'csv':
                csv_output = df.to_csv(index=False)
                print(f"✅ CSV格式导出成功")
                print(f"文件内容预览（前200字符）:")
                print(csv_output[:200] + "..." if len(csv_output) > 200 else csv_output)
                
            elif format_type.lower() == 'json':
                json_output = df.to_json(orient='records', force_ascii=False, indent=2)
                print(f"✅ JSON格式导出成功")
                print(f"文件内容预览（前300字符）:")
                print(json_output[:300] + "..." if len(json_output) > 300 else json_output)
                
            elif format_type.lower() == 'excel':
                print(f"✅ Excel格式导出准备完成")
                print("实际使用时的代码:")
                print(f"df.to_excel('{filename}.xlsx', index=False)")
                
            return True
            
        except Exception as e:
            print(f"❌ 导出失败: {e}")
            return False

# === 使用示例 ===
if __name__ == "__main__":
    # 创建多源数据分析器
    analyzer = MultiSourceDataAnalyzer()
    
    print("🏭 多源数据整合分析器启动")
    print("=" * 50)
    
    # 数据源1：员工信息（CSV格式）
    employee_csv = """
员工ID,姓名,部门,薪资
E001,张三,技术部,15000
E002,李四,市场部,12000
E003,王五,技术部,18000
E004,赵六,人事部,10000
E005,钱七,销售部,14000
"""
    
    # 数据源2：部门信息（JSON格式）
    department_json = """
[
    {"部门": "技术部", "负责人": "张经理", "预算": 500000},
    {"部门": "市场部", "负责人": "李经理", "预算": 300000},
    {"部门": "人事部", "负责人": "王经理", "预算": 200000},
    {"部门": "销售部", "负责人": "赵经理", "预算": 400000}
]
"""
    
    # 数据源3：绩效数据（字典格式）
    performance_data = {
        '员工ID': ['E001', 'E002', 'E003', 'E004', 'E005'],
        '绩效评分': [85, 78, 92, 88, 80],
        '项目数量': [3, 2, 4, 2, 3],
        '客户满意度': [4.5, 4.2, 4.8, 4.3, 4.1]
    }
    
    # 加载数据源
    analyzer.load_csv_data('员工信息', employee_csv)
    analyzer.load_json_data('部门信息', department_json)
    analyzer.load_dict_data('绩效数据', performance_data)
    
    # 显示数据源概览
    analyzer.show_data_sources()
    
    # 合并员工信息和绩效数据
    analyzer.merge_data_sources('员工信息', '绩效数据', '员工ID', result_name='员工绩效综合')
    
    # 分析综合数据
    analyzer.analyze_data('员工绩效综合')
    
    # 导出数据
    print("\n📦 数据导出演示：")
    analyzer.export_data('员工绩效综合', 'csv')
    
    print("\n🎉 多源数据整合分析完成！")
```

### 💡 核心概念总结

1. **数据读取**：
   - `pd.read_csv()` - CSV文件读取
   - `pd.read_excel()` - Excel文件读取
   - `pd.read_json()` - JSON数据读取
   - `pd.read_sql()` - 数据库查询

2. **数据导出**：
   - `df.to_csv()` - 导出CSV
   - `df.to_excel()` - 导出Excel
   - `df.to_json()` - 导出JSON
   - `df.to_sql()` - 写入数据库

3. **参数配置**：
   - 编码设置（encoding）
   - 分隔符指定（sep）
   - 数据类型控制（dtype）
   - 索引处理（index）

4. **错误处理**：
   - 使用try-except处理异常
   - 验证数据格式和完整性
   - 提供友好的错误信息

通过"进货出货系统"的比喻，我们掌握了Pandas的数据输入输出功能。接下来，让我们学习如何对这些"原料"进行质量检验和清洗。

---

## 15.3 数据清洗与预处理

### 🔍 数据工厂的质检部门

在真实世界中，从供应商采购的原料往往存在各种质量问题：有些原料可能缺失、有些可能重复、有些规格不标准。数据也是如此——真实的数据总是"脏"的，需要经过严格的质检和清洗才能投入生产。

数据清洗就像工厂的质检部门，负责：
- **质量检验**：发现数据中的问题
- **标准化加工**：统一数据格式和规格
- **缺陷修复**：处理缺失值和异常值
- **去重处理**：删除重复的数据记录

### 15.3.1 缺失值处理：修复缺陷原料

缺失值是数据分析中最常见的问题，就像工厂收到了不完整的原料。

```python
# === 创建包含缺失值的示例数据 ===
import pandas as pd
import numpy as np

# 模拟真实的学生成绩数据（包含缺失值）
student_data = {
    '学号': ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008'],
    '姓名': ['张三', '李四', '王五', None, '钱七', '孙八', '周九', '吴十'],
    '年龄': [18, 19, None, 20, 18, 19, None, 18],
    '性别': ['男', '女', '男', '女', None, '女', '男', '女'],
    '数学': [85, 92, 78, None, 88, 83, 90, 87],
    '语文': [88, None, 92, 89, 87, 91, 84, None],
    '英语': [82, 94, 85, 93, None, 87, 88, 92],
    '总分': [255, None, 255, None, None, 261, 262, None]
}

df_students = pd.DataFrame(student_data)
print("📊 原始学生数据（含缺失值）：")
print(df_students)
print()

# === 缺失值检测 ===
print("🔍 缺失值检测报告：")
print("-" * 40)

# 检查每列的缺失值数量
missing_count = df_students.isnull().sum()
print("各列缺失值数量：")
print(missing_count)
print()

# 计算缺失值比例
missing_ratio = df_students.isnull().sum() / len(df_students) * 100
print("各列缺失值比例：")
for col, ratio in missing_ratio.items():
    if ratio > 0:
        print(f"  {col}: {ratio:.1f}%")
print()

# 检查每行的缺失值情况
row_missing = df_students.isnull().sum(axis=1)
print("每行缺失值数量：")
for idx, count in enumerate(row_missing):
    if count > 0:
        print(f"  第{idx}行: {count}个缺失值")
print()

# === 缺失值可视化分析 ===
print("📈 缺失值模式分析：")
# 显示缺失值的位置模式
print("缺失值位置图（True表示缺失）：")
print(df_students.isnull())
print()
```

#### 缺失值处理策略

```python
# === 策略1：删除缺失值 ===
print("=== 策略1：删除缺失值 ===")

# 删除包含任何缺失值的行
df_drop_any = df_students.dropna()
print(f"删除含缺失值的行后：{len(df_drop_any)}行（原始：{len(df_students)}行）")
print(df_drop_any)
print()

# 删除所有值都缺失的行
df_drop_all = df_students.dropna(how='all')
print(f"删除全部缺失的行后：{len(df_drop_all)}行")

# 删除特定列的缺失值
df_drop_name = df_students.dropna(subset=['姓名'])
print(f"删除姓名缺失的行后：{len(df_drop_name)}行")
print()

# === 策略2：填充缺失值 ===
print("=== 策略2：填充缺失值 ===")

# 创建数据副本用于填充
df_filled = df_students.copy()

# 用固定值填充
df_filled['姓名'] = df_filled['姓名'].fillna('未知学生')
print("姓名列填充后：")
print(df_filled['姓名'])
print()

# 用均值填充数值列
age_mean = df_filled['年龄'].mean()
df_filled['年龄'] = df_filled['年龄'].fillna(age_mean)
print(f"年龄列用均值({age_mean:.1f})填充后：")
print(df_filled['年龄'])
print()

# 用众数填充分类列
gender_mode = df_filled['性别'].mode()[0]  # 获取众数
df_filled['性别'] = df_filled['性别'].fillna(gender_mode)
print(f"性别列用众数({gender_mode})填充后：")
print(df_filled['性别'])
print()

# 用前一个值填充（前向填充）
df_filled['数学'] = df_filled['数学'].fillna(method='ffill')
print("数学成绩前向填充后：")
print(df_filled['数学'])
print()

# 用后一个值填充（后向填充）
df_filled['语文'] = df_filled['语文'].fillna(method='bfill')
print("语文成绩后向填充后：")
print(df_filled['语文'])
print()

# === 策略3：插值填充 ===
print("=== 策略3：插值填充 ===")

# 线性插值
df_interpolated = df_students.copy()
df_interpolated['英语'] = df_interpolated['英语'].interpolate()
print("英语成绩线性插值后：")
print(df_interpolated['英语'])
print()

# 显示最终清洗结果
print("=== 最终清洗结果 ===")
print(df_filled)
```

### 15.3.2 重复数据处理：去除冗余原料

```python
# === 创建包含重复数据的示例 ===
duplicate_data = {
    '订单ID': ['O001', 'O002', 'O003', 'O002', 'O004', 'O003', 'O005'],
    '客户名': ['张三', '李四', '王五', '李四', '赵六', '王五', '钱七'],
    '产品': ['笔记本', '手机', '平板', '手机', '耳机', '平板', '鼠标'],
    '数量': [1, 2, 1, 2, 3, 1, 1],
    '金额': [5000, 3000, 2000, 3000, 200, 2000, 50]
}

df_orders = pd.DataFrame(duplicate_data)
print("📦 订单数据（含重复）：")
print(df_orders)
print()

# === 重复数据检测 ===
print("🔍 重复数据检测：")

# 检查完全重复的行
duplicated_rows = df_orders.duplicated()
print("完全重复的行：")
print(duplicated_rows)
print(f"重复行数量：{duplicated_rows.sum()}")
print()

# 查看重复的行
print("重复的行内容：")
print(df_orders[duplicated_rows])
print()

# 基于特定列检查重复
duplicated_orders = df_orders.duplicated(subset=['订单ID'])
print("基于订单ID的重复：")
print(duplicated_orders)
print(f"重复订单数量：{duplicated_orders.sum()}")
print()

# === 重复数据处理 ===
print("=== 重复数据处理 ===")

# 删除完全重复的行（保留第一个）
df_no_duplicates = df_orders.drop_duplicates()
print("删除完全重复行后：")
print(df_no_duplicates)
print()

# 基于特定列删除重复（保留最后一个）
df_unique_orders = df_orders.drop_duplicates(subset=['订单ID'], keep='last')
print("基于订单ID去重（保留最后一个）：")
print(df_unique_orders)
print()

# 标记重复数据而不删除
df_orders['是否重复'] = df_orders.duplicated(subset=['订单ID'])
print("标记重复数据：")
print(df_orders)
```

### 15.3.3 数据类型转换：规格标准化

```python
# === 数据类型问题示例 ===
messy_data = {
    '员工ID': ['E001', 'E002', 'E003', 'E004'],
    '入职日期': ['2020-01-15', '2019/07/22', '2021.03.10', '20220815'],
    '薪资': ['15000', '18000.5', '12,000', '¥20000'],
    '年龄': ['28', '32.0', '25', '29'],
    '是否在职': ['是', 'True', '1', 'yes']
}

df_messy = pd.DataFrame(messy_data)
print("📊 原始数据（类型混乱）：")
print(df_messy)
print()
print("数据类型：")
print(df_messy.dtypes)
print()

# === 日期类型转换 ===
print("=== 日期类型转换 ===")

def clean_date(date_str):
    """清洗日期字符串"""
    # 替换各种分隔符为标准格式
    date_str = str(date_str).replace('/', '-').replace('.', '-')
    
    # 处理没有分隔符的日期
    if len(date_str) == 8 and date_str.isdigit():
        return f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}"
    
    return date_str

# 清洗日期数据
df_messy['入职日期_清洗'] = df_messy['入职日期'].apply(clean_date)
df_messy['入职日期_标准'] = pd.to_datetime(df_messy['入职日期_清洗'])

print("日期转换结果：")
print(df_messy[['入职日期', '入职日期_清洗', '入职日期_标准']])
print()

# === 数值类型转换 ===
print("=== 数值类型转换 ===")

def clean_salary(salary_str):
    """清洗薪资数据"""
    # 移除货币符号、逗号等
    salary_str = str(salary_str).replace('¥', '').replace(',', '').replace('$', '')
    return float(salary_str)

# 清洗薪资数据
df_messy['薪资_数值'] = df_messy['薪资'].apply(clean_salary)
df_messy['年龄_整数'] = df_messy['年龄'].astype(int)

print("数值转换结果：")
print(df_messy[['薪资', '薪资_数值', '年龄', '年龄_整数']])
print()

# === 布尔类型转换 ===
print("=== 布尔类型转换 ===")

def clean_boolean(bool_str):
    """清洗布尔数据"""
    bool_str = str(bool_str).lower()
    if bool_str in ['是', 'true', '1', 'yes', 'y']:
        return True
    elif bool_str in ['否', 'false', '0', 'no', 'n']:
        return False
    else:
        return None

# 清洗布尔数据
df_messy['在职状态'] = df_messy['是否在职'].apply(clean_boolean)

print("布尔转换结果：")
print(df_messy[['是否在职', '在职状态']])
print()

print("最终清洗后的数据类型：")
print(df_messy[['入职日期_标准', '薪资_数值', '年龄_整数', '在职状态']].dtypes)
```

### 15.3.4 异常值检测与处理

```python
# === 创建包含异常值的数据 ===
np.random.seed(42)  # 设置随机种子确保结果可重复

# 正常的销售数据
normal_sales = np.random.normal(10000, 2000, 100)  # 均值10000，标准差2000
# 添加一些异常值
outliers = [50000, -5000, 80000, 100000]
all_sales = np.concatenate([normal_sales, outliers])

sales_data = {
    '日期': pd.date_range('2025-01-01', periods=len(all_sales), freq='D'),
    '销售额': all_sales,
    '销售员': [f'员工{i%10+1}' for i in range(len(all_sales))]
}

df_sales = pd.DataFrame(sales_data)
print("📈 销售数据（含异常值）：")
print(df_sales.tail(10))  # 显示最后10行，包含异常值
print()

# === 异常值检测方法 ===
print("=== 异常值检测方法 ===")

# 方法1：3σ原则（三倍标准差）
mean_sales = df_sales['销售额'].mean()
std_sales = df_sales['销售额'].std()
upper_bound = mean_sales + 3 * std_sales
lower_bound = mean_sales - 3 * std_sales

print(f"3σ原则边界：")
print(f"  均值: {mean_sales:.2f}")
print(f"  标准差: {std_sales:.2f}")
print(f"  上界: {upper_bound:.2f}")
print(f"  下界: {lower_bound:.2f}")

outliers_3sigma = df_sales[
    (df_sales['销售额'] > upper_bound) | 
    (df_sales['销售额'] < lower_bound)
]
print(f"3σ原则检测到 {len(outliers_3sigma)} 个异常值")
print(outliers_3sigma)
print()

# 方法2：IQR（四分位距）方法
Q1 = df_sales['销售额'].quantile(0.25)
Q3 = df_sales['销售额'].quantile(0.75)
IQR = Q3 - Q1
lower_fence = Q1 - 1.5 * IQR
upper_fence = Q3 + 1.5 * IQR

print(f"IQR方法边界：")
print(f"  Q1: {Q1:.2f}")
print(f"  Q3: {Q3:.2f}")
print(f"  IQR: {IQR:.2f}")
print(f"  下栅栏: {lower_fence:.2f}")
print(f"  上栅栏: {upper_fence:.2f}")

outliers_iqr = df_sales[
    (df_sales['销售额'] > upper_fence) | 
    (df_sales['销售额'] < lower_fence)
]
print(f"IQR方法检测到 {len(outliers_iqr)} 个异常值")
print(outliers_iqr)
print()

# === 异常值处理策略 ===
print("=== 异常值处理策略 ===")

# 策略1：删除异常值
df_no_outliers = df_sales[
    (df_sales['销售额'] >= lower_fence) & 
    (df_sales['销售额'] <= upper_fence)
]
print(f"删除异常值后：{len(df_no_outliers)}行（原始：{len(df_sales)}行）")

# 策略2：用边界值替换异常值
df_capped = df_sales.copy()
df_capped['销售额'] = df_capped['销售额'].clip(lower=lower_fence, upper=upper_fence)
print("异常值替换为边界值后的统计：")
print(df_capped['销售额'].describe())
print()

# 策略3：用中位数替换异常值
df_median_filled = df_sales.copy()
median_sales = df_sales['销售额'].median()
is_outlier = (df_sales['销售额'] > upper_fence) | (df_sales['销售额'] < lower_fence)
df_median_filled.loc[is_outlier, '销售额'] = median_sales
print(f"用中位数({median_sales:.2f})替换异常值后的统计：")
print(df_median_filled['销售额'].describe())
```

### 🎯 实践项目：智能数据清洗工具

让我们创建一个综合的数据清洗工具：

```python
class SmartDataCleaner:
    """智能数据清洗工具
    
    模拟数据工厂的全自动质检流水线：
    - 自动检测数据质量问题
    - 提供多种清洗策略选择
    - 生成详细的清洗报告
    - 保留清洗历史记录
    """
    
    def __init__(self):
        self.original_data = None
        self.cleaned_data = None
        self.cleaning_log = []
        
    def load_data(self, df):
        """加载待清洗的数据"""
        self.original_data = df.copy()
        self.cleaned_data = df.copy()
        self.cleaning_log = []
        print(f"✅ 数据加载成功，共 {len(df)} 行 {len(df.columns)} 列")
        
    def analyze_data_quality(self):
        """分析数据质量"""
        if self.cleaned_data is None:
            print("❌ 请先加载数据")
            return
            
        print("\n🔍 数据质量分析报告")
        print("=" * 50)
        
        # 基本信息
        print(f"数据形状: {self.cleaned_data.shape}")
        print(f"内存使用: {self.cleaned_data.memory_usage(deep=True).sum() / 1024:.2f} KB")
        print()
        
        # 缺失值分析
        missing_info = self.cleaned_data.isnull().sum()
        if missing_info.sum() > 0:
            print("⚠️ 缺失值情况:")
            for col, count in missing_info.items():
                if count > 0:
                    ratio = count / len(self.cleaned_data) * 100
                    print(f"  {col}: {count}个 ({ratio:.1f}%)")
        else:
            print("✅ 无缺失值")
        print()
        
        # 重复值分析
        duplicate_count = self.cleaned_data.duplicated().sum()
        if duplicate_count > 0:
            print(f"⚠️ 发现 {duplicate_count} 行重复数据")
        else:
            print("✅ 无重复数据")
        print()
        
        # 数据类型分析
        print("📊 数据类型分布:")
        type_counts = self.cleaned_data.dtypes.value_counts()
        for dtype, count in type_counts.items():
            print(f"  {dtype}: {count}列")
        print()
        
        # 异常值分析（仅针对数值列）
        numeric_cols = self.cleaned_data.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            print("📈 数值列异常值检测（IQR方法）:")
            for col in numeric_cols:
                Q1 = self.cleaned_data[col].quantile(0.25)
                Q3 = self.cleaned_data[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_fence = Q1 - 1.5 * IQR
                upper_fence = Q3 + 1.5 * IQR
                
                outliers = self.cleaned_data[
                    (self.cleaned_data[col] < lower_fence) | 
                    (self.cleaned_data[col] > upper_fence)
                ]
                
                if len(outliers) > 0:
                    print(f"  {col}: {len(outliers)}个异常值")
                else:
                    print(f"  {col}: 无异常值")
        print()
        
    def handle_missing_values(self, strategy='auto', columns=None):
        """处理缺失值"""
        if columns is None:
            columns = self.cleaned_data.columns
            
        for col in columns:
            if self.cleaned_data[col].isnull().sum() == 0:
                continue
                
            if strategy == 'auto':
                # 自动选择策略
                if self.cleaned_data[col].dtype in ['int64', 'float64']:
                    # 数值列用中位数填充
                    fill_value = self.cleaned_data[col].median()
                    self.cleaned_data[col].fillna(fill_value, inplace=True)
                    self.cleaning_log.append(f"列 '{col}' 缺失值用中位数 {fill_value:.2f} 填充")
                else:
                    # 分类列用众数填充
                    mode_values = self.cleaned_data[col].mode()
                    if len(mode_values) > 0:
                        fill_value = mode_values[0]
                        self.cleaned_data[col].fillna(fill_value, inplace=True)
                        self.cleaning_log.append(f"列 '{col}' 缺失值用众数 '{fill_value}' 填充")
                        
            elif strategy == 'drop':
                # 删除包含缺失值的行
                before_count = len(self.cleaned_data)
                self.cleaned_data.dropna(subset=[col], inplace=True)
                after_count = len(self.cleaned_data)
                self.cleaning_log.append(f"删除列 '{col}' 的缺失值，减少 {before_count - after_count} 行")
                
        print(f"✅ 缺失值处理完成（策略：{strategy}）")
        
    def handle_duplicates(self, subset=None, keep='first'):
        """处理重复值"""
        before_count = len(self.cleaned_data)
        self.cleaned_data.drop_duplicates(subset=subset, keep=keep, inplace=True)
        after_count = len(self.cleaned_data)
        
        removed_count = before_count - after_count
        if removed_count > 0:
            self.cleaning_log.append(f"删除 {removed_count} 行重复数据")
            print(f"✅ 删除了 {removed_count} 行重复数据")
        else:
            print("✅ 未发现重复数据")
            
    def handle_outliers(self, columns=None, method='iqr', action='cap'):
        """处理异常值"""
        if columns is None:
            columns = self.cleaned_data.select_dtypes(include=[np.number]).columns
            
        for col in columns:
            if method == 'iqr':
                Q1 = self.cleaned_data[col].quantile(0.25)
                Q3 = self.cleaned_data[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
            else:  # 3sigma
                mean_val = self.cleaned_data[col].mean()
                std_val = self.cleaned_data[col].std()
                lower_bound = mean_val - 3 * std_val
                upper_bound = mean_val + 3 * std_val
                
            # 检测异常值
            outliers_mask = (
                (self.cleaned_data[col] < lower_bound) | 
                (self.cleaned_data[col] > upper_bound)
            )
            outliers_count = outliers_mask.sum()
            
            if outliers_count > 0:
                if action == 'cap':
                    # 用边界值替换
                    self.cleaned_data[col] = self.cleaned_data[col].clip(
                        lower=lower_bound, upper=upper_bound
                    )
                    self.cleaning_log.append(
                        f"列 '{col}' 的 {outliers_count} 个异常值被边界值替换"
                    )
                elif action == 'remove':
                    # 删除异常值
                    self.cleaned_data = self.cleaned_data[~outliers_mask]
                    self.cleaning_log.append(
                        f"删除列 '{col}' 的 {outliers_count} 个异常值"
                    )
                    
        print(f"✅ 异常值处理完成（方法：{method}，操作：{action}）")
        
    def convert_data_types(self, type_mapping):
        """转换数据类型"""
        for col, target_type in type_mapping.items():
            if col in self.cleaned_data.columns:
                try:
                    if target_type == 'datetime':
                        self.cleaned_data[col] = pd.to_datetime(self.cleaned_data[col])
                    else:
                        self.cleaned_data[col] = self.cleaned_data[col].astype(target_type)
                    self.cleaning_log.append(f"列 '{col}' 转换为 {target_type} 类型")
                except Exception as e:
                    print(f"❌ 列 '{col}' 类型转换失败: {e}")
                    
        print("✅ 数据类型转换完成")
        
    def generate_cleaning_report(self):
        """生成清洗报告"""
        print("\n📋 数据清洗报告")
        print("=" * 50)
        
        print(f"原始数据: {self.original_data.shape}")
        print(f"清洗后数据: {self.cleaned_data.shape}")
        
        if len(self.cleaning_log) > 0:
            print("\n🔧 执行的清洗操作:")
            for i, operation in enumerate(self.cleaning_log, 1):
                print(f"  {i}. {operation}")
        else:
            print("\n✅ 数据无需清洗")
            
        print("\n📊 清洗前后对比:")
        print("缺失值数量:")
        print(f"  清洗前: {self.original_data.isnull().sum().sum()}")
        print(f"  清洗后: {self.cleaned_data.isnull().sum().sum()}")
        
        print("重复行数量:")
        print(f"  清洗前: {self.original_data.duplicated().sum()}")
        print(f"  清洗后: {self.cleaned_data.duplicated().sum()}")
        
    def get_cleaned_data(self):
        """获取清洗后的数据"""
        return self.cleaned_data.copy()

# === 使用示例 ===
if __name__ == "__main__":
    # 创建测试数据
    test_data = {
        '员工ID': ['E001', 'E002', 'E003', 'E002', 'E004', 'E005'],  # 包含重复
        '姓名': ['张三', '李四', None, '李四', '赵六', '钱七'],        # 包含缺失值
        '年龄': [25, 30, 28, 30, 150, 22],                         # 包含异常值
        '薪资': [5000, 8000, 6000, 8000, None, 7000],             # 包含缺失值
        '入职日期': ['2020-01-01', '2019-06-15', '2021-03-10', '2019-06-15', '2022-08-20', '2023-01-15']
    }
    
    df_test = pd.DataFrame(test_data)
    
    # 创建清洗工具
    cleaner = SmartDataCleaner()
    
    print("🏭 智能数据清洗工具启动")
    print("=" * 50)
    
    # 加载数据
    cleaner.load_data(df_test)
    
    # 分析数据质量
    cleaner.analyze_data_quality()
    
    # 执行清洗操作
    cleaner.handle_missing_values(strategy='auto')
    cleaner.handle_duplicates()
    cleaner.handle_outliers(method='iqr', action='cap')
    
    # 类型转换
    type_mapping = {
        '入职日期': 'datetime',
        '年龄': 'int',
        '薪资': 'float'
    }
    cleaner.convert_data_types(type_mapping)
    
    # 生成报告
    cleaner.generate_cleaning_report()
    
    # 获取清洗后的数据
    cleaned_df = cleaner.get_cleaned_data()
    print("\n📊 最终清洗结果:")
    print(cleaned_df)
    print("\n数据类型:")
    print(cleaned_df.dtypes)
    
    print("\n🎉 数据清洗完成！")
```

### 💡 核心概念总结

1. **缺失值处理**：
   - 检测：`df.isnull()`, `df.info()`
   - 删除：`df.dropna()`
   - 填充：`df.fillna()`, `df.interpolate()`

2. **重复数据处理**：
   - 检测：`df.duplicated()`
   - 删除：`df.drop_duplicates()`

3. **数据类型转换**：
   - 基本转换：`df.astype()`
   - 日期转换：`pd.to_datetime()`
   - 数值转换：`pd.to_numeric()`

4. **异常值处理**：
   - 3σ原则：均值±3倍标准差
   - IQR方法：Q1-1.5×IQR 到 Q3+1.5×IQR
   - 处理策略：删除、替换、标记

通过"质检部门"的比喻，我们掌握了数据清洗的核心技能。接下来，让我们学习如何对清洗后的数据进行深入分析和可视化展示。

---

## 15.4 数据分析与可视化

### 📊 数据工厂的分析报告部门

经过质检部门的严格把关，我们的数据已经变得干净、标准。现在轮到分析报告部门登场了！这个部门负责：
- **统计分析**：从数据中提取关键指标和趋势
- **分组聚合**：按不同维度汇总数据
- **透视分析**：多角度审视数据
- **可视化展示**：制作图表让数据"说话"

### 15.4.1 描述性统计分析：数据的基本画像

```python
# === 创建综合分析数据集 ===
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文显示和图表样式
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")

# 创建电商销售数据
np.random.seed(42)
n_records = 1000

sales_data = {
    '订单ID': [f'ORD{i:05d}' for i in range(1, n_records + 1)],
    '客户ID': [f'C{np.random.randint(1, 201):04d}' for _ in range(n_records)],
    '产品类别': np.random.choice(['电子产品', '服装', '家居', '图书', '运动'], n_records, 
                              p=[0.3, 0.25, 0.2, 0.15, 0.1]),
    '销售额': np.random.lognormal(mean=7, sigma=0.8, size=n_records).round(2),
    '数量': np.random.poisson(lam=2, size=n_records) + 1,
    '销售日期': pd.date_range('2023-01-01', periods=n_records, freq='H'),
    '销售渠道': np.random.choice(['线上', '线下'], n_records, p=[0.7, 0.3]),
    '客户年龄': np.random.normal(35, 12, n_records).astype(int).clip(18, 70),
    '客户性别': np.random.choice(['男', '女'], n_records, p=[0.45, 0.55])
}

df_sales = pd.DataFrame(sales_data)
df_sales['月份'] = df_sales['销售日期'].dt.month
df_sales['星期'] = df_sales['销售日期'].dt.day_name()

print("📊 电商销售数据概览：")
print(df_sales.head())
print()
print(f"数据集大小：{df_sales.shape}")
print()

# === 基础描述性统计 ===
print("=== 基础描述性统计 ===")

# 数值列统计
print("📈 数值列描述性统计：")
numeric_stats = df_sales[['销售额', '数量', '客户年龄']].describe()
print(numeric_stats)
print()

# 分类列统计
print("📝 分类列统计：")
categorical_cols = ['产品类别', '销售渠道', '客户性别']
for col in categorical_cols:
    print(f"\n{col} 分布：")
    value_counts = df_sales[col].value_counts()
    percentages = df_sales[col].value_counts(normalize=True) * 100
    
    for value, count in value_counts.items():
        percentage = percentages[value]
        print(f"  {value}: {count}个 ({percentage:.1f}%)")

# === 高级统计分析 ===
print("\n=== 高级统计分析 ===")

# 销售额分析
print("💰 销售额深度分析：")
sales_amount = df_sales['销售额']

print(f"  总销售额: ¥{sales_amount.sum():,.2f}")
print(f"  平均销售额: ¥{sales_amount.mean():.2f}")
print(f"  中位数销售额: ¥{sales_amount.median():.2f}")
print(f"  销售额标准差: ¥{sales_amount.std():.2f}")
print(f"  销售额变异系数: {sales_amount.std() / sales_amount.mean():.3f}")

# 分位数分析
quantiles = [0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99]
print(f"\n  销售额分位数分析：")
for q in quantiles:
    value = sales_amount.quantile(q)
    print(f"    {q*100:.0f}%分位数: ¥{value:.2f}")

# 偏度和峰度
from scipy import stats
skewness = stats.skew(sales_amount)
kurtosis = stats.kurtosis(sales_amount)
print(f"\n  偏度 (Skewness): {skewness:.3f}")
print(f"  峰度 (Kurtosis): {kurtosis:.3f}")
```

### 15.4.2 分组聚合操作：多维度数据汇总

```python
# === 分组聚合分析 ===
print("\n=== 分组聚合分析 ===")

# 按产品类别分组
print("📦 按产品类别分组分析：")
category_analysis = df_sales.groupby('产品类别').agg({
    '销售额': ['sum', 'mean', 'count'],
    '数量': ['sum', 'mean'],
    '客户年龄': 'mean'
}).round(2)

# 扁平化列名
category_analysis.columns = ['_'.join(col).strip() for col in category_analysis.columns]
print(category_analysis)
print()

# 按销售渠道分组
print("🛒 按销售渠道分组分析：")
channel_analysis = df_sales.groupby('销售渠道').agg({
    '销售额': ['sum', 'mean', 'std'],
    '数量': 'sum',
    '客户年龄': 'mean'
}).round(2)

channel_analysis.columns = ['_'.join(col).strip() for col in channel_analysis.columns]
print(channel_analysis)
print()

# 多层分组
print("🎯 多维度分组分析（产品类别 × 销售渠道）：")
multi_group = df_sales.groupby(['产品类别', '销售渠道']).agg({
    '销售额': ['sum', 'mean'],
    '数量': 'sum'
}).round(2)

print(multi_group)
print()

# 时间序列分组
print("📅 按月份分组分析：")
monthly_analysis = df_sales.groupby('月份').agg({
    '销售额': ['sum', 'mean'],
    '数量': 'sum',
    '订单ID': 'count'  # 订单数量
}).round(2)

monthly_analysis.columns = ['_'.join(col).strip() for col in monthly_analysis.columns]
print(monthly_analysis)
print()

# 自定义聚合函数
print("🔧 自定义聚合分析：")
def coefficient_of_variation(x):
    """变异系数"""
    return x.std() / x.mean() if x.mean() != 0 else 0

def sales_range(x):
    """销售额范围"""
    return x.max() - x.min()

custom_agg = df_sales.groupby('产品类别')['销售额'].agg([
    ('平均值', 'mean'),
    ('标准差', 'std'),
    ('变异系数', coefficient_of_variation),
    ('销售范围', sales_range),
    ('最大值', 'max'),
    ('最小值', 'min')
]).round(3)

print(custom_agg)
```

### 15.4.3 数据透视表：多角度数据审视

```python
# === 数据透视表分析 ===
print("\n=== 数据透视表分析 ===")

# 基础透视表
print("📊 基础透视表（产品类别 vs 销售渠道）：")
pivot_basic = pd.pivot_table(
    df_sales,
    values='销售额',
    index='产品类别',
    columns='销售渠道',
    aggfunc='sum',
    fill_value=0,
    margins=True  # 添加总计行和列
)
print(pivot_basic)
print()

# 多值透视表
print("📈 多指标透视表：")
pivot_multi = pd.pivot_table(
    df_sales,
    values=['销售额', '数量'],
    index='产品类别',
    columns='销售渠道',
    aggfunc={'销售额': 'sum', '数量': 'mean'},
    fill_value=0
)
print(pivot_multi)
print()

# 多层索引透视表
print("🎯 多层索引透视表（按月份和性别）：")
pivot_complex = pd.pivot_table(
    df_sales,
    values='销售额',
    index=['产品类别', '客户性别'],
    columns='月份',
    aggfunc='mean',
    fill_value=0
)
print(pivot_complex.head(10))
print()

# 透视表百分比分析
print("📊 透视表百分比分析：")
pivot_pct = pd.pivot_table(
    df_sales,
    values='销售额',
    index='产品类别',
    columns='销售渠道',
    aggfunc='sum',
    fill_value=0
)

# 计算行百分比（每个产品类别在不同渠道的占比）
pivot_pct_row = pivot_pct.div(pivot_pct.sum(axis=1), axis=0) * 100
print("各产品类别在不同渠道的销售占比（%）：")
print(pivot_pct_row.round(1))
print()

# 计算列百分比（每个渠道中不同产品的占比）
pivot_pct_col = pivot_pct.div(pivot_pct.sum(axis=0), axis=1) * 100
print("各渠道中不同产品类别的销售占比（%）：")
print(pivot_pct_col.round(1))
```

### 15.4.4 数据可视化：让数据说话

```python
# === 数据可视化 ===
print("\n=== 数据可视化展示 ===")

# 创建图表画布
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('电商销售数据分析仪表板', fontsize=16, fontweight='bold')

# 1. 销售额分布直方图
axes[0, 0].hist(df_sales['销售额'], bins=50, alpha=0.7, color='skyblue', edgecolor='black')
axes[0, 0].set_title('销售额分布')
axes[0, 0].set_xlabel('销售额 (¥)')
axes[0, 0].set_ylabel('频次')
axes[0, 0].axvline(df_sales['销售额'].mean(), color='red', linestyle='--', 
                   label=f'平均值: ¥{df_sales["销售额"].mean():.2f}')
axes[0, 0].legend()

# 2. 产品类别销售额柱状图
category_sales = df_sales.groupby('产品类别')['销售额'].sum().sort_values(ascending=False)
bars = axes[0, 1].bar(range(len(category_sales)), category_sales.values, 
                      color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])
axes[0, 1].set_title('各产品类别销售额')
axes[0, 1].set_xlabel('产品类别')
axes[0, 1].set_ylabel('销售额 (¥)')
axes[0, 1].set_xticks(range(len(category_sales)))
axes[0, 1].set_xticklabels(category_sales.index, rotation=45)

# 在柱子上添加数值标签
for i, bar in enumerate(bars):
    height = bar.get_height()
    axes[0, 1].text(bar.get_x() + bar.get_width()/2., height,
                    f'¥{height:,.0f}', ha='center', va='bottom', fontsize=9)

# 3. 销售渠道饼图
channel_counts = df_sales['销售渠道'].value_counts()
colors = ['#FF9999', '#66B2FF']
wedges, texts, autotexts = axes[0, 2].pie(channel_counts.values, labels=channel_counts.index, 
                                          autopct='%1.1f%%', colors=colors, startangle=90)
axes[0, 2].set_title('销售渠道分布')

# 4. 月度销售趋势线图
monthly_sales = df_sales.groupby('月份')['销售额'].sum()
axes[1, 0].plot(monthly_sales.index, monthly_sales.values, marker='o', linewidth=2, 
                markersize=8, color='#2E86AB')
axes[1, 0].set_title('月度销售趋势')
axes[1, 0].set_xlabel('月份')
axes[1, 0].set_ylabel('销售额 (¥)')
axes[1, 0].grid(True, alpha=0.3)

# 添加数值标签
for x, y in zip(monthly_sales.index, monthly_sales.values):
    axes[1, 0].annotate(f'¥{y:,.0f}', (x, y), textcoords="offset points", 
                        xytext=(0,10), ha='center', fontsize=8)

# 5. 客户年龄与销售额散点图
scatter = axes[1, 1].scatter(df_sales['客户年龄'], df_sales['销售额'], 
                            alpha=0.6, c=df_sales['销售额'], cmap='viridis', s=30)
axes[1, 1].set_title('客户年龄 vs 销售额')
axes[1, 1].set_xlabel('客户年龄')
axes[1, 1].set_ylabel('销售额 (¥)')

# 添加趋势线
z = np.polyfit(df_sales['客户年龄'], df_sales['销售额'], 1)
p = np.poly1d(z)
axes[1, 1].plot(df_sales['客户年龄'].sort_values(), 
                p(df_sales['客户年龄'].sort_values()), "r--", alpha=0.8)

# 6. 热力图：产品类别 vs 客户性别
heatmap_data = pd.pivot_table(df_sales, values='销售额', 
                             index='产品类别', columns='客户性别', 
                             aggfunc='mean', fill_value=0)
im = axes[1, 2].imshow(heatmap_data.values, cmap='YlOrRd', aspect='auto')
axes[1, 2].set_title('产品类别 vs 客户性别热力图')
axes[1, 2].set_xticks(range(len(heatmap_data.columns)))
axes[1, 2].set_xticklabels(heatmap_data.columns)
axes[1, 2].set_yticks(range(len(heatmap_data.index)))
axes[1, 2].set_yticklabels(heatmap_data.index)

# 在热力图上添加数值
for i in range(len(heatmap_data.index)):
    for j in range(len(heatmap_data.columns)):
        text = axes[1, 2].text(j, i, f'{heatmap_data.iloc[i, j]:.0f}',
                              ha="center", va="center", color="black", fontsize=8)

plt.tight_layout()
plt.show()

print("📊 可视化图表已生成！")
print()

# === 相关性分析 ===
print("=== 相关性分析 ===")
correlation_data = df_sales[['销售额', '数量', '客户年龄']].corr()
print("数值变量相关性矩阵：")
print(correlation_data.round(3))
print()

# 解释相关性
print("📈 相关性解读：")
for i in range(len(correlation_data.columns)):
    for j in range(i+1, len(correlation_data.columns)):
        var1 = correlation_data.columns[i]
        var2 = correlation_data.columns[j]
        corr_value = correlation_data.iloc[i, j]
        
        if abs(corr_value) > 0.7:
            strength = "强"
        elif abs(corr_value) > 0.3:
            strength = "中等"
        else:
            strength = "弱"
            
        direction = "正" if corr_value > 0 else "负"
        print(f"  {var1} 与 {var2}: {direction}相关，强度{strength} (r={corr_value:.3f})")
```

### 🎯 实践项目：销售数据分析仪表板

让我们创建一个完整的销售数据分析仪表板：

```python
class SalesAnalyticsDashboard:
    """销售数据分析仪表板
    
    模拟数据工厂的智能分析报告系统：
    - 全方位数据分析：描述性统计、趋势分析、关联分析
    - 多维度数据透视：时间、产品、客户、渠道等维度
    - 智能可视化：自动选择最佳图表类型
    - 洞察报告生成：自动发现数据中的关键洞察
    """
    
    def __init__(self, data):
        self.data = data.copy()
        self.insights = []
        
    def basic_analysis(self):
        """基础数据分析"""
        print("📊 基础数据分析报告")
        print("=" * 50)
        
        # 数据概览
        print(f"数据集大小: {self.data.shape[0]} 行 × {self.data.shape[1]} 列")
        print(f"时间范围: {self.data['销售日期'].min()} 至 {self.data['销售日期'].max()}")
        print()
        
        # 关键指标
        total_sales = self.data['销售额'].sum()
        total_orders = len(self.data)
        avg_order_value = self.data['销售额'].mean()
        unique_customers = self.data['客户ID'].nunique()
        
        print("🎯 关键业务指标:")
        print(f"  总销售额: ¥{total_sales:,.2f}")
        print(f"  总订单数: {total_orders:,}")
        print(f"  平均订单价值: ¥{avg_order_value:.2f}")
        print(f"  独立客户数: {unique_customers:,}")
        print(f"  客户平均订单数: {total_orders / unique_customers:.1f}")
        print()
        
        # 产品分析
        print("📦 产品类别分析:")
        category_stats = self.data.groupby('产品类别').agg({
            '销售额': ['sum', 'mean'],
            '订单ID': 'count'
        }).round(2)
        
        category_stats.columns = ['总销售额', '平均销售额', '订单数']
        category_stats['销售额占比'] = (category_stats['总销售额'] / total_sales * 100).round(1)
        category_stats = category_stats.sort_values('总销售额', ascending=False)
        
        print(category_stats)
        print()
        
        # 自动洞察发现
        self._discover_insights()
        
    def time_series_analysis(self):
        """时间序列分析"""
        print("📅 时间序列分析")
        print("=" * 50)
        
        # 按日期聚合
        daily_sales = self.data.groupby(self.data['销售日期'].dt.date).agg({
            '销售额': 'sum',
            '订单ID': 'count'
        }).reset_index()
        daily_sales.columns = ['日期', '销售额', '订单数']
        
        print("📈 每日销售趋势:")
        print(f"  最高日销售额: ¥{daily_sales['销售额'].max():,.2f}")
        print(f"  最低日销售额: ¥{daily_sales['销售额'].min():,.2f}")
        print(f"  平均日销售额: ¥{daily_sales['销售额'].mean():.2f}")
        print(f"  销售额标准差: ¥{daily_sales['销售额'].std():.2f}")
        print()
        
        # 按月份分析
        monthly_stats = self.data.groupby('月份').agg({
            '销售额': ['sum', 'mean'],
            '订单ID': 'count'
        }).round(2)
        monthly_stats.columns = ['月销售额', '平均订单价值', '订单数']
        
        print("📊 月度销售分析:")
        print(monthly_stats)
        print()
        
        # 增长率分析
        monthly_growth = monthly_stats['月销售额'].pct_change() * 100
        print("📈 月度增长率:")
        for month, growth in monthly_growth.items():
            if not pd.isna(growth):
                direction = "📈" if growth > 0 else "📉"
                print(f"  {month}月: {direction} {growth:.1f}%")
        print()
        
    def customer_analysis(self):
        """客户分析"""
        print("👥 客户行为分析")
        print("=" * 50)
        
        # 客户价值分析
        customer_stats = self.data.groupby('客户ID').agg({
            '销售额': ['sum', 'mean', 'count'],
            '销售日期': ['min', 'max']
        })
        customer_stats.columns = ['总消费', '平均订单价值', '订单数', '首次购买', '最后购买']
        
        # 客户生命周期（天数）
        customer_stats['生命周期天数'] = (
            customer_stats['最后购买'] - customer_stats['首次购买']
        ).dt.days + 1
        
        print("🏆 客户价值分析:")
        print(f"  平均客户总消费: ¥{customer_stats['总消费'].mean():.2f}")
        print(f"  平均客户订单数: {customer_stats['订单数'].mean():.1f}")
        print(f"  平均客户生命周期: {customer_stats['生命周期天数'].mean():.1f} 天")
        print()
        
        # 客户分层
        # 使用RFM模型的简化版本
        customer_stats['消费等级'] = pd.qcut(customer_stats['总消费'], 
                                        q=3, labels=['低价值', '中价值', '高价值'])
        customer_stats['频次等级'] = pd.qcut(customer_stats['订单数'], 
                                        q=3, labels=['低频', '中频', '高频'])
        
        # 客户分层统计
        customer_segments = customer_stats.groupby(['消费等级', '频次等级']).size().unstack(fill_value=0)
        print("📊 客户分层矩阵:")
        print(customer_segments)
        print()
        
        # 性别和年龄分析
        demo_analysis = self.data.groupby(['客户性别', pd.cut(self.data['客户年龄'], 
                                                           bins=[0, 25, 35, 45, 55, 100], 
                                                           labels=['18-25', '26-35', '36-45', '46-55', '55+'])]).agg({
            '销售额': ['sum', 'mean'],
            '订单ID': 'count'
        }).round(2)
        
        print("👫 客户人口统计分析:")
        print(demo_analysis)
        print()
        
    def product_performance_analysis(self):
        """产品绩效分析"""
        print("📦 产品绩效分析")
        print("=" * 50)
        
        # 产品类别绩效
        category_performance = self.data.groupby('产品类别').agg({
            '销售额': ['sum', 'mean', 'std'],
            '数量': ['sum', 'mean'],
            '订单ID': 'count'
        }).round(2)
        
        category_performance.columns = ['总销售额', '平均销售额', '销售额标准差', 
                                      '总销量', '平均销量', '订单数']
        
        # 计算变异系数
        category_performance['变异系数'] = (
            category_performance['销售额标准差'] / category_performance['平均销售额']
        ).round(3)
        
        # 按总销售额排序
        category_performance = category_performance.sort_values('总销售额', ascending=False)
        
        print("🏆 产品类别绩效排行:")
        print(category_performance)
        print()
        
        # 渠道效果分析
        channel_analysis = self.data.groupby(['产品类别', '销售渠道']).agg({
            '销售额': 'sum',
            '订单ID': 'count'
        }).unstack(fill_value=0)
        
        print("🛒 渠道销售效果分析:")
        print(channel_analysis)
        print()
        
    def generate_insights_report(self):
        """生成洞察报告"""
        print("💡 数据洞察报告")
        print("=" * 50)
        
        if self.insights:
            for i, insight in enumerate(self.insights, 1):
                print(f"{i}. {insight}")
        else:
            print("未发现特殊洞察")
        print()
        
    def _discover_insights(self):
        """自动发现数据洞察"""
        # 洞察1：最受欢迎的产品类别
        top_category = self.data.groupby('产品类别')['销售额'].sum().idxmax()
        top_category_sales = self.data.groupby('产品类别')['销售额'].sum().max()
        total_sales = self.data['销售额'].sum()
        top_category_pct = (top_category_sales / total_sales) * 100
        
        self.insights.append(
            f"📊 {top_category}是最受欢迎的产品类别，占总销售额的{top_category_pct:.1f}%"
        )
        
        # 洞察2：销售渠道效果
        channel_comparison = self.data.groupby('销售渠道')['销售额'].mean()
        if channel_comparison['线上'] > channel_comparison['线下']:
            better_channel = '线上'
            diff_pct = ((channel_comparison['线上'] - channel_comparison['线下']) / 
                       channel_comparison['线下']) * 100
        else:
            better_channel = '线下'
            diff_pct = ((channel_comparison['线下'] - channel_comparison['线上']) / 
                       channel_comparison['线上']) * 100
            
        self.insights.append(
            f"🛒 {better_channel}渠道的平均订单价值比另一渠道高{diff_pct:.1f}%"
        )
        
        # 洞察3：客户年龄与消费关系
        age_corr = self.data['客户年龄'].corr(self.data['销售额'])
        if abs(age_corr) > 0.1:
            direction = "正相关" if age_corr > 0 else "负相关"
            self.insights.append(
                f"👥 客户年龄与消费金额呈{direction}关系 (相关系数: {age_corr:.3f})"
            )
            
        # 洞察4：性别消费差异
        gender_avg = self.data.groupby('客户性别')['销售额'].mean()
        if abs(gender_avg['男'] - gender_avg['女']) > 50:
            higher_gender = '男性' if gender_avg['男'] > gender_avg['女'] else '女性'
            diff_amount = abs(gender_avg['男'] - gender_avg['女'])
            self.insights.append(
                f"👫 {higher_gender}客户的平均消费比另一性别高¥{diff_amount:.2f}"
            )

# === 使用示例 ===
if __name__ == "__main__":
    print("🏭 销售数据分析仪表板启动")
    print("=" * 60)
    
    # 创建分析仪表板
    dashboard = SalesAnalyticsDashboard(df_sales)
    
    # 执行全面分析
    dashboard.basic_analysis()
    dashboard.time_series_analysis()
    dashboard.customer_analysis()
    dashboard.product_performance_analysis()
    dashboard.generate_insights_report()
    
    print("🎉 销售数据分析完成！")
```

### 💡 核心概念总结

1. **描述性统计**：
   - 基本统计：`df.describe()`, `df.mean()`, `df.std()`
   - 分位数分析：`df.quantile()`
   - 分布特征：偏度、峰度

2. **分组聚合**：
   - 单维分组：`df.groupby('column')`
   - 多维分组：`df.groupby(['col1', 'col2'])`
   - 聚合函数：`sum`, `mean`, `count`, `std`

3. **数据透视**：
   - 透视表：`pd.pivot_table()`
   - 交叉表：`pd.crosstab()`
   - 多层索引处理

4. **数据可视化**：
   - 直方图：分布分析
   - 柱状图：分类比较
   - 线图：趋势分析
   - 散点图：关系分析
   - 热力图：相关性展示

通过"分析报告部门"的比喻，我们掌握了Pandas数据分析的核心技能。数据工厂的完整流程——从原料入库到质检清洗，再到深度分析和可视化报告——现在你都能熟练操作了！

---

## 📚 本章总结

### 🎯 核心知识回顾

通过本章的学习，我们完整地体验了"数据工厂"的运作流程：

1. **原料仓库管理（数据结构）**
   - Series：一维数据的标签数组
   - DataFrame：二维数据的标签表格
   - Index：高效的标签索引系统

2. **进货出货系统（数据输入输出）**
   - 多格式数据读取：CSV、Excel、JSON、数据库
   - 灵活的数据导出：支持多种格式和参数配置
   - 网络数据获取：API接口和在线数据源

3. **质检部门（数据清洗）**
   - 缺失值处理：检测、删除、填充、插值
   - 重复数据处理：识别和去重策略
   - 数据类型转换：标准化数据格式
   - 异常值处理：检测方法和处理策略

4. **分析报告部门（数据分析与可视化）**
   - 描述性统计：全面的数据画像
   - 分组聚合：多维度数据汇总
   - 数据透视：灵活的数据重组
   - 可视化展示：让数据说话

### 📊 技能掌握评估

| 技能领域 | 掌握程度 | 核心方法 | 实际应用 |
|---------|---------|----------|----------|
| 数据结构 | ⭐⭐⭐⭐⭐ | Series, DataFrame, Index | 学生成绩管理系统 |
| 数据IO | ⭐⭐⭐⭐⭐ | read_csv, to_excel, read_sql | 多源数据整合分析器 |
| 数据清洗 | ⭐⭐⭐⭐⭐ | dropna, fillna, drop_duplicates | 智能数据清洗工具 |
| 数据分析 | ⭐⭐⭐⭐⭐ | groupby, pivot_table, describe | 销售数据分析仪表板 |
| 数据可视化 | ⭐⭐⭐⭐⭐ | matplotlib, seaborn | 多维度图表展示 |

### 🚀 学习成果展示

通过本章学习，你已经具备了：

1. **企业级数据处理能力**
   - 处理真实世界的"脏"数据
   - 设计完整的数据处理流程
   - 构建可重用的数据分析工具

2. **数据分析思维**
   - 从业务角度理解数据
   - 多维度审视数据问题
   - 自动发现数据洞察

3. **项目实战经验**
   - 完成了5个完整的企业级项目
   - 编写了1800+行高质量代码
   - 掌握了数据分析的完整工作流

### 🎯 进阶学习方向

1. **高级数据分析**
   - 时间序列分析
   - 统计假设检验
   - 机器学习预处理

2. **大数据处理**
   - Dask并行计算
   - 数据库优化
   - 内存管理技巧

3. **可视化进阶**
   - 交互式图表（Plotly）
   - 地理数据可视化
   - 动态仪表板

4. **业务应用**
   - 用户行为分析
   - 财务数据分析
   - 运营数据分析

### 💼 职场应用价值

掌握Pandas数据分析技能，你可以胜任：

- **数据分析师**：处理业务数据，生成分析报告
- **业务分析师**：支持商业决策，优化业务流程  
- **产品经理**：分析用户行为，指导产品迭代
- **运营专员**：监控运营指标，优化运营策略
- **研究员**：处理研究数据，验证研究假设

### 🌟 最佳实践总结

1. **数据处理原则**
   - 始终保留原始数据副本
   - 记录每步数据处理操作
   - 验证数据处理结果的合理性

2. **代码组织建议**
   - 使用类封装复杂的数据处理逻辑
   - 编写可重用的工具函数
   - 添加详细的注释和文档

3. **性能优化技巧**
   - 合理选择数据类型
   - 避免不必要的数据复制
   - 使用向量化操作替代循环

4. **可视化设计原则**
   - 选择合适的图表类型
   - 保持图表简洁清晰
   - 添加必要的标签和说明

恭喜你！你已经成功掌握了Pandas数据分析的核心技能。这些技能将成为你数据科学之路的重要基石，为后续学习机器学习和人工智能技术打下坚实基础。

记住：数据分析不仅是技术活，更是一门艺术。继续实践，不断探索，你将在数据的海洋中发现更多宝藏！🎉 