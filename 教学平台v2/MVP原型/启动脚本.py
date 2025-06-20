#!/usr/bin/env python3
"""
Python智能体开发教学平台v2.0 - 快速启动脚本

基于nbgrader + JupyterHub的教学平台演示
"""

import os
import sys
import subprocess
import time
from pathlib import Path
import argparse
import yaml


class PlatformManager:
    """教学平台管理器"""
    
    def __init__(self, work_dir: str = None):
        self.work_dir = Path(work_dir) if work_dir else Path.cwd() / "教学平台v2"
        self.work_dir.mkdir(parents=True, exist_ok=True)
        
    def setup_environment(self):
        """设置环境"""
        print("🔧 设置开发环境...")
        
        # 创建目录结构
        dirs = [
            'jupyterhub/config',
            'content',
            'data/hub',
            'nginx/conf.d',
            'content-manager',
            'postgres'
        ]
        
        for dir_path in dirs:
            (self.work_dir / dir_path).mkdir(parents=True, exist_ok=True)
        
        # 创建基础配置文件
        self.create_jupyterhub_config()
        self.create_nginx_config()
        self.create_requirements()
        
        print("✅ 环境设置完成")
        
    def create_jupyterhub_config(self):
        """创建JupyterHub配置"""
        config_content = """
# JupyterHub配置文件
import os

# 基础配置
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000

# 数据库配置
c.JupyterHub.db_url = 'postgresql://jupyterhub:educationhub123@postgres:5432/jupyterhub'

# 认证配置 - 使用本地用户认证
c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'
c.DummyAuthenticator.password = "python123"

# 管理员用户
c.Authenticator.admin_users = {'admin', 'teacher'}

# Spawner配置
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = 'jupyter/datascience-notebook:latest'
c.DockerSpawner.remove = True
c.DockerSpawner.network_name = 'python-edu-network'

# 容器配置
c.DockerSpawner.volumes = {
    '/srv/content': '/home/jovyan/course-content',
    '/data/hub/{username}': '/home/jovyan/work'
}

# nbgrader配置
c.JupyterHub.services = [
    {
        'name': 'nbgrader-formgrader',
        'url': 'http://127.0.0.1:9999',
        'command': [
            'python', '-m', 'nbgrader', 'formgrader',
            '--port=9999',
            '--no-browser'
        ],
        'environment': {
            'NBGRADER_CONFIG_FILE': '/srv/jupyterhub/config/nbgrader_config.py'
        }
    }
]

# 日志配置
c.JupyterHub.log_level = 'INFO'
"""
        
        config_file = self.work_dir / 'jupyterhub/config/jupyterhub_config.py'
        config_file.write_text(config_content, encoding='utf-8')
        
    def create_nginx_config(self):
        """创建Nginx配置"""
        nginx_content = """
upstream jupyterhub {
    server jupyterhub:8000;
}

server {
    listen 80;
    server_name localhost;
    
    location / {
        proxy_pass http://jupyterhub;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # WebSocket支持
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        
        # 超时设置
        proxy_read_timeout 300s;
        proxy_connect_timeout 10s;
    }
    
    # 静态资源
    location /static/ {
        alias /usr/share/nginx/html/static/;
        expires 1d;
        add_header Cache-Control "public, immutable";
    }
}
"""
        
        nginx_file = self.work_dir / 'nginx/conf.d/default.conf'
        nginx_file.write_text(nginx_content, encoding='utf-8')
        
    def create_requirements(self):
        """创建依赖文件"""
        requirements = """
# JupyterHub和相关组件
jupyterhub==4.0.2
dockerspawner==12.1.0
psycopg2-binary==2.9.7

# nbgrader
nbgrader==0.9.1

# 内容转换工具
nbformat==5.9.2
pyyaml==6.0.1
markdown==3.5.1

# 数据分析工具（用于教学内容）
numpy==1.24.3
pandas==2.0.3
matplotlib==3.7.2
seaborn==0.12.2
scikit-learn==1.3.0

# Web框架（用于扩展功能）
fastapi==0.103.1
uvicorn==0.23.2
"""
        
        req_file = self.work_dir / 'requirements.txt'
        req_file.write_text(requirements, encoding='utf-8')
        
    def create_docker_compose(self):
        """创建Docker Compose文件"""
        compose_content = """
version: '3.8'

services:
  jupyterhub:
    build:
      context: ./jupyterhub
      dockerfile: Dockerfile
    container_name: python-edu-hub
    ports:
      - "8000:8000"
    volumes:
      - ./jupyterhub/config:/srv/jupyterhub/config
      - ./data/hub:/data
      - ./content:/srv/content
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      - POSTGRES_PASSWORD=educationhub123
    depends_on:
      - postgres
    networks:
      - python-edu-network

  postgres:
    image: postgres:14-alpine
    container_name: python-edu-db
    environment:
      - POSTGRES_DB=jupyterhub
      - POSTGRES_USER=jupyterhub
      - POSTGRES_PASSWORD=educationhub123
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - python-edu-network

  nginx:
    image: nginx:alpine
    container_name: python-edu-proxy
    ports:
      - "80:80"
    volumes:
      - ./nginx/conf.d:/etc/nginx/conf.d
      - ./static:/usr/share/nginx/html/static
    depends_on:
      - jupyterhub
    networks:
      - python-edu-network

volumes:
  postgres_data:

networks:
  python-edu-network:
    driver: bridge
"""
        
        compose_file = self.work_dir / 'docker-compose.yml'
        compose_file.write_text(compose_content, encoding='utf-8')
        
    def create_jupyterhub_dockerfile(self):
        """创建JupyterHub Dockerfile"""
        dockerfile_content = """
FROM jupyterhub/jupyterhub:4.0.2

USER root

# 安装依赖
RUN apt-get update && \\
    apt-get install -y --no-install-recommends \\
        postgresql-client \\
        build-essential \\
        python3-dev && \\
    rm -rf /var/lib/apt/lists/*

# 复制requirements并安装Python包
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# 复制配置文件
COPY config/ /srv/jupyterhub/config/

# 创建用户和设置权限
RUN useradd -m -s /bin/bash jovyan && \\
    mkdir -p /srv/content && \\
    chown -R jovyan:jovyan /srv/content

# 设置工作目录
WORKDIR /srv/jupyterhub

# 启动命令
CMD ["jupyterhub", "-f", "/srv/jupyterhub/config/jupyterhub_config.py"]
"""
        
        dockerfile = self.work_dir / 'jupyterhub/Dockerfile'
        dockerfile.write_text(dockerfile_content, encoding='utf-8')
        
        # 复制requirements.txt到jupyterhub目录
        req_source = self.work_dir / 'requirements.txt'
        req_target = self.work_dir / 'jupyterhub/requirements.txt'
        req_target.write_text(req_source.read_text(encoding='utf-8'), encoding='utf-8')
        
    def convert_content(self):
        """转换教学内容"""
        print("📚 转换教学内容...")
        
        # 检查源文件是否存在
        source_dir = Path("第一册-Python基础与核心技术")
        if not source_dir.exists():
            print(f"⚠️  源文件目录不存在: {source_dir}")
            print("请确保第一册的Markdown文件在当前目录下")
            return False
        
        # 创建简化的转换脚本
        converter_script = """
#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

# 简化演示：直接复制几个示例文件
source_dir = Path("第一册-Python基础与核心技术")
target_dir = Path("教学平台v2/content")

# 创建示例课程结构
examples = {
    "chapter-01": {
        "title": "Python环境搭建与基础语法",
        "content": '''
# 第1章 Python环境搭建与基础语法

## 学习目标
- 掌握Python环境搭建
- 理解Python基础语法
- 能够编写简单的Python程序

## 1.1 Python简介
Python是一种高级编程语言...

## 1.2 基础语法
```python
# 这是一个简单的Python程序
print("Hello, World!")
```
'''
    },
    "chapter-02": {
        "title": "变量与数据类型",
        "content": '''
# 第2章 变量与数据类型

## 学习目标
- 理解变量的概念
- 掌握Python的基本数据类型
- 学会使用运算符

## 2.1 变量定义
```python
name = "Python"
age = 30
is_language = True
```
'''
    }
}

for chapter_id, chapter_data in examples.items():
    chapter_dir = target_dir / chapter_id
    chapter_dir.mkdir(parents=True, exist_ok=True)
    
         # 创建内容文件
     content_file = chapter_dir / "content.md"
     content_file.write_text(chapter_data["content"], encoding='utf-8')
    
    print(f"创建章节: {chapter_data['title']}")

print("✅ 内容转换完成")
"""
        
        # 执行转换
        exec(converter_script)
        
        return True
        
    def start_platform(self):
        """启动平台"""
        print("🚀 启动教学平台...")
        
        # 切换到工作目录
        os.chdir(self.work_dir)
        
        # 创建Docker Compose文件
        self.create_docker_compose()
        self.create_jupyterhub_dockerfile()
        
        # 启动服务
        try:
            subprocess.run(["docker-compose", "up", "-d"], check=True)
            print("✅ 平台启动成功！")
            print("\n🌐 访问地址:")
            print("   - JupyterHub: http://localhost:8000")
            print("   - 用户名: admin 或 teacher")
            print("   - 密码: python123")
            print("\n📚 教学内容已准备就绪")
            
        except subprocess.CalledProcessError as e:
            print(f"❌ 启动失败: {e}")
            return False
        except FileNotFoundError:
            print("❌ Docker Compose未安装，请先安装Docker和Docker Compose")
            return False
            
        return True
        
    def stop_platform(self):
        """停止平台"""
        print("🛑 停止教学平台...")
        
        os.chdir(self.work_dir)
        
        try:
            subprocess.run(["docker-compose", "down"], check=True)
            print("✅ 平台已停止")
        except subprocess.CalledProcessError as e:
            print(f"❌ 停止失败: {e}")
            
    def show_status(self):
        """显示平台状态"""
        print("📊 平台状态:")
        
        os.chdir(self.work_dir)
        
        try:
            result = subprocess.run(["docker-compose", "ps"], 
                                  capture_output=True, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"❌ 状态查询失败: {e}")
            
    def create_demo_content(self):
        """创建演示内容"""
        print("📝 创建演示内容...")
        
        # 创建一个简单的Jupyter Notebook作为演示
        demo_notebook = {
            "cells": [
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "# Python基础教程演示\n",
                        "\n",
                        "这是一个基于nbgrader的Python教学演示。\n",
                        "\n",
                        "## 学习目标\n",
                        "- 理解变量的使用\n",
                        "- 掌握基本的数据类型\n",
                        "- 学会使用print函数"
                    ]
                },
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "## 练习1: 变量定义\n",
                        "\n",
                        "请定义一个变量`name`，并赋值为你的姓名："
                    ]
                },
                {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {
                        "nbgrader": {
                            "grade": False,
                            "grade_id": "exercise_1",
                            "locked": False,
                            "schema_version": 3,
                            "solution": True
                        }
                    },
                    "outputs": [],
                    "source": [
                        "# 请在这里定义变量name\n",
                        "# YOUR CODE HERE\n",
                        "name = \"请输入你的姓名\""
                    ]
                },
                {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {
                        "nbgrader": {
                            "grade": True,
                            "grade_id": "test_exercise_1",
                            "locked": True,
                            "points": 5,
                            "schema_version": 3,
                            "solution": False
                        }
                    },
                    "outputs": [],
                    "source": [
                        "# 测试用例\n",
                        "assert isinstance(name, str), \"name应该是字符串类型\"\n",
                        "assert len(name) > 0, \"name不能为空\"\n",
                        "print(f\"✓ 测试通过! 你好，{name}！\")"
                    ]
                }
            ],
            "metadata": {
                "kernelspec": {
                    "display_name": "Python 3",
                    "language": "python",
                    "name": "python3"
                },
                "language_info": {
                    "name": "python",
                    "version": "3.8.5"
                }
            },
            "nbformat": 4,
            "nbformat_minor": 4
        }
        
        # 保存演示notebook
        demo_dir = self.work_dir / "content/demo"
        demo_dir.mkdir(parents=True, exist_ok=True)
        
        import json
        demo_file = demo_dir / "python-basics-demo.ipynb"
        demo_file.write_text(json.dumps(demo_notebook, indent=2, ensure_ascii=False), encoding='utf-8')
        
        print("✅ 演示内容创建完成")


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="Python智能体开发教学平台v2.0")
    parser.add_argument("command", choices=["setup", "start", "stop", "status", "demo"],
                       help="执行的命令")
    parser.add_argument("--work-dir", help="工作目录")
    
    args = parser.parse_args()
    
    platform = PlatformManager(args.work_dir)
    
    if args.command == "setup":
        platform.setup_environment()
        platform.convert_content()
        platform.create_demo_content()
        print("\n🎉 设置完成！下一步运行: python 启动脚本.py start")
        
    elif args.command == "start":
        # 检查当前目录的docker-compose.yml文件
        if not Path("docker-compose.yml").exists():
            print("❌ 请先运行 setup 命令")
            return
        platform.start_platform()
        
    elif args.command == "stop":
        platform.stop_platform()
        
    elif args.command == "status":
        platform.show_status()
        
    elif args.command == "demo":
        platform.create_demo_content()
        
    else:
        parser.print_help()


if __name__ == "__main__":
    print("🐍 Python智能体开发教学平台 v2.0")
    print("基于 nbgrader + JupyterHub 构建")
    print("=" * 50)
    
    main() 