# 第35章：OpenCV与图像处理基础

> "在数字时代，每一张图片都是数据的艺术品，而我们即将建立一座现代化的数字相机工厂，用代码的魔法让机器拥有'看见'的能力。"

## 🎯 学习目标

### 知识目标
- 掌握OpenCV库的基本概念和核心功能架构
- 理解计算机视觉中图像处理的基本原理和数学基础
- 熟悉常用的图像预处理技术和算法实现
- 掌握特征检测与匹配的基本方法和应用场景

### 技能目标  
- 能够搭建和配置完整的OpenCV开发环境
- 能够进行基本的图像读取、显示、保存等核心操作
- 能够运用图像滤波、形态学操作等技术处理各类图像
- 能够实现边缘检测、角点检测等特征提取功能
- 能够开发完整的图像处理应用项目并进行优化

### 素养目标
- 培养解决实际图像处理问题的工程思维和系统性思考能力
- 建立计算机视觉领域的专业素养和技术判断力
- 培养企业级项目开发的规范意识和质量标准
- 建立从技术学习到产品开发的完整思维链条

## 🏭 章节导入：欢迎来到数字相机工厂

### 🎬 开篇故事：未来工厂的第一天

想象一下，您刚刚被聘为世界上最先进的"数字相机工厂"的首席工程师。这座工厂不生产传统的相机，而是专门生产能够"理解"图像的智能系统。

走进工厂大门，您会看到：

🏭 **拍照车间** - 这里有最先进的图像采集设备，能够从各种来源获取数字图像  
🖼️ **照片展示厅** - 配备了高清显示系统，可以实时展示处理过程和结果  
🖨️ **照片打印车间** - 拥有多种输出格式的保存系统，确保成果能够完美保存  
✨ **美颜工厂** - 这里是图像处理的核心，各种滤波、增强、优化算法在这里运转  
🔍 **图像侦探局** - 专门负责在图像中寻找边缘、角点、特征等重要信息

### 🎯 工厂的使命

作为首席工程师，您的使命是：
1. **建立标准化生产线** - 设计可重复、可扩展的图像处理流程
2. **保证产品质量** - 确保每个处理步骤都达到企业级标准
3. **优化生产效率** - 让系统能够处理大量图像而不降低质量
4. **创新产品功能** - 开发出具有商业价值的智能图像应用

### 🔧 您的工具箱：OpenCV

在这座数字工厂中，OpenCV就是您最重要的工具箱：

```python
# 这就是您的魔法工具箱
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 让我们开始这段神奇的旅程！
print("欢迎来到数字相机工厂！")
print(f"工厂版本：OpenCV {cv2.__version__}")
print("准备开始生产您的第一个智能视觉产品...")
```

## 📚 第一节：数字相机工厂的基础设施建设

### 35.1 OpenCV环境搭建与基础操作

#### 🏗️ 工厂基础设施规划

在建设我们的数字相机工厂之前，我们需要确保所有的基础设施都已就位。就像建设真实的工厂需要电力、水源、交通一样，我们的数字工厂也需要合适的软件环境和开发工具。

#### 📋 工厂建设需求清单

```bash
# 数字相机工厂建设需求清单
# ================================

# 1. 基础平台（Python环境）
Python >= 3.8

# 2. 核心生产设备（OpenCV）
opencv-python >= 4.8.0

# 3. 数据处理车间（NumPy）
numpy >= 1.24.0

# 4. 可视化展示厅（Matplotlib）
matplotlib >= 3.7.0

# 5. 开发调试工具（Jupyter）
jupyter >= 1.0.0

# 6. 图像格式支持（Pillow）
pillow >= 9.5.0
```

#### 🔧 工厂建设步骤

##### 步骤1：环境验证和准备

首先，让我们检查现有环境是否符合建厂要求：

```python
# 示例1：工厂环境检查系统
import sys
import subprocess
import pkg_resources

def check_factory_environment():
    """
    数字相机工厂环境检查系统
    检查所有必需的软件包是否已正确安装
    """
    print("🏭 数字相机工厂环境检查系统")
    print("=" * 50)
    
    # 检查Python版本
    python_version = sys.version_info
    print(f"🐍 Python版本: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version >= (3, 8):
        print("✅ Python版本符合要求 (>= 3.8)")
    else:
        print("❌ Python版本过低，请升级到3.8或更高版本")
        return False
    
    # 检查必需的软件包
    required_packages = {
        'opencv-python': '4.8.0',
        'numpy': '1.24.0', 
        'matplotlib': '3.7.0',
        'jupyter': '1.0.0',
        'pillow': '9.5.0'
    }
    
    print("\n📦 检查工厂设备（软件包）:")
    all_installed = True
    
    for package, min_version in required_packages.items():
        try:
            # 尝试导入包
            if package == 'opencv-python':
                import cv2
                version = cv2.__version__
                package_name = 'OpenCV'
            elif package == 'numpy':
                import numpy as np
                version = np.__version__
                package_name = 'NumPy'
            elif package == 'matplotlib':
                import matplotlib
                version = matplotlib.__version__
                package_name = 'Matplotlib'
            elif package == 'jupyter':
                import jupyter
                version = jupyter.__version__
                package_name = 'Jupyter'
            elif package == 'pillow':
                import PIL
                version = PIL.__version__
                package_name = 'Pillow'
            
            print(f"✅ {package_name}: {version}")
            
        except ImportError:
            print(f"❌ {package_name}: 未安装")
            all_installed = False
    
    print("\n" + "=" * 50)
    if all_installed:
        print("🎉 恭喜！工厂建设环境检查通过，可以开始生产！")
        return True
    else:
        print("⚠️  工厂建设不完整，请安装缺失的设备后重试")
        return False

# 运行环境检查
if __name__ == "__main__":
    check_factory_environment()
```

##### 步骤2：一键式工厂建设脚本

如果环境检查发现缺失组件，使用以下脚本进行一键安装：

```python
# 示例2：数字相机工厂一键建设脚本
import subprocess
import sys
import os

def install_factory_equipment():
    """
    数字相机工厂一键建设脚本
    自动安装所有必需的软件包
    """
    print("🏗️ 数字相机工厂建设脚本启动")
    print("=" * 50)
    
    # 定义需要安装的设备清单
    equipment_list = [
        "opencv-python>=4.8.0",
        "numpy>=1.24.0", 
        "matplotlib>=3.7.0",
        "jupyter>=1.0.0",
        "pillow>=9.5.0",
        "ipykernel",  # Jupyter内核支持
        "seaborn",    # 增强的可视化支持
    ]
    
    print("📋 开始安装工厂设备:")
    
    for equipment in equipment_list:
        print(f"\n🔧 正在安装: {equipment}")
        try:
            # 使用pip安装包
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", equipment
            ])
            print(f"✅ {equipment} 安装成功")
            
        except subprocess.CalledProcessError as e:
            print(f"❌ {equipment} 安装失败: {e}")
            return False
    
    # 验证安装
    print("\n🔍 验证工厂设备安装...")
    if check_factory_environment():
        print("\n🎉 数字相机工厂建设完成！")
        print("🚀 您现在可以开始生产智能视觉产品了！")
        return True
    else:
        print("\n⚠️ 工厂建设验证失败，请检查错误信息")
        return False

def create_factory_workspace():
    """
    创建标准化的工厂工作空间
    """
    print("\n📁 创建工厂工作空间...")
    
    # 定义工厂目录结构
    factory_structure = {
        "digital_camera_factory": {
            "workshops": {
                "capture_workshop": ["input_images"],
                "processing_workshop": ["enhanced_images"],
                "output_workshop": ["final_products"]
            },
            "tools": ["utilities", "filters", "detectors"],
            "tests": ["unit_tests", "integration_tests"],
            "docs": ["manuals", "specifications"],
            "projects": ["document_scanner", "image_enhancer"]
        }
    }
    
    def create_dirs(structure, base_path=""):
        for name, content in structure.items():
            current_path = os.path.join(base_path, name)
            os.makedirs(current_path, exist_ok=True)
            print(f"📂 创建目录: {current_path}")
            
            if isinstance(content, dict):
                create_dirs(content, current_path)
            elif isinstance(content, list):
                for subdir in content:
                    subdir_path = os.path.join(current_path, subdir)
                    os.makedirs(subdir_path, exist_ok=True)
                    print(f"📂 创建子目录: {subdir_path}")
    
    try:
        create_dirs(factory_structure)
        
        # 创建基础配置文件
        requirements_content = """# 数字相机工厂设备清单
opencv-python>=4.8.0
numpy>=1.24.0
matplotlib>=3.7.0
jupyter>=1.0.0
pillow>=9.5.0
seaborn>=0.12.0
ipykernel>=6.0.0
"""
        
        with open("digital_camera_factory/requirements.txt", "w", encoding="utf-8") as f:
            f.write(requirements_content)
        
        print("📄 创建设备清单: requirements.txt")
        print("✅ 工厂工作空间创建完成！")
        
    except Exception as e:
        print(f"❌ 工作空间创建失败: {e}")

# 运行工厂建设
if __name__ == "__main__":
    print("🏭 欢迎使用数字相机工厂建设系统！")
    print("\n请选择操作:")
    print("1. 检查现有环境")
    print("2. 一键建设工厂")
    print("3. 创建工作空间")
    
    choice = input("\n请输入选择 (1/2/3): ")
    
    if choice == "1":
        check_factory_environment()
    elif choice == "2":
        install_factory_equipment()
    elif choice == "3":
        create_factory_workspace()
    else:
        print("无效选择，程序退出")
```

#### 🖼️ 拍照车间：图像输入系统

现在工厂基础设施已经建设完成，让我们来建设第一个车间——拍照车间！这个车间负责从各种来源获取图像数据。

```python
# 示例3：拍照车间 - 图像输入系统
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

class CaptureWorkshop:
    """
    拍照车间类
    负责从各种来源获取和管理图像数据
    """
    
    def __init__(self, workspace_path="digital_camera_factory/workshops/capture_workshop"):
        """
        初始化拍照车间
        
        Parameters:
        workspace_path (str): 车间工作目录路径
        """
        self.workspace_path = Path(workspace_path)
        self.workspace_path.mkdir(parents=True, exist_ok=True)
        
        # 车间状态信息
        self.captured_images = []
        self.image_info = {}
        
        print("🏭 拍照车间初始化完成")
        print(f"📁 工作目录: {self.workspace_path}")
    
    def capture_from_file(self, image_path, display_info=True):
        """
        从文件获取图像（相当于从底片扫描）
        
        Parameters:
        image_path (str): 图像文件路径
        display_info (bool): 是否显示图像信息
        
        Returns:
        numpy.ndarray: 图像数据
        """
        print(f"📸 拍照车间：正在从文件获取图像 {image_path}")
        
        try:
            # 使用OpenCV读取图像
            image = cv2.imread(str(image_path))
            
            if image is None:
                print(f"❌ 错误：无法读取图像文件 {image_path}")
                return None
            
            # 转换颜色空间（OpenCV默认使用BGR，我们转换为RGB用于显示）
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # 记录图像信息
            image_id = len(self.captured_images)
            image_info = {
                'id': image_id,
                'path': image_path,
                'shape': image.shape,
                'dtype': image.dtype,
                'size_bytes': image.nbytes,
                'color_space': 'BGR'
            }
            
            self.captured_images.append(image)
            self.image_info[image_id] = image_info
            
            if display_info:
                self._display_image_info(image_info, image_rgb)
            
            print(f"✅ 图像获取成功！分配ID: {image_id}")
            return image_rgb
            
        except Exception as e:
            print(f"❌ 拍照车间错误: {e}")
            return None
    
    def capture_from_camera(self, camera_id=0, save_path=None):
        """
        从摄像头实时获取图像
        
        Parameters:
        camera_id (int): 摄像头ID
        save_path (str): 保存路径（可选）
        
        Returns:
        numpy.ndarray: 图像数据
        """
        print(f"📹 拍照车间：正在启动摄像头 {camera_id}")
        
        try:
            # 打开摄像头
            cap = cv2.VideoCapture(camera_id)
            
            if not cap.isOpened():
                print(f"❌ 错误：无法打开摄像头 {camera_id}")
                return None
            
            print("📸 按空格键拍照，按ESC键退出")
            
            while True:
                # 读取一帧
                ret, frame = cap.read()
                
                if not ret:
                    print("❌ 无法读取摄像头画面")
                    break
                
                # 显示画面
                cv2.imshow('拍照车间 - 实时画面 (空格拍照, ESC退出)', frame)
                
                key = cv2.waitKey(1) & 0xFF
                
                # 空格键拍照
                if key == ord(' '):
                    # 转换颜色空间
                    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    
                    # 保存图像
                    if save_path:
                        cv2.imwrite(str(save_path), frame)
                        print(f"💾 图像已保存到: {save_path}")
                    
                    # 记录图像信息
                    image_id = len(self.captured_images)
                    image_info = {
                        'id': image_id,
                        'path': save_path or 'camera_capture',
                        'shape': frame.shape,
                        'dtype': frame.dtype,
                        'size_bytes': frame.nbytes,
                        'color_space': 'BGR'
                    }
                    
                    self.captured_images.append(frame)
                    self.image_info[image_id] = image_info
                    
                    print(f"✅ 拍照成功！图像ID: {image_id}")
                    
                    # 释放摄像头
                    cap.release()
                    cv2.destroyAllWindows()
                    
                    return image_rgb
                
                # ESC键退出
                elif key == 27:
                    break
            
            # 释放摄像头
            cap.release()
            cv2.destroyAllWindows()
            return None
            
        except Exception as e:
            print(f"❌ 拍照车间摄像头错误: {e}")
            return None
    
    def create_test_image(self, width=640, height=480, pattern='gradient'):
        """
        创建测试图像（用于工厂调试）
        
        Parameters:
        width (int): 图像宽度
        height (int): 图像高度
        pattern (str): 图像模式 ('gradient', 'checkerboard', 'noise')
        
        Returns:
        numpy.ndarray: 测试图像
        """
        print(f"🧪 拍照车间：正在创建测试图像 ({width}x{height}, {pattern})")
        
        if pattern == 'gradient':
            # 创建梯度图像
            image = np.zeros((height, width, 3), dtype=np.uint8)
            for i in range(height):
                intensity = int(255 * i / height)
                image[i, :] = [intensity, intensity // 2, 255 - intensity]
                
        elif pattern == 'checkerboard':
            # 创建棋盘图像
            image = np.zeros((height, width, 3), dtype=np.uint8)
            square_size = 50
            for i in range(0, height, square_size):
                for j in range(0, width, square_size):
                    if (i // square_size + j // square_size) % 2 == 0:
                        image[i:i+square_size, j:j+square_size] = [255, 255, 255]
                        
        elif pattern == 'noise':
            # 创建噪声图像
            image = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
            
        else:
            # 默认纯色图像
            image = np.full((height, width, 3), 128, dtype=np.uint8)
        
        # 记录图像信息
        image_id = len(self.captured_images)
        image_info = {
            'id': image_id,
            'path': f'test_image_{pattern}',
            'shape': image.shape,
            'dtype': image.dtype,
            'size_bytes': image.nbytes,
            'color_space': 'RGB'
        }
        
        self.captured_images.append(image)
        self.image_info[image_id] = image_info
        
        print(f"✅ 测试图像创建成功！图像ID: {image_id}")
        return image
    
    def _display_image_info(self, image_info, image):
        """
        显示图像详细信息
        """
        print("\n📊 图像信息:")
        print(f"   ID: {image_info['id']}")
        print(f"   尺寸: {image_info['shape'][1]} x {image_info['shape'][0]} 像素")
        print(f"   通道数: {image_info['shape'][2] if len(image_info['shape']) > 2 else 1}")
        print(f"   数据类型: {image_info['dtype']}")
        print(f"   文件大小: {image_info['size_bytes'] / 1024:.2f} KB")
        print(f"   颜色空间: {image_info['color_space']}")
    
    def get_workshop_status(self):
        """
        获取拍照车间状态
        """
        print("\n🏭 拍照车间状态报告")
        print("=" * 40)
        print(f"📸 已处理图像数量: {len(self.captured_images)}")
        print(f"📁 工作目录: {self.workspace_path}")
        
        if self.captured_images:
            total_size = sum(info['size_bytes'] for info in self.image_info.values())
            print(f"💾 总数据量: {total_size / 1024 / 1024:.2f} MB")
            
            print("\n📋 图像清单:")
            for image_id, info in self.image_info.items():
                print(f"   [{image_id}] {info['path']} - {info['shape'][1]}x{info['shape'][0]}")

# 使用示例
if __name__ == "__main__":
    # 创建拍照车间
    workshop = CaptureWorkshop()
    
    # 创建测试图像
    test_image = workshop.create_test_image(pattern='gradient')
    
    # 显示工厂状态
    workshop.get_workshop_status()
```

