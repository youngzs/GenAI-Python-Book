from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import subprocess
import tempfile
import os
import sys
import io
import contextlib
import traceback
import re
import json
import markdown
from datetime import datetime

app = Flask(__name__)
CORS(app)

# 配置
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'py', 'txt', 'md'}
MAX_EXECUTION_TIME = 5  # 最大执行时间（秒）

# 确保上传目录存在
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

class CodeExecutor:
    """安全的Python代码执行器"""
    
    FORBIDDEN_IMPORTS = [
        'os', 'sys', 'subprocess', 'shutil', 'glob', 'importlib',
        'pickle', 'eval', 'exec', 'compile', '__import__',
        'open', 'file', 'input', 'raw_input'
    ]
    
    ALLOWED_IMPORTS = [
        'math', 'random', 'datetime', 'json', 'string', 're',
        'collections', 'itertools', 'functools', 'operator'
    ]
    
    @staticmethod
    def check_code_safety(code):
        """检查代码安全性"""
        # 检查禁用的导入
        for forbidden in CodeExecutor.FORBIDDEN_IMPORTS:
            if f'import {forbidden}' in code or f'from {forbidden}' in code:
                return False, f"不允许导入模块: {forbidden}"
        
        # 检查危险函数调用
        dangerous_patterns = [
            r'open\s*\(',
            r'file\s*\(',
            r'exec\s*\(',
            r'eval\s*\(',
            r'__import__',
            r'input\s*\(',
            r'raw_input\s*\('
        ]
        
        for pattern in dangerous_patterns:
            if re.search(pattern, code):
                return False, f"包含不安全的操作: {pattern}"
        
        return True, "代码安全检查通过"
    
    @staticmethod
    def execute_code(code, input_data=""):
        """安全执行Python代码"""
        is_safe, message = CodeExecutor.check_code_safety(code)
        if not is_safe:
            return False, message, ""
        
        # 重定向标准输出
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        old_stdin = sys.stdin
        
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()
        stdin_input = io.StringIO(input_data)
        
        try:
            sys.stdout = stdout_capture
            sys.stderr = stderr_capture
            sys.stdin = stdin_input
            
            # 创建受限的全局环境
            safe_globals = {
                '__builtins__': {
                    'print': print,
                    'len': len,
                    'str': str,
                    'int': int,
                    'float': float,
                    'bool': bool,
                    'list': list,
                    'dict': dict,
                    'tuple': tuple,
                    'set': set,
                    'range': range,
                    'enumerate': enumerate,
                    'zip': zip,
                    'map': map,
                    'filter': filter,
                    'sorted': sorted,
                    'sum': sum,
                    'max': max,
                    'min': min,
                    'abs': abs,
                    'round': round,
                    'type': type,
                    'isinstance': isinstance,
                    'hasattr': hasattr,
                    'getattr': getattr,
                    'setattr': setattr,
                    'ValueError': ValueError,
                    'TypeError': TypeError,
                    'IndexError': IndexError,
                    'KeyError': KeyError,
                }
            }
            
            # 添加允许的模块
            import math
            import random
            import datetime
            import json as json_module
            import string
            import re as re_module
            
            safe_globals['math'] = math
            safe_globals['random'] = random
            safe_globals['datetime'] = datetime
            safe_globals['json'] = json_module
            safe_globals['string'] = string
            safe_globals['re'] = re_module
            
            # 执行代码
            exec(code, safe_globals)
            
            return True, "执行成功", stdout_capture.getvalue()
            
        except Exception as e:
            error_msg = f"执行错误: {str(e)}\n{traceback.format_exc()}"
            return False, error_msg, stderr_capture.getvalue()
        
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr
            sys.stdin = old_stdin

