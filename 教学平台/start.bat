@echo off
echo.
echo ========================================
echo    Python智能体开发教学平台
echo ========================================
echo.
echo 正在启动教学平台...
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误：未找到Python，请先安装Python 3.8+
    pause
    exit /b 1
)

REM 检查是否存在虚拟环境
if not exist "venv\" (
    echo 正在创建虚拟环境...
    python -m venv venv
    echo 虚拟环境创建完成
)

REM 激活虚拟环境
echo 激活虚拟环境...
call venv\Scripts\activate.bat

REM 安装依赖
echo 检查并安装依赖包...
pip install -r requirements.txt

echo.
echo ========================================
echo 教学平台启动成功！
echo.
echo 请在浏览器中访问：http://localhost:5000
echo.
echo 按 Ctrl+C 停止服务器
echo ========================================
echo.

REM 启动Flask应用
python app.py

pause 