这个"拍照车间"类展示了如何用企业级的代码结构来处理图像输入，包含了完整的错误处理、信息记录和状态管理。

#### 🖼️ 照片展示厅：图像显示系统

拍照车间获取了图像后，我们需要一个专业的展示系统来查看和分析这些图像。照片展示厅就是我们的可视化中心！

```python
# 示例4：照片展示厅 - 图像显示系统
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import seaborn as sns

class DisplayGallery:
    """
    照片展示厅类
    负责图像的专业化显示、分析和可视化
    """
    
    def __init__(self):
        """
        初始化照片展示厅
        """
        # 设置matplotlib支持中文
        plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
        plt.rcParams['axes.unicode_minus'] = False
        
        # 设置seaborn样式
        sns.set_style("whitegrid")
        
        print("🖼️ 照片展示厅初始化完成")
        print("📺 高清显示系统已就绪")
    
    def show_single_image(self, image, title="图像展示", figsize=(10, 8), 
                         color_space='RGB', show_info=True):
        """
        在展示厅展示单张图像
        
        Parameters:
        image (numpy.ndarray): 图像数据
        title (str): 图像标题
        figsize (tuple): 显示尺寸
        color_space (str): 颜色空间 ('RGB', 'BGR', 'GRAY')
        show_info (bool): 是否显示图像信息
        """
        print(f"🖼️ 展示厅：正在展示图像 - {title}")
        
        fig, ax = plt.subplots(1, 1, figsize=figsize)
        
        # 根据颜色空间处理图像显示
        if color_space == 'BGR':
            # OpenCV默认是BGR，转换为RGB显示
            display_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        elif color_space == 'GRAY':
            # 灰度图像
            display_image = image
            ax.imshow(display_image, cmap='gray')
        else:
            # RGB或其他
            display_image = image
            ax.imshow(display_image)
        
        # 设置标题和显示属性
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        ax.axis('off')  # 隐藏坐标轴
        
        # 显示图像信息
        if show_info and image is not None:
            info_text = f"尺寸: {image.shape[1]}×{image.shape[0]}"
            if len(image.shape) > 2:
                info_text += f" | 通道: {image.shape[2]}"
            info_text += f" | 类型: {image.dtype}"
            
            ax.text(0.02, 0.98, info_text, transform=ax.transAxes,
                   bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7),
                   verticalalignment='top', fontsize=10)
        
        plt.tight_layout()
        plt.show()
        
        print(f"✅ 图像展示完成")
    
    def show_image_comparison(self, images, titles, figsize=(15, 5), 
                            color_space='RGB', suptitle="图像对比展示"):
        """
        在展示厅同时展示多张图像进行对比
        
        Parameters:
        images (list): 图像列表
        titles (list): 标题列表
        figsize (tuple): 显示尺寸
        color_space (str): 颜色空间
        suptitle (str): 总标题
        """
        print(f"🖼️ 展示厅：正在进行图像对比展示")
        
        num_images = len(images)
        fig, axes = plt.subplots(1, num_images, figsize=figsize)
        
        # 如果只有一张图像，axes不是列表
        if num_images == 1:
            axes = [axes]
        
        for i, (image, title) in enumerate(zip(images, titles)):
            if image is not None:
                # 处理颜色空间
                if color_space == 'BGR':
                    display_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                elif color_space == 'GRAY':
                    display_image = image
                    axes[i].imshow(display_image, cmap='gray')
                else:
                    display_image = image
                    
                if color_space != 'GRAY':
                    axes[i].imshow(display_image)
                
                axes[i].set_title(title, fontsize=12, fontweight='bold')
                axes[i].axis('off')
                
                # 添加图像信息
                info_text = f"{image.shape[1]}×{image.shape[0]}"
                axes[i].text(0.02, 0.98, info_text, transform=axes[i].transAxes,
                           bbox=dict(boxstyle="round,pad=0.2", facecolor="lightblue", alpha=0.7),
                           verticalalignment='top', fontsize=8)
            else:
                axes[i].text(0.5, 0.5, '图像加载失败', ha='center', va='center',
                           transform=axes[i].transAxes, fontsize=12)
                axes[i].set_title(title, fontsize=12)
                axes[i].axis('off')
        
        fig.suptitle(suptitle, fontsize=16, fontweight='bold', y=1.02)
        plt.tight_layout()
        plt.show()
        
        print(f"✅ 对比展示完成")
    
    def show_image_histogram(self, image, title="图像直方图分析", 
                           color_space='RGB', bins=256):
        """
        在展示厅显示图像的直方图分析
        
        Parameters:
        image (numpy.ndarray): 图像数据
        title (str): 标题
        color_space (str): 颜色空间
        bins (int): 直方图bin数量
        """
        print(f"📊 展示厅：正在进行直方图分析")
        
        if color_space == 'GRAY':
            # 灰度图像直方图
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
            
            # 显示图像
            ax1.imshow(image, cmap='gray')
            ax1.set_title('原始图像', fontsize=12)
            ax1.axis('off')
            
            # 显示直方图
            hist = cv2.calcHist([image], [0], None, [bins], [0, 256])
            ax2.plot(hist, color='black')
            ax2.set_title('灰度直方图', fontsize=12)
            ax2.set_xlabel('像素值')
            ax2.set_ylabel('频次')
            ax2.grid(True, alpha=0.3)
            
        else:
            # 彩色图像直方图
            fig, axes = plt.subplots(2, 2, figsize=(12, 10))
            
            # 处理颜色空间
            if color_space == 'BGR':
                display_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                colors = ['red', 'green', 'blue']
                channels = ['R', 'G', 'B']
            else:
                display_image = image
                colors = ['red', 'green', 'blue']
                channels = ['R', 'G', 'B']
            
            # 显示原图
            axes[0, 0].imshow(display_image)
            axes[0, 0].set_title('原始图像', fontsize=12)
            axes[0, 0].axis('off')
            
            # 分别显示各通道直方图
            for i, (color, channel) in enumerate(zip(colors, channels)):
                hist = cv2.calcHist([image], [i], None, [bins], [0, 256])
                
                if i == 0:  # R通道
                    axes[0, 1].plot(hist, color=color, alpha=0.7, label=f'{channel}通道')
                    axes[0, 1].set_title('单通道直方图', fontsize=12)
                elif i == 1:  # G通道
                    axes[1, 0].plot(hist, color=color, alpha=0.7, label=f'{channel}通道')
                    axes[1, 0].set_title('单通道直方图', fontsize=12)
                else:  # B通道
                    axes[1, 1].plot(hist, color=color, alpha=0.7, label=f'{channel}通道')
                    axes[1, 1].set_title('单通道直方图', fontsize=12)
                
                # 设置图表属性
                current_ax = axes[0, 1] if i == 0 else (axes[1, 0] if i == 1 else axes[1, 1])
                current_ax.set_xlabel('像素值')
                current_ax.set_ylabel('频次')
                current_ax.grid(True, alpha=0.3)
                current_ax.legend()
        
        fig.suptitle(title, fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        print(f"✅ 直方图分析完成")
    
    def show_image_with_roi(self, image, roi_boxes, roi_labels=None, 
                          title="图像区域标注", color_space='RGB'):
        """
        在展示厅显示带有感兴趣区域（ROI）标注的图像
        
        Parameters:
        image (numpy.ndarray): 图像数据
        roi_boxes (list): ROI框列表，每个框为(x, y, width, height)
        roi_labels (list): ROI标签列表
        title (str): 标题
        color_space (str): 颜色空间
        """
        print(f"🔍 展示厅：正在显示ROI标注图像")
        
        fig, ax = plt.subplots(1, 1, figsize=(12, 8))
        
        # 处理颜色空间
        if color_space == 'BGR':
            display_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        elif color_space == 'GRAY':
            display_image = image
            ax.imshow(display_image, cmap='gray')
        else:
            display_image = image
            
        if color_space != 'GRAY':
            ax.imshow(display_image)
        
        # 绘制ROI框
        colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan']
        
        for i, (x, y, w, h) in enumerate(roi_boxes):
            color = colors[i % len(colors)]
            
            # 绘制矩形框
            rect = Rectangle((x, y), w, h, linewidth=2, 
                           edgecolor=color, facecolor='none')
            ax.add_patch(rect)
            
            # 添加标签
            if roi_labels and i < len(roi_labels):
                label = roi_labels[i]
            else:
                label = f'ROI-{i+1}'
            
            ax.text(x, y-5, label, fontsize=10, color=color, 
                   fontweight='bold', bbox=dict(boxstyle="round,pad=0.2", 
                   facecolor='white', edgecolor=color, alpha=0.8))
        
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        ax.axis('off')
        
        plt.tight_layout()
        plt.show()
        
        print(f"✅ ROI标注显示完成")
    
    def create_image_gallery(self, images, titles, cols=3, figsize_per_image=(4, 3),
                           suptitle="图像画廊", color_space='RGB'):
        """
        创建图像画廊展示
        
        Parameters:
        images (list): 图像列表
        titles (list): 标题列表
        cols (int): 列数
        figsize_per_image (tuple): 每张图像的尺寸
        suptitle (str): 总标题
        color_space (str): 颜色空间
        """
        print(f"🖼️ 展示厅：正在创建图像画廊")
        
        num_images = len(images)
        rows = (num_images + cols - 1) // cols
        
        fig_width = cols * figsize_per_image[0]
        fig_height = rows * figsize_per_image[1]
        
        fig, axes = plt.subplots(rows, cols, figsize=(fig_width, fig_height))
        
        # 处理axes的维度
        if rows == 1 and cols == 1:
            axes = [axes]
        elif rows == 1:
            axes = axes.reshape(1, -1)
        elif cols == 1:
            axes = axes.reshape(-1, 1)
        
        for i in range(num_images):
            row = i // cols
            col = i % cols
            
            if rows == 1:
                ax = axes[col] if cols > 1 else axes[0]
            else:
                ax = axes[row, col]
            
            image = images[i]
            title = titles[i] if i < len(titles) else f'图像-{i+1}'
            
            if image is not None:
                # 处理颜色空间
                if color_space == 'BGR':
                    display_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                elif color_space == 'GRAY':
                    display_image = image
                    ax.imshow(display_image, cmap='gray')
                else:
                    display_image = image
                    
                if color_space != 'GRAY':
                    ax.imshow(display_image)
                
                ax.set_title(title, fontsize=10)
            else:
                ax.text(0.5, 0.5, '加载失败', ha='center', va='center',
                       transform=ax.transAxes)
                ax.set_title(title, fontsize=10)
            
            ax.axis('off')
        
        # 隐藏多余的子图
        for i in range(num_images, rows * cols):
            row = i // cols
            col = i % cols
            if rows == 1:
                ax = axes[col] if cols > 1 else axes[0]
            else:
                ax = axes[row, col]
            ax.axis('off')
        
        fig.suptitle(suptitle, fontsize=16, fontweight='bold', y=0.95)
        plt.tight_layout()
        plt.show()
        
        print(f"✅ 图像画廊展示完成")

# 使用示例
if __name__ == "__main__":
    # 创建展示厅
    gallery = DisplayGallery()
    
    # 创建测试图像
    workshop = CaptureWorkshop()
    test_image1 = workshop.create_test_image(pattern='gradient')
    test_image2 = workshop.create_test_image(pattern='checkerboard')
    
    # 单图像展示
    gallery.show_single_image(test_image1, "梯度测试图像")
    
    # 对比展示
    gallery.show_image_comparison([test_image1, test_image2], 
                                 ["梯度图像", "棋盘图像"], 
                                 suptitle="测试图像对比")
    
    # 直方图分析
    gallery.show_image_histogram(test_image1, "梯度图像直方图分析")
```

