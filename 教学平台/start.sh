#!/bin/bash

echo "========================================"
echo "    Python智能体开发教学平台"
echo "========================================"
echo ""
echo "正在启动教学平台..."
echo ""

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    echo "错误：未找到Python3，请先安装Python 3.8+"
    exit 1
fi

# 检查是否存在虚拟环境
if [ ! -d "venv" ]; then
    echo "正在创建虚拟环境..."
    python3 -m venv venv
    echo "虚拟环境创建完成"
fi

# 激活虚拟环境
echo "激活虚拟环境..."
source venv/bin/activate

# 安装依赖
echo "检查并安装依赖包..."
pip install -r requirements.txt

echo ""
echo "========================================"
echo "教学平台启动成功！"
echo ""
echo "请在浏览器中访问：http://localhost:5000"
echo ""
echo "按 Ctrl+C 停止服务器"
echo "========================================"
echo ""

# 启动Flask应用
python app.py 