class ContentManager:
    """内容管理器"""
    
    @staticmethod
    def load_chapter_content(chapter_id):
        """加载章节内容"""
        try:
            file_path = f"第一册-Python基础与核心技术/第{chapter_id}章*.md"
            # 这里应该实际读取markdown文件
            # 为演示返回示例内容
            return {
                'title': f'第{chapter_id}章内容',
                'content': f'这是第{chapter_id}章的内容...',
                'examples': [],
                'exercises': []
            }
        except Exception as e:
            return {'error': str(e)}
    
    @staticmethod
    def get_exercise_by_id(exercise_id):
        """根据ID获取练习题"""
        exercises_db = {
            'chapter1_exercise1': {
                'title': '个人信息输出程序',
                'description': '编写一个程序，要求用户输入姓名、年龄和爱好，然后格式化输出个人信息。',
                'difficulty': '基础',
                'template': '''name = input("请输入您的姓名：")
age = input("请输入您的年龄：")
hobby = input("请输入您的爱好：")

# TODO: 使用f-string格式化输出
print(f"个人信息卡")
# 请完成剩余代码...''',
                'test_cases': [
                    {'input': '张三\n20\n编程', 'expected_output': '个人信息卡\n==================\n姓名：张三\n年龄：20岁\n爱好：编程'}
                ]
            }
        }
        
        return exercises_db.get(exercise_id, {})

class AIAssistant:
    """AI助手，提供代码分析和建议"""
    
    @staticmethod
    def analyze_code(code):
        """分析代码质量"""
        suggestions = []
        score = 100
        
        # 检查代码长度
        if len(code.strip()) < 10:
            suggestions.append("代码太短，建议添加更多功能")
            score -= 20
        
        # 检查注释
        comment_lines = [line for line in code.split('\n') if line.strip().startsWith('#')]
        if len(comment_lines) == 0:
            suggestions.append("建议添加注释来解释代码功能")
            score -= 10
        
        # 检查变量命名
        if re.search(r'\b[a-z]\b', code):
            suggestions.append("建议使用更有意义的变量名")
            score -= 5
        
        # 检查print语句
        if 'print(' in code:
            suggestions.append("很好！使用了print语句进行输出")
        else:
            suggestions.append("考虑添加print语句来显示结果")
            score -= 10
        
        return {
            'score': max(score, 0),
            'suggestions': suggestions,
            'overall': '很好' if score >= 80 else '良好' if score >= 60 else '需要改进'
        }
    
    @staticmethod
    def get_hint(exercise_id):
        """获取练习提示"""
        hints_db = {
            'chapter1_exercise1': [
                "使用f-string格式化字符串：f'文本{变量}'",
                "记住使用input()函数获取用户输入",
                "可以使用多个print()语句来格式化输出",
                "注意输出格式要整齐美观"
            ]
        }
        
        hints = hints_db.get(exercise_id, ["继续努力，你能做到的！"])
        return random.choice(hints)

# 路由定义
@app.route('/')
def index():
    """主页"""
    return send_from_directory('.', 'index.html')

@app.route('/api/run-python', methods=['POST'])
def run_python():
    """执行Python代码"""
    try:
        data = request.get_json()
        code = data.get('code', '')
        input_data = data.get('input', '')
        
        if not code.strip():
            return jsonify({
                'success': False,
                'error': '代码不能为空',
                'output': ''
            })
        
        # 执行代码
        success, message, output = CodeExecutor.execute_code(code, input_data)
        
        return jsonify({
            'success': success,
            'message': message,
            'output': output,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'服务器错误: {str(e)}',
            'output': ''
        })

@app.route('/api/evaluate-code', methods=['POST'])
def evaluate_code():
    """评估代码质量"""
    try:
        data = request.get_json()
        code = data.get('code', '')
        exercise_id = data.get('exercise_id', '')
        
        if not code.strip():
            return jsonify({
                'success': False,
                'error': '代码不能为空'
            })
        
        # 先执行代码检查是否能运行
        success, message, output = CodeExecutor.execute_code(code)
        
        # AI分析代码
        analysis = AIAssistant.analyze_code(code)
        
        # 如果有练习ID，检查是否满足要求
        exercise_check = {}
        if exercise_id:
            exercise = ContentManager.get_exercise_by_id(exercise_id)
            if exercise:
                # 这里可以添加更复杂的测试逻辑
                exercise_check = {
                    'exercise_title': exercise.get('title', ''),
                    'passed': success,
                    'feedback': '代码能够正常运行' if success else '代码执行出错'
                }
        
        return jsonify({
            'success': True,
            'execution': {
                'success': success,
                'output': output,
                'message': message
            },
            'analysis': analysis,
            'exercise_check': exercise_check,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'评估错误: {str(e)}'
        })

@app.route('/api/get-hint', methods=['POST'])
def get_hint():
    """获取学习提示"""
    try:
        data = request.get_json()
        exercise_id = data.get('exercise_id', '')
        
        hint = AIAssistant.get_hint(exercise_id)
        
        return jsonify({
            'success': True,
            'hint': hint,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'获取提示失败: {str(e)}'
        })

@app.route('/api/chapter/<int:chapter_id>')
def get_chapter(chapter_id):
    """获取章节内容"""
    try:
        content = ContentManager.load_chapter_content(chapter_id)
        return jsonify({
            'success': True,
            'chapter_id': chapter_id,
            'content': content
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'加载章节失败: {str(e)}'
        })

@app.route('/api/exercise/<exercise_id>')
def get_exercise(exercise_id):
    """获取练习题详情"""
    try:
        exercise = ContentManager.get_exercise_by_id(exercise_id)
        if not exercise:
            return jsonify({
                'success': False,
                'error': '练习题不存在'
            })
        
        return jsonify({
            'success': True,
            'exercise': exercise
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'获取练习题失败: {str(e)}'
        })

@app.route('/api/progress', methods=['GET', 'POST'])
def handle_progress():
    """处理学习进度"""
    if request.method == 'GET':
        # 获取进度（这里应该从数据库读取）
        return jsonify({
            'success': True,
            'progress': {
                'completed_chapters': [],
                'total_chapters': 18,
                'current_chapter': 1,
                'exercises_completed': 0,
                'total_exercises': 72
            }
        })
    
    elif request.method == 'POST':
        # 保存进度
        try:
            data = request.get_json()
            # 这里应该保存到数据库
            return jsonify({
                'success': True,
                'message': '进度保存成功'
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': f'保存进度失败: {str(e)}'
            })

@app.route('/api/examples')
def get_code_examples():
    """获取代码示例"""
    examples = [
        {
            'title': 'Hello World',
            'code': '''print("Hello, Python!")
print("欢迎来到编程世界！")

name = "Python学习者"
print(f"你好，{name}！")''',
            'description': '最基础的Python程序'
        },
        {
            'title': '变量和数据类型',
            'code': '''# 不同类型的变量
age = 25
height = 175.5
name = "张三"
is_student = True

# 输出变量信息
print(f"姓名：{name}")
print(f"年龄：{age}")
print(f"身高：{height}cm")
print(f"学生身份：{is_student}")
print(f"变量类型：{type(name)}")''',
            'description': '演示Python的基本数据类型'
        },
        {
            'title': '简单计算器',
            'code': '''# 简单计算器
num1 = 10
num2 = 3

print("=== 计算器结果 ===")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2:.2f}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")''',
            'description': '演示Python的数学运算'
        },
        {
            'title': '条件判断',
            'code': '''# 条件判断示例
score = 85

print(f"学生成绩：{score}")

if score >= 90:
    grade = "优秀"
    print("🎉 恭喜你获得优秀成绩！")
elif score >= 80:
    grade = "良好" 
    print("👍 成绩良好，继续努力！")
elif score >= 60:
    grade = "及格"
    print("✓ 成绩及格，还有提升空间")
else:
    grade = "不及格"
    print("❌ 成绩不及格，需要加油了")

print(f"评级：{grade}")''',
            'description': '演示条件判断语句'
        },
        {
            'title': '循环结构',
            'code': '''# 循环结构示例
print("=== for循环 ===")
for i in range(5):
    print(f"这是第{i+1}次循环")

print("\n=== while循环 ===")
count = 0
while count < 3:
    print(f"计数：{count}")
    count += 1

print("\n=== 列表循环 ===")
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"我喜欢吃{fruit}")

print("\n=== 九九乘法表 ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}×{j}={i*j}", end="  ")
    print()''',
            'description': '演示循环结构的使用'
        }
    ]
    
    return jsonify({
        'success': True,
        'examples': examples
    })

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({
        'success': False,
        'error': '请求的资源不存在'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'error': '服务器内部错误'
    }), 500

if __name__ == '__main__':
    print("🚀 Python教学平台启动中...")
    print("📚 课程内容：第一册 Python基础与核心技术 (18章)")
    print("💻 在线编程：支持实时代码执行和评估")
    print("🤖 AI助手：提供智能提示和代码分析")
    print("🌐 访问地址：http://localhost:5000")
    print("-" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000) 