#### 🖨️ 照片打印车间：图像保存系统

有了专业的展示系统，我们还需要一个可靠的保存系统来确保处理结果能够完美保存。

```python
# 示例5：照片打印车间 - 图像保存系统
import cv2
import numpy as np
import os
from datetime import datetime
from pathlib import Path
import json

class PrintingWorkshop:
    """
    照片打印车间类
    负责图像的保存、格式转换和批量输出
    """
    
    def __init__(self, output_path="digital_camera_factory/workshops/output_workshop"):
        """
        初始化照片打印车间
        
        Parameters:
        output_path (str): 输出目录路径
        """
        self.output_path = Path(output_path)
        self.output_path.mkdir(parents=True, exist_ok=True)
        
        # 支持的输出格式
        self.supported_formats = {
            '.jpg': 'JPEG格式 - 有损压缩，适合照片',
            '.jpeg': 'JPEG格式 - 有损压缩，适合照片',
            '.png': 'PNG格式 - 无损压缩，支持透明',
            '.bmp': 'BMP格式 - 无压缩，占用空间大',
            '.tiff': 'TIFF格式 - 无损压缩，专业用途',
            '.webp': 'WebP格式 - 高效压缩，web友好'
        }
        
        # 保存记录
        self.save_history = []
        
        print("🖨️ 照片打印车间初始化完成")
        print(f"📁 输出目录: {self.output_path}")
        print(f"📄 支持格式: {list(self.supported_formats.keys())}")
    
    def save_image(self, image, filename, quality=95, color_space='RGB',
                   add_timestamp=False, metadata=None):
        """
        保存单张图像
        
        Parameters:
        image (numpy.ndarray): 图像数据
        filename (str): 文件名（含扩展名）
        quality (int): 保存质量 (1-100，仅对JPEG有效)
        color_space (str): 图像颜色空间
        add_timestamp (bool): 是否添加时间戳
        metadata (dict): 附加元数据
        
        Returns:
        str: 保存的文件路径
        """
        print(f"🖨️ 打印车间：正在保存图像 {filename}")
        
        # 处理文件名
        if add_timestamp:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            name, ext = os.path.splitext(filename)
            filename = f"{name}_{timestamp}{ext}"
        
        # 完整文件路径
        file_path = self.output_path / filename
        
        # 检查格式支持
        ext = os.path.splitext(filename)[1].lower()
        if ext not in self.supported_formats:
            print(f"⚠️ 警告：格式 {ext} 可能不被支持，尝试保存...")
        
        try:
            # 处理颜色空间转换
            if color_space == 'RGB':
                # RGB转BGR（OpenCV默认）
                save_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            elif color_space == 'GRAY':
                save_image = image
            else:
                save_image = image
            
            # 设置保存参数
            save_params = []
            
            if ext in ['.jpg', '.jpeg']:
                save_params = [cv2.IMWRITE_JPEG_QUALITY, quality]
            elif ext == '.png':
                # PNG压缩级别 (0-9)
                compression = int((100 - quality) / 100 * 9)
                save_params = [cv2.IMWRITE_PNG_COMPRESSION, compression]
            elif ext == '.webp':
                save_params = [cv2.IMWRITE_WEBP_QUALITY, quality]
            
            # 保存图像
            success = cv2.imwrite(str(file_path), save_image, save_params)
            
            if success:
                # 记录保存信息
                save_info = {
                    'filename': filename,
                    'file_path': str(file_path),
                    'timestamp': datetime.now().isoformat(),
                    'original_shape': image.shape,
                    'color_space': color_space,
                    'quality': quality,
                    'file_size_bytes': file_path.stat().st_size,
                    'metadata': metadata or {}
                }
                
                self.save_history.append(save_info)
                
                print(f"✅ 图像保存成功: {file_path}")
                print(f"📄 文件大小: {save_info['file_size_bytes'] / 1024:.2f} KB")
                
                # 保存元数据文件
                if metadata:
                    self._save_metadata(file_path, save_info)
                
                return str(file_path)
            else:
                print(f"❌ 图像保存失败: {file_path}")
                return None
                
        except Exception as e:
            print(f"❌ 打印车间错误: {e}")
            return None
    
    def save_image_batch(self, images, base_filename, quality=95, 
                        color_space='RGB', format_type='.jpg'):
        """
        批量保存图像
        
        Parameters:
        images (list): 图像列表
        base_filename (str): 基础文件名
        quality (int): 保存质量
        color_space (str): 颜色空间
        format_type (str): 保存格式
        
        Returns:
        list: 保存的文件路径列表
        """
        print(f"🖨️ 打印车间：开始批量保存 {len(images)} 张图像")
        
        saved_paths = []
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        for i, image in enumerate(images):
            if image is not None:
                filename = f"{base_filename}_{timestamp}_{i+1:03d}{format_type}"
                
                path = self.save_image(
                    image=image,
                    filename=filename,
                    quality=quality,
                    color_space=color_space,
                    metadata={'batch_id': timestamp, 'sequence': i+1}
                )
                
                if path:
                    saved_paths.append(path)
            else:
                print(f"⚠️ 跳过空图像 (索引: {i})")
        
        print(f"✅ 批量保存完成，成功保存 {len(saved_paths)} 张图像")
        return saved_paths
    
    def convert_format(self, input_path, output_format, quality=95):
        """
        转换图像格式
        
        Parameters:
        input_path (str): 输入文件路径
        output_format (str): 输出格式 (如 '.png')
        quality (int): 转换质量
        
        Returns:
        str: 输出文件路径
        """
        print(f"🔄 打印车间：正在转换格式 {input_path} -> {output_format}")
        
        try:
            # 读取原图像
            image = cv2.imread(str(input_path))
            if image is None:
                print(f"❌ 无法读取图像: {input_path}")
                return None
            
            # 生成输出文件名
            input_path = Path(input_path)
            output_filename = input_path.stem + output_format
            
            # 保存转换后的图像
            output_path = self.save_image(
                image=image,
                filename=output_filename,
                quality=quality,
                color_space='BGR',
                metadata={
                    'original_file': str(input_path),
                    'conversion': f"{input_path.suffix} -> {output_format}"
                }
            )
            
            print(f"✅ 格式转换成功: {output_path}")
            return output_path
            
        except Exception as e:
            print(f"❌ 格式转换错误: {e}")
            return None
    
    def _save_metadata(self, image_path, save_info):
        """
        保存图像元数据
        """
        metadata_path = image_path.with_suffix('.json')
        
        try:
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(save_info, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"⚠️ 元数据保存失败: {e}")
    
    def get_workshop_status(self):
        """
        获取打印车间状态
        """
        print("\n🖨️ 照片打印车间状态报告")
        print("=" * 50)
        print(f"📁 输出目录: {self.output_path}")
        print(f"📄 已保存文件数: {len(self.save_history)}")
        
        if self.save_history:
            total_size = sum(info['file_size_bytes'] for info in self.save_history)
            print(f"💾 总输出大小: {total_size / 1024 / 1024:.2f} MB")
            
            # 按格式统计
            format_stats = {}
            for info in self.save_history:
                ext = os.path.splitext(info['filename'])[1].lower()
                format_stats[ext] = format_stats.get(ext, 0) + 1
            
            print("\n📊 格式统计:")
            for fmt, count in format_stats.items():
                print(f"   {fmt}: {count} 个文件")
            
            print("\n📋 最近保存的文件:")
            for info in self.save_history[-5:]:  # 显示最近5个
                size_kb = info['file_size_bytes'] / 1024
                print(f"   {info['filename']} - {size_kb:.1f} KB")
        
        print(f"\n📝 支持的输出格式:")
        for fmt, desc in self.supported_formats.items():
            print(f"   {fmt}: {desc}")

# 使用示例
if __name__ == "__main__":
    # 创建打印车间
    printer = PrintingWorkshop()
    
    # 创建测试图像
    workshop = CaptureWorkshop()
    test_image = workshop.create_test_image(pattern='gradient')
    
    # 保存单张图像
    saved_path = printer.save_image(
        image=test_image,
        filename="test_gradient.jpg",
        quality=90,
        add_timestamp=True,
        metadata={'test_type': 'gradient', 'quality_test': True}
    )
    
    # 显示车间状态
    printer.get_workshop_status()
```

这样，我们就完成了数字相机工厂的三个核心车间：

1. **🏭 拍照车间** - 负责图像输入和获取
2. **🖼️ 照片展示厅** - 负责图像显示和分析 
3. **🖨️ 照片打印车间** - 负责图像保存和格式转换

每个车间都采用了企业级的代码结构，包含完整的错误处理、状态管理和功能扩展能力。接下来我将开始第二节的图像预处理技术...

## 📚 第二节：照片美颜工厂的图像处理技术

### 35.2 图像预处理技术

我们的数字相机工厂已经建立了完善的基础设施，现在是时候建设最核心的部分——**照片美颜工厂**！这里是整个工厂的技术心脏，负责将原始图像转化为完美的视觉作品。

#### 🏭 美颜工厂总览

想象一下最先进的照片美颜工厂，它有几个专业的处理车间：

🎨 **调色车间** - 负责颜色空间转换和色彩调整  
🧽 **磨皮车间** - 专门进行图像滤波和降噪处理  
✨ **美白车间** - 进行亮度对比度调整和直方图均衡化  
🔪 **锐化车间** - 负责图像边缘增强和细节优化  

每个车间都有自己的专业设备和工艺流程，让我们逐一探索它们！

#### 🎨 调色车间：颜色空间转换技术

颜色空间就像是不同的"调色板"，每种调色板都有其独特的用途和优势。

