#!/usr/bin/env python3
"""
Markdown to Jupyter Notebook Converter for Python教程

功能:
1. 解析Markdown文件结构
2. 提取代码块和练习题
3. 生成nbgrader格式的Jupyter Notebook
4. 设置自动评分点和测试用例
"""

import re
import json
import nbformat
from pathlib import Path
from typing import List, Dict, Tuple
import yaml
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell


class MarkdownToNotebook:
    """Markdown文件转换为Jupyter Notebook的转换器"""
    
    def __init__(self, source_dir: str, output_dir: str):
        self.source_dir = Path(source_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # 正则表达式模式
        self.code_pattern = re.compile(r'```python\n(.*?)\n```', re.DOTALL)
        self.exercise_pattern = re.compile(r'### 练习题?\s*(\d+)[:：]\s*(.*?)\n(.*?)(?=###|$)', re.DOTALL)
        self.project_pattern = re.compile(r'## 综合项目[:：]\s*(.*?)\n(.*?)(?=##|$)', re.DOTALL)
        
    def convert_all_chapters(self):
        """转换所有章节"""
        chapter_files = sorted(self.source_dir.glob("第*章-*.md"))
        
        for chapter_file in chapter_files:
            print(f"转换章节: {chapter_file.name}")
            self.convert_chapter(chapter_file)
            
    def convert_chapter(self, chapter_file: Path):
        """转换单个章节"""
        # 读取Markdown内容
        content = chapter_file.read_text(encoding='utf-8')
        
        # 解析章节信息
        chapter_info = self.parse_chapter_info(chapter_file.name, content)
        
        # 创建输出目录
        chapter_dir = self.output_dir / f"chapter-{chapter_info['number']:02d}"
        chapter_dir.mkdir(parents=True, exist_ok=True)
        
        # 生成主要内容notebook
        self.create_content_notebook(content, chapter_info, chapter_dir)
        
        # 生成练习题notebook
        self.create_exercises_notebook(content, chapter_info, chapter_dir)
        
        # 生成项目案例notebook
        self.create_project_notebook(content, chapter_info, chapter_dir)
        
        # 生成配置文件
        self.create_nbgrader_config(chapter_info, chapter_dir)
        
    def parse_chapter_info(self, filename: str, content: str) -> Dict:
        """解析章节信息"""
        # 从文件名提取章节号
        chapter_match = re.search(r'第(\d+)章-(.+)\.md', filename)
        if not chapter_match:
            raise ValueError(f"无法解析章节信息: {filename}")
            
        chapter_num = int(chapter_match.group(1))
        chapter_title = chapter_match.group(2)
        
        # 提取学习目标
        objectives_match = re.search(r'## 学习目标\n(.*?)(?=##|$)', content, re.DOTALL)
        objectives = []
        if objectives_match:
            objectives = [obj.strip('- ').strip() 
                         for obj in objectives_match.group(1).split('\n') 
                         if obj.strip().startswith('-')]
        
        return {
            'number': chapter_num,
            'title': chapter_title,
            'filename': filename,
            'objectives': objectives
        }
        
    def create_content_notebook(self, content: str, chapter_info: Dict, output_dir: Path):
        """创建主要内容的notebook"""
        nb = new_notebook()
        
        # 添加标题
        title_cell = new_markdown_cell(source=f"# 第{chapter_info['number']}章 {chapter_info['title']}")
        nb.cells.append(title_cell)
        
        # 添加学习目标
        if chapter_info['objectives']:
            objectives_text = "## 学习目标\n\n" + "\n".join([f"- {obj}" for obj in chapter_info['objectives']])
            nb.cells.append(new_markdown_cell(source=objectives_text))
        
        # 分析内容结构
        sections = self.split_content_by_sections(content)
        
        for section in sections:
            # 添加markdown内容
            if section['markdown']:
                nb.cells.append(new_markdown_cell(source=section['markdown']))
            
            # 添加代码示例
            for code_block in section['code_blocks']:
                # 添加说明文本
                if code_block['description']:
                    nb.cells.append(new_markdown_cell(source=f"**示例**: {code_block['description']}"))
                
                # 添加代码单元格
                code_cell = new_code_cell(source=code_block['code'])
                nb.cells.append(code_cell)
        
        # 保存notebook
        output_file = output_dir / f"{chapter_info['number']:02d}-content.ipynb"
        with open(output_file, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
            
    def create_exercises_notebook(self, content: str, chapter_info: Dict, output_dir: Path):
        """创建练习题notebook"""
        exercises = self.extract_exercises(content)
        if not exercises:
            return
            
        nb = new_notebook()
        
        # 添加标题
        title_cell = new_markdown_cell(source=f"# 第{chapter_info['number']}章 练习题")
        nb.cells.append(title_cell)
        
        for i, exercise in enumerate(exercises, 1):
            # 练习题标题和描述
            exercise_title = f"## 练习 {i}: {exercise['title']}"
            exercise_desc = f"{exercise_title}\n\n{exercise['description']}"
            nb.cells.append(new_markdown_cell(source=exercise_desc))
            
            # 学生答题区域
            student_cell = new_code_cell(source=exercise['template'])
            # 添加nbgrader标记
            student_cell.metadata = {
                "nbgrader": {
                    "grade": False,
                    "grade_id": f"exercise_{i}_answer",
                    "locked": False,
                    "schema_version": 3,
                    "solution": True,
                    "task": False
                }
            }
            nb.cells.append(student_cell)
            
            # 测试用例
            if exercise['tests']:
                test_cell = new_code_cell(source=exercise['tests'])
                test_cell.metadata = {
                    "nbgrader": {
                        "grade": True,
                        "grade_id": f"exercise_{i}_test",
                        "locked": True,
                        "points": exercise['points'],
                        "schema_version": 3,
                        "solution": False,
                        "task": False
                    }
                }
                nb.cells.append(test_cell)
        
        # 保存notebook
        output_file = output_dir / f"{chapter_info['number']:02d}-exercises.ipynb"
        with open(output_file, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
            
    def create_project_notebook(self, content: str, chapter_info: Dict, output_dir: Path):
        """创建综合项目notebook"""
        projects = self.extract_projects(content)
        if not projects:
            return
            
        nb = new_notebook()
        
        # 添加标题
        title_cell = new_markdown_cell(source=f"# 第{chapter_info['number']}章 综合项目")
        nb.cells.append(title_cell)
        
        for project in projects:
            # 项目标题和描述
            project_desc = f"## {project['title']}\n\n{project['description']}"
            nb.cells.append(new_markdown_cell(source=project_desc))
            
            # 需求分析
            if project['requirements']:
                req_text = "### 需求分析\n\n" + "\n".join([f"- {req}" for req in project['requirements']])
                nb.cells.append(new_markdown_cell(source=req_text))
            
            # 代码实现区域
            impl_cell = new_code_cell(source=project['template'])
            impl_cell.metadata = {
                "nbgrader": {
                    "grade": False,
                    "grade_id": f"project_implementation",
                    "locked": False,
                    "schema_version": 3,
                    "solution": True,
                    "task": False
                }
            }
            nb.cells.append(impl_cell)
            
            # 测试区域
            if project['tests']:
                test_cell = new_code_cell(source=project['tests'])
                test_cell.metadata = {
                    "nbgrader": {
                        "grade": True,
                        "grade_id": f"project_test",
                        "locked": True,
                        "points": project['points'],
                        "schema_version": 3,
                        "solution": False,
                        "task": False
                    }
                }
                nb.cells.append(test_cell)
        
        # 保存notebook
        output_file = output_dir / f"{chapter_info['number']:02d}-project.ipynb"
        with open(output_file, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
            
    def split_content_by_sections(self, content: str) -> List[Dict]:
        """按章节分割内容"""
        sections = []
        
        # 按二级标题分割
        section_pattern = re.compile(r'^## (.+)$', re.MULTILINE)
        section_matches = list(section_pattern.finditer(content))
        
        for i, match in enumerate(section_matches):
            start_pos = match.start()
            end_pos = section_matches[i + 1].start() if i + 1 < len(section_matches) else len(content)
            
            section_content = content[start_pos:end_pos]
            section_title = match.group(1)
            
            # 提取代码块
            code_blocks = self.extract_code_blocks(section_content)
            
            # 移除代码块后的markdown内容
            markdown_content = section_content
            for code_block in code_blocks:
                markdown_content = markdown_content.replace(f"```python\n{code_block['code']}\n```", "")
            
            sections.append({
                'title': section_title,
                'markdown': markdown_content.strip(),
                'code_blocks': code_blocks
            })
        
        return sections
        
    def extract_code_blocks(self, content: str) -> List[Dict]:
        """提取代码块"""
        code_blocks = []
        
        for match in self.code_pattern.finditer(content):
            code = match.group(1).strip()
            
            # 查找代码块前的描述
            description = ""
            before_code = content[:match.start()]
            desc_match = re.search(r'(?:示例|例子|代码)[:：]?\s*(.+?)(?=\n|$)', before_code.split('\n')[-3:][0] if before_code.split('\n') else "")
            if desc_match:
                description = desc_match.group(1).strip()
            
            code_blocks.append({
                'code': code,
                'description': description
            })
        
        return code_blocks
        
    def extract_exercises(self, content: str) -> List[Dict]:
        """提取练习题"""
        exercises = []
        
        for match in self.exercise_pattern.finditer(content):
            exercise_num = match.group(1)
            exercise_title = match.group(2).strip()
            exercise_content = match.group(3).strip()
            
            # 解析练习题内容
            exercise_info = self.parse_exercise_content(exercise_content)
            
            exercises.append({
                'number': exercise_num,
                'title': exercise_title,
                'description': exercise_info['description'],
                'template': exercise_info['template'],  
                'tests': exercise_info['tests'],
                'points': exercise_info['points']
            })
        
        return exercises
        
    def parse_exercise_content(self, content: str) -> Dict:
        """解析练习题内容"""
        lines = content.split('\n')
        
        description = []
        template = "# 请在这里编写你的代码\n"
        tests = ""
        points = 5  # 默认分值
        
        in_requirements = False
        in_template = False
        in_tests = False
        
        for line in lines:
            line = line.strip()
            
            if line.startswith('**要求') or line.startswith('要求'):
                in_requirements = True
                continue
            elif line.startswith('**提示') or line.startswith('提示'):
                in_requirements = False
                continue
            elif '```python' in line:
                in_template = True
                continue
            elif '```' in line and in_template:
                in_template = False
                continue
            elif in_template:
                if not template.endswith("# 请在这里编写你的代码\n"):
                    template += line + '\n'
            elif in_requirements:
                description.append(line)
        
        # 生成基础测试用例
        if '输入' in content and '输出' in content:
            tests = self.generate_basic_test(content)
        
        return {
            'description': '\n'.join(description),
            'template': template,
            'tests': tests,
            'points': points
        }
        
    def generate_basic_test(self, content: str) -> str:
        """生成基础测试用例"""
        # 这里可以实现更复杂的测试用例生成逻辑
        return """
# 基础测试用例
# 请根据具体练习要求修改

try:
    # 测试代码执行
    assert True, "代码执行成功"
    print("✓ 测试通过")
except Exception as e:
    print(f"✗ 测试失败: {e}")
    raise
"""
        
    def extract_projects(self, content: str) -> List[Dict]:
        """提取综合项目"""
        projects = []
        
        for match in self.project_pattern.finditer(content):
            project_title = match.group(1).strip()
            project_content = match.group(2).strip()
            
            # 解析项目内容
            project_info = self.parse_project_content(project_content)
            
            projects.append({
                'title': project_title,
                'description': project_info['description'],
                'requirements': project_info['requirements'],
                'template': project_info['template'],
                'tests': project_info['tests'],
                'points': project_info['points']
            })
        
        return projects
        
    def parse_project_content(self, content: str) -> Dict:
        """解析项目内容"""
        # 类似于练习题解析，但更复杂
        return {
            'description': content[:200] + "..." if len(content) > 200 else content,
            'requirements': [],
            'template': "# 综合项目代码实现\n# 请根据需求完成以下功能\n\n",
            'tests': "# 项目测试用例\nprint('项目完成')",
            'points': 20  # 项目分值更高
        }
        
    def create_nbgrader_config(self, chapter_info: Dict, output_dir: Path):
        """创建nbgrader配置文件"""
        config = {
            'course_id': 'python-fundamentals',
            'assignment_id': f"chapter-{chapter_info['number']:02d}",
            'student_id': '*',
            'release_date': '2025-02-01 00:00:00',
            'due_date': '2025-02-08 23:59:59'
        }
        
        config_file = output_dir / 'nbgrader_config.yaml'
        with open(config_file, 'w', encoding='utf-8') as f:
            yaml.dump(config, f, default_flow_style=False, allow_unicode=True)


def main():
    """主函数"""
    import os
    
    source_dir = os.environ.get('SOURCE_DIR', './source')
    output_dir = os.environ.get('OUTPUT_DIR', './output')
    
    print(f"开始转换: {source_dir} -> {output_dir}")
    
    converter = MarkdownToNotebook(source_dir, output_dir)
    converter.convert_all_chapters()
    
    print("转换完成！")


if __name__ == "__main__":
    main() 