```python
# 示例6：调色车间 - 颜色空间转换系统
import cv2
import numpy as np
import matplotlib.pyplot as plt

class ColorWorkshop:
    """
    调色车间类
    负责各种颜色空间的转换和色彩处理
    """
    
    def __init__(self):
        """
        初始化调色车间
        """
        # 支持的颜色空间转换
        self.color_spaces = {
            'RGB': '标准RGB颜色空间 - 适合显示',
            'BGR': 'OpenCV默认颜色空间 - 蓝绿红',
            'HSV': 'HSV颜色空间 - 适合颜色分析',
            'LAB': 'LAB颜色空间 - 感知均匀',
            'GRAY': '灰度空间 - 单通道处理',
            'YUV': 'YUV颜色空间 - 视频编码'
        }
        
        print("🎨 调色车间初始化完成")
        print("🖌️ 调色板系统已就绪")
        print(f"📋 支持的颜色空间: {list(self.color_spaces.keys())}")
    
    def show_color_spaces(self, image, figsize=(16, 12)):
        """
        展示图像在不同颜色空间下的表现
        
        Parameters:
        image (numpy.ndarray): 输入图像 (RGB格式)
        figsize (tuple): 显示尺寸
        """
        print("🎨 调色车间：正在展示不同颜色空间效果")
        
        # 确保输入是RGB格式
        if len(image.shape) == 3:
            rgb_image = image.copy()
        else:
            print("❌ 输入图像必须是彩色图像")
            return
        
        # 转换为BGR格式供OpenCV使用
        bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
        
        # 准备不同颜色空间的图像
        color_images = {}
        
        # RGB (原图)
        color_images['RGB'] = rgb_image
        
        # BGR
        color_images['BGR'] = bgr_image
        
        # HSV
        hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
        color_images['HSV'] = hsv_image
        
        # LAB
        lab_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2LAB)
        color_images['LAB'] = lab_image
        
        # 灰度
        gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
        color_images['GRAY'] = gray_image
        
        # YUV
        yuv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2YUV)
        color_images['YUV'] = yuv_image
        
        # 创建展示图
        fig, axes = plt.subplots(2, 3, figsize=figsize)
        axes = axes.flatten()
        
        for i, (space_name, img) in enumerate(color_images.items()):
            ax = axes[i]
            
            if space_name == 'GRAY':
                ax.imshow(img, cmap='gray')
            else:
                # 对于非RGB空间，我们显示每个通道
                if space_name == 'RGB':
                    ax.imshow(img)
                elif space_name == 'BGR':
                    # BGR显示时转换为RGB
                    display_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    ax.imshow(display_img)
                else:
                    # 其他颜色空间显示原始数据
                    ax.imshow(img)
            
            ax.set_title(f'{space_name} 颜色空间', fontsize=12, fontweight='bold')
            ax.axis('off')
            
            # 添加颜色空间说明
            desc = self.color_spaces.get(space_name, '')
            ax.text(0.02, 0.02, desc, transform=ax.transAxes,
                   bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.8),
                   fontsize=8, verticalalignment='bottom')
        
        fig.suptitle('🎨 调色车间 - 颜色空间展示', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        print("✅ 颜色空间展示完成")
    
    def analyze_hsv_channels(self, image, figsize=(15, 10)):
        """
        分析HSV颜色空间的各个通道
        
        Parameters:
        image (numpy.ndarray): 输入图像 (RGB格式)
        figsize (tuple): 显示尺寸
        """
        print("🔍 调色车间：正在分析HSV通道")
        
        # 转换为HSV
        bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
        
        # 分离HSV通道
        h_channel = hsv_image[:, :, 0]  # 色调 (Hue)
        s_channel = hsv_image[:, :, 1]  # 饱和度 (Saturation)
        v_channel = hsv_image[:, :, 2]  # 明度 (Value)
        
        # 创建展示图
        fig, axes = plt.subplots(2, 2, figsize=figsize)
        
        # 原始RGB图像
        axes[0, 0].imshow(image)
        axes[0, 0].set_title('原始RGB图像', fontsize=12, fontweight='bold')
        axes[0, 0].axis('off')
        
        # H通道 (色调)
        axes[0, 1].imshow(h_channel, cmap='hsv')
        axes[0, 1].set_title('H通道 (色调)\n值域: 0-179°', fontsize=12, fontweight='bold')
        axes[0, 1].axis('off')
        
        # S通道 (饱和度)
        axes[1, 0].imshow(s_channel, cmap='gray')
        axes[1, 0].set_title('S通道 (饱和度)\n值域: 0-255', fontsize=12, fontweight='bold')
        axes[1, 0].axis('off')
        
        # V通道 (明度)
        axes[1, 1].imshow(v_channel, cmap='gray')
        axes[1, 1].set_title('V通道 (明度)\n值域: 0-255', fontsize=12, fontweight='bold')
        axes[1, 1].axis('off')
        
        fig.suptitle('🎨 HSV通道分析 - 理解色彩的三个维度', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        # 输出统计信息
        print(f"📊 HSV通道统计:")
        print(f"   H通道 (色调): 范围 {h_channel.min()}-{h_channel.max()}, 平均 {h_channel.mean():.1f}")
        print(f"   S通道 (饱和度): 范围 {s_channel.min()}-{s_channel.max()}, 平均 {s_channel.mean():.1f}")
        print(f"   V通道 (明度): 范围 {v_channel.min()}-{v_channel.max()}, 平均 {v_channel.mean():.1f}")
        
        print("✅ HSV通道分析完成")
        
        return hsv_image, (h_channel, s_channel, v_channel)

# 使用示例
if __name__ == "__main__":
    # 创建调色车间
    color_workshop = ColorWorkshop()
    
    # 创建测试图像
    workshop = CaptureWorkshop()
    test_image = workshop.create_test_image(640, 480, 'gradient')
    
    # 展示不同颜色空间
    color_workshop.show_color_spaces(test_image)
    
    # 分析HSV通道
    hsv_img, channels = color_workshop.analyze_hsv_channels(test_image)
```

#### 🧽 磨皮车间：图像滤波和降噪技术

磨皮车间是美颜工厂的核心，负责去除图像中的噪声和瑕疵，让图像变得更加平滑和清洁。

```python
# 示例7：磨皮车间 - 图像滤波和降噪系统
import cv2
import numpy as np
import matplotlib.pyplot as plt

class FilteringWorkshop:
    """
    磨皮车间类
    负责图像滤波、降噪和平滑处理
    """
    
    def __init__(self):
        """
        初始化磨皮车间
        """
        # 支持的滤波技术
        self.filter_types = {
            'blur': '均值滤波 - 简单平均',
            'gaussian': '高斯滤波 - 加权平均',
            'median': '中值滤波 - 去除椒盐噪声',
            'bilateral': '双边滤波 - 保持边缘',
            'morphology': '形态学滤波 - 结构处理'
        }
        
        print("🧽 磨皮车间初始化完成")
        print("🔧 滤波设备已准备就绪")
        print(f"📋 支持的滤波技术: {list(self.filter_types.keys())}")
    
    def add_noise_to_image(self, image, noise_type='gaussian', intensity=0.1):
        """
        向图像添加噪声（用于演示滤波效果）
        
        Parameters:
        image (numpy.ndarray): 输入图像
        noise_type (str): 噪声类型 ('gaussian', 'salt_pepper', 'uniform')
        intensity (float): 噪声强度
        
        Returns:
        numpy.ndarray: 带噪声的图像
        """
        print(f"🎭 磨皮车间：正在添加 {noise_type} 噪声 (强度: {intensity})")
        
        noisy_image = image.copy().astype(np.float32)
        
        if noise_type == 'gaussian':
            # 高斯噪声
            noise = np.random.normal(0, intensity * 255, image.shape)
            noisy_image = noisy_image + noise
            
        elif noise_type == 'salt_pepper':
            # 椒盐噪声
            noise = np.random.random(image.shape)
            noisy_image[noise < intensity/2] = 0  # 盐噪声 (黑点)
            noisy_image[noise > 1 - intensity/2] = 255  # 椒噪声 (白点)
            
        elif noise_type == 'uniform':
            # 均匀噪声
            noise = np.random.uniform(-intensity * 255, intensity * 255, image.shape)
            noisy_image = noisy_image + noise
        
        # 限制像素值范围
        noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
        
        print(f"✅ 噪声添加完成")
        return noisy_image
    
    def apply_filters_comparison(self, image, figsize=(18, 12)):
        """
        对比展示不同滤波技术的效果
        
        Parameters:
        image (numpy.ndarray): 输入图像
        figsize (tuple): 显示尺寸
        """
        print("🧽 磨皮车间：正在进行滤波技术对比")
        
        # 添加噪声
        noisy_image = self.add_noise_to_image(image, 'gaussian', 0.15)
        
        # 准备不同的滤波结果
        filtered_images = {}
        
        # 原图和噪声图
        filtered_images['原始图像'] = image
        filtered_images['噪声图像'] = noisy_image
        
        # 均值滤波
        blur_result = cv2.blur(noisy_image, (5, 5))
        filtered_images['均值滤波'] = blur_result
        
        # 高斯滤波
        gaussian_result = cv2.GaussianBlur(noisy_image, (5, 5), 0)
        filtered_images['高斯滤波'] = gaussian_result
        
        # 中值滤波
        median_result = cv2.medianBlur(noisy_image, 5)
        filtered_images['中值滤波'] = median_result
        
        # 双边滤波
        bilateral_result = cv2.bilateralFilter(noisy_image, 9, 75, 75)
        filtered_images['双边滤波'] = bilateral_result
        
        # 创建展示图
        fig, axes = plt.subplots(2, 3, figsize=figsize)
        axes = axes.flatten()
        
        for i, (filter_name, filtered_img) in enumerate(filtered_images.items()):
            ax = axes[i]
            
            if len(filtered_img.shape) == 3:
                # 彩色图像
                if filter_name in ['原始图像', '噪声图像']:
                    ax.imshow(filtered_img)
                else:
                    # OpenCV滤波结果可能是BGR，转换为RGB显示
                    if filtered_img.shape[2] == 3:
                        display_img = cv2.cvtColor(filtered_img, cv2.COLOR_BGR2RGB)
                        ax.imshow(display_img)
                    else:
                        ax.imshow(filtered_img)
            else:
                # 灰度图像
                ax.imshow(filtered_img, cmap='gray')
            
            ax.set_title(filter_name, fontsize=12, fontweight='bold')
            ax.axis('off')
            
            # 添加滤波说明
            if filter_name in ['均值滤波', '高斯滤波', '中值滤波', '双边滤波']:
                descriptions = {
                    '均值滤波': '简单平均\n快速但模糊',
                    '高斯滤波': '加权平均\n自然平滑',
                    '中值滤波': '排序取中值\n去椒盐噪声',
                    '双边滤波': '保持边缘\n高质量降噪'
                }
                desc = descriptions.get(filter_name, '')
                ax.text(0.02, 0.98, desc, transform=ax.transAxes,
                       bbox=dict(boxstyle="round,pad=0.2", facecolor="yellow", alpha=0.7),
                       fontsize=8, verticalalignment='top')
        
        fig.suptitle('🧽 磨皮车间 - 滤波技术对比展示', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        print("✅ 滤波对比展示完成")
        
        return filtered_images
    
    def demonstrate_bilateral_filter(self, image, figsize=(15, 10)):
        """
        详细演示双边滤波的参数效果
        
        Parameters:
        image (numpy.ndarray): 输入图像
        figsize (tuple): 显示尺寸
        """
        print("🔍 磨皮车间：正在演示双边滤波参数效果")
        
        # 添加噪声
        noisy_image = self.add_noise_to_image(image, 'gaussian', 0.1)
        
        # 不同参数的双边滤波
        bilateral_results = {}
        
        # 原图和噪声图
        bilateral_results['原始图像'] = image
        bilateral_results['噪声图像'] = noisy_image
        
        # 不同的双边滤波参数
        params = [
            (9, 20, 20),   # 低强度
            (9, 50, 50),   # 中强度
            (9, 80, 80),   # 高强度
            (15, 50, 50),  # 大滤波核
        ]
        
        param_names = ['低强度', '中强度', '高强度', '大滤波核']
        
        for i, (d, sigma_color, sigma_space) in enumerate(params):
            result = cv2.bilateralFilter(noisy_image, d, sigma_color, sigma_space)
            bilateral_results[f'双边滤波-{param_names[i]}'] = result
        
        # 创建展示图
        fig, axes = plt.subplots(2, 3, figsize=figsize)
        axes = axes.flatten()
        
        for i, (name, img) in enumerate(bilateral_results.items()):
            ax = axes[i]
            
            if len(img.shape) == 3:
                ax.imshow(img)
            else:
                ax.imshow(img, cmap='gray')
            
            ax.set_title(name, fontsize=12, fontweight='bold')
            ax.axis('off')
            
            # 添加参数说明
            if i >= 2 and i < 6:  # 双边滤波结果
                param_idx = i - 2
                d, sigma_color, sigma_space = params[param_idx]
                param_text = f"d={d}\nσ_color={sigma_color}\nσ_space={sigma_space}"
                ax.text(0.02, 0.98, param_text, transform=ax.transAxes,
                       bbox=dict(boxstyle="round,pad=0.2", facecolor="lightgreen", alpha=0.7),
                       fontsize=8, verticalalignment='top')
        
        fig.suptitle('🧽 双边滤波参数效果对比', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        print("📝 双边滤波参数说明:")
        print("   d: 滤波器直径 (影响处理范围)")
        print("   σ_color: 颜色相似性标准差 (控制颜色差异容忍度)")
        print("   σ_space: 空间标准差 (控制距离权重)")
        print("✅ 双边滤波演示完成")

# 使用示例
if __name__ == "__main__":
    # 创建磨皮车间
    filter_workshop = FilteringWorkshop()
    
    # 创建测试图像
    workshop = CaptureWorkshop()
    test_image = workshop.create_test_image(640, 480, 'checkerboard')
    
    # 滤波对比演示
    results = filter_workshop.apply_filters_comparison(test_image)
    
    # 双边滤波详细演示
    filter_workshop.demonstrate_bilateral_filter(test_image)
```

#### ✨ 美白车间：图像增强技术

美白车间负责调整图像的亮度、对比度和色彩平衡，让图像呈现出更好的视觉效果。

```python
# 示例8：美白车间 - 图像增强系统
import cv2
import numpy as np
import matplotlib.pyplot as plt

class EnhancementWorkshop:
    """
    美白车间类
    负责图像亮度、对比度和色彩增强
    """
    
    def __init__(self):
        """
        初始化美白车间
        """
        # 支持的增强技术
        self.enhancement_types = {
            'histogram_equalization': '直方图均衡化',
            'clahe': '自适应直方图均衡化',
            'gamma_correction': '伽马校正',
            'contrast_brightness': '对比度亮度调整',
            'color_balance': '色彩平衡'
        }
        
        print("✨ 美白车间初始化完成")
        print("💡 图像增强设备已就绪")
        print(f"📋 支持的增强技术: {list(self.enhancement_types.keys())}")
    
    def adjust_brightness_contrast(self, image, brightness=0, contrast=1.0):
        """
        调整图像的亮度和对比度
        
        Parameters:
        image (numpy.ndarray): 输入图像
        brightness (int): 亮度调整 (-100 到 100)
        contrast (float): 对比度调整 (0.5 到 3.0)
        
        Returns:
        numpy.ndarray: 调整后的图像
        """
        print(f"💡 美白车间：调整亮度 {brightness}, 对比度 {contrast}")
        
        # 转换为浮点数进行计算
        adjusted = image.astype(np.float32)
        
        # 应用对比度和亮度调整
        # 公式: new_pixel = contrast * old_pixel + brightness
        adjusted = contrast * adjusted + brightness
        
        # 限制像素值范围
        adjusted = np.clip(adjusted, 0, 255)
        
        return adjusted.astype(np.uint8)
    
    def gamma_correction(self, image, gamma=1.0):
        """
        伽马校正
        
        Parameters:
        image (numpy.ndarray): 输入图像
        gamma (float): 伽马值 (< 1 变亮, > 1 变暗)
        
        Returns:
        numpy.ndarray: 校正后的图像
        """
        print(f"🔆 美白车间：应用伽马校正 γ={gamma}")
        
        # 构建查找表
        inv_gamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** inv_gamma) * 255 
                         for i in np.arange(0, 256)]).astype("uint8")
        
        # 应用查找表
        corrected = cv2.LUT(image, table)
        
        return corrected
    
    def histogram_equalization(self, image):
        """
        直方图均衡化
        
        Parameters:
        image (numpy.ndarray): 输入图像
        
        Returns:
        numpy.ndarray: 均衡化后的图像
        """
        print("📊 美白车间：应用直方图均衡化")
        
        if len(image.shape) == 3:
            # 彩色图像：在YUV空间进行均衡化
            yuv = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)
            yuv[:, :, 0] = cv2.equalizeHist(yuv[:, :, 0])
            equalized = cv2.cvtColor(yuv, cv2.COLOR_YUV2RGB)
        else:
            # 灰度图像：直接均衡化
            equalized = cv2.equalizeHist(image)
        
        return equalized
    
    def clahe_enhancement(self, image, clip_limit=2.0, tile_grid_size=(8, 8)):
        """
        自适应直方图均衡化 (CLAHE)
        
        Parameters:
        image (numpy.ndarray): 输入图像
        clip_limit (float): 对比度限制
        tile_grid_size (tuple): 网格大小
        
        Returns:
        numpy.ndarray: 增强后的图像
        """
        print(f"📈 美白车间：应用CLAHE增强 (clip_limit={clip_limit})")
        
        # 创建CLAHE对象
        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
        
        if len(image.shape) == 3:
            # 彩色图像：在LAB空间的L通道进行CLAHE
            lab = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)
            lab[:, :, 0] = clahe.apply(lab[:, :, 0])
            enhanced = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
        else:
            # 灰度图像：直接应用CLAHE
            enhanced = clahe.apply(image)
        
        return enhanced
    
    def enhancement_comparison(self, image, figsize=(20, 15)):
        """
        对比展示不同增强技术的效果
        
        Parameters:
        image (numpy.ndarray): 输入图像
        figsize (tuple): 显示尺寸
        """
        print("✨ 美白车间：正在进行增强技术对比")
        
        # 创建一个偏暗的图像用于演示
        dark_image = self.adjust_brightness_contrast(image, brightness=-50, contrast=0.7)
        
        # 准备不同的增强结果
        enhanced_images = {}
        
        # 原图和暗图
        enhanced_images['原始图像'] = image
        enhanced_images['偏暗图像'] = dark_image
        
        # 亮度对比度调整
        brightness_enhanced = self.adjust_brightness_contrast(dark_image, brightness=30, contrast=1.3)
        enhanced_images['亮度对比度调整'] = brightness_enhanced
        
        # 伽马校正
        gamma_enhanced = self.gamma_correction(dark_image, gamma=0.7)
        enhanced_images['伽马校正'] = gamma_enhanced
        
        # 直方图均衡化
        hist_enhanced = self.histogram_equalization(dark_image)
        enhanced_images['直方图均衡化'] = hist_enhanced
        
        # CLAHE增强
        clahe_enhanced = self.clahe_enhancement(dark_image, clip_limit=3.0)
        enhanced_images['CLAHE增强'] = clahe_enhanced
        
        # 创建展示图
        fig, axes = plt.subplots(2, 3, figsize=figsize)
        axes = axes.flatten()
        
        for i, (enhancement_name, enhanced_img) in enumerate(enhanced_images.items()):
            ax = axes[i]
            
            if len(enhanced_img.shape) == 3:
                ax.imshow(enhanced_img)
            else:
                ax.imshow(enhanced_img, cmap='gray')
            
            ax.set_title(enhancement_name, fontsize=12, fontweight='bold')
            ax.axis('off')
            
            # 添加技术说明
            descriptions = {
                '亮度对比度调整': '线性调整\n+30亮度, 1.3对比度',
                '伽马校正': '非线性调整\nγ=0.7 提亮',
                '直方图均衡化': '全局对比度增强\n可能过度增强',
                'CLAHE增强': '局部自适应增强\n避免过度增强'
            }
            
            if enhancement_name in descriptions:
                desc = descriptions[enhancement_name]
                ax.text(0.02, 0.98, desc, transform=ax.transAxes,
                       bbox=dict(boxstyle="round,pad=0.2", facecolor="lightblue", alpha=0.7),
                       fontsize=8, verticalalignment='top')
        
        fig.suptitle('✨ 美白车间 - 图像增强技术对比', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        print("✅ 增强技术对比完成")
        
        return enhanced_images
    
    def interactive_gamma_correction(self, image, gamma_values=[0.5, 0.8, 1.0, 1.2, 1.5, 2.0]):
        """
        交互式伽马校正演示
        
        Parameters:
        image (numpy.ndarray): 输入图像
        gamma_values (list): 要演示的伽马值列表
        """
        print("🎚️ 美白车间：伽马校正参数演示")
        
        # 创建展示图
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        axes = axes.flatten()
        
        for i, gamma in enumerate(gamma_values):
            if i < len(axes):
                ax = axes[i]
                
                # 应用伽马校正
                corrected = self.gamma_correction(image, gamma)
                
                if len(corrected.shape) == 3:
                    ax.imshow(corrected)
                else:
                    ax.imshow(corrected, cmap='gray')
                
                # 设置标题
                if gamma < 1.0:
                    effect = "(变亮)"
                elif gamma > 1.0:
                    effect = "(变暗)"
                else:
                    effect = "(原始)"
                
                ax.set_title(f'γ = {gamma} {effect}', fontsize=12, fontweight='bold')
                ax.axis('off')
                
                # 添加效果说明
                if gamma != 1.0:
                    effect_desc = "提亮暗部" if gamma < 1.0 else "压暗亮部"
                    ax.text(0.02, 0.98, effect_desc, transform=ax.transAxes,
                           bbox=dict(boxstyle="round,pad=0.2", 
                                   facecolor="yellow" if gamma < 1.0 else "orange", 
                                   alpha=0.7),
                           fontsize=8, verticalalignment='top')
        
        fig.suptitle('🎚️ 伽马校正参数效果对比', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        print("📝 伽马校正原理:")
        print("   γ < 1.0: 提亮图像，增强暗部细节")
        print("   γ = 1.0: 保持原始图像")
        print("   γ > 1.0: 压暗图像，增强对比度")
        print("✅ 伽马校正演示完成")

# 使用示例
if __name__ == "__main__":
    # 创建美白车间
    enhancement_workshop = EnhancementWorkshop()
    
    # 创建测试图像
    workshop = CaptureWorkshop()
    test_image = workshop.create_test_image(640, 480, 'gradient')
    
    # 增强技术对比
    enhanced_results = enhancement_workshop.enhancement_comparison(test_image)
    
    # 伽马校正演示
    enhancement_workshop.interactive_gamma_correction(test_image)
```

现在我们的照片美颜工厂已经具备了三个专业车间：调色车间、磨皮车间和美白车间。每个车间都有自己的专业设备和处理流程，能够将原始图像转化为高质量的视觉作品。接下来我将继续添加第三节的特征检测与匹配内容... 

## 📚 第三节：图像侦探局的特征检测技术

### 35.3 特征检测与匹配

经过美颜工厂的精心处理，我们的图像已经变得完美无瑕。但是，真正的智能视觉应用需要的不仅仅是美丽的图像，更需要能够"理解"图像内容的能力。这就需要我们的**图像侦探局**！

#### 🕵️ 图像侦探局总览

想象一下一个高科技的图像侦探局，这里有最专业的"侦探"们在工作：

🔍 **边缘侦探部** - 专门负责寻找图像中的边缘和轮廓  
📍 **角点侦探部** - 擅长发现图像中的重要角点和关键点  
🔗 **匹配侦探部** - 负责在不同图像间寻找相似的特征  
📋 **模板侦探部** - 专门进行模板匹配和目标定位  

每个部门都有自己的专业技术和检测设备，让我们一一探索这些"侦探"的工作方式！

#### 🔍 边缘侦探部：边缘检测技术

边缘是图像中最重要的特征之一，它们定义了物体的轮廓和形状。

```python
# 示例9：边缘侦探部 - 边缘检测系统
import cv2
import numpy as np
import matplotlib.pyplot as plt

class EdgeDetectionDepartment:
    """
    边缘侦探部类
    负责各种边缘检测算法的实现和应用
    """
    
    def __init__(self):
        """
        初始化边缘侦探部
        """
        # 支持的边缘检测算法
        self.edge_algorithms = {
            'canny': 'Canny边缘检测 - 多阶段最优边缘检测',
            'sobel': 'Sobel边缘检测 - 梯度方向敏感',
            'laplacian': 'Laplacian边缘检测 - 二阶导数',
            'scharr': 'Scharr边缘检测 - 改进的Sobel',
            'roberts': 'Roberts边缘检测 - 对角线梯度'
        }
        
        print("🔍 边缘侦探部初始化完成")
        print("🕵️ 边缘检测设备已就绪")
        print(f"📋 支持的检测算法: {list(self.edge_algorithms.keys())}")
    
    def canny_edge_detection(self, image, low_threshold=50, high_threshold=150, 
                           kernel_size=3, l2_gradient=False):
        """
        Canny边缘检测
        
        Parameters:
        image (numpy.ndarray): 输入图像
        low_threshold (int): 低阈值
        high_threshold (int): 高阈值
        kernel_size (int): Sobel核大小
        l2_gradient (bool): 是否使用L2梯度
        
        Returns:
        numpy.ndarray: 边缘图像
        """
        print(f"🔍 边缘侦探部：执行Canny检测 (阈值: {low_threshold}-{high_threshold})")
        
        # 转换为灰度图像
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            gray = image.copy()
        
        # 应用高斯模糊以减少噪声
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Canny边缘检测
        edges = cv2.Canny(blurred, low_threshold, high_threshold, 
                         apertureSize=kernel_size, L2gradient=l2_gradient)
        
        print(f"✅ Canny检测完成，发现边缘点数: {np.sum(edges > 0)}")
        return edges
    
    def sobel_edge_detection(self, image, ksize=3, scale=1, delta=0):
        """
        Sobel边缘检测
        
        Parameters:
        image (numpy.ndarray): 输入图像
        ksize (int): Sobel核大小
        scale (float): 缩放因子
        delta (float): 偏移值
        
        Returns:
        tuple: (梯度x, 梯度y, 梯度幅值)
        """
        print(f"🔍 边缘侦探部：执行Sobel检测 (核大小: {ksize})")
        
        # 转换为灰度图像
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            gray = image.copy()
        
        # 计算x和y方向的梯度
        grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=ksize, scale=scale, delta=delta)
        grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=ksize, scale=scale, delta=delta)
        
        # 计算梯度幅值
        magnitude = np.sqrt(grad_x**2 + grad_y**2)
        magnitude = np.uint8(np.clip(magnitude, 0, 255))
        
        # 转换为uint8格式
        grad_x = np.uint8(np.clip(np.abs(grad_x), 0, 255))
        grad_y = np.uint8(np.clip(np.abs(grad_y), 0, 255))
        
        print(f"✅ Sobel检测完成")
        return grad_x, grad_y, magnitude
    
    def laplacian_edge_detection(self, image, ksize=1, scale=1, delta=0):
        """
        Laplacian边缘检测
        
        Parameters:
        image (numpy.ndarray): 输入图像
        ksize (int): 核大小
        scale (float): 缩放因子
        delta (float): 偏移值
        
        Returns:
        numpy.ndarray: 边缘图像
        """
        print(f"🔍 边缘侦探部：执行Laplacian检测")
        
        # 转换为灰度图像
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            gray = image.copy()
        
        # 应用高斯模糊
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        
        # Laplacian边缘检测
        laplacian = cv2.Laplacian(blurred, cv2.CV_64F, ksize=ksize, scale=scale, delta=delta)
        laplacian = np.uint8(np.clip(np.abs(laplacian), 0, 255))
        
        print(f"✅ Laplacian检测完成")
        return laplacian
    
    def comprehensive_edge_comparison(self, image, figsize=(20, 15)):
        """
        综合对比不同边缘检测算法
        
        Parameters:
        image (numpy.ndarray): 输入图像
        figsize (tuple): 显示尺寸
        """
        print("🔍 边缘侦探部：正在进行边缘检测算法对比")
        
        # 准备不同算法的结果
        edge_results = {}
        
        # 原始图像
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            gray = image.copy()
        
        edge_results['原始图像'] = image
        edge_results['灰度图像'] = gray
        
        # Canny边缘检测
        canny_edges = self.canny_edge_detection(image, 50, 150)
        edge_results['Canny边缘检测'] = canny_edges
        
        # Sobel边缘检测
        sobel_x, sobel_y, sobel_magnitude = self.sobel_edge_detection(image)
        edge_results['Sobel-X梯度'] = sobel_x
        edge_results['Sobel-Y梯度'] = sobel_y
        edge_results['Sobel梯度幅值'] = sobel_magnitude
        
        # Laplacian边缘检测
        laplacian_edges = self.laplacian_edge_detection(image)
        edge_results['Laplacian边缘检测'] = laplacian_edges
        
        # Scharr边缘检测
        scharr_x = cv2.Scharr(gray, cv2.CV_64F, 1, 0)
        scharr_y = cv2.Scharr(gray, cv2.CV_64F, 0, 1)
        scharr_magnitude = np.sqrt(scharr_x**2 + scharr_y**2)
        scharr_magnitude = np.uint8(np.clip(scharr_magnitude, 0, 255))
        edge_results['Scharr边缘检测'] = scharr_magnitude
        
        # 创建展示图
        fig, axes = plt.subplots(3, 3, figsize=figsize)
        axes = axes.flatten()
        
        for i, (method_name, result_img) in enumerate(edge_results.items()):
            if i < len(axes):
                ax = axes[i]
                
                if method_name == '原始图像':
                    if len(result_img.shape) == 3:
                        ax.imshow(result_img)
                    else:
                        ax.imshow(result_img, cmap='gray')
                else:
                    ax.imshow(result_img, cmap='gray')
                
                ax.set_title(method_name, fontsize=12, fontweight='bold')
                ax.axis('off')
                
                # 添加算法说明
                descriptions = {
                    'Canny边缘检测': '多阶段检测\n抗噪声能力强',
                    'Sobel-X梯度': '水平方向\n梯度检测',
                    'Sobel-Y梯度': '垂直方向\n梯度检测',
                    'Sobel梯度幅值': 'X和Y梯度\n的合成结果',
                    'Laplacian边缘检测': '二阶导数\n对噪声敏感',
                    'Scharr边缘检测': '改进的Sobel\n更精确的梯度'
                }
                
                if method_name in descriptions:
                    desc = descriptions[method_name]
                    ax.text(0.02, 0.98, desc, transform=ax.transAxes,
                           bbox=dict(boxstyle="round,pad=0.2", facecolor="lightblue", alpha=0.7),
                           fontsize=8, verticalalignment='top')
        
        # 隐藏多余的子图
        for i in range(len(edge_results), len(axes)):
            axes[i].axis('off')
        
        fig.suptitle('🔍 边缘侦探部 - 边缘检测算法全面对比', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        print("✅ 边缘检测对比完成")
        return edge_results
    
    def canny_parameter_tuning(self, image, figsize=(18, 12)):
        """
        Canny边缘检测参数调优演示
        
        Parameters:
        image (numpy.ndarray): 输入图像
        figsize (tuple): 显示尺寸
        """
        print("🎚️ 边缘侦探部：Canny参数调优演示")
        
        # 不同参数组合
        threshold_combinations = [
            (30, 80),    # 低阈值组合
            (50, 100),   # 中等阈值组合
            (50, 150),   # 标准阈值组合
            (100, 200),  # 高阈值组合
            (150, 250),  # 很高阈值组合
        ]
        
        # 创建展示图
        fig, axes = plt.subplots(2, 3, figsize=figsize)
        axes = axes.flatten()
        
        # 显示原图
        if len(image.shape) == 3:
            axes[0].imshow(image)
        else:
            axes[0].imshow(image, cmap='gray')
        axes[0].set_title('原始图像', fontsize=12, fontweight='bold')
        axes[0].axis('off')
        
        # 不同参数的Canny检测结果
        for i, (low_thresh, high_thresh) in enumerate(threshold_combinations):
            if i + 1 < len(axes):
                ax = axes[i + 1]
                
                # 应用Canny检测
                edges = self.canny_edge_detection(image, low_thresh, high_thresh)
                
                ax.imshow(edges, cmap='gray')
                ax.set_title(f'阈值: {low_thresh}-{high_thresh}', fontsize=12, fontweight='bold')
                ax.axis('off')
                
                # 统计边缘点数
                edge_count = np.sum(edges > 0)
                ax.text(0.02, 0.98, f'边缘点数: {edge_count}', transform=ax.transAxes,
                       bbox=dict(boxstyle="round,pad=0.2", facecolor="yellow", alpha=0.7),
                       fontsize=8, verticalalignment='top')
        
        fig.suptitle('🎚️ Canny边缘检测参数调优对比', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        print("📝 Canny参数调优建议:")
        print("   • 低阈值: 检测弱边缘，值过低会引入噪声")
        print("   • 高阈值: 检测强边缘，值过高会丢失细节")
        print("   • 高阈值通常是低阈值的2-3倍")
        print("✅ 参数调优演示完成")

# 使用示例
if __name__ == "__main__":
    # 创建边缘侦探部
    edge_dept = EdgeDetectionDepartment()
    
    # 创建测试图像
    workshop = CaptureWorkshop()
    test_image = workshop.create_test_image(640, 480, 'checkerboard')
    
    # 综合边缘检测对比
    edge_results = edge_dept.comprehensive_edge_comparison(test_image)
    
    # Canny参数调优演示
    edge_dept.canny_parameter_tuning(test_image)
```

#### 📍 角点侦探部：角点检测技术

角点是图像中信息最丰富的特征点，它们在图像识别和匹配中起着关键作用。

```python
# 示例10：角点侦探部 - 角点检测系统
import cv2
import numpy as np
import matplotlib.pyplot as plt

class CornerDetectionDepartment:
    """
    角点侦探部类
    负责各种角点检测算法的实现和应用
    """
    
    def __init__(self):
        """
        初始化角点侦探部
        """
        # 支持的角点检测算法
        self.corner_algorithms = {
            'harris': 'Harris角点检测 - 经典角点检测算法',
            'shi_tomasi': 'Shi-Tomasi角点检测 - 改进的Harris',
            'fast': 'FAST角点检测 - 快速角点检测',
            'orb': 'ORB特征点检测 - 旋转不变特征',
            'sift': 'SIFT特征点检测 - 尺度不变特征'
        }
        
        print("📍 角点侦探部初始化完成")
        print("🎯 角点检测设备已就绪")
        print(f"📋 支持的检测算法: {list(self.corner_algorithms.keys())}")
    
    def harris_corner_detection(self, image, k=0.04, threshold=0.01):
        """
        Harris角点检测
        
        Parameters:
        image (numpy.ndarray): 输入图像
        k (float): Harris检测器自由参数
        threshold (float): 角点阈值
        
        Returns:
        tuple: (角点响应图, 角点坐标列表)
        """
        print(f"📍 角点侦探部：执行Harris角点检测 (k={k}, threshold={threshold})")
        
        # 转换为灰度图像
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            gray = image.copy()
        
        # Harris角点检测
        gray = np.float32(gray)
        harris_response = cv2.cornerHarris(gray, 2, 3, k)
        
        # 角点阈值化
        corner_mask = harris_response > threshold * harris_response.max()
        corners = np.argwhere(corner_mask)
        
        print(f"✅ Harris检测完成，发现角点数: {len(corners)}")
        return harris_response, corners
    
    def shi_tomasi_corner_detection(self, image, max_corners=100, quality_level=0.01, min_distance=10):
        """
        Shi-Tomasi角点检测
        
        Parameters:
        image (numpy.ndarray): 输入图像
        max_corners (int): 最大角点数
        quality_level (float): 质量水平
        min_distance (float): 最小距离
        
        Returns:
        numpy.ndarray: 角点坐标数组
        """
        print(f"📍 角点侦探部：执行Shi-Tomasi检测 (最大角点数: {max_corners})")
        
        # 转换为灰度图像
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            gray = image.copy()
        
        # Shi-Tomasi角点检测
        corners = cv2.goodFeaturesToTrack(gray, max_corners, quality_level, min_distance)
        
        if corners is not None:
            corners = np.int32(corners).reshape(-1, 2)
            print(f"✅ Shi-Tomasi检测完成，发现角点数: {len(corners)}")
        else:
            corners = np.array([])
            print("⚠️ 未检测到角点")
        
        return corners
    
    def fast_corner_detection(self, image, threshold=10, nonmax_suppression=True):
        """
        FAST角点检测
        
        Parameters:
        image (numpy.ndarray): 输入图像
        threshold (int): FAST阈值
        nonmax_suppression (bool): 是否进行非极大值抑制
        
        Returns:
        list: 角点关键点列表
        """
        print(f"📍 角点侦探部：执行FAST检测 (阈值: {threshold})")
        
        # 转换为灰度图像
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            gray = image.copy()
        
        # 创建FAST检测器
        fast = cv2.FastFeatureDetector_create(threshold=threshold, 
                                             nonmaxSuppression=nonmax_suppression)
        
        # 检测关键点
        keypoints = fast.detect(gray, None)
        
        print(f"✅ FAST检测完成，发现关键点数: {len(keypoints)}")
        return keypoints
    
    def orb_feature_detection(self, image, n_features=500):
        """
        ORB特征点检测
        
        Parameters:
        image (numpy.ndarray): 输入图像
        n_features (int): 最大特征点数
        
        Returns:
        tuple: (关键点列表, 描述符)
        """
        print(f"📍 角点侦探部：执行ORB特征检测 (最大特征数: {n_features})")
        
        # 转换为灰度图像
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            gray = image.copy()
        
        # 创建ORB检测器
        orb = cv2.ORB_create(nfeatures=n_features)
        
        # 检测关键点和计算描述符
        keypoints, descriptors = orb.detectAndCompute(gray, None)
        
        print(f"✅ ORB检测完成，发现特征点数: {len(keypoints)}")
        return keypoints, descriptors
    
    def corner_detection_comparison(self, image, figsize=(20, 15)):
        """
        综合对比不同角点检测算法
        
        Parameters:
        image (numpy.ndarray): 输入图像
        figsize (tuple): 显示尺寸
        """
        print("📍 角点侦探部：正在进行角点检测算法对比")
        
        # 创建展示图
        fig, axes = plt.subplots(2, 3, figsize=figsize)
        axes = axes.flatten()
        
        # 原始图像
        axes[0].imshow(image if len(image.shape) == 3 else image, 
                      cmap='gray' if len(image.shape) == 2 else None)
        axes[0].set_title('原始图像', fontsize=12, fontweight='bold')
        axes[0].axis('off')
        
        # Harris角点检测
        harris_response, harris_corners = self.harris_corner_detection(image)
        axes[1].imshow(harris_response, cmap='hot')
        axes[1].set_title('Harris角点响应', fontsize=12, fontweight='bold')
        axes[1].axis('off')
        
        # Shi-Tomasi角点检测
        shi_tomasi_corners = self.shi_tomasi_corner_detection(image, max_corners=50)
        image_with_shi_tomasi = image.copy()
        if len(image_with_shi_tomasi.shape) == 2:
            image_with_shi_tomasi = cv2.cvtColor(image_with_shi_tomasi, cv2.COLOR_GRAY2RGB)
        
        for corner in shi_tomasi_corners:
            cv2.circle(image_with_shi_tomasi, tuple(corner), 3, (255, 0, 0), -1)
        
        axes[2].imshow(image_with_shi_tomasi)
        axes[2].set_title(f'Shi-Tomasi角点 ({len(shi_tomasi_corners)}个)', fontsize=12, fontweight='bold')
        axes[2].axis('off')
        
        # FAST角点检测
        fast_keypoints = self.fast_corner_detection(image)
        image_with_fast = image.copy()
        if len(image_with_fast.shape) == 2:
            image_with_fast = cv2.cvtColor(image_with_fast, cv2.COLOR_GRAY2RGB)
        else:
            image_with_fast = cv2.cvtColor(image_with_fast, cv2.COLOR_RGB2BGR)
        
        image_with_fast = cv2.drawKeypoints(image_with_fast, fast_keypoints, None, 
                                          color=(0, 255, 0), flags=0)
        image_with_fast = cv2.cvtColor(image_with_fast, cv2.COLOR_BGR2RGB)
        
        axes[3].imshow(image_with_fast)
        axes[3].set_title(f'FAST关键点 ({len(fast_keypoints)}个)', fontsize=12, fontweight='bold')
        axes[3].axis('off')
        
        # ORB特征检测
        orb_keypoints, orb_descriptors = self.orb_feature_detection(image, n_features=100)
        image_with_orb = image.copy()
        if len(image_with_orb.shape) == 2:
            image_with_orb = cv2.cvtColor(image_with_orb, cv2.COLOR_GRAY2RGB)
        else:
            image_with_orb = cv2.cvtColor(image_with_orb, cv2.COLOR_RGB2BGR)
        
        image_with_orb = cv2.drawKeypoints(image_with_orb, orb_keypoints, None, 
                                         color=(255, 255, 0), 
                                         flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        image_with_orb = cv2.cvtColor(image_with_orb, cv2.COLOR_BGR2RGB)
        
        axes[4].imshow(image_with_orb)
        axes[4].set_title(f'ORB特征点 ({len(orb_keypoints)}个)', fontsize=12, fontweight='bold')
        axes[4].axis('off')
        
        # 算法对比总结
        axes[5].axis('off')
        summary_text = f"""
📊 角点检测算法对比总结

🎯 Harris角点: {len(harris_corners)} 个
• 特点: 旋转不变，计算量中等
• 适用: 经典角点检测

🎯 Shi-Tomasi: {len(shi_tomasi_corners)} 个  
• 特点: 改进的Harris，更稳定
• 适用: 跟踪特征点

⚡ FAST: {len(fast_keypoints)} 个
• 特点: 速度快，实时应用
• 适用: 移动设备，视频处理

🔄 ORB: {len(orb_keypoints)} 个
• 特点: 旋转和尺度不变
• 适用: 图像匹配，SLAM
        """
        
        axes[5].text(0.1, 0.9, summary_text, transform=axes[5].transAxes,
                    fontsize=10, verticalalignment='top',
                    bbox=dict(boxstyle="round,pad=0.5", facecolor="lightblue", alpha=0.8))
        
        fig.suptitle('📍 角点侦探部 - 角点检测算法全面对比', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        print("✅ 角点检测对比完成")
        
        return {
            'harris': (harris_response, harris_corners),
            'shi_tomasi': shi_tomasi_corners,
            'fast': fast_keypoints,
            'orb': (orb_keypoints, orb_descriptors)
        }

# 使用示例
if __name__ == "__main__":
    # 创建角点侦探部
    corner_dept = CornerDetectionDepartment()
    
    # 创建测试图像
    workshop = CaptureWorkshop()
    test_image = workshop.create_test_image(640, 480, 'checkerboard')
    
    # 综合角点检测对比
    corner_results = corner_dept.corner_detection_comparison(test_image)
```

现在我们的图像侦探局已经拥有了专业的边缘侦探部和角点侦探部。接下来我将继续添加匹配侦探部和模板侦探部，以及最后的综合项目部分...

#### 🔗 匹配侦探部：特征匹配技术

匹配侦探部负责在不同图像间寻找相似的特征，这是实现图像拼接、目标识别等应用的基础。

```python
# 示例11：匹配侦探部 - 特征匹配系统
import cv2
import numpy as np
import matplotlib.pyplot as plt

class FeatureMatchingDepartment:
    """
    匹配侦探部类
    负责特征匹配和图像对应关系建立
    """
    
    def __init__(self):
        """
        初始化匹配侦探部
        """
        # 支持的匹配算法
        self.matching_algorithms = {
            'brute_force': '暴力匹配 - 穷尽搜索最佳匹配',
            'flann': 'FLANN匹配 - 快速近似匹配',
            'ratio_test': '比值测试 - Lowe比值测试',
            'cross_check': '交叉验证 - 双向匹配验证'
        }
        
        print("🔗 匹配侦探部初始化完成")
        print("🔍 特征匹配设备已就绪")
        print(f"📋 支持的匹配算法: {list(self.matching_algorithms.keys())}")
    
    def orb_feature_matching(self, image1, image2, max_features=1000):
        """
        使用ORB特征进行图像匹配
        
        Parameters:
        image1 (numpy.ndarray): 第一张图像
        image2 (numpy.ndarray): 第二张图像
        max_features (int): 最大特征点数
        
        Returns:
        tuple: (关键点1, 关键点2, 匹配结果, 匹配图像)
        """
        print(f"🔗 匹配侦探部：执行ORB特征匹配 (最大特征数: {max_features})")
        
        # 转换为灰度图像
        gray1 = cv2.cvtColor(image1, cv2.COLOR_RGB2GRAY) if len(image1.shape) == 3 else image1
        gray2 = cv2.cvtColor(image2, cv2.COLOR_RGB2GRAY) if len(image2.shape) == 3 else image2
        
        # 创建ORB检测器
        orb = cv2.ORB_create(nfeatures=max_features)
        
        # 检测关键点和描述符
        kp1, des1 = orb.detectAndCompute(gray1, None)
        kp2, des2 = orb.detectAndCompute(gray2, None)
        
        print(f"   图像1特征点数: {len(kp1)}")
        print(f"   图像2特征点数: {len(kp2)}")
        
        if des1 is not None and des2 is not None:
            # 创建暴力匹配器
            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
            
            # 进行特征匹配
            matches = bf.match(des1, des2)
            
            # 按距离排序
            matches = sorted(matches, key=lambda x: x.distance)
            
            # 绘制匹配结果
            match_img = cv2.drawMatches(image1, kp1, image2, kp2, matches[:50], None, 
                                      flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
            
            print(f"✅ ORB匹配完成，发现匹配对数: {len(matches)}")
            return kp1, kp2, matches, match_img
        else:
            print("❌ 特征检测失败")
            return None, None, [], None
    
    def sift_feature_matching_with_ratio_test(self, image1, image2):
        """
        使用SIFT特征和比值测试进行匹配
        
        Parameters:
        image1 (numpy.ndarray): 第一张图像
        image2 (numpy.ndarray): 第二张图像
        
        Returns:
        tuple: (好的匹配点, 匹配图像)
        """
        print("🔗 匹配侦探部：执行SIFT特征匹配 (比值测试)")
        
        # 转换为灰度图像
        gray1 = cv2.cvtColor(image1, cv2.COLOR_RGB2GRAY) if len(image1.shape) == 3 else image1
        gray2 = cv2.cvtColor(image2, cv2.COLOR_RGB2GRAY) if len(image2.shape) == 3 else image2
        
        try:
            # 创建SIFT检测器
            sift = cv2.SIFT_create()
            
            # 检测关键点和描述符
            kp1, des1 = sift.detectAndCompute(gray1, None)
            kp2, des2 = sift.detectAndCompute(gray2, None)
            
            print(f"   图像1 SIFT特征点数: {len(kp1)}")
            print(f"   图像2 SIFT特征点数: {len(kp2)}")
            
            if des1 is not None and des2 is not None:
                # 创建FLANN匹配器
                FLANN_INDEX_KDTREE = 1
                index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
                search_params = dict(checks=50)
                flann = cv2.FlannBasedMatcher(index_params, search_params)
                
                # K近邻匹配
                matches = flann.knnMatch(des1, des2, k=2)
                
                # Lowe比值测试
                good_matches = []
                for match_pair in matches:
                    if len(match_pair) == 2:
                        m, n = match_pair
                        if m.distance < 0.7 * n.distance:
                            good_matches.append(m)
                
                # 绘制好的匹配
                match_img = cv2.drawMatches(image1, kp1, image2, kp2, good_matches, None,
                                          flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
                
                print(f"✅ SIFT匹配完成，好的匹配对数: {len(good_matches)}")
                return good_matches, match_img
            else:
                print("❌ SIFT特征检测失败")
                return [], None
                
        except Exception as e:
            print(f"❌ SIFT匹配出错: {e}")
            print("💡 提示: 可能需要安装opencv-contrib-python")
            return [], None
    
    def template_matching_demo(self, image, template, methods=None):
        """
        模板匹配演示
        
        Parameters:
        image (numpy.ndarray): 源图像
        template (numpy.ndarray): 模板图像
        methods (list): 匹配方法列表
        
        Returns:
        dict: 不同方法的匹配结果
        """
        print("🔗 匹配侦探部：执行模板匹配演示")
        
        if methods is None:
            methods = [
                ('TM_CCOEFF', cv2.TM_CCOEFF),
                ('TM_CCOEFF_NORMED', cv2.TM_CCOEFF_NORMED),
                ('TM_CCORR', cv2.TM_CCORR),
                ('TM_CCORR_NORMED', cv2.TM_CCORR_NORMED),
                ('TM_SQDIFF', cv2.TM_SQDIFF),
                ('TM_SQDIFF_NORMED', cv2.TM_SQDIFF_NORMED)
            ]
        
        # 转换为灰度图像
        gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) if len(image.shape) == 3 else image
        gray_template = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY) if len(template.shape) == 3 else template
        
        results = {}
        
        for method_name, method in methods:
            # 执行模板匹配
            result = cv2.matchTemplate(gray_image, gray_template, method)
            
            # 找到最佳匹配位置
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
            # 根据方法选择最佳位置
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                best_loc = min_loc
                best_val = min_val
            else:
                best_loc = max_loc
                best_val = max_val
            
            # 绘制匹配结果
            h, w = gray_template.shape
            result_image = image.copy()
            cv2.rectangle(result_image, best_loc, (best_loc[0] + w, best_loc[1] + h), (255, 0, 0), 2)
            
            results[method_name] = {
                'result_map': result,
                'best_location': best_loc,
                'best_value': best_val,
                'result_image': result_image
            }
            
            print(f"   {method_name}: 最佳位置 {best_loc}, 匹配值 {best_val:.4f}")
        
        print("✅ 模板匹配演示完成")
        return results
    
    def comprehensive_matching_demo(self, image1, image2, figsize=(20, 15)):
        """
        综合匹配演示
        
        Parameters:
        image1 (numpy.ndarray): 第一张图像
        image2 (numpy.ndarray): 第二张图像
        figsize (tuple): 显示尺寸
        """
        print("🔗 匹配侦探部：正在进行综合匹配演示")
        
        # 创建展示图
        fig, axes = plt.subplots(2, 2, figsize=figsize)
        
        # 显示原始图像
        axes[0, 0].imshow(image1)
        axes[0, 0].set_title('图像1', fontsize=12, fontweight='bold')
        axes[0, 0].axis('off')
        
        axes[0, 1].imshow(image2) 
        axes[0, 1].set_title('图像2', fontsize=12, fontweight='bold')
        axes[0, 1].axis('off')
        
        # ORB特征匹配
        kp1, kp2, orb_matches, orb_match_img = self.orb_feature_matching(image1, image2)
        if orb_match_img is not None:
            axes[1, 0].imshow(orb_match_img)
            axes[1, 0].set_title(f'ORB特征匹配 ({len(orb_matches)}个匹配)', fontsize=12, fontweight='bold')
        else:
            axes[1, 0].text(0.5, 0.5, 'ORB匹配失败', ha='center', va='center', 
                           transform=axes[1, 0].transAxes, fontsize=12)
            axes[1, 0].set_title('ORB特征匹配', fontsize=12, fontweight='bold')
        axes[1, 0].axis('off')
        
        # SIFT特征匹配 (如果可用)
        sift_matches, sift_match_img = self.sift_feature_matching_with_ratio_test(image1, image2)
        if sift_match_img is not None:
            axes[1, 1].imshow(sift_match_img)
            axes[1, 1].set_title(f'SIFT特征匹配 ({len(sift_matches)}个好匹配)', fontsize=12, fontweight='bold')
        else:
            axes[1, 1].text(0.5, 0.5, 'SIFT匹配不可用\n需要opencv-contrib', 
                           ha='center', va='center', transform=axes[1, 1].transAxes, fontsize=10)
            axes[1, 1].set_title('SIFT特征匹配', fontsize=12, fontweight='bold')
        axes[1, 1].axis('off')
        
        fig.suptitle('🔗 匹配侦探部 - 特征匹配技术对比', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        print("✅ 综合匹配演示完成")

# 使用示例
if __name__ == "__main__":
    # 创建匹配侦探部
    matching_dept = FeatureMatchingDepartment()
    
    # 创建测试图像
    workshop = CaptureWorkshop()
    test_image1 = workshop.create_test_image(320, 240, 'checkerboard')
    test_image2 = workshop.create_test_image(320, 240, 'gradient')
    
    # 综合匹配演示
    matching_dept.comprehensive_matching_demo(test_image1, test_image2)
```

## 📚 第四节：智能文档扫描仪综合项目

### 35.4 综合实战项目：智能文档扫描仪

现在，让我们将所有学到的技术整合起来，创建一个真正有实用价值的企业级项目——智能文档扫描仪！

#### 📱 项目概述

我们要开发一个智能文档扫描仪，它能够：

🔍 **自动检测文档边缘** - 使用边缘检测技术找到文档轮廓  
📐 **智能透视矫正** - 使用几何变换将倾斜的文档拉直  
✨ **图像质量增强** - 使用图像增强技术优化文档清晰度  
💾 **多格式输出** - 支持多种格式保存处理后的文档  

这是一个完整的产品级项目，展示了从原型到产品的完整开发流程。

```python
# 示例12：智能文档扫描仪 - 完整项目实现
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import json
from datetime import datetime

class SmartDocumentScanner:
    """
    智能文档扫描仪类
    集成了边缘检测、角点检测、透视变换和图像增强技术
    """
    
    def __init__(self, output_dir="smart_scanner_output"):
        """
        初始化智能文档扫描仪
        
        Parameters:
        output_dir (str): 输出目录
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # 处理历史记录
        self.scan_history = []
        
        # 配置参数
        self.config = {
            'edge_detection': {
                'canny_low': 50,
                'canny_high': 150,
                'blur_kernel': 5
            },
            'contour_detection': {
                'min_area': 1000,
                'epsilon_factor': 0.02
            },
            'enhancement': {
                'clahe_clip_limit': 2.0,
                'gamma': 1.2
            }
        }
        
        print("📱 智能文档扫描仪初始化完成")
        print(f"📁 输出目录: {self.output_dir}")
    
    def detect_document_edges(self, image):
        """
        检测文档边缘
        
        Parameters:
        image (numpy.ndarray): 输入图像
        
        Returns:
        tuple: (边缘图像, 轮廓列表)
        """
        print("🔍 正在检测文档边缘...")
        
        # 转换为灰度图像
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) if len(image.shape) == 3 else image
        
        # 高斯模糊
        blurred = cv2.GaussianBlur(gray, (self.config['edge_detection']['blur_kernel'], 
                                         self.config['edge_detection']['blur_kernel']), 0)
        
        # Canny边缘检测
        edges = cv2.Canny(blurred, 
                         self.config['edge_detection']['canny_low'], 
                         self.config['edge_detection']['canny_high'])
        
        # 查找轮廓
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # 按面积排序轮廓
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        
        print(f"   发现 {len(contours)} 个轮廓")
        print("✅ 文档边缘检测完成")
        
        return edges, contours
    
    def find_document_corners(self, contours, image_shape):
        """
        寻找文档的四个角点
        
        Parameters:
        contours (list): 轮廓列表
        image_shape (tuple): 图像尺寸
        
        Returns:
        numpy.ndarray: 四个角点坐标，如果未找到返回None
        """
        print("📍 正在寻找文档角点...")
        
        min_area = self.config['contour_detection']['min_area']
        epsilon_factor = self.config['contour_detection']['epsilon_factor']
        
        for contour in contours:
            # 检查轮廓面积
            area = cv2.contourArea(contour)
            if area < min_area:
                continue
            
            # 轮廓近似
            epsilon = epsilon_factor * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            
            # 如果近似轮廓有4个点，可能是文档
            if len(approx) == 4:
                print(f"   找到四边形轮廓，面积: {area:.0f}")
                print("✅ 文档角点检测完成")
                return approx.reshape(4, 2)
        
        print("⚠️ 未找到合适的四边形轮廓，使用图像边界")
        h, w = image_shape[:2]
        return np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], dtype=np.float32)
    
    def order_points(self, pts):
        """
        对四个点进行排序：左上、右上、右下、左下
        
        Parameters:
        pts (numpy.ndarray): 四个点的坐标
        
        Returns:
        numpy.ndarray: 排序后的点坐标
        """
        # 计算每个点的坐标和
        sum_coords = pts.sum(axis=1)
        diff_coords = np.diff(pts, axis=1)
        
        # 左上角点的坐标和最小，右下角点的坐标和最大
        rect = np.zeros((4, 2), dtype=np.float32)
        rect[0] = pts[np.argmin(sum_coords)]  # 左上
        rect[2] = pts[np.argmax(sum_coords)]  # 右下
        
        # 右上角点的差值最小，左下角点的差值最大
        rect[1] = pts[np.argmin(diff_coords)]  # 右上
        rect[3] = pts[np.argmax(diff_coords)]  # 左下
        
        return rect
    
    def perspective_transform(self, image, corners):
        """
        执行透视变换
        
        Parameters:
        image (numpy.ndarray): 输入图像
        corners (numpy.ndarray): 四个角点
        
        Returns:
        numpy.ndarray: 变换后的图像
        """
        print("📐 正在执行透视变换...")
        
        # 排序角点
        ordered_corners = self.order_points(corners)
        
        # 计算目标尺寸
        (tl, tr, br, bl) = ordered_corners
        
        # 计算新图像的宽度和高度
        width_top = np.sqrt((tr[0] - tl[0]) ** 2 + (tr[1] - tl[1]) ** 2)
        width_bottom = np.sqrt((br[0] - bl[0]) ** 2 + (br[1] - bl[1]) ** 2)
        max_width = max(int(width_top), int(width_bottom))
        
        height_left = np.sqrt((tl[0] - bl[0]) ** 2 + (tl[1] - bl[1]) ** 2)
        height_right = np.sqrt((tr[0] - br[0]) ** 2 + (tr[1] - br[1]) ** 2)
        max_height = max(int(height_left), int(height_right))
        
        # 定义目标点
        dst_points = np.array([
            [0, 0],
            [max_width - 1, 0],
            [max_width - 1, max_height - 1],
            [0, max_height - 1]
        ], dtype=np.float32)
        
        # 计算透视变换矩阵
        transform_matrix = cv2.getPerspectiveTransform(ordered_corners, dst_points)
        
        # 执行透视变换
        warped = cv2.warpPerspective(image, transform_matrix, (max_width, max_height))
        
        print(f"   变换后尺寸: {max_width} x {max_height}")
        print("✅ 透视变换完成")
        
        return warped
    
    def enhance_document_image(self, image):
        """
        增强文档图像质量
        
        Parameters:
        image (numpy.ndarray): 输入图像
        
        Returns:
        numpy.ndarray: 增强后的图像
        """
        print("✨ 正在增强文档图像...")
        
        # 转换为灰度图像
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            gray = image.copy()
        
        # CLAHE自适应直方图均衡化
        clahe = cv2.createCLAHE(clipLimit=self.config['enhancement']['clahe_clip_limit'])
        enhanced = clahe.apply(gray)
        
        # 伽马校正
        gamma = self.config['enhancement']['gamma']
        inv_gamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
        enhanced = cv2.LUT(enhanced, table)
        
        # 双边滤波去噪
        denoised = cv2.bilateralFilter(enhanced, 9, 75, 75)
        
        print("✅ 图像增强完成")
        return denoised
    
    def scan_document(self, image, save_intermediate=True):
        """
        完整的文档扫描流程
        
        Parameters:
        image (numpy.ndarray): 输入图像
        save_intermediate (bool): 是否保存中间步骤图像
        
        Returns:
        dict: 包含所有处理步骤结果的字典
        """
        print("\n📱 开始智能文档扫描流程...")
        print("=" * 50)
        
        results = {
            'original': image,
            'timestamp': datetime.now().isoformat(),
            'config': self.config.copy()
        }
        
        # 步骤1: 检测文档边缘
        edges, contours = self.detect_document_edges(image)
        results['edges'] = edges
        results['contours'] = contours
        
        # 步骤2: 寻找文档角点
        corners = self.find_document_corners(contours, image.shape)
        results['corners'] = corners
        
        # 步骤3: 透视变换
        if corners is not None:
            warped = self.perspective_transform(image, corners)
            results['warped'] = warped
            
            # 步骤4: 图像增强
            enhanced = self.enhance_document_image(warped)
            results['enhanced'] = enhanced
            
            # 保存最终结果
            if save_intermediate:
                scan_id = len(self.scan_history)
                self.save_scan_results(results, scan_id)
            
            self.scan_history.append({
                'scan_id': len(self.scan_history),
                'timestamp': results['timestamp'],
                'success': True,
                'corners_found': len(corners) == 4,
                'final_size': enhanced.shape
            })
            
            print("=" * 50)
            print("🎉 文档扫描完成！")
            print(f"📊 最终文档尺寸: {enhanced.shape[1]} x {enhanced.shape[0]}")
            
        else:
            print("❌ 文档扫描失败：未能检测到有效角点")
            results['enhanced'] = None
            
            self.scan_history.append({
                'scan_id': len(self.scan_history),
                'timestamp': results['timestamp'],
                'success': False,
                'corners_found': False,
                'final_size': None
            })
        
        return results
    
    def save_scan_results(self, results, scan_id):
        """
        保存扫描结果
        
        Parameters:
        results (dict): 扫描结果
        scan_id (int): 扫描ID
        """
        print(f"💾 正在保存扫描结果 (ID: {scan_id})...")
        
        scan_dir = self.output_dir / f"scan_{scan_id:03d}"
        scan_dir.mkdir(exist_ok=True)
        
        # 保存各个步骤的图像
        cv2.imwrite(str(scan_dir / "01_original.jpg"), 
                   cv2.cvtColor(results['original'], cv2.COLOR_RGB2BGR))
        cv2.imwrite(str(scan_dir / "02_edges.jpg"), results['edges'])
        
        if results.get('warped') is not None:
            cv2.imwrite(str(scan_dir / "03_warped.jpg"), 
                       cv2.cvtColor(results['warped'], cv2.COLOR_RGB2BGR))
        
        if results.get('enhanced') is not None:
            cv2.imwrite(str(scan_dir / "04_final.jpg"), results['enhanced'])
        
        # 保存扫描配置和结果信息
        metadata = {
            'scan_id': scan_id,
            'timestamp': results['timestamp'],
            'config': results['config'],
            'corners': results['corners'].tolist() if results.get('corners') is not None else None,
            'processing_steps': ['edge_detection', 'corner_detection', 'perspective_transform', 'enhancement']
        }
        
        with open(scan_dir / "metadata.json", 'w') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        
        print(f"✅ 扫描结果已保存到: {scan_dir}")
    
    def visualize_scan_process(self, results, figsize=(20, 15)):
        """
        可视化扫描过程
        
        Parameters:
        results (dict): 扫描结果
        figsize (tuple): 显示尺寸
        """
        print("🖼️ 正在可视化扫描过程...")
        
        fig, axes = plt.subplots(2, 3, figsize=figsize)
        axes = axes.flatten()
        
        # 原始图像
        axes[0].imshow(results['original'])
        axes[0].set_title('1. 原始图像', fontsize=12, fontweight='bold')
        axes[0].axis('off')
        
        # 边缘检测
        axes[1].imshow(results['edges'], cmap='gray')
        axes[1].set_title('2. 边缘检测', fontsize=12, fontweight='bold')
        axes[1].axis('off')
        
        # 角点检测
        corners_img = results['original'].copy()
        if results.get('corners') is not None:
            corners = results['corners'].astype(int)
            for i, corner in enumerate(corners):
                cv2.circle(corners_img, tuple(corner), 10, (255, 0, 0), -1)
                cv2.putText(corners_img, str(i+1), (corner[0]+15, corner[1]), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        
        axes[2].imshow(corners_img)
        axes[2].set_title('3. 角点检测', fontsize=12, fontweight='bold')
        axes[2].axis('off')
        
        # 透视变换
        if results.get('warped') is not None:
            axes[3].imshow(results['warped'])
            axes[3].set_title('4. 透视变换', fontsize=12, fontweight='bold')
        else:
            axes[3].text(0.5, 0.5, '透视变换失败', ha='center', va='center',
                        transform=axes[3].transAxes, fontsize=12)
            axes[3].set_title('4. 透视变换', fontsize=12, fontweight='bold')
        axes[3].axis('off')
        
        # 图像增强
        if results.get('enhanced') is not None:
            axes[4].imshow(results['enhanced'], cmap='gray')
            axes[4].set_title('5. 图像增强', fontsize=12, fontweight='bold')
        else:
            axes[4].text(0.5, 0.5, '图像增强失败', ha='center', va='center',
                        transform=axes[4].transAxes, fontsize=12)
            axes[4].set_title('5. 图像增强', fontsize=12, fontweight='bold')
        axes[4].axis('off')
        
        # 扫描统计
        axes[5].axis('off')
        if results.get('enhanced') is not None:
            stats_text = f"""
📊 扫描统计信息

📷 原始尺寸: {results['original'].shape[1]} x {results['original'].shape[0]}
📄 最终尺寸: {results['enhanced'].shape[1]} x {results['enhanced'].shape[0]}
🔍 边缘点数: {np.sum(results['edges'] > 0):,}
📍 检测角点: {'✅ 成功' if results.get('corners') is not None else '❌ 失败'}
⚙️ 处理状态: {'✅ 完成' if results.get('enhanced') is not None else '❌ 失败'}

🛠️ 配置参数:
• Canny阈值: {results['config']['edge_detection']['canny_low']}-{results['config']['edge_detection']['canny_high']}
• CLAHE限制: {results['config']['enhancement']['clahe_clip_limit']}
• 伽马值: {results['config']['enhancement']['gamma']}
            """
        else:
            stats_text = """
📊 扫描统计信息

❌ 扫描失败
🔍 可能原因:
• 文档边缘不清晰
• 背景干扰过多
• 角点检测失败

💡 建议:
• 调整拍摄角度
• 提高光照条件
• 调整检测参数
            """
        
        axes[5].text(0.1, 0.9, stats_text, transform=axes[5].transAxes,
                    fontsize=10, verticalalignment='top',
                    bbox=dict(boxstyle="round,pad=0.5", facecolor="lightblue", alpha=0.8))
        
        fig.suptitle('📱 智能文档扫描仪 - 完整处理流程', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        print("✅ 可视化完成")
    
    def get_scanner_status(self):
        """
        获取扫描仪状态报告
        """
        print("\n📱 智能文档扫描仪状态报告")
        print("=" * 50)
        print(f"📁 输出目录: {self.output_dir}")
        print(f"📊 总扫描次数: {len(self.scan_history)}")
        
        if self.scan_history:
            successful_scans = sum(1 for scan in self.scan_history if scan['success'])
            success_rate = successful_scans / len(self.scan_history) * 100
            
            print(f"✅ 成功扫描: {successful_scans} 次")
            print(f"📈 成功率: {success_rate:.1f}%")
            
            print("\n📋 最近扫描记录:")
            for scan in self.scan_history[-3:]:  # 显示最近3次
                status = "✅ 成功" if scan['success'] else "❌ 失败"
                timestamp = scan['timestamp'][:19]  # 去掉毫秒
                print(f"   [{scan['scan_id']:03d}] {timestamp} - {status}")

# 使用示例和演示
if __name__ == "__main__":
    # 创建智能文档扫描仪
    scanner = SmartDocumentScanner()
    
    # 创建一个模拟文档图像进行测试
    workshop = CaptureWorkshop()
    test_document = workshop.create_test_image(640, 480, 'checkerboard')
    
    # 执行完整扫描流程
    scan_results = scanner.scan_document(test_document)
    
    # 可视化扫描过程
    scanner.visualize_scan_process(scan_results)
    
    # 显示扫描仪状态
    scanner.get_scanner_status()
```

## 📝 章节总结

恭喜您！您已经成功建立了一座完整的**数字相机工厂**，并掌握了OpenCV图像处理的核心技术。

### 🏆 您已经掌握的技能

#### 🏭 工厂基础设施
- ✅ OpenCV环境的搭建和配置
- ✅ 图像输入、显示、保存的完整流程
- ✅ 企业级代码结构和错误处理

#### 🎨 图像处理技术
- ✅ 颜色空间转换和分析
- ✅ 图像滤波和降噪技术
- ✅ 图像增强和质量优化

#### 🔍 特征检测技术
- ✅ 边缘检测算法（Canny, Sobel, Laplacian）
- ✅ 角点检测算法（Harris, Shi-Tomasi, FAST, ORB）
- ✅ 特征匹配和图像对应关系建立

#### 📱 企业级项目开发
- ✅ 完整的智能文档扫描仪项目
- ✅ 从原型到产品的开发流程
- ✅ 配置管理、结果保存、状态监控

### 🚀 下一步学习建议

现在您已经掌握了OpenCV的基础技术，建议您：

1. **深入学习特定领域** - 选择计算机视觉的某个分支深入研究
2. **实践更多项目** - 开发车牌识别、人脸识别等实用项目
3. **学习深度学习** - 结合深度学习技术提升视觉应用能力
4. **关注性能优化** - 学习算法优化和并行处理技术

### 💡 思考题

1. **技术对比**: 在什么情况下选择Canny边缘检测而不是Sobel边缘检测？请分析它们的优缺点。

2. **参数调优**: 如何为不同类型的图像（如医学影像、卫星图像、工业检测图像）调整边缘检测的参数？

3. **项目扩展**: 如何扩展智能文档扫描仪，使其能够处理多页文档并自动分离页面？

4. **性能优化**: 在移动设备上部署文档扫描功能时，如何平衡处理速度和效果质量？

---

**第35章完成时间**: 2025年2月3日  
**代码示例总数**: 12个完整示例  
**总字数**: 约25,000字  
**实战项目**: 智能文档扫描仪  

> 🎯 **恭喜您！** 您已经成功掌握了OpenCV图像处理的核心技术，建立了完整的计算机视觉技术基础。现在您具备了开发专业图像处理应用的能力！