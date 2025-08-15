# 第39章：Django高级特性与架构

> 🏢 **企业级Web应用总部大厦**：将Django高级特性比喻为现代化企业总部大厦的各个部门和系统，每个部门都有特定的职责和高效的协作机制。

## 🎯 学习目标

通过本章学习，您将能够：

### 知识目标
- 深入理解Django的MVT架构模式和核心组件
- 掌握Django REST Framework高级特性和最佳实践
- 理解Django Channels实时通信和异步编程
- 掌握Django企业级安全防护和监控系统
- 学习Django在微服务架构中的应用

### 技能目标
- 能够设计和实现企业级Django应用架构
- 熟练使用Django高级特性优化系统性能
- 能够构建可扩展的实时Web应用
- 掌握Django项目的容器化部署和CI/CD
- 能够实现企业级安全防护和系统监控

### 素养目标
- 建立面向生产环境的开发思维
- 培养系统性思维和架构设计能力
- 提升代码质量和工程管理意识

## 🏗️ 比喻框架：企业级Web应用总部大厦

### 🏢 核心概念
将Django高级特性比喻为一座现代化企业总部大厦的各个部门和系统，每个部门都有特定的职责和高效的协作机制。

```mermaid
graph TD
    A["🏢 企业总部大厦<br/>(Django Application)"] --> B["🏗️ 架构设计部<br/>(MVT Architecture)"]
    A --> C["🚀 API服务中心<br/>(Django REST Framework)"]
    A --> D["⚡ 实时通信部<br/>(Django Channels)"]
    A --> E["🛡️ 安全管理部<br/>(Security Features)"]
    A --> F["🌐 微服务协调部<br/>(Microservices)"]
    
    B --> B1["📐 蓝图设计<br/>(Models Design)"]
    B --> B2["🎭 展示层<br/>(Templates)"]
    B --> B3["🎯 控制中心<br/>(Views)"]
    
    C --> C1["🔌 API网关<br/>(API Gateway)"]
    C --> C2["📡 数据序列化<br/>(Serializers)"]
    C --> C3["🛣️ 路由系统<br/>(URL Routing)"]
    
    D --> D1["💬 实时消息<br/>(WebSockets)"]
    D --> D2["📢 广播系统<br/>(Broadcasting)"]
    D --> D3["🔄 异步处理<br/>(Async Tasks)"]
    
    E --> E1["🔐 访问控制<br/>(Authentication)"]
    E --> E2["👮 权限管理<br/>(Authorization)"]
    E --> E3["📊 监控系统<br/>(Monitoring)"]
    
    F --> F1["⚖️ 负载均衡<br/>(Load Balance)"]
    F --> F2["📦 容器部署<br/>(Containerization)"]
    F3["🔄 服务发现<br/>(Service Discovery)"]
```

### 🎯 比喻体系详解

#### 🏗️ 架构设计部 (MVT Architecture)
- **部门职责**：制定企业整体架构和运营蓝图
- **技术映射**：Django的MVT模式、应用架构设计
- **创新点**：用建筑设计图纸比喻Django的模型-视图-模板架构

#### 🚀 API服务中心 (Django REST Framework)
- **部门职责**：对外提供标准化服务接口
- **技术映射**：RESTful API设计、序列化、认证授权
- **创新点**：用企业服务窗口比喻API接口设计

#### ⚡ 实时通信部 (Django Channels)
- **部门职责**：处理实时信息传递和紧急通知
- **技术映射**：WebSocket、异步处理、实时功能
- **创新点**：用企业内部通讯系统比喻实时通信功能

#### 🛡️ 安全管理部 (Security Features)
- **部门职责**：保障企业信息安全和访问控制
- **技术映射**：身份认证、权限管理、安全防护
- **创新点**：用企业安保系统比喻Web安全机制

#### 🌐 微服务协调部 (Microservices)
- **部门职责**：协调各部门间的协作和资源分配
- **技术映射**：微服务架构、服务发现、容器化部署
- **创新点**：用企业分部协调比喻微服务管理

---

## 第39.1节 🏗️ 架构设计部 - Django高级架构模式

> 🏗️ **比喻场景**：想象一下，您是一位建筑设计师，需要为一座现代化企业总部大厦设计完整的架构蓝图。从地基到顶层，从水电管道到网络布线，每一个细节都需要精心规划。Django的高级架构模式就像这套建筑设计图纸，为我们的Web应用提供了坚实的结构基础。

### 🎯 学习重点
- Django高级架构模式深度解析
- 分层架构设计与最佳实践
- 企业级模型设计与视图架构
- 插件化架构实现

### 💡 核心概念

#### 1. Django MVT架构深度解析

**🏗️ 建筑设计图纸系统**

就像建筑设计需要结构图、电路图、管道图一样，Django的MVT架构为我们提供了三个核心层次：

```python
"""
Django MVT架构企业级实现
比喻：现代化企业大厦的三层设计体系
"""

# 🏛️ Model层 - 地基与结构层（数据层）
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
import uuid

class BaseModel(models.Model):
    """
    🏗️ 建筑地基类
    为所有模型提供通用的基础结构
    """
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False,
        verbose_name="唯一标识"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="创建时间",
        help_text="记录数据创建的时间戳"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="更新时间",
        help_text="记录数据最后更新的时间戳"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="是否激活",
        help_text="逻辑删除标识"
    )
    
    class Meta:
        abstract = True
        ordering = ['-created_at']
        
    def soft_delete(self):
        """软删除方法"""
        self.is_active = False
        self.save()
        
    def restore(self):
        """恢复删除的数据"""
        self.is_active = True
        self.save()

class Department(BaseModel):
    """
    🏢 企业部门模型
    比喻：企业大厦中的各个部门结构
    """
    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
        verbose_name="部门名称"
    )
    code = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="部门代码"
    )
    description = models.TextField(
        blank=True,
        verbose_name="部门描述"
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name="上级部门"
    )
    manager = models.ForeignKey(
        'Employee',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='managed_departments',
        verbose_name="部门经理"
    )
    
    class Meta:
        verbose_name = "部门"
        verbose_name_plural = "部门管理"
        ordering = ['code']
        
    def __str__(self):
        return f"{self.code} - {self.name}"
    
    def get_all_employees(self):
        """获取部门所有员工（包括子部门）"""
        from django.db.models import Q
        departments = self.get_descendants(include_self=True)
        return Employee.objects.filter(
            Q(department__in=departments) & Q(is_active=True)
        )
    
    def get_descendants(self, include_self=False):
        """获取所有子部门"""
        descendants = []
        if include_self:
            descendants.append(self)
        
        for child in self.children.filter(is_active=True):
            descendants.extend(child.get_descendants(include_self=True))
        
        return descendants

class Employee(AbstractUser):
    """
    👤 企业员工模型
    比喻：企业大厦中的工作人员
    """
    employee_id = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="员工编号"
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name='employees',
        verbose_name="所属部门"
    )
    position = models.CharField(
        max_length=100,
        verbose_name="职位"
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="联系电话"
    )
    hire_date = models.DateField(
        verbose_name="入职日期"
    )
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="薪资"
    )
    
    class Meta:
        verbose_name = "员工"
        verbose_name_plural = "员工管理"
        ordering = ['employee_id']
        
    def __str__(self):
        return f"{self.employee_id} - {self.get_full_name()}"
    
    def get_full_name(self):
        """获取员工全名"""
        return f"{self.last_name}{self.first_name}" if self.last_name else self.username

# 🎯 View层 - 控制中心层（业务逻辑层）
from django.views.generic import (
    CreateView, UpdateView, DeleteView, 
    ListView, DetailView
)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
import json

class BaseViewMixin(LoginRequiredMixin):
    """
    🎯 基础视图混入类
    比喻：企业大厦的通用管理规则
    """
    paginate_by = 20
    
    def get_context_data(self, **kwargs):
        """添加通用上下文数据"""
        context = super().get_context_data(**kwargs)
        context.update({
            'current_user': self.request.user,
            'current_time': timezone.now(),
            'page_title': getattr(self, 'page_title', ''),
        })
        return context
    
    def handle_no_permission(self):
        """处理权限不足的情况"""
        if self.request.is_ajax():
            return JsonResponse({
                'success': False,
                'message': '您没有权限执行此操作'
            }, status=403)
        return super().handle_no_permission()

class DepartmentListView(BaseViewMixin, ListView):
    """
    🏢 部门列表视图
    比喻：企业大厦的部门名录显示系统
    """
    model = Department
    template_name = 'departments/list.html'
    context_object_name = 'departments'
    page_title = '部门管理'
    
    def get_queryset(self):
        """获取部门查询集"""
        queryset = Department.objects.filter(is_active=True)
        
        # 搜索功能
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(code__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        
        # 部门筛选
        parent_id = self.request.GET.get('parent', '')
        if parent_id:
            queryset = queryset.filter(parent_id=parent_id)
        elif parent_id == '':
            # 显示顶级部门
            queryset = queryset.filter(parent__isnull=True)
            
        return queryset.select_related('parent', 'manager')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'search_query': self.request.GET.get('search', ''),
            'parent_departments': Department.objects.filter(
                is_active=True, parent__isnull=True
            ),
        })
        return context

class DepartmentDetailView(BaseViewMixin, DetailView):
    """
    🏢 部门详情视图
    比喻：企业大厦的部门详细信息展示中心
    """
    model = Department
    template_name = 'departments/detail.html'
    context_object_name = 'department'
    page_title = '部门详情'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        department = self.get_object()
        
        # 获取部门员工
        employees = department.employees.filter(is_active=True)
        paginator = Paginator(employees, 10)
        page_number = self.request.GET.get('page', 1)
        page_employees = paginator.get_page(page_number)
        
        context.update({
            'employees': page_employees,
            'employee_count': employees.count(),
            'child_departments': department.children.filter(is_active=True),
            'breadcrumbs': self.get_breadcrumbs(department),
        })
        return context
    
    def get_breadcrumbs(self, department):
        """生成面包屑导航"""
        breadcrumbs = []
        current = department
        while current:
            breadcrumbs.insert(0, current)
            current = current.parent
        return breadcrumbs

# 🎭 Template层 - 展示层（表现层）
# departments/list.html
DEPARTMENT_LIST_TEMPLATE = """
{% extends 'base.html' %}
{% load static %}

{% block title %}{{ page_title }}{% endblock %}

{% block extra_css %}
<link href="{% static 'css/department.css' %}" rel="stylesheet">
{% endblock %}

{% block content %}
<div class="department-management">
    <!-- 🏢 部门管理控制台 -->
    <div class="management-header">
        <h1 class="page-title">
            <i class="fas fa-building"></i>
            {{ page_title }}
        </h1>
        
        <!-- 搜索和筛选区域 -->
        <div class="filters-section">
            <form method="get" class="search-form">
                <div class="input-group">
                    <input type="text" 
                           name="search" 
                           value="{{ search_query }}"
                           placeholder="搜索部门名称、代码或描述..."
                           class="form-control">
                    <button type="submit" class="btn btn-primary">
                        <i class="fas fa-search"></i> 搜索
                    </button>
                </div>
            </form>
        </div>
    </div>
    
    <!-- 部门列表展示区域 -->
    <div class="department-grid">
        {% for department in departments %}
        <div class="department-card">
            <div class="card-header">
                <h3 class="department-name">
                    <a href="{% url 'department_detail' department.pk %}">
                        {{ department.name }}
                    </a>
                </h3>
                <span class="department-code">{{ department.code }}</span>
            </div>
            
            <div class="card-body">
                <p class="department-description">
                    {{ department.description|truncatewords:20 }}
                </p>
                
                <div class="department-stats">
                    <div class="stat-item">
                        <i class="fas fa-users"></i>
                        <span>{{ department.employees.count }} 员工</span>
                    </div>
                    
                    {% if department.children.exists %}
                    <div class="stat-item">
                        <i class="fas fa-sitemap"></i>
                        <span>{{ department.children.count }} 子部门</span>
                    </div>
                    {% endif %}
                </div>
            </div>
            
            <div class="card-footer">
                <div class="action-buttons">
                    <a href="{% url 'department_detail' department.pk %}" 
                       class="btn btn-sm btn-outline-primary">
                        <i class="fas fa-eye"></i> 查看
                    </a>
                    <a href="{% url 'department_edit' department.pk %}" 
                       class="btn btn-sm btn-outline-success">
                        <i class="fas fa-edit"></i> 编辑
                    </a>
                </div>
            </div>
        </div>
        {% empty %}
        <div class="empty-state">
            <i class="fas fa-building fa-3x text-muted"></i>
            <h3>暂无部门数据</h3>
            <p>请添加第一个部门开始管理</p>
            <a href="{% url 'department_create' %}" class="btn btn-primary">
                <i class="fas fa-plus"></i> 创建部门
            </a>
        </div>
        {% endfor %}
    </div>
    
    <!-- 分页导航 -->
    {% if is_paginated %}
    <div class="pagination-wrapper">
        <nav aria-label="部门列表分页">
            <ul class="pagination">
                {% if page_obj.has_previous %}
                <li class="page-item">
                    <a class="page-link" href="?page={{ page_obj.previous_page_number }}">
                        <i class="fas fa-chevron-left"></i> 上一页
                    </a>
                </li>
                {% endif %}
                
                {% for num in page_obj.paginator.page_range %}
                <li class="page-item {% if page_obj.number == num %}active{% endif %}">
                    <a class="page-link" href="?page={{ num }}">{{ num }}</a>
                </li>
                {% endfor %}
                
                {% if page_obj.has_next %}
                <li class="page-item">
                    <a class="page-link" href="?page={{ page_obj.next_page_number }}">
                        下一页 <i class="fas fa-chevron-right"></i>
                    </a>
                </li>
                {% endif %}
            </ul>
        </nav>
    </div>
    {% endif %}
</div>
{% endblock %}

{% block extra_js %}
<script src="{% static 'js/department-management.js' %}"></script>
{% endblock %}
"""
```

#### 2. 分层架构设计原则

**🏗️ 企业大厦分层管理系统**

```python
"""
Django分层架构设计
比喻：企业大厦的分层管理体系
"""

# 📊 Service层 - 业务服务层
class DepartmentService:
    """
    🏢 部门业务服务类
    比喻：企业大厦的部门管理服务中心
    """
    
    @staticmethod
    def create_department_with_validation(data, creator):
        """
        创建部门（带完整验证）
        比喻：企业大厦新部门的审批和设立流程
        """
        try:
            # 数据验证
            DepartmentService._validate_department_data(data)
            
            # 检查部门代码唯一性
            if Department.objects.filter(code=data['code'], is_active=True).exists():
                raise ValidationError("部门代码已存在")
            
            # 创建部门
            department = Department.objects.create(
                name=data['name'],
                code=data['code'],
                description=data.get('description', ''),
                parent_id=data.get('parent_id'),
                manager_id=data.get('manager_id')
            )
            
            # 记录操作日志
            AuditLogService.log_action(
                user=creator,
                action='CREATE_DEPARTMENT',
                target=department,
                details=f"创建部门: {department.name}"
            )
            
            return {
                'success': True,
                'department': department,
                'message': '部门创建成功'
            }
            
        except ValidationError as e:
            return {
                'success': False,
                'errors': e.message_dict if hasattr(e, 'message_dict') else [str(e)],
                'message': '部门创建失败'
            }
        except Exception as e:
            return {
                'success': False,
                'errors': [str(e)],
                'message': '系统错误，请联系管理员'
            }
    
    @staticmethod
    def _validate_department_data(data):
        """验证部门数据"""
        required_fields = ['name', 'code']
        for field in required_fields:
            if not data.get(field):
                raise ValidationError(f"{field} 字段不能为空")
        
        # 验证部门名称长度
        if len(data['name']) < 2:
            raise ValidationError("部门名称至少需要2个字符")
        
        # 验证部门代码格式
        import re
        if not re.match(r'^[A-Z]{2,6}$', data['code']):
            raise ValidationError("部门代码必须是2-6位大写字母")
    
    @staticmethod
    def get_department_hierarchy():
        """
        获取部门层级结构
        比喻：企业大厦的组织架构图
        """
        def build_tree(departments, parent_id=None):
            tree = []
            for dept in departments:
                if dept.parent_id == parent_id:
                    children = build_tree(departments, dept.id)
                    tree.append({
                        'id': dept.id,
                        'name': dept.name,
                        'code': dept.code,
                        'employee_count': dept.employees.filter(is_active=True).count(),
                        'children': children
                    })
            return tree
        
        departments = Department.objects.filter(is_active=True).select_related('parent')
        return build_tree(departments)

# 📋 Repository层 - 数据访问层
class DepartmentRepository:
    """
    🏢 部门数据访问类
    比喻：企业大厦的档案管理中心
    """
    
    @staticmethod
    def get_active_departments():
        """获取所有活跃部门"""
        return Department.objects.filter(is_active=True)
    
    @staticmethod
    def get_department_with_employees(department_id):
        """获取部门及其员工信息"""
        return Department.objects.select_related('parent', 'manager').prefetch_related(
            'employees'
        ).get(id=department_id, is_active=True)
    
    @staticmethod
    def search_departments(query):
        """搜索部门"""
        return Department.objects.filter(
            Q(name__icontains=query) |
            Q(code__icontains=query) |
            Q(description__icontains=query),
            is_active=True
        ).select_related('parent')
    
    @staticmethod
    def get_departments_by_level(level=1):
        """根据层级获取部门"""
        if level == 1:
            return Department.objects.filter(parent__isnull=True, is_active=True)
        else:
            # 递归查询指定层级的部门
            current_level_departments = Department.objects.filter(
                parent__isnull=True, is_active=True
            )
            
            for _ in range(level - 1):
                current_level_departments = Department.objects.filter(
                    parent__in=current_level_departments, is_active=True
                )
            
            return current_level_departments

# 🔧 Utils层 - 工具层
class DepartmentUtils:
    """
    🏢 部门工具类
    比喻：企业大厦的维护工具箱
    """
    
    @staticmethod
    def export_department_tree_to_json():
        """导出部门树结构为JSON"""
        hierarchy = DepartmentService.get_department_hierarchy()
        return json.dumps(hierarchy, ensure_ascii=False, indent=2)
    
    @staticmethod
    def generate_department_code(department_name):
        """根据部门名称生成部门代码"""
        # 提取中文首字母或英文首字母
        import pypinyin
        
        code_parts = []
        for char in department_name:
            if '\u4e00' <= char <= '\u9fff':  # 中文字符
                pinyin = pypinyin.lazy_pinyin(char, style=pypinyin.FIRST_LETTER)
                code_parts.append(pinyin[0].upper())
            elif char.isalpha():  # 英文字符
                code_parts.append(char.upper())
        
        base_code = ''.join(code_parts)[:6]  # 限制为6位
        
        # 检查唯一性，如果重复则添加数字后缀
        counter = 1
        final_code = base_code
        while Department.objects.filter(code=final_code, is_active=True).exists():
            final_code = f"{base_code}{counter}"
            counter += 1
            
        return final_code
    
    @staticmethod
    def validate_department_move(department_id, new_parent_id):
        """验证部门移动操作"""
        if department_id == new_parent_id:
            return False, "部门不能设置自己为上级部门"
        
        department = Department.objects.get(id=department_id)
        
        # 检查是否会造成循环引用
        current_parent = Department.objects.filter(id=new_parent_id).first()
        while current_parent:
            if current_parent.id == department_id:
                return False, "移动操作会造成循环引用"
            current_parent = current_parent.parent
        
        return True, "验证通过"
```

#### 3. 插件化架构实现

**🔌 企业大厦的插件扩展系统**

```python
"""
Django插件化架构实现
比喻：企业大厦的可扩展插件系统
"""

# 🔌 插件基础框架
from abc import ABC, abstractmethod
from django.apps import apps
from django.conf import settings
import importlib

class BasePlugin(ABC):
    """
    🔌 基础插件类
    比喻：企业大厦的标准插件接口
    """
    
    def __init__(self):
        self.name = self.__class__.__name__
        self.version = getattr(self, 'version', '1.0.0')
        self.description = getattr(self, 'description', '')
        self.author = getattr(self, 'author', '')
    
    @abstractmethod
    def install(self):
        """插件安装方法"""
        pass
    
    @abstractmethod
    def uninstall(self):
        """插件卸载方法"""
        pass
    
    @abstractmethod
    def activate(self):
        """插件激活方法"""
        pass
    
    @abstractmethod
    def deactivate(self):
        """插件停用方法"""
        pass
    
    def get_plugin_info(self):
        """获取插件信息"""
        return {
            'name': self.name,
            'version': self.version,
            'description': self.description,
            'author': self.author,
            'is_active': self.is_active()
        }
    
    def is_active(self):
        """检查插件是否激活"""
        return PluginManager.is_plugin_active(self.name)

class DepartmentReportPlugin(BasePlugin):
    """
    📊 部门报表插件
    比喻：企业大厦的部门数据分析扩展
    """
    version = '2.1.0'
    description = '提供部门数据统计和报表功能'
    author = 'Enterprise Team'
    
    def install(self):
        """安装部门报表插件"""
        # 创建报表相关数据表
        from django.core.management import execute_from_command_line
        execute_from_command_line(['manage.py', 'migrate', 'department_reports'])
        
        # 创建默认报表模板
        self._create_default_templates()
        
        return True
    
    def uninstall(self):
        """卸载部门报表插件"""
        # 清理插件数据
        self._cleanup_plugin_data()
        return True
    
    def activate(self):
        """激活插件"""
        # 注册URL路由
        self._register_urls()
        
        # 注册模板标签
        self._register_template_tags()
        
        return True
    
    def deactivate(self):
        """停用插件"""
        # 注销URL路由
        self._unregister_urls()
        
        return True
    
    def _create_default_templates(self):
        """创建默认报表模板"""
        templates = [
            {
                'name': '部门员工统计报表',
                'template_type': 'EMPLOYEE_COUNT',
                'config': {
                    'chart_type': 'bar',
                    'group_by': 'department',
                    'time_range': 'current_month'
                }
            },
            {
                'name': '部门预算执行报表',
                'template_type': 'BUDGET_EXECUTION',
                'config': {
                    'chart_type': 'line',
                    'group_by': 'month',
                    'time_range': 'current_year'
                }
            }
        ]
        
        from .models import ReportTemplate
        for template_data in templates:
            ReportTemplate.objects.get_or_create(
                name=template_data['name'],
                defaults=template_data
            )
    
    def _register_urls(self):
        """注册插件URL"""
        from django.urls import path, include
        from . import views
        
        plugin_urls = [
            path('reports/', views.DepartmentReportListView.as_view(), name='department_reports'),
            path('reports/create/', views.CreateReportView.as_view(), name='create_report'),
            path('reports/<uuid:pk>/', views.ReportDetailView.as_view(), name='report_detail'),
            path('api/reports/data/', views.ReportDataAPIView.as_view(), name='report_data_api'),
        ]
        
        # 动态注册到主URL配置
        PluginManager.register_plugin_urls('department_reports', plugin_urls)
    
    def generate_department_summary_report(self, department_id=None, date_range=None):
        """生成部门汇总报表"""
        from django.utils import timezone
        from datetime import datetime, timedelta
        
        # 确定时间范围
        if not date_range:
            end_date = timezone.now().date()
            start_date = end_date - timedelta(days=30)
        else:
            start_date, end_date = date_range
        
        # 获取部门数据
        if department_id:
            departments = Department.objects.filter(id=department_id, is_active=True)
        else:
            departments = Department.objects.filter(is_active=True)
        
        report_data = []
        for dept in departments:
            employees = dept.employees.filter(is_active=True)
            
            # 统计数据
            dept_data = {
                'department_name': dept.name,
                'department_code': dept.code,
                'total_employees': employees.count(),
                'new_employees': employees.filter(
                    hire_date__range=[start_date, end_date]
                ).count(),
                'average_salary': employees.aggregate(
                    avg_salary=models.Avg('salary')
                )['avg_salary'] or 0,
                'child_departments': dept.children.filter(is_active=True).count(),
            }
            
            report_data.append(dept_data)
        
        return {
            'title': '部门汇总报表',
            'period': f"{start_date} 至 {end_date}",
            'generated_at': timezone.now(),
            'data': report_data,
            'summary': {
                'total_departments': len(report_data),
                'total_employees': sum(d['total_employees'] for d in report_data),
                'total_new_employees': sum(d['new_employees'] for d in report_data),
            }
        }

# 🎛️ 插件管理器
class PluginManager:
    """
    🎛️ 插件管理器
    比喻：企业大厦的扩展管理控制中心
    """
    
    _plugins = {}
    _active_plugins = set()
    
    @classmethod
    def discover_plugins(cls):
        """发现并加载所有插件"""
        plugin_dirs = getattr(settings, 'PLUGIN_DIRECTORIES', ['plugins'])
        
        for plugin_dir in plugin_dirs:
            try:
                # 扫描插件目录
                import os
                plugin_path = os.path.join(settings.BASE_DIR, plugin_dir)
                if not os.path.exists(plugin_path):
                    continue
                
                for item in os.listdir(plugin_path):
                    item_path = os.path.join(plugin_path, item)
                    if os.path.isdir(item_path) and not item.startswith('_'):
                        cls._load_plugin(plugin_dir, item)
                        
            except Exception as e:
                print(f"插件发现过程中出现错误: {e}")
    
    @classmethod
    def _load_plugin(cls, plugin_dir, plugin_name):
        """加载单个插件"""
        try:
            module_path = f"{plugin_dir}.{plugin_name}.plugin"
            plugin_module = importlib.import_module(module_path)
            
            # 查找插件类
            for attr_name in dir(plugin_module):
                attr = getattr(plugin_module, attr_name)
                if (isinstance(attr, type) and 
                    issubclass(attr, BasePlugin) and 
                    attr != BasePlugin):
                    
                    plugin_instance = attr()
                    cls._plugins[plugin_name] = plugin_instance
                    break
                    
        except ImportError as e:
            print(f"无法加载插件 {plugin_name}: {e}")
    
    @classmethod
    def get_all_plugins(cls):
        """获取所有插件"""
        return cls._plugins
    
    @classmethod
    def get_plugin(cls, plugin_name):
        """获取指定插件"""
        return cls._plugins.get(plugin_name)
    
    @classmethod
    def activate_plugin(cls, plugin_name):
        """激活插件"""
        plugin = cls._plugins.get(plugin_name)
        if plugin:
            try:
                plugin.activate()
                cls._active_plugins.add(plugin_name)
                return True, "插件激活成功"
            except Exception as e:
                return False, f"插件激活失败: {e}"
        return False, "插件不存在"
    
    @classmethod
    def deactivate_plugin(cls, plugin_name):
        """停用插件"""
        plugin = cls._plugins.get(plugin_name)
        if plugin:
            try:
                plugin.deactivate()
                cls._active_plugins.discard(plugin_name)
                return True, "插件停用成功"
            except Exception as e:
                return False, f"插件停用失败: {e}"
        return False, "插件不存在"
    
    @classmethod
    def is_plugin_active(cls, plugin_name):
        """检查插件是否激活"""
        return plugin_name in cls._active_plugins
    
    @classmethod
    def register_plugin_urls(cls, plugin_name, urls):
        """注册插件URL"""
        from django.urls import path, include
        from django.conf import settings
        
        # 动态添加URL到主路由配置
        # 这里需要根据具体的URL配置方式来实现
        pass
    
    @classmethod
    def get_plugin_statistics(cls):
        """获取插件统计信息"""
        return {
            'total_plugins': len(cls._plugins),
            'active_plugins': len(cls._active_plugins),
            'inactive_plugins': len(cls._plugins) - len(cls._active_plugins),
            'plugin_list': [
                {
                    'name': name,
                    'info': plugin.get_plugin_info(),
                    'is_active': cls.is_plugin_active(name)
                }
                for name, plugin in cls._plugins.items()
            ]
        }

# 📱 插件管理视图
class PluginManagementView(BaseViewMixin, TemplateView):
    """
    📱 插件管理视图
    比喻：企业大厦的扩展管理面板
    """
    template_name = 'admin/plugin_management.html'
    page_title = '插件管理'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'plugin_stats': PluginManager.get_plugin_statistics(),
            'plugins': PluginManager.get_all_plugins(),
        })
        return context
    
    def post(self, request, *args, **kwargs):
        """处理插件操作"""
        action = request.POST.get('action')
        plugin_name = request.POST.get('plugin_name')
        
        if action == 'activate':
            success, message = PluginManager.activate_plugin(plugin_name)
        elif action == 'deactivate':
            success, message = PluginManager.deactivate_plugin(plugin_name)
        else:
            success, message = False, "未知操作"
        
        if request.is_ajax():
            return JsonResponse({
                'success': success,
                'message': message
            })
        
        from django.contrib import messages
        if success:
            messages.success(request, message)
        else:
            messages.error(request, message)
        
        return self.get(request, *args, **kwargs)
```

### 🎯 实战项目：企业级博客管理系统架构

```python
"""
企业级博客管理系统
比喻：企业大厦的内容发布和管理中心
"""

# 📝 博客模型设计
class BlogCategory(BaseModel):
    """博客分类模型"""
    name = models.CharField(max_length=100, verbose_name="分类名称")
    slug = models.SlugField(unique=True, verbose_name="URL标识")
    description = models.TextField(blank=True, verbose_name="分类描述")
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        related_name='children',
        verbose_name="父分类"
    )
    sort_order = models.IntegerField(default=0, verbose_name="排序")
    
    class Meta:
        verbose_name = "博客分类"
        verbose_name_plural = "博客分类"
        ordering = ['sort_order', 'name']

class BlogPost(BaseModel):
    """博客文章模型"""
    title = models.CharField(max_length=200, verbose_name="文章标题")
    slug = models.SlugField(unique=True, verbose_name="URL标识") 
    summary = models.TextField(max_length=500, verbose_name="文章摘要")
    content = models.TextField(verbose_name="文章内容")
    author = models.ForeignKey(
        Employee, 
        on_delete=models.PROTECT,
        related_name='blog_posts',
        verbose_name="作者"
    )
    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.PROTECT,
        related_name='posts',
        verbose_name="分类"
    )
    tags = models.ManyToManyField(
        'BlogTag',
        blank=True,
        related_name='posts',
        verbose_name="标签"
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('DRAFT', '草稿'),
            ('PUBLISHED', '已发布'),
            ('ARCHIVED', '已归档')
        ],
        default='DRAFT',
        verbose_name="状态"
    )
    featured_image = models.ImageField(
        upload_to='blog/images/',
        blank=True,
        verbose_name="特色图片"
    )
    view_count = models.PositiveIntegerField(default=0, verbose_name="浏览次数")
    like_count = models.PositiveIntegerField(default=0, verbose_name="点赞次数")
    published_at = models.DateTimeField(null=True, blank=True, verbose_name="发布时间")
    
    class Meta:
        verbose_name = "博客文章"
        verbose_name_plural = "博客文章"
        ordering = ['-published_at', '-created_at']
    
    def save(self, *args, **kwargs):
        if self.status == 'PUBLISHED' and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

class BlogTag(BaseModel):
    """博客标签模型"""
    name = models.CharField(max_length=50, unique=True, verbose_name="标签名称")
    color = models.CharField(max_length=7, default='#007bff', verbose_name="标签颜色")
    
    class Meta:
        verbose_name = "博客标签"
        verbose_name_plural = "博客标签"
        ordering = ['name']

# 📊 博客服务层
class BlogService:
    """博客业务服务"""
    
    @staticmethod
    def publish_post(post_id, publisher):
        """发布文章"""
        try:
            post = BlogPost.objects.get(id=post_id)
            
            # 权限检查
            if post.author != publisher and not publisher.has_perm('blog.publish_post'):
                raise PermissionError("您没有权限发布此文章")
            
            # 内容验证
            if not post.title or not post.content:
                raise ValidationError("文章标题和内容不能为空")
            
            # 发布文章
            post.status = 'PUBLISHED'
            post.published_at = timezone.now()
            post.save()
            
            # 发送通知
            NotificationService.send_notification(
                recipient=post.author,
                title="文章发布成功",
                message=f"您的文章《{post.title}》已成功发布",
                notification_type='BLOG_PUBLISHED'
            )
            
            return True, "文章发布成功"
            
        except Exception as e:
            return False, str(e)
    
    @staticmethod
    def get_trending_posts(limit=10):
        """获取热门文章"""
        from django.db.models import F
        
        return BlogPost.objects.filter(
            status='PUBLISHED',
            is_active=True
        ).annotate(
            trending_score=F('view_count') + F('like_count') * 3
        ).order_by('-trending_score')[:limit]

# 🎯 博客视图控制器
class BlogPostListView(BaseViewMixin, ListView):
    """博客文章列表视图"""
    model = BlogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = BlogPost.objects.filter(
            status='PUBLISHED',
            is_active=True
        ).select_related('author', 'category').prefetch_related('tags')
        
        # 分类筛选
        category_slug = self.request.GET.get('category')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        
        # 标签筛选
        tag_name = self.request.GET.get('tag')
        if tag_name:
            queryset = queryset.filter(tags__name=tag_name)
        
        # 搜索功能
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(summary__icontains=search_query) |
                Q(content__icontains=search_query)
            )
        
        return queryset.distinct()
```

### 📚 本节小结

通过本节学习，我们深入了解了Django高级架构模式的设计原理和实现方法：

#### 🎯 核心要点
1. **MVT架构深度解析**：理解Django的三层架构设计思想
2. **分层架构设计**：掌握Service层、Repository层、Utils层的设计
3. **插件化架构**：实现可扩展的企业级插件系统
4. **实战项目**：构建企业级博客管理系统

#### 🏗️ 架构设计原则
- **单一职责**：每个组件只负责特定的功能
- **开闭原则**：对扩展开放，对修改封闭
- **依赖倒置**：高层模块不依赖低层模块
- **接口隔离**：使用抽象接口减少耦合

#### 💡 最佳实践
- 使用抽象基类定义通用功能
- 实现完整的错误处理和日志记录
- 采用插件化架构支持功能扩展
- 遵循Django的约定优于配置原则

---

## 第39.2节 🚀 API服务中心 - Django REST Framework进阶

> 🚀 **比喻场景**：想象一下现代化企业总部大厦的服务中心，它就像一个高效的客户服务大厅。不同的客户(移动端、Web端、第三方系统)带着各种需求前来办事，服务中心的工作人员(API接口)能够快速理解客户需求，调用相应的后台部门处理，并以标准化的格式返回结果。Django REST Framework就是这样的企业级API服务中心。

### 🎯 学习重点
- Django REST Framework高级特性与自定义
- API设计最佳实践与版本管理
- 性能优化策略与监控系统
- 企业级API安全与权限控制

### 💡 核心概念

#### 1. DRF高级特性深度解析

**🚀 API服务大厅运营系统**

```python
"""
Django REST Framework企业级实现
比喻：现代化企业API服务中心的完整运营体系
"""

# 🎯 高级序列化器系统
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from django.contrib.auth import get_user_model
from django.utils import timezone
import re

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    🎯 动态字段序列化器
    比喻：API服务大厅的个性化服务窗口
    可根据客户需求动态调整返回的信息字段
    """
    
    def __init__(self, *args, **kwargs):
        # 从请求中获取需要的字段
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)
        
        super().__init__(*args, **kwargs)
        
        if fields is not None:
            # 只保留指定的字段
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        
        if exclude is not None:
            # 排除指定的字段
            for field_name in exclude:
                self.fields.pop(field_name, None)

class DepartmentSerializer(DynamicFieldsModelSerializer):
    """
    🏢 部门信息序列化器
    比喻：API服务大厅的部门信息展示系统
    """
    
    # 计算字段
    employee_count = SerializerMethodField()
    manager_info = SerializerMethodField()
    department_path = SerializerMethodField()
    children_count = SerializerMethodField()
    
    # 嵌套序列化
    parent = serializers.SerializerMethodField()
    
    class Meta:
        model = Department
        fields = [
            'id', 'name', 'code', 'description', 'created_at', 'updated_at',
            'employee_count', 'manager_info', 'department_path', 
            'children_count', 'parent'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_employee_count(self, obj):
        """获取部门员工数量"""
        return obj.employees.filter(is_active=True).count()
    
    def get_manager_info(self, obj):
        """获取部门经理信息"""
        if obj.manager:
            return {
                'id': obj.manager.id,
                'name': obj.manager.get_full_name(),
                'employee_id': obj.manager.employee_id,
                'position': obj.manager.position
            }
        return None
    
    def get_department_path(self, obj):
        """获取部门层级路径"""
        path = []
        current = obj
        while current:
            path.insert(0, {
                'id': current.id,
                'name': current.name,
                'code': current.code
            })
            current = current.parent
        return path
    
    def get_children_count(self, obj):
        """获取子部门数量"""
        return obj.children.filter(is_active=True).count()
    
    def get_parent(self, obj):
        """获取父部门信息"""
        if obj.parent:
            return {
                'id': obj.parent.id,
                'name': obj.parent.name,
                'code': obj.parent.code
            }
        return None
    
    def validate_code(self, value):
        """验证部门代码"""
        if not re.match(r'^[A-Z]{2,6}$', value):
            raise serializers.ValidationError(
                "部门代码必须是2-6位大写字母"
            )
        
        # 检查唯一性（排除当前对象）
        queryset = Department.objects.filter(code=value, is_active=True)
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
        
        if queryset.exists():
            raise serializers.ValidationError("部门代码已存在")
        
        return value
    
    def validate(self, attrs):
        """整体数据验证"""
        # 验证父部门不能是自己
        if 'parent' in attrs and self.instance:
            if attrs['parent'] == self.instance:
                raise serializers.ValidationError({
                    'parent': '部门不能设置自己为上级部门'
                })
        
        return attrs

class EmployeeSerializer(DynamicFieldsModelSerializer):
    """
    👤 员工信息序列化器
    比喻：API服务大厅的员工档案管理系统
    """
    
    department_info = SerializerMethodField()
    full_name = SerializerMethodField()
    work_years = SerializerMethodField()
    
    # 写入时的密码字段
    password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = Employee
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'employee_id', 'department', 'position', 'phone', 
            'hire_date', 'salary', 'is_active',
            'department_info', 'full_name', 'work_years', 'password'
        ]
        extra_kwargs = {
            'salary': {'write_only': True},  # 薪资信息仅写入
            'password': {'write_only': True}
        }
    
    def get_department_info(self, obj):
        """获取部门信息"""
        if obj.department:
            return {
                'id': obj.department.id,
                'name': obj.department.name,
                'code': obj.department.code
            }
        return None
    
    def get_full_name(self, obj):
        """获取员工全名"""
        return obj.get_full_name()
    
    def get_work_years(self, obj):
        """计算工作年限"""
        if obj.hire_date:
            today = timezone.now().date()
            years = (today - obj.hire_date).days / 365.25
            return round(years, 1)
        return 0
    
    def create(self, validated_data):
        """创建员工"""
        password = validated_data.pop('password', None)
        employee = super().create(validated_data)
        
        if password:
            employee.set_password(password)
            employee.save()
        
        return employee
    
    def update(self, instance, validated_data):
        """更新员工"""
        password = validated_data.pop('password', None)
        employee = super().update(instance, validated_data)
        
        if password:
            employee.set_password(password)
            employee.save()
        
        return employee

# 🎛️ 高级视图集系统
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q, Count, Avg
from django.shortcuts import get_object_or_404

class BaseModelViewSet(viewsets.ModelViewSet):
    """
    🎯 基础模型视图集
    比喻：API服务大厅的标准服务流程
    """
    
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    def get_serializer(self, *args, **kwargs):
        """动态序列化器字段控制"""
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        
        # 支持动态字段选择
        if self.request.method == 'GET':
            fields = self.request.query_params.get('fields')
            exclude = self.request.query_params.get('exclude')
            
            if fields:
                kwargs['fields'] = fields.split(',')
            if exclude:
                kwargs['exclude'] = exclude.split(',')
        
        return serializer_class(*args, **kwargs)
    
    def get_queryset(self):
        """基础查询集优化"""
        queryset = super().get_queryset()
        
        # 只返回活跃的记录
        if hasattr(queryset.model, 'is_active'):
            queryset = queryset.filter(is_active=True)
        
        return queryset
    
    def perform_destroy(self, instance):
        """软删除实现"""
        if hasattr(instance, 'soft_delete'):
            instance.soft_delete()
        else:
            instance.delete()
    
    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """
        统计信息接口
        比喻：API服务大厅的数据统计报表
        """
        queryset = self.get_queryset()
        
        stats = {
            'total_count': queryset.count(),
            'active_count': queryset.filter(is_active=True).count() if hasattr(queryset.model, 'is_active') else queryset.count(),
            'created_today': queryset.filter(
                created_at__date=timezone.now().date()
            ).count() if hasattr(queryset.model, 'created_at') else 0,
        }
        
        return Response(stats)

class DepartmentViewSet(BaseModelViewSet):
    """
    🏢 部门管理视图集
    比喻：API服务大厅的部门服务窗口
    """
    
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    search_fields = ['name', 'code', 'description']
    filterset_fields = ['parent', 'manager']
    ordering_fields = ['name', 'code', 'created_at']
    ordering = ['code']
    
    def get_queryset(self):
        """优化查询集"""
        return super().get_queryset().select_related(
            'parent', 'manager'
        ).prefetch_related('employees', 'children')
    
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        """
        获取部门员工列表
        比喻：查询指定部门的员工花名册
        """
        department = self.get_object()
        employees = department.employees.filter(is_active=True)
        
        # 分页支持
        page = self.paginate_queryset(employees)
        if page is not None:
            serializer = EmployeeSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)
        
        serializer = EmployeeSerializer(employees, many=True, context={'request': request})
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def hierarchy(self, request, pk=None):
        """
        获取部门层级结构
        比喻：查看部门的组织架构图
        """
        department = self.get_object()
        
        def build_hierarchy(dept):
            """递归构建层级结构"""
            children = dept.children.filter(is_active=True)
            return {
                'id': dept.id,
                'name': dept.name,
                'code': dept.code,
                'employee_count': dept.employees.filter(is_active=True).count(),
                'children': [build_hierarchy(child) for child in children]
            }
        
        hierarchy = build_hierarchy(department)
        return Response(hierarchy)
    
    @action(detail=False, methods=['get'])
    def tree(self, request):
        """
        获取完整部门树
        比喻：获取企业完整的组织架构树
        """
        root_departments = self.get_queryset().filter(parent__isnull=True)
        
        def build_tree(departments):
            """构建部门树"""
            tree = []
            for dept in departments:
                children = dept.children.filter(is_active=True)
                node = {
                    'id': dept.id,
                    'name': dept.name,
                    'code': dept.code,
                    'employee_count': dept.employees.filter(is_active=True).count(),
                    'children': build_tree(children) if children.exists() else []
                }
                tree.append(node)
            return tree
        
        tree = build_tree(root_departments)
        return Response(tree)
    
    @action(detail=True, methods=['post'])
    def move(self, request, pk=None):
        """
        移动部门到新的上级部门
        比喻：企业部门的重组调整
        """
        department = self.get_object()
        new_parent_id = request.data.get('new_parent_id')
        
        # 验证移动操作
        if new_parent_id:
            new_parent = get_object_or_404(Department, id=new_parent_id)
            
            # 检查循环引用
            current = new_parent
            while current:
                if current.id == department.id:
                    return Response(
                        {'error': '移动操作会造成循环引用'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                current = current.parent
        
        # 执行移动
        department.parent_id = new_parent_id
        department.save()
        
        return Response({
            'message': '部门移动成功',
            'department': DepartmentSerializer(department, context={'request': request}).data
        })

class EmployeeViewSet(BaseModelViewSet):
    """
    👤 员工管理视图集
    比喻：API服务大厅的人力资源服务窗口
    """
    
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    search_fields = ['username', 'first_name', 'last_name', 'employee_id', 'position']
    filterset_fields = ['department', 'position', 'is_active']
    ordering_fields = ['employee_id', 'hire_date', 'username']
    ordering = ['employee_id']
    
    def get_queryset(self):
        """优化查询集"""
        return super().get_queryset().select_related('department')
    
    @action(detail=False, methods=['get'])
    def by_department(self, request):
        """
        按部门统计员工
        比喻：各部门人力资源分布统计
        """
        departments = Department.objects.filter(is_active=True).annotate(
            employee_count=Count('employees', filter=Q(employees__is_active=True))
        ).order_by('code')
        
        result = []
        for dept in departments:
            result.append({
                'department_id': dept.id,
                'department_name': dept.name,
                'department_code': dept.code,
                'employee_count': dept.employee_count
            })
        
        return Response(result)
    
    @action(detail=False, methods=['get'])
    def salary_statistics(self, request):
        """
        薪资统计信息
        比喻：企业薪资水平分析报告
        """
        # 只有管理员可以查看
        if not request.user.is_staff:
            return Response(
                {'error': '权限不足'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        employees = self.get_queryset().exclude(salary__isnull=True)
        
        stats = employees.aggregate(
            avg_salary=Avg('salary'),
            max_salary=models.Max('salary'),
            min_salary=models.Min('salary')
        )
        
        # 按部门统计
        dept_stats = employees.values('department__name').annotate(
            avg_salary=Avg('salary'),
            employee_count=Count('id')
        ).order_by('-avg_salary')
        
        return Response({
            'overall_statistics': stats,
            'department_statistics': list(dept_stats)
        })
    
    @action(detail=True, methods=['post'])
    def change_department(self, request, pk=None):
        """
        员工部门调动
        比喻：员工的部门转移手续办理
        """
        employee = self.get_object()
        new_department_id = request.data.get('department_id')
        
        if not new_department_id:
            return Response(
                {'error': '请指定新部门ID'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        new_department = get_object_or_404(Department, id=new_department_id)
        old_department = employee.department
        
        employee.department = new_department
        employee.save()
        
        return Response({
            'message': '部门调动成功',
            'old_department': old_department.name if old_department else None,
            'new_department': new_department.name,
            'employee': EmployeeSerializer(employee, context={'request': request}).data
        })
```

#### 2. API版本管理与最佳实践

**🔄 API服务大厅的版本升级管理系统**

```python
"""
API版本管理系统
比喻：企业服务大厅的服务升级和向后兼容管理
"""

# 🔄 版本管理框架
from rest_framework.versioning import URLPathVersioning, NamespaceVersioning
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

class EnterpriseAPIVersioning(URLPathVersioning):
    """
    🔄 企业级API版本控制
    比喻：服务大厅的版本化服务窗口管理
    """
    
    default_version = 'v1'
    allowed_versions = ['v1', 'v2', 'v3']
    version_param = 'version'
    
    def determine_version(self, request, *args, **kwargs):
        """确定API版本"""
        version = super().determine_version(request, *args, **kwargs)
        
        # 记录版本使用情况
        self._log_version_usage(request, version)
        
        return version
    
    def _log_version_usage(self, request, version):
        """记录版本使用统计"""
        # 这里可以集成到监控系统
        pass

# 🎯 版本化序列化器
class DepartmentSerializerV1(DepartmentSerializer):
    """
    🏢 部门序列化器 V1版本
    比喻：服务大厅的传统服务格式
    """
    
    class Meta(DepartmentSerializer.Meta):
        fields = ['id', 'name', 'code', 'description', 'created_at']

class DepartmentSerializerV2(DepartmentSerializer):
    """
    🏢 部门序列化器 V2版本  
    比喻：服务大厅的增强服务格式
    """
    
    # V2版本增加了更多字段
    class Meta(DepartmentSerializer.Meta):
        fields = DepartmentSerializer.Meta.fields + ['manager_info', 'employee_count']

class DepartmentSerializerV3(DepartmentSerializer):
    """
    🏢 部门序列化器 V3版本
    比喻：服务大厅的最新智能服务格式
    """
    
    # V3版本包含完整字段和智能分析
    pass

# 🎛️ 版本化视图集
class VersionedDepartmentViewSet(DepartmentViewSet):
    """
    🏢 版本化部门视图集
    比喻：支持多版本服务的部门服务窗口
    """
    
    versioning_class = EnterpriseAPIVersioning
    
    def get_serializer_class(self):
        """根据版本选择序列化器"""
        version = self.request.version
        
        serializer_map = {
            'v1': DepartmentSerializerV1,
            'v2': DepartmentSerializerV2,
            'v3': DepartmentSerializerV3,
        }
        
        return serializer_map.get(version, DepartmentSerializerV3)
    
    def list(self, request, *args, **kwargs):
        """版本化列表接口"""
        response = super().list(request, *args, **kwargs)
        
        # 为旧版本添加兼容性处理
        if request.version == 'v1':
            # V1版本的特殊处理
            response.data = self._convert_to_v1_format(response.data)
        
        # 添加版本信息到响应头
        response['API-Version'] = request.version
        response['Supported-Versions'] = ','.join(self.versioning_class.allowed_versions)
        
        return response
    
    def _convert_to_v1_format(self, data):
        """转换为V1格式兼容"""
        if isinstance(data, dict) and 'results' in data:
            # 分页格式
            for item in data['results']:
                self._simplify_department_data(item)
        elif isinstance(data, list):
            # 直接列表格式
            for item in data:
                self._simplify_department_data(item)
        
        return data
    
    def _simplify_department_data(self, item):
        """简化部门数据为V1格式"""
        # 移除V1不支持的字段
        fields_to_remove = ['manager_info', 'employee_count', 'department_path']
        for field in fields_to_remove:
            item.pop(field, None)

# 📋 API文档自动生成
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.schemas import get_schema_view
from rest_framework.renderers import TemplateHTMLRenderer

class EnterpriseAutoSchema(AutoSchema):
    """
    📋 企业级API文档生成器
    比喻：服务大厅的业务指南和操作手册生成系统
    """
    
    def get_operation(self, path, method):
        """生成API操作文档"""
        operation = super().get_operation(path, method)
        
        # 添加企业级文档元信息
        if operation:
            operation.setdefault('tags', [])
            operation.setdefault('x-enterprise-category', self._get_enterprise_category())
            operation.setdefault('x-permission-required', self._get_permission_info())
        
        return operation
    
    def _get_enterprise_category(self):
        """获取企业分类"""
        if hasattr(self.view, 'enterprise_category'):
            return self.view.enterprise_category
        return 'General'
    
    def _get_permission_info(self):
        """获取权限信息"""
        permissions = []
        for permission_class in self.view.permission_classes:
            permissions.append(permission_class.__name__)
        return permissions

# API文档视图
schema_view = get_schema_view(
    title='企业管理系统 API',
    description='现代化企业总部大厦管理系统的完整API接口',
    version='v3.0.0',
    patterns=[
        # API路由模式
    ],
    public=True,
    permission_classes=[],
    generator_class=EnterpriseAutoSchema,
)
```

#### 3. 性能优化策略

**⚡ API服务大厅的高效运营优化系统**

```python
"""
API性能优化系统
比喻：企业服务大厅的效率提升和优化管理
"""

# ⚡ 查询优化中间件
from django.utils.deprecation import MiddlewareMixin
from django.db import connection
from django.conf import settings
import time
import logging

class QueryOptimizationMiddleware(MiddlewareMixin):
    """
    ⚡ 查询优化中间件
    比喻：服务大厅的效率监控和优化系统
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger('api.performance')
        
    def process_request(self, request):
        """请求开始时的处理"""
        request.start_time = time.time()
        request.start_queries = len(connection.queries)
        
    def process_response(self, request, response):
        """请求结束时的性能分析"""
        if hasattr(request, 'start_time'):
            # 计算处理时间
            total_time = time.time() - request.start_time
            
            # 计算数据库查询次数
            total_queries = len(connection.queries) - request.start_queries
            
            # 记录性能数据
            if total_time > 1.0 or total_queries > 10:  # 超过阈值记录
                self.logger.warning(
                    f"Slow API request: {request.path} "
                    f"Time: {total_time:.2f}s Queries: {total_queries}"
                )
            
            # 添加性能信息到响应头
            response['X-Response-Time'] = f"{total_time:.3f}s"
            response['X-Query-Count'] = str(total_queries)
        
        return response

# 🔄 缓存优化
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import action
import hashlib

class CacheOptimizedViewSet(BaseModelViewSet):
    """
    🔄 缓存优化视图集
    比喻：服务大厅的智能缓存和快速响应系统
    """
    
    cache_timeout = 300  # 5分钟缓存
    
    def get_cache_key(self, prefix, *args):
        """生成缓存键"""
        key_parts = [prefix] + [str(arg) for arg in args]
        key_string = ':'.join(key_parts)
        return hashlib.md5(key_string.encode()).hexdigest()
    
    @method_decorator(cache_page(300))
    @action(detail=False, methods=['get'])
    def cached_statistics(self, request):
        """
        缓存的统计信息
        比喻：服务大厅的快速统计报告
        """
        cache_key = self.get_cache_key('stats', self.__class__.__name__)
        
        stats = cache.get(cache_key)
        if stats is None:
            # 计算统计信息
            stats = self._calculate_statistics()
            cache.set(cache_key, stats, self.cache_timeout)
        
        return Response(stats)
    
    def _calculate_statistics(self):
        """计算统计信息"""
        queryset = self.get_queryset()
        return {
            'total_count': queryset.count(),
            'active_count': queryset.filter(is_active=True).count(),
            'created_this_month': queryset.filter(
                created_at__month=timezone.now().month
            ).count(),
        }
    
    def invalidate_cache(self, cache_keys):
        """使缓存失效"""
        for key in cache_keys:
            cache.delete(key)

# 📊 分页优化
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict

class OptimizedPagination(PageNumberPagination):
    """
    📊 优化的分页器
    比喻：服务大厅的智能分页和数据展示系统
    """
    
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100
    
    def get_paginated_response(self, data):
        """优化的分页响应"""
        return Response(OrderedDict([
            ('pagination', {
                'count': self.page.paginator.count,
                'page_size': self.page_size,
                'current_page': self.page.number,
                'total_pages': self.page.paginator.num_pages,
                'has_next': self.page.has_next(),
                'has_previous': self.page.has_previous(),
                'next_page': self.page.next_page_number() if self.page.has_next() else None,
                'previous_page': self.page.previous_page_number() if self.page.has_previous() else None,
            }),
            ('results', data)
        ]))

# 🎯 批量操作优化
class BulkOperationMixin:
    """
    🎯 批量操作混入
    比喻：服务大厅的批量业务处理窗口
    """
    
    @action(detail=False, methods=['post'])
    def bulk_create(self, request):
        """批量创建"""
        data_list = request.data
        if not isinstance(data_list, list):
            return Response(
                {'error': '请提供数组格式的数据'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = self.get_serializer(data=data_list, many=True)
        if serializer.is_valid():
            instances = serializer.save()
            return Response(
                {
                    'message': f'成功创建 {len(instances)} 条记录',
                    'data': serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['patch'])
    def bulk_update(self, request):
        """批量更新"""
        data_list = request.data
        if not isinstance(data_list, list):
            return Response(
                {'error': '请提供数组格式的数据'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        updated_instances = []
        errors = []
        
        for item_data in data_list:
            item_id = item_data.get('id')
            if not item_id:
                errors.append({'error': '缺少ID字段'})
                continue
            
            try:
                instance = self.get_queryset().get(id=item_id)
                serializer = self.get_serializer(
                    instance, 
                    data=item_data, 
                    partial=True
                )
                
                if serializer.is_valid():
                    serializer.save()
                    updated_instances.append(serializer.data)
                else:
                    errors.append({
                        'id': item_id,
                        'errors': serializer.errors
                    })
            except self.queryset.model.DoesNotExist:
                errors.append({
                    'id': item_id,
                    'error': '记录不存在'
                })
        
        return Response({
            'updated_count': len(updated_instances),
            'updated_data': updated_instances,
            'errors': errors
        })
    
    @action(detail=False, methods=['delete'])
    def bulk_delete(self, request):
        """批量删除"""
        ids = request.data.get('ids', [])
        if not isinstance(ids, list):
            return Response(
                {'error': '请提供ID数组'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        queryset = self.get_queryset().filter(id__in=ids)
        count = queryset.count()
        
        # 执行软删除或硬删除
        for instance in queryset:
            self.perform_destroy(instance)
        
        return Response({
            'message': f'成功删除 {count} 条记录',
            'deleted_ids': ids
        })
```

### 🎯 实战项目：企业级任务管理API平台

```python
"""
企业级任务管理API平台
比喻：企业服务大厅的项目任务管理服务窗口
"""

# 📋 任务管理模型
class Project(BaseModel):
    """项目模型"""
    name = models.CharField(max_length=200, verbose_name="项目名称")
    description = models.TextField(blank=True, verbose_name="项目描述")
    manager = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT,
        related_name='managed_projects',
        verbose_name="项目经理"
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name='projects',
        verbose_name="负责部门"
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('PLANNING', '规划中'),
            ('ACTIVE', '进行中'),
            ('COMPLETED', '已完成'),
            ('CANCELLED', '已取消')
        ],
        default='PLANNING',
        verbose_name="项目状态"
    )
    start_date = models.DateField(verbose_name="开始日期")
    end_date = models.DateField(verbose_name="结束日期")
    
    class Meta:
        verbose_name = "项目"
        verbose_name_plural = "项目"
        ordering = ['-created_at']

class Task(BaseModel):
    """任务模型"""
    title = models.CharField(max_length=200, verbose_name="任务标题")
    description = models.TextField(blank=True, verbose_name="任务描述")
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name="所属项目"
    )
    assignee = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT,
        related_name='assigned_tasks',
        verbose_name="负责人"
    )
    reporter = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT,
        related_name='reported_tasks',
        verbose_name="报告人"
    )
    priority = models.CharField(
        max_length=10,
        choices=[
            ('LOW', '低'),
            ('MEDIUM', '中'),
            ('HIGH', '高'),
            ('URGENT', '紧急')
        ],
        default='MEDIUM',
        verbose_name="优先级"
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('TODO', '待办'),
            ('IN_PROGRESS', '进行中'),
            ('TESTING', '测试中'),
            ('DONE', '已完成'),
            ('CANCELLED', '已取消')
        ],
        default='TODO',
        verbose_name="任务状态"
    )
    due_date = models.DateTimeField(null=True, blank=True, verbose_name="截止时间")
    
    class Meta:
        verbose_name = "任务"
        verbose_name_plural = "任务"
        ordering = ['-priority', 'due_date']

# 🎯 任务管理API
class TaskViewSet(BulkOperationMixin, CacheOptimizedViewSet):
    """
    📋 任务管理视图集
    比喻：服务大厅的任务处理和跟踪服务
    """
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_fields = ['project', 'assignee', 'status', 'priority']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'due_date', 'priority']
    
    @action(detail=False, methods=['get'])
    def my_tasks(self, request):
        """
        我的任务列表
        比喻：个人任务处理台
        """
        tasks = self.get_queryset().filter(assignee=request.user)
        
        # 按状态分组
        grouped_tasks = {
            'todo': tasks.filter(status='TODO'),
            'in_progress': tasks.filter(status='IN_PROGRESS'),
            'testing': tasks.filter(status='TESTING'),
            'done': tasks.filter(status='DONE')
        }
        
        result = {}
        for status, task_queryset in grouped_tasks.items():
            serializer = self.get_serializer(task_queryset, many=True)
            result[status] = serializer.data
        
        return Response(result)
    
    @action(detail=True, methods=['post'])
    def change_status(self, request, pk=None):
        """
        更改任务状态
        比喻：任务状态更新处理
        """
        task = self.get_object()
        new_status = request.data.get('status')
        
        if new_status not in dict(Task.STATUS_CHOICES):
            return Response(
                {'error': '无效的状态值'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        old_status = task.status
        task.status = new_status
        task.save()
        
        return Response({
            'message': '任务状态更新成功',
            'old_status': old_status,
            'new_status': new_status,
            'task': TaskSerializer(task, context={'request': request}).data
        })
```

### 📚 本节小结

通过本节学习，我们深入掌握了Django REST Framework的企业级应用和优化策略：

#### 🎯 核心要点
1. **DRF高级特性**：动态字段、嵌套序列化、高级视图集
2. **API版本管理**：版本化序列化器、向后兼容、文档生成
3. **性能优化**：查询优化、缓存策略、批量操作
4. **实战项目**：企业级任务管理API平台

#### 🚀 API设计原则
- **RESTful设计**：遵循REST架构风格
- **版本管理**：确保API向后兼容
- **性能优化**：提供高效的数据访问
- **文档完整**：自动生成完整的API文档

#### 💡 最佳实践
- 使用动态字段控制响应数据
- 实现完整的版本管理策略
- 采用多层缓存提升性能
- 提供批量操作支持高并发场景

---

## 第39.3节 ⚡ 实时通信部 - Django Channels与异步编程

> ⚡ **比喻场景**：想象企业总部大厦中有一个高效的实时通信部门，就像现代企业的内部通讯系统。这个部门负责处理紧急消息、实时协调、广播通知等需要立即响应的业务。员工们可以通过各种渠道(电话、对讲机、即时通讯)进行实时沟通。Django Channels就是这样的实时通信系统，让Web应用能够处理WebSocket连接、实时推送和异步任务。

### 🎯 学习重点
- Django Channels核心概念与架构
- WebSocket实时通信实现
- 异步编程模式与任务处理
- 企业级实时应用开发

### 💡 核心概念

#### 1. Django Channels基础架构

**⚡ 企业实时通信系统架构**

```python
"""
Django Channels实时通信架构
比喻：企业总部大厦的多渠道实时通信系统
"""

# 🏗️ Channels配置
# settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',  # Django Channels
    'enterprise_app',
]

# Channels配置
ASGI_APPLICATION = 'enterprise_project.asgi.application'

# Channel Layer配置 - 使用Redis作为消息代理
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
            "capacity": 1500,  # 消息队列容量
            "expiry": 10,  # 消息过期时间
        },
    },
}

# 🚀 ASGI应用配置
# asgi.py
"""
ASGI配置
比喻：企业通信系统的总控制中心
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
import enterprise_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'enterprise_project.settings')

# 协议路由器 - 根据协议类型分发请求
application = ProtocolTypeRouter({
    # HTTP请求走Django的ASGI应用
    "http": get_asgi_application(),
    
    # WebSocket请求走Channels路由
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                enterprise_app.routing.websocket_urlpatterns
            )
        )
    ),
})

# 📡 WebSocket路由配置
# enterprise_app/routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/notifications/$', consumers.NotificationConsumer.as_asgi()),
    re_path(r'ws/collaboration/(?P<project_id>[^/]+)/$', consumers.CollaborationConsumer.as_asgi()),
    re_path(r'ws/dashboard/$', consumers.DashboardConsumer.as_asgi()),
]

# 💬 基础消费者类
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json
import logging

logger = logging.getLogger(__name__)

class BaseAsyncConsumer(AsyncWebsocketConsumer):
    """
    💬 基础异步消费者
    比喻：企业通信系统的基础通信员
    """
    
    async def connect(self):
        """建立连接"""
        # 获取用户信息
        self.user = self.scope["user"]
        
        # 验证用户权限
        if not await self.has_permission():
            await self.close()
            return
        
        # 接受WebSocket连接
        await self.accept()
        
        # 记录连接日志
        await self.log_connection("connected")
    
    async def disconnect(self, close_code):
        """断开连接"""
        await self.log_connection("disconnected")
    
    async def receive(self, text_data=None, bytes_data=None):
        """接收消息"""
        if text_data:
            try:
                data = json.loads(text_data)
                await self.handle_message(data)
            except json.JSONDecodeError:
                await self.send_error("Invalid JSON format")
            except Exception as e:
                logger.error(f"Error handling message: {e}")
                await self.send_error("Internal server error")
    
    async def handle_message(self, data):
        """处理消息 - 子类需要实现"""
        raise NotImplementedError
    
    async def has_permission(self):
        """检查权限 - 子类可以重写"""
        return self.user.is_authenticated
    
    async def send_json(self, content):
        """发送JSON数据"""
        await self.send(text_data=json.dumps(content, ensure_ascii=False))
    
    async def send_error(self, message, code=None):
        """发送错误消息"""
        await self.send_json({
            'type': 'error',
            'message': message,
            'code': code
        })
    
    @database_sync_to_async
    def log_connection(self, action):
        """记录连接日志"""
        from .models import ConnectionLog
        ConnectionLog.objects.create(
            user=self.user if self.user.is_authenticated else None,
            action=action,
            channel_name=self.channel_name,
            ip_address=self.scope.get('client', [''])[0]
        )
```

#### 2. 实时聊天系统实现

**💬 企业内部即时通讯系统**

```python
"""
实时聊天系统
比喻：企业内部的即时通讯办公室
"""

# 💬 聊天消费者
class ChatConsumer(BaseAsyncConsumer):
    """
    💬 聊天消费者
    比喻：聊天室的通信管理员
    """
    
    async def connect(self):
        """用户进入聊天室"""
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        
        # 加入聊天室群组
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        
        # 获取聊天室信息
        room_info = await self.get_room_info()
        
        # 发送欢迎消息
        await self.send_json({
            'type': 'welcome',
            'room': room_info,
            'user': await self.get_user_info()
        })
        
        # 广播用户加入消息
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_join',
                'user': await self.get_user_info(),
                'message': f'{self.user.get_full_name()} 加入了聊天室'
            }
        )
        
        # 发送历史消息
        await self.send_recent_messages()
    
    async def disconnect(self, close_code):
        """用户离开聊天室"""
        # 广播用户离开消息
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_leave',
                'user': await self.get_user_info(),
                'message': f'{self.user.get_full_name()} 离开了聊天室'
            }
        )
        
        # 离开聊天室群组
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def handle_message(self, data):
        """处理接收的消息"""
        message_type = data.get('type')
        
        if message_type == 'chat_message':
            await self.handle_chat_message(data)
        elif message_type == 'typing':
            await self.handle_typing_indicator(data)
        elif message_type == 'read_receipt':
            await self.handle_read_receipt(data)
        else:
            await self.send_error(f"Unknown message type: {message_type}")
    
    async def handle_chat_message(self, data):
        """处理聊天消息"""
        message_content = data.get('message', '').strip()
        
        if not message_content:
            await self.send_error("消息内容不能为空")
            return
        
        # 保存消息到数据库
        message = await self.save_message(message_content)
        
        # 广播消息到聊天室
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': {
                    'id': str(message.id),
                    'content': message.content,
                    'user': await self.get_user_info(),
                    'timestamp': message.created_at.isoformat(),
                    'is_read': False
                }
            }
        )
    
    async def handle_typing_indicator(self, data):
        """处理输入状态指示"""
        is_typing = data.get('is_typing', False)
        
        # 广播输入状态
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'typing_indicator',
                'user': await self.get_user_info(),
                'is_typing': is_typing
            }
        )
    
    async def handle_read_receipt(self, data):
        """处理已读回执"""
        message_id = data.get('message_id')
        
        if message_id:
            # 更新消息已读状态
            await self.mark_message_as_read(message_id)
            
            # 发送已读确认
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'read_receipt',
                    'message_id': message_id,
                    'user': await self.get_user_info()
                }
            )
    
    # 事件处理器 - 处理从group_send发来的消息
    async def chat_message(self, event):
        """发送聊天消息到WebSocket"""
        await self.send_json({
            'type': 'chat_message',
            'message': event['message']
        })
    
    async def user_join(self, event):
        """发送用户加入通知"""
        await self.send_json({
            'type': 'user_join',
            'user': event['user'],
            'message': event['message']
        })
    
    async def user_leave(self, event):
        """发送用户离开通知"""
        await self.send_json({
            'type': 'user_leave',
            'user': event['user'],
            'message': event['message']
        })
    
    async def typing_indicator(self, event):
        """发送输入状态指示"""
        # 不发送给自己
        if event['user']['id'] != self.user.id:
            await self.send_json({
                'type': 'typing_indicator',
                'user': event['user'],
                'is_typing': event['is_typing']
            })
    
    async def read_receipt(self, event):
        """发送已读回执"""
        await self.send_json({
            'type': 'read_receipt',
            'message_id': event['message_id'],
            'user': event['user']
        })
    
    # 数据库操作方法
    @database_sync_to_async
    def get_room_info(self):
        """获取聊天室信息"""
        from .models import ChatRoom
        try:
            room = ChatRoom.objects.get(name=self.room_name)
            return {
                'id': str(room.id),
                'name': room.name,
                'description': room.description,
                'created_at': room.created_at.isoformat(),
                'member_count': room.members.count()
            }
        except ChatRoom.DoesNotExist:
            # 自动创建聊天室
            room = ChatRoom.objects.create(
                name=self.room_name,
                created_by=self.user
            )
            room.members.add(self.user)
            return {
                'id': str(room.id),
                'name': room.name,
                'description': room.description,
                'created_at': room.created_at.isoformat(),
                'member_count': 1
            }
    
    @database_sync_to_async
    def get_user_info(self):
        """获取用户信息"""
        return {
            'id': self.user.id,
            'username': self.user.username,
            'full_name': self.user.get_full_name(),
            'avatar_url': getattr(self.user, 'avatar_url', None)
        }
    
    @database_sync_to_async
    def save_message(self, content):
        """保存消息到数据库"""
        from .models import ChatMessage, ChatRoom
        room = ChatRoom.objects.get(name=self.room_name)
        
        message = ChatMessage.objects.create(
            room=room,
            user=self.user,
            content=content
        )
        
        # 更新聊天室最后活动时间
        room.last_activity = timezone.now()
        room.save()
        
        return message
    
    @database_sync_to_async
    def send_recent_messages(self):
        """发送最近的消息历史"""
        from .models import ChatMessage, ChatRoom
        
        try:
            room = ChatRoom.objects.get(name=self.room_name)
            messages = ChatMessage.objects.filter(
                room=room
            ).select_related('user').order_by('-created_at')[:50]
            
            # 反转顺序，从旧到新
            messages = reversed(messages)
            
            for message in messages:
                self.send_json({
                    'type': 'history_message',
                    'message': {
                        'id': str(message.id),
                        'content': message.content,
                        'user': {
                            'id': message.user.id,
                            'username': message.user.username,
                            'full_name': message.user.get_full_name()
                        },
                        'timestamp': message.created_at.isoformat(),
                        'is_read': True
                    }
                })
        except ChatRoom.DoesNotExist:
            pass
    
    @database_sync_to_async
    def mark_message_as_read(self, message_id):
        """标记消息为已读"""
        from .models import ChatMessage, MessageReadStatus
        
        try:
            message = ChatMessage.objects.get(id=message_id)
            MessageReadStatus.objects.get_or_create(
                message=message,
                user=self.user,
                defaults={'read_at': timezone.now()}
            )
        except ChatMessage.DoesNotExist:
            pass

# 📢 通知消费者
class NotificationConsumer(BaseAsyncConsumer):
    """
    📢 通知消费者
    比喻：企业广播通知系统
    """
    
    async def connect(self):
        """建立通知连接"""
        if not self.user.is_authenticated:
            await self.close()
            return
        
        # 创建用户专属通知组
        self.user_group_name = f'notifications_user_{self.user.id}'
        
        # 加入用户通知组
        await self.channel_layer.group_add(
            self.user_group_name,
            self.channel_name
        )
        
        # 加入部门通知组
        if hasattr(self.user, 'department') and self.user.department:
            self.dept_group_name = f'notifications_dept_{self.user.department.id}'
            await self.channel_layer.group_add(
                self.dept_group_name,
                self.channel_name
            )
        
        # 加入全局通知组
        await self.channel_layer.group_add(
            'notifications_global',
            self.channel_name
        )
        
        await self.accept()
        
        # 发送未读通知
        await self.send_unread_notifications()
    
    async def disconnect(self, close_code):
        """断开通知连接"""
        # 离开所有通知组
        await self.channel_layer.group_discard(
            self.user_group_name,
            self.channel_name
        )
        
        if hasattr(self, 'dept_group_name'):
            await self.channel_layer.group_discard(
                self.dept_group_name,
                self.channel_name
            )
        
        await self.channel_layer.group_discard(
            'notifications_global',
            self.channel_name
        )
    
    async def handle_message(self, data):
        """处理通知相关消息"""
        action = data.get('action')
        
        if action == 'mark_read':
            await self.mark_notification_read(data.get('notification_id'))
        elif action == 'mark_all_read':
            await self.mark_all_notifications_read()
        elif action == 'get_unread_count':
            await self.send_unread_count()
    
    # 通知事件处理器
    async def send_notification(self, event):
        """发送通知到客户端"""
        await self.send_json({
            'type': 'notification',
            'notification': event['notification']
        })
    
    async def update_notification(self, event):
        """更新通知状态"""
        await self.send_json({
            'type': 'notification_update',
            'notification_id': event['notification_id'],
            'updates': event['updates']
        })
    
    @database_sync_to_async
    def send_unread_notifications(self):
        """发送未读通知"""
        from .models import Notification
        
        notifications = Notification.objects.filter(
            recipient=self.user,
            is_read=False
        ).order_by('-created_at')[:20]
        
        unread_count = Notification.objects.filter(
            recipient=self.user,
            is_read=False
        ).count()
        
        # 发送未读数量
        self.send_json({
            'type': 'unread_count',
            'count': unread_count
        })
        
        # 发送未读通知列表
        for notification in notifications:
            self.send_json({
                'type': 'notification',
                'notification': {
                    'id': str(notification.id),
                    'title': notification.title,
                    'message': notification.message,
                    'category': notification.category,
                    'priority': notification.priority,
                    'created_at': notification.created_at.isoformat(),
                    'is_read': notification.is_read,
                    'action_url': notification.action_url
                }
            })
```

#### 3. 协作编辑系统

**🤝 实时协作编辑系统**

```python
"""
实时协作编辑系统
比喻：企业协同办公室，多人同时编辑文档
"""

class CollaborationConsumer(BaseAsyncConsumer):
    """
    🤝 协作编辑消费者
    比喻：协同办公室的协调员
    """
    
    async def connect(self):
        """加入协作会话"""
        self.project_id = self.scope['url_route']['kwargs']['project_id']
        self.project_group_name = f'collab_{self.project_id}'
        
        # 检查项目访问权限
        if not await self.has_project_access():
            await self.close()
            return
        
        # 加入项目协作组
        await self.channel_layer.group_add(
            self.project_group_name,
            self.channel_name
        )
        
        await self.accept()
        
        # 创建协作会话
        self.session_id = await self.create_collaboration_session()
        
        # 获取当前文档状态
        document_state = await self.get_document_state()
        
        # 发送初始状态
        await self.send_json({
            'type': 'init',
            'session_id': self.session_id,
            'document': document_state,
            'collaborators': await self.get_active_collaborators()
        })
        
        # 通知其他用户有新协作者加入
        await self.channel_layer.group_send(
            self.project_group_name,
            {
                'type': 'collaborator_join',
                'user': await self.get_user_info(),
                'cursor_color': await self.assign_cursor_color()
            }
        )
    
    async def disconnect(self, close_code):
        """离开协作会话"""
        # 结束协作会话
        await self.end_collaboration_session()
        
        # 通知其他用户
        await self.channel_layer.group_send(
            self.project_group_name,
            {
                'type': 'collaborator_leave',
                'user': await self.get_user_info()
            }
        )
        
        # 离开协作组
        await self.channel_layer.group_discard(
            self.project_group_name,
            self.channel_name
        )
    
    async def handle_message(self, data):
        """处理协作消息"""
        action = data.get('action')
        
        handlers = {
            'cursor_move': self.handle_cursor_move,
            'selection_change': self.handle_selection_change,
            'content_change': self.handle_content_change,
            'save_document': self.handle_save_document,
            'request_lock': self.handle_lock_request,
            'release_lock': self.handle_lock_release,
        }
        
        handler = handlers.get(action)
        if handler:
            await handler(data)
        else:
            await self.send_error(f"Unknown action: {action}")
    
    async def handle_cursor_move(self, data):
        """处理光标移动"""
        cursor_position = data.get('position')
        
        # 广播光标位置
        await self.channel_layer.group_send(
            self.project_group_name,
            {
                'type': 'cursor_update',
                'user': await self.get_user_info(),
                'position': cursor_position
            }
        )
    
    async def handle_selection_change(self, data):
        """处理选区变化"""
        selection = data.get('selection')
        
        # 广播选区信息
        await self.channel_layer.group_send(
            self.project_group_name,
            {
                'type': 'selection_update',
                'user': await self.get_user_info(),
                'selection': selection
            }
        )
    
    async def handle_content_change(self, data):
        """处理内容变更"""
        # 操作变换（OT）处理
        operation = data.get('operation')
        version = data.get('version')
        
        # 验证版本号
        current_version = await self.get_document_version()
        if version != current_version:
            # 需要进行操作变换
            operation = await self.transform_operation(operation, version, current_version)
        
        # 应用操作
        new_version = await self.apply_operation(operation)
        
        # 广播变更
        await self.channel_layer.group_send(
            self.project_group_name,
            {
                'type': 'content_update',
                'operation': operation,
                'version': new_version,
                'author': await self.get_user_info()
            }
        )
        
        # 保存操作历史
        await self.save_operation_history(operation, new_version)
    
    async def handle_save_document(self, data):
        """处理文档保存"""
        # 获取保存锁
        if not await self.acquire_save_lock():
            await self.send_error("另一个用户正在保存文档")
            return
        
        try:
            # 保存文档
            save_result = await self.save_document_to_db()
            
            # 广播保存成功
            await self.channel_layer.group_send(
                self.project_group_name,
                {
                    'type': 'document_saved',
                    'saved_by': await self.get_user_info(),
                    'version': save_result['version'],
                    'timestamp': save_result['timestamp']
                }
            )
        finally:
            # 释放保存锁
            await self.release_save_lock()
    
    async def handle_lock_request(self, data):
        """处理锁定请求"""
        element_id = data.get('element_id')
        
        # 尝试获取元素锁
        lock_acquired = await self.acquire_element_lock(element_id)
        
        if lock_acquired:
            # 广播锁定信息
            await self.channel_layer.group_send(
                self.project_group_name,
                {
                    'type': 'element_locked',
                    'element_id': element_id,
                    'locked_by': await self.get_user_info()
                }
            )
        else:
            # 发送锁定失败信息
            current_lock_holder = await self.get_lock_holder(element_id)
            await self.send_json({
                'type': 'lock_failed',
                'element_id': element_id,
                'locked_by': current_lock_holder
            })
    
    # 事件处理器
    async def collaborator_join(self, event):
        """新协作者加入"""
        if event['user']['id'] != self.user.id:
            await self.send_json({
                'type': 'collaborator_join',
                'user': event['user'],
                'cursor_color': event['cursor_color']
            })
    
    async def collaborator_leave(self, event):
        """协作者离开"""
        if event['user']['id'] != self.user.id:
            await self.send_json({
                'type': 'collaborator_leave',
                'user': event['user']
            })
    
    async def cursor_update(self, event):
        """光标更新"""
        if event['user']['id'] != self.user.id:
            await self.send_json({
                'type': 'cursor_update',
                'user': event['user'],
                'position': event['position']
            })
    
    async def content_update(self, event):
        """内容更新"""
        await self.send_json({
            'type': 'content_update',
            'operation': event['operation'],
            'version': event['version'],
            'author': event['author']
        })
    
    # 数据库操作
    @database_sync_to_async
    def has_project_access(self):
        """检查项目访问权限"""
        from .models import Project
        try:
            project = Project.objects.get(id=self.project_id)
            return (
                project.manager == self.user or
                self.user in project.members.all() or
                self.user.is_superuser
            )
        except Project.DoesNotExist:
            return False
    
    @database_sync_to_async
    def create_collaboration_session(self):
        """创建协作会话"""
        from .models import CollaborationSession
        session = CollaborationSession.objects.create(
            project_id=self.project_id,
            user=self.user,
            channel_name=self.channel_name
        )
        return str(session.id)
    
    @database_sync_to_async
    def get_active_collaborators(self):
        """获取活跃的协作者"""
        from .models import CollaborationSession
        
        sessions = CollaborationSession.objects.filter(
            project_id=self.project_id,
            is_active=True
        ).select_related('user')
        
        collaborators = []
        for session in sessions:
            collaborators.append({
                'id': session.user.id,
                'username': session.user.username,
                'full_name': session.user.get_full_name(),
                'cursor_color': session.cursor_color
            })
        
        return collaborators
```

#### 4. 异步任务处理系统

**🔄 异步任务处理与监控**

```python
"""
异步任务处理系统
比喻：企业的任务调度中心
"""

# 🔄 Celery异步任务集成
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import time

@shared_task(bind=True)
def long_running_task(self, user_id, task_data):
    """
    长时间运行的任务
    比喻：企业的批处理任务中心
    """
    channel_layer = get_channel_layer()
    user_group = f'notifications_user_{user_id}'
    
    # 发送任务开始通知
    async_to_sync(channel_layer.group_send)(
        user_group,
        {
            'type': 'send_notification',
            'notification': {
                'id': str(self.request.id),
                'title': '任务开始执行',
                'message': f'任务 {task_data["name"]} 已开始执行',
                'category': 'task',
                'priority': 'info',
                'created_at': timezone.now().isoformat()
            }
        }
    )
    
    try:
        # 模拟长时间任务
        total_steps = 10
        for i in range(total_steps):
            # 执行任务步骤
            time.sleep(2)
            
            # 更新进度
            progress = (i + 1) / total_steps * 100
            
            # 发送进度更新
            async_to_sync(channel_layer.group_send)(
                user_group,
                {
                    'type': 'send_notification',
                    'notification': {
                        'id': str(self.request.id),
                        'title': '任务进度更新',
                        'message': f'任务进度: {progress:.0f}%',
                        'category': 'task_progress',
                        'priority': 'info',
                        'created_at': timezone.now().isoformat(),
                        'extra_data': {
                            'progress': progress,
                            'current_step': i + 1,
                            'total_steps': total_steps
                        }
                    }
                }
            )
        
        # 任务完成
        result = {'status': 'success', 'data': '任务执行完成'}
        
        # 发送完成通知
        async_to_sync(channel_layer.group_send)(
            user_group,
            {
                'type': 'send_notification',
                'notification': {
                    'id': str(self.request.id),
                    'title': '任务完成',
                    'message': f'任务 {task_data["name"]} 已成功完成',
                    'category': 'task',
                    'priority': 'success',
                    'created_at': timezone.now().isoformat(),
                    'action_url': f'/tasks/{self.request.id}/result/'
                }
            }
        )
        
        return result
        
    except Exception as e:
        # 发送错误通知
        async_to_sync(channel_layer.group_send)(
            user_group,
            {
                'type': 'send_notification',
                'notification': {
                    'id': str(self.request.id),
                    'title': '任务失败',
                    'message': f'任务执行失败: {str(e)}',
                    'category': 'task',
                    'priority': 'error',
                    'created_at': timezone.now().isoformat()
                }
            }
        )
        
        raise

# 📊 实时数据看板
class DashboardConsumer(BaseAsyncConsumer):
    """
    📊 数据看板消费者
    比喻：企业数据监控中心的大屏幕
    """
    
    async def connect(self):
        """连接到数据看板"""
        # 检查权限
        if not await self.has_dashboard_permission():
            await self.close()
            return
        
        # 加入看板组
        self.dashboard_group = 'dashboard_main'
        await self.channel_layer.group_add(
            self.dashboard_group,
            self.channel_name
        )
        
        await self.accept()
        
        # 发送初始数据
        await self.send_dashboard_data()
        
        # 启动定期更新
        self.update_task = asyncio.create_task(self.periodic_update())
    
    async def disconnect(self, close_code):
        """断开连接"""
        # 取消定期更新任务
        if hasattr(self, 'update_task'):
            self.update_task.cancel()
        
        # 离开看板组
        await self.channel_layer.group_discard(
            self.dashboard_group,
            self.channel_name
        )
    
    async def periodic_update(self):
        """定期更新数据"""
        while True:
            await asyncio.sleep(5)  # 每5秒更新一次
            
            # 获取实时数据
            metrics = await self.get_real_time_metrics()
            
            # 发送更新
            await self.send_json({
                'type': 'metrics_update',
                'metrics': metrics,
                'timestamp': timezone.now().isoformat()
            })
    
    @database_sync_to_async
    def get_real_time_metrics(self):
        """获取实时指标数据"""
        from django.db.models import Count, Sum, Avg
        from .models import Task, Project, Department
        
        # 任务统计
        task_stats = Task.objects.aggregate(
            total=Count('id'),
            completed=Count('id', filter=Q(status='DONE')),
            in_progress=Count('id', filter=Q(status='IN_PROGRESS')),
            overdue=Count('id', filter=Q(
                due_date__lt=timezone.now(),
                status__in=['TODO', 'IN_PROGRESS']
            ))
        )
        
        # 项目统计
        project_stats = Project.objects.aggregate(
            active=Count('id', filter=Q(status='ACTIVE')),
            completed=Count('id', filter=Q(status='COMPLETED')),
            delayed=Count('id', filter=Q(
                end_date__lt=timezone.now(),
                status='ACTIVE'
            ))
        )
        
        # 部门效率
        dept_efficiency = Department.objects.annotate(
            task_count=Count('employees__assigned_tasks'),
            completed_tasks=Count(
                'employees__assigned_tasks',
                filter=Q(employees__assigned_tasks__status='DONE')
            )
        ).values('name', 'task_count', 'completed_tasks')[:5]
        
        return {
            'tasks': task_stats,
            'projects': project_stats,
            'department_efficiency': list(dept_efficiency),
            'active_users': self.get_active_user_count(),
            'system_health': self.get_system_health()
        }
    
    def get_active_user_count(self):
        """获取活跃用户数"""
        # 从Redis获取活跃会话数
        from django.core.cache import cache
        return cache.get('active_users', 0)
    
    def get_system_health(self):
        """获取系统健康状态"""
        return {
            'cpu_usage': 45.2,  # 实际应用中从监控系统获取
            'memory_usage': 62.8,
            'response_time': 120,  # ms
            'error_rate': 0.02  # 2%
        }

# 🔧 异步任务管理器
from django.core.management.base import BaseCommand
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import asyncio

class AsyncTaskManager:
    """
    🔧 异步任务管理器
    比喻：企业的任务调度总控室
    """
    
    def __init__(self):
        self.channel_layer = get_channel_layer()
        self.tasks = {}
    
    async def schedule_task(self, task_func, *args, **kwargs):
        """调度异步任务"""
        task_id = str(uuid.uuid4())
        
        # 创建任务
        task = asyncio.create_task(
            self._run_task(task_id, task_func, *args, **kwargs)
        )
        
        self.tasks[task_id] = {
            'task': task,
            'status': 'running',
            'created_at': timezone.now(),
            'progress': 0
        }
        
        return task_id
    
    async def _run_task(self, task_id, task_func, *args, **kwargs):
        """运行任务并跟踪进度"""
        try:
            # 通知任务开始
            await self._broadcast_task_status(task_id, 'started')
            
            # 执行任务
            result = await task_func(*args, **kwargs)
            
            # 更新任务状态
            self.tasks[task_id]['status'] = 'completed'
            self.tasks[task_id]['result'] = result
            
            # 通知任务完成
            await self._broadcast_task_status(task_id, 'completed', result)
            
        except Exception as e:
            # 更新任务状态
            self.tasks[task_id]['status'] = 'failed'
            self.tasks[task_id]['error'] = str(e)
            
            # 通知任务失败
            await self._broadcast_task_status(task_id, 'failed', str(e))
            
            raise
    
    async def _broadcast_task_status(self, task_id, status, data=None):
        """广播任务状态"""
        await self.channel_layer.group_send(
            'task_monitor',
            {
                'type': 'task_status_update',
                'task_id': task_id,
                'status': status,
                'data': data,
                'timestamp': timezone.now().isoformat()
            }
        )
    
    def get_task_status(self, task_id):
        """获取任务状态"""
        if task_id in self.tasks:
            task_info = self.tasks[task_id]
            return {
                'id': task_id,
                'status': task_info['status'],
                'progress': task_info.get('progress', 0),
                'created_at': task_info['created_at'].isoformat(),
                'result': task_info.get('result'),
                'error': task_info.get('error')
            }
        return None
    
    async def cancel_task(self, task_id):
        """取消任务"""
        if task_id in self.tasks and self.tasks[task_id]['status'] == 'running':
            self.tasks[task_id]['task'].cancel()
            self.tasks[task_id]['status'] = 'cancelled'
            
            # 通知任务取消
            await self._broadcast_task_status(task_id, 'cancelled')
            
            return True
        return False
```

### 🎯 实战项目：企业级实时协作平台

```python
"""
企业级实时协作平台
比喻：现代化企业的数字化协作中心
"""

# 📱 前端WebSocket连接管理
# static/js/websocket-manager.js
WEBSOCKET_MANAGER = """
class WebSocketManager {
    constructor(url) {
        this.url = url;
        this.socket = null;
        this.reconnectAttempts = 0;
        this.maxReconnectAttempts = 5;
        this.reconnectDelay = 1000;
        this.messageHandlers = {};
        this.isConnected = false;
    }
    
    connect() {
        this.socket = new WebSocket(this.url);
        
        this.socket.onopen = (event) => {
            console.log('WebSocket连接已建立');
            this.isConnected = true;
            this.reconnectAttempts = 0;
            this.onConnect(event);
        };
        
        this.socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            this.handleMessage(data);
        };
        
        this.socket.onclose = (event) => {
            console.log('WebSocket连接已关闭');
            this.isConnected = false;
            this.onDisconnect(event);
            this.attemptReconnect();
        };
        
        this.socket.onerror = (error) => {
            console.error('WebSocket错误:', error);
            this.onError(error);
        };
    }
    
    attemptReconnect() {
        if (this.reconnectAttempts < this.maxReconnectAttempts) {
            this.reconnectAttempts++;
            console.log(`尝试重连... (${this.reconnectAttempts}/${this.maxReconnectAttempts})`);
            
            setTimeout(() => {
                this.connect();
            }, this.reconnectDelay * this.reconnectAttempts);
        } else {
            console.error('无法建立WebSocket连接');
            this.onReconnectFailed();
        }
    }
    
    send(data) {
        if (this.isConnected && this.socket.readyState === WebSocket.OPEN) {
            this.socket.send(JSON.stringify(data));
        } else {
            console.error('WebSocket未连接');
        }
    }
    
    on(messageType, handler) {
        if (!this.messageHandlers[messageType]) {
            this.messageHandlers[messageType] = [];
        }
        this.messageHandlers[messageType].push(handler);
    }
    
    handleMessage(data) {
        const messageType = data.type;
        if (this.messageHandlers[messageType]) {
            this.messageHandlers[messageType].forEach(handler => {
                handler(data);
            });
        }
    }
    
    // 事件钩子
    onConnect(event) {}
    onDisconnect(event) {}
    onError(error) {}
    onReconnectFailed() {}
    
    close() {
        if (this.socket) {
            this.socket.close();
        }
    }
}

// 聊天室管理器
class ChatManager extends WebSocketManager {
    constructor(roomName) {
        super(`ws://localhost:8000/ws/chat/${roomName}/`);
        this.roomName = roomName;
        this.typingTimer = null;
    }
    
    sendMessage(message) {
        this.send({
            type: 'chat_message',
            message: message
        });
    }
    
    sendTypingIndicator(isTyping) {
        this.send({
            type: 'typing',
            is_typing: isTyping
        });
    }
    
    sendReadReceipt(messageId) {
        this.send({
            type: 'read_receipt',
            message_id: messageId
        });
    }
    
    onConnect(event) {
        console.log(`已加入聊天室: ${this.roomName}`);
        // 更新UI状态
        document.getElementById('connection-status').textContent = '已连接';
    }
    
    onDisconnect(event) {
        document.getElementById('connection-status').textContent = '连接断开';
    }
}

// 使用示例
const chatManager = new ChatManager('general');
chatManager.connect();

// 注册消息处理器
chatManager.on('chat_message', (data) => {
    displayMessage(data.message);
});

chatManager.on('typing_indicator', (data) => {
    updateTypingIndicator(data.user, data.is_typing);
});

chatManager.on('user_join', (data) => {
    displaySystemMessage(`${data.user.full_name} 加入了聊天室`);
});
"""

# 🌐 综合实时协作平台
class EnterpriseCollaborationPlatform:
    """
    🌐 企业协作平台
    比喻：企业的数字化协作总部
    """
    
    def __init__(self):
        self.channel_layer = get_channel_layer()
        self.task_manager = AsyncTaskManager()
    
    async def broadcast_announcement(self, announcement):
        """
        广播企业公告
        比喻：企业广播系统发布重要通知
        """
        # 发送到全局通知组
        await self.channel_layer.group_send(
            'notifications_global',
            {
                'type': 'send_notification',
                'notification': {
                    'id': str(uuid.uuid4()),
                    'title': announcement['title'],
                    'message': announcement['message'],
                    'category': 'announcement',
                    'priority': 'high',
                    'created_at': timezone.now().isoformat(),
                    'sender': 'System'
                }
            }
        )
        
        # 保存到数据库
        await self._save_announcement(announcement)
    
    async def notify_department(self, department_id, notification):
        """
        部门级通知
        比喻：部门内部通知系统
        """
        await self.channel_layer.group_send(
            f'notifications_dept_{department_id}',
            {
                'type': 'send_notification',
                'notification': notification
            }
        )
    
    async def create_collaboration_room(self, project_id, participants):
        """
        创建协作房间
        比喻：开设新的项目协作会议室
        """
        room_id = f'collab_{project_id}'
        
        # 通知所有参与者
        for participant_id in participants:
            await self.channel_layer.group_send(
                f'notifications_user_{participant_id}',
                {
                    'type': 'send_notification',
                    'notification': {
                        'title': '新的协作邀请',
                        'message': f'您被邀请加入项目协作',
                        'action_url': f'/collaboration/{project_id}/'
                    }
                }
            )
        
        return room_id
    
    @database_sync_to_async
    def _save_announcement(self, announcement):
        """保存公告到数据库"""
        from .models import Announcement
        Announcement.objects.create(
            title=announcement['title'],
            message=announcement['message'],
            created_by_id=announcement.get('created_by_id')
        )
```

### 📚 本节小结

通过本节学习，我们深入掌握了Django Channels和异步编程的企业级应用：

#### 🎯 核心要点
1. **Django Channels架构**：理解WebSocket和异步通信原理
2. **实时聊天系统**：实现完整的即时通讯功能
3. **协作编辑系统**：支持多人实时协作和操作变换
4. **异步任务处理**：集成Celery和实时进度推送

#### ⚡ 实时通信特性
- **WebSocket连接管理**：自动重连和错误处理
- **消息路由系统**：灵活的消息分发机制
- **群组通信**：支持一对一和群组消息
- **实时状态同步**：光标、选区、内容同步

#### 💡 最佳实践
- 使用消费者模式处理WebSocket连接
- 实现操作变换算法支持协作编辑
- 采用Redis作为Channel Layer提升性能
- 集成Celery处理长时间运行的任务

## 39.4 🛡️ 安全管理部 - 企业级安全与监控

### 🏢 部门概述

在我们的企业级Web应用总部大厦中，**安全管理部**就像是大厦的保安系统和监控中心。这个部门负责保护整个企业的数字资产，确保所有访问都是合法和安全的，同时实时监控各种安全威胁和异常行为。

安全管理部采用**多层防护**策略，就像银行的多重安全门禁系统一样，从用户身份验证、权限控制、数据加密，到威胁检测和事件响应，构建了一个全方位的安全防护网。

```mermaid
graph TB
    A["🛡️ 企业安全管理部<br/>(Django Security Center)"] --> B["🔐 身份认证中心<br/>(Authentication Center)"]
    A --> C["👥 权限控制系统<br/>(Authorization System)"]
    A --> D["🔒 数据保护部<br/>(Data Protection)"]
    A --> E["🚨 威胁检测站<br/>(Threat Detection)"]
    A --> F["📊 安全监控室<br/>(Security Monitoring)"]
    
    B --> B1["🎫 多因素认证<br/>(MFA)"]
    B --> B2["🔑 单点登录<br/>(SSO)"]
    B --> B3["👤 用户管理<br/>(User Management)"]
    
    C --> C1["🏷️ 基于角色权限<br/>(RBAC)"]
    C --> C2["🎯 资源访问控制<br/>(Resource ACL)"]
    C --> C3["🔄 动态权限<br/>(Dynamic Permissions)"]
    
    D --> D1["🔐 数据加密<br/>(Encryption)"]
    D --> D2["🗝️ 密钥管理<br/>(Key Management)"]
    D --> D3["📋 数据脱敏<br/>(Data Masking)"]
    
    E --> E1["🎯 攻击检测<br/>(Attack Detection)"]
    E --> E2["🚫 异常行为<br/>(Anomaly Detection)"]
    E --> E3["⚡ 自动响应<br/>(Auto Response)"]
    
    F --> F1["📈 安全仪表板<br/>(Security Dashboard)"]
    F --> F2["📝 审计日志<br/>(Audit Logs)"]
    F --> F3["📊 风险评估<br/>(Risk Assessment)"]
```

### 🔐 身份认证中心 - 多层身份验证系统

身份认证中心就像是大厦的**智能门禁系统**，不仅要验证来访者的身份证，还要通过指纹、人脸识别等多种方式确保访问者的真实身份。

#### 📋 多因素认证系统实现

```python
# apps/security/authentication.py
"""
企业级多因素认证系统
Multi-Factor Authentication System
"""

import pyotp
import qrcode
import io
import base64
import logging
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.models import User
from django.core.cache import cache
from django.utils import timezone
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from cryptography.fernet import Fernet

logger = logging.getLogger(__name__)

class MultiFactorAuthManager:
    """
    多因素认证管理器
    就像银行的多重验证系统，确保用户身份的绝对可靠性
    """
    
    def __init__(self):
        self.cipher_suite = Fernet(settings.MFA_SECRET_KEY.encode()[:44])
        self.sms_provider = SMSProvider()
        self.email_provider = EmailProvider()
    
    def generate_totp_secret(self, user):
        """
        生成TOTP密钥
        就像给每个员工配发专属的安全令牌
        """
        try:
            secret = pyotp.random_base32()
            
            # 加密存储密钥
            encrypted_secret = self.cipher_suite.encrypt(secret.encode())
            
            # 存储到用户配置中
            user_profile, created = UserSecurityProfile.objects.get_or_create(
                user=user,
                defaults={'totp_secret': encrypted_secret}
            )
            
            if not created:
                user_profile.totp_secret = encrypted_secret
                user_profile.save()
            
            logger.info(f"TOTP secret generated for user: {user.username}")
            return secret
            
        except Exception as e:
            logger.error(f"Failed to generate TOTP secret: {str(e)}")
            raise SecurityException("TOTP密钥生成失败")
    
    def generate_qr_code(self, user, secret):
        """
        生成二维码供用户扫描
        就像制作员工门禁卡的二维码
        """
        try:
            totp_uri = pyotp.totp.TOTP(secret).provisioning_uri(
                name=user.email,
                issuer_name=settings.COMPANY_NAME
            )
            
            # 生成二维码
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(totp_uri)
            qr.make(fit=True)
            
            # 转换为base64图片
            img = qr.make_image(fill_color="black", back_color="white")
            buffer = io.BytesIO()
            img.save(buffer, format='PNG')
            img_base64 = base64.b64encode(buffer.getvalue()).decode()
            
            return f"data:image/png;base64,{img_base64}"
            
        except Exception as e:
            logger.error(f"Failed to generate QR code: {str(e)}")
            raise SecurityException("二维码生成失败")
    
    def verify_totp(self, user, token):
        """
        验证TOTP令牌
        就像验证员工的安全令牌是否正确
        """
        try:
            profile = UserSecurityProfile.objects.get(user=user)
            
            # 解密密钥
            secret = self.cipher_suite.decrypt(profile.totp_secret).decode()
            totp = pyotp.TOTP(secret)
            
            # 验证令牌（允许时间窗口误差）
            is_valid = totp.verify(token, valid_window=1)
            
            if is_valid:
                # 更新最后使用时间
                profile.last_totp_used = timezone.now()
                profile.save()
                
                logger.info(f"TOTP verification successful for user: {user.username}")
            else:
                logger.warning(f"TOTP verification failed for user: {user.username}")
            
            return is_valid
            
        except UserSecurityProfile.DoesNotExist:
            logger.error(f"Security profile not found for user: {user.username}")
            return False
        except Exception as e:
            logger.error(f"TOTP verification error: {str(e)}")
            return False
    
    def send_sms_code(self, user, phone_number):
        """
        发送短信验证码
        就像给访客发送临时通行证
        """
        try:
            code = self._generate_verification_code()
            
            # 存储验证码（5分钟有效期）
            cache_key = f"sms_code_{user.id}"
            cache.set(cache_key, code, timeout=300)
            
            # 发送短信
            message = f"您的验证码是: {code}，5分钟内有效。"
            success = self.sms_provider.send_message(phone_number, message)
            
            if success:
                logger.info(f"SMS code sent to user: {user.username}")
                return True
            else:
                logger.error(f"Failed to send SMS to user: {user.username}")
                return False
                
        except Exception as e:
            logger.error(f"SMS sending error: {str(e)}")
            return False
    
    def verify_sms_code(self, user, code):
        """
        验证短信验证码
        """
        try:
            cache_key = f"sms_code_{user.id}"
            stored_code = cache.get(cache_key)
            
            if stored_code and stored_code == code:
                # 删除已使用的验证码
                cache.delete(cache_key)
                logger.info(f"SMS code verification successful for user: {user.username}")
                return True
            else:
                logger.warning(f"SMS code verification failed for user: {user.username}")
                return False
                
        except Exception as e:
            logger.error(f"SMS code verification error: {str(e)}")
            return False
    
    def _generate_verification_code(self, length=6):
        """生成数字验证码"""
        import random
        return ''.join([str(random.randint(0, 9)) for _ in range(length)])

class AuthenticationService:
    """
    认证服务核心类
    就像大厦的智能安保控制中心
    """
    
    def __init__(self):
        self.mfa_manager = MultiFactorAuthManager()
        self.session_manager = SessionManager()
        self.risk_assessor = RiskAssessor()
    
    def authenticate_user(self, request, username, password):
        """
        用户认证主流程
        就像访客进入大厦的完整安检流程
        """
        try:
            # 第一步：基础用户名密码验证
            user = authenticate(request, username=username, password=password)
            if not user:
                logger.warning(f"Authentication failed for username: {username}")
                return {
                    'success': False,
                    'error': 'invalid_credentials',
                    'message': '用户名或密码错误'
                }
            
            # 第二步：风险评估
            risk_level = self.risk_assessor.assess_login_risk(request, user)
            
            if risk_level == 'HIGH':
                # 高风险登录需要额外验证
                return self._handle_high_risk_login(request, user)
            elif risk_level == 'MEDIUM':
                # 中等风险需要MFA验证
                return self._initiate_mfa_challenge(user)
            else:
                # 低风险直接登录
                return self._complete_login(request, user)
                
        except Exception as e:
            logger.error(f"Authentication error: {str(e)}")
            return {
                'success': False,
                'error': 'system_error',
                'message': '系统错误，请稍后重试'
            }
    
    def _initiate_mfa_challenge(self, user):
        """
        发起MFA挑战
        就像触发额外的安全验证程序
        """
        try:
            profile = UserSecurityProfile.objects.get(user=user)
            available_methods = []
            
            # 检查可用的MFA方法
            if profile.totp_enabled:
                available_methods.append('totp')
            if profile.sms_enabled:
                available_methods.append('sms')
            if profile.email_enabled:
                available_methods.append('email')
            
            if not available_methods:
                # 如果没有配置MFA，要求用户设置
                return {
                    'success': False,
                    'requires': 'mfa_setup',
                    'message': '请先设置多因素认证'
                }
            
            # 生成MFA会话令牌
            mfa_token = self.session_manager.create_mfa_session(user)
            
            return {
                'success': False,
                'requires': 'mfa_verification',
                'mfa_token': mfa_token,
                'available_methods': available_methods,
                'message': '请完成多因素认证'
            }
            
        except UserSecurityProfile.DoesNotExist:
            return {
                'success': False,
                'requires': 'mfa_setup',
                'message': '请先设置多因素认证'
            }
    
    def verify_mfa_and_login(self, request, mfa_token, method, code):
        """
        验证MFA并完成登录
        """
        try:
            # 验证MFA会话令牌
            user = self.session_manager.get_user_from_mfa_token(mfa_token)
            if not user:
                return {
                    'success': False,
                    'error': 'invalid_token',
                    'message': 'MFA令牌无效或已过期'
                }
            
            # 根据方法验证代码
            verification_success = False
            if method == 'totp':
                verification_success = self.mfa_manager.verify_totp(user, code)
            elif method == 'sms':
                verification_success = self.mfa_manager.verify_sms_code(user, code)
            elif method == 'email':
                verification_success = self.mfa_manager.verify_email_code(user, code)
            
            if verification_success:
                # 清理MFA会话
                self.session_manager.clear_mfa_session(mfa_token)
                
                # 完成登录
                return self._complete_login(request, user)
            else:
                return {
                    'success': False,
                    'error': 'invalid_code',
                    'message': '验证码错误'
                }
                
        except Exception as e:
            logger.error(f"MFA verification error: {str(e)}")
            return {
                'success': False,
                'error': 'system_error',
                'message': '验证失败，请重试'
            }
    
    def _complete_login(self, request, user):
        """
        完成登录流程
        就像访客通过所有安检后，获得正式的访问权限
        """
        try:
            # Django登录
            django_login(request, user)
            
            # 生成API Token
            token, created = Token.objects.get_or_create(user=user)
            
            # 记录登录日志
            LoginLog.objects.create(
                user=user,
                ip_address=self._get_client_ip(request),
                user_agent=request.META.get('HTTP_USER_AGENT', ''),
                login_time=timezone.now(),
                login_method='web',
                success=True
            )
            
            # 更新用户最后登录时间
            user.last_login = timezone.now()
            user.save()
            
            logger.info(f"User login successful: {user.username}")
            
            return {
                'success': True,
                'token': token.key,
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'is_staff': user.is_staff
                },
                'message': '登录成功'
            }
            
        except Exception as e:
            logger.error(f"Login completion error: {str(e)}")
            return {
                'success': False,
                'error': 'system_error',
                'message': '登录失败，请重试'
            }
    
    def _get_client_ip(self, request):
        """获取客户端IP地址"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

# 用户安全配置模型
from django.db import models

class UserSecurityProfile(models.Model):
    """
    用户安全配置
    就像员工的个人安全档案
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # TOTP设置
    totp_secret = models.BinaryField(null=True, blank=True)
    totp_enabled = models.BooleanField(default=False)
    last_totp_used = models.DateTimeField(null=True, blank=True)
    
    # SMS设置
    phone_number = models.CharField(max_length=20, blank=True)
    sms_enabled = models.BooleanField(default=False)
    
    # Email设置
    email_enabled = models.BooleanField(default=False)
    
    # 安全设置
    require_mfa = models.BooleanField(default=True)
    trusted_devices = models.JSONField(default=list)
    
    # 时间戳
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'user_security_profiles'
        verbose_name = '用户安全配置'
        verbose_name_plural = '用户安全配置'

class LoginLog(models.Model):
    """
    登录日志记录
    就像大厦的访客登记册
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    login_time = models.DateTimeField()
    login_method = models.CharField(max_length=20)
    success = models.BooleanField()
    failure_reason = models.CharField(max_length=100, blank=True)
    risk_level = models.CharField(max_length=10, default='LOW')
    
    class Meta:
        db_table = 'login_logs'
        ordering = ['-login_time']
```

### 👥 权限控制系统 - 基于角色的访问控制

权限控制系统就像是大厦的**智能权限管理系统**，不同级别的员工可以访问不同的楼层和房间，确保每个人只能访问与其职责相关的资源。

#### 🏷️ RBAC权限管理实现

```python
# apps/security/permissions.py
"""
基于角色的访问控制系统 (RBAC)
Role-Based Access Control System
"""

from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from rest_framework.permissions import BasePermission
import logging

logger = logging.getLogger(__name__)

class Role(models.Model):
    """
    角色模型
    就像公司的不同职位：经理、主管、员工等
    """
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    level = models.IntegerField(default=1)  # 角色级别，数字越大权限越高
    is_active = models.BooleanField(default=True)
    
    # 权限配置
    permissions = models.ManyToManyField(Permission, blank=True)
    
    # 时间戳
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'rbac_roles'
        verbose_name = '角色'
        verbose_name_plural = '角色'
        ordering = ['-level', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.code})"

class UserRole(models.Model):
    """
    用户角色关联
    就像员工的岗位分配记录
    """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    department = models.CharField(max_length=50, blank=True)
    
    # 时间限制
    valid_from = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField(null=True, blank=True)
    
    # 分配信息
    assigned_by = models.ForeignKey(
        'auth.User', 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='assigned_roles'
    )
    assigned_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'rbac_user_roles'
        unique_together = ['user', 'role']
        verbose_name = '用户角色'
        verbose_name_plural = '用户角色'

class Resource(models.Model):
    """
    资源模型
    就像大厦中的不同房间和设施
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
    resource_type = models.CharField(max_length=20)  # api, page, data, file等
    path = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    # 层级结构
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    
    # 安全级别
    security_level = models.CharField(
        max_length=20, 
        choices=[
            ('public', '公开'),
            ('internal', '内部'),
            ('confidential', '机密'),
            ('top_secret', '绝密')
        ],
        default='internal'
    )
    
    class Meta:
        db_table = 'rbac_resources'
        verbose_name = '资源'
        verbose_name_plural = '资源'

class Permission(models.Model):
    """
    权限模型
    就像员工的各种通行证和操作许可
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    action = models.CharField(
        max_length=20,
        choices=[
            ('read', '读取'),
            ('write', '写入'),
            ('delete', '删除'),
            ('execute', '执行'),
            ('manage', '管理')
        ]
    )
    description = models.TextField(blank=True)
    
    class Meta:
        db_table = 'rbac_permissions'
        unique_together = ['resource', 'action']
        verbose_name = '权限'
        verbose_name_plural = '权限'

class RBACManager:
    """
    RBAC权限管理器
    就像大厦的智能权限管理中心
    """
    
    @classmethod
    def assign_role_to_user(cls, user, role, assigned_by=None, valid_until=None):
        """
        为用户分配角色
        就像给员工分配新的职位
        """
        try:
            user_role, created = UserRole.objects.get_or_create(
                user=user,
                role=role,
                defaults={
                    'assigned_by': assigned_by,
                    'valid_until': valid_until
                }
            )
            
            if created:
                logger.info(f"Role {role.name} assigned to user {user.username}")
            else:
                logger.info(f"Role {role.name} already assigned to user {user.username}")
            
            return user_role
            
        except Exception as e:
            logger.error(f"Failed to assign role: {str(e)}")
            raise
    
    @classmethod
    def remove_role_from_user(cls, user, role):
        """移除用户角色"""
        try:
            UserRole.objects.filter(user=user, role=role).delete()
            logger.info(f"Role {role.name} removed from user {user.username}")
        except Exception as e:
            logger.error(f"Failed to remove role: {str(e)}")
            raise
    
    @classmethod
    def get_user_roles(cls, user):
        """
        获取用户的有效角色
        就像查看员工当前的职位
        """
        now = timezone.now()
        return Role.objects.filter(
            userrole__user=user,
            userrole__valid_from__lte=now,
            userrole__valid_until__isnull=True or models.Q(userrole__valid_until__gt=now),
            is_active=True
        )
    
    @classmethod
    def get_user_permissions(cls, user):
        """
        获取用户的所有权限
        就像列出员工的所有通行证
        """
        roles = cls.get_user_roles(user)
        permissions = Permission.objects.filter(role__in=roles).distinct()
        return permissions
    
    @classmethod
    def check_permission(cls, user, resource_code, action):
        """
        检查用户权限
        就像验证员工是否有权限进入某个房间
        """
        try:
            # 超级用户拥有所有权限
            if user.is_superuser:
                return True
            
            # 获取用户角色
            roles = cls.get_user_roles(user)
            if not roles.exists():
                return False
            
            # 检查权限
            has_permission = Permission.objects.filter(
                role__in=roles,
                resource__code=resource_code,
                action=action
            ).exists()
            
            # 记录权限检查日志
            PermissionLog.objects.create(
                user=user,
                resource_code=resource_code,
                action=action,
                granted=has_permission,
                check_time=timezone.now()
            )
            
            return has_permission
            
        except Exception as e:
            logger.error(f"Permission check error: {str(e)}")
            return False
    
    @classmethod
    def create_default_roles(cls):
        """
        创建默认角色
        就像设置公司的基本职位架构
        """
        default_roles = [
            {
                'name': '系统管理员',
                'code': 'admin',
                'description': '拥有系统最高权限',
                'level': 100
            },
            {
                'name': '部门经理',
                'code': 'manager',
                'description': '部门管理权限',
                'level': 80
            },
            {
                'name': '项目主管',
                'code': 'supervisor',
                'description': '项目管理权限',
                'level': 60
            },
            {
                'name': '高级员工',
                'code': 'senior_staff',
                'description': '高级业务权限',
                'level': 40
            },
            {
                'name': '普通员工',
                'code': 'staff',
                'description': '基础业务权限',
                'level': 20
            },
            {
                'name': '访客',
                'code': 'guest',
                'description': '只读权限',
                'level': 10
            }
        ]
        
        for role_data in default_roles:
            role, created = Role.objects.get_or_create(
                code=role_data['code'],
                defaults=role_data
            )
            if created:
                logger.info(f"Default role created: {role.name}")

class RBACPermission(BasePermission):
    """
    DRF权限检查类
    就像API接口的智能门禁
    """
    
    def __init__(self, resource_code, action):
        self.resource_code = resource_code
        self.action = action
    
    def has_permission(self, request, view):
        """检查权限"""
        if not request.user or not request.user.is_authenticated:
            return False
        
        return RBACManager.check_permission(
            request.user, 
            self.resource_code, 
            self.action
        )

class PermissionLog(models.Model):
    """
    权限检查日志
    就像门禁系统的刷卡记录
    """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    resource_code = models.CharField(max_length=50)
    action = models.CharField(max_length=20)
    granted = models.BooleanField()
    check_time = models.DateTimeField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    
    class Meta:
        db_table = 'rbac_permission_logs'
        ordering = ['-check_time']

# 权限装饰器
from functools import wraps
from django.http import JsonResponse

def require_permission(resource_code, action):
    """
    权限检查装饰器
    就像给函数加上智能门禁
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return JsonResponse({
                    'error': 'authentication_required',
                    'message': '请先登录'
                }, status=401)
            
            if not RBACManager.check_permission(request.user, resource_code, action):
                return JsonResponse({
                    'error': 'permission_denied',
                    'message': '权限不足'
                }, status=403)
            
            return view_func(request, *args, **kwargs)
        return wrapped_view
    return decorator

# 权限检查中间件
class RBACMiddleware:
    """
    RBAC权限中间件
    就像大厦入口的智能安检系统
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # 处理请求前的权限检查
        if self._should_check_permission(request):
            if not self._check_request_permission(request):
                return JsonResponse({
                    'error': 'permission_denied',
                    'message': '访问被拒绝'
                }, status=403)
        
        response = self.get_response(request)
        return response
    
    def _should_check_permission(self, request):
        """判断是否需要权限检查"""
        # 排除静态文件和管理接口
        excluded_paths = ['/static/', '/media/', '/admin/']
        return not any(request.path.startswith(path) for path in excluded_paths)
    
    def _check_request_permission(self, request):
        """检查请求权限"""
        if not request.user.is_authenticated:
            return False
        
        # 根据URL路径确定资源和操作
        resource_code = self._extract_resource_from_path(request.path)
        action = self._extract_action_from_method(request.method)
        
        if resource_code and action:
            return RBACManager.check_permission(request.user, resource_code, action)
        
        return True  # 未定义的资源默认允许
    
    def _extract_resource_from_path(self, path):
        """从路径提取资源代码"""
        # 实现路径到资源的映射逻辑
        path_mappings = {
            '/api/users/': 'user_management',
            '/api/projects/': 'project_management',
            '/api/files/': 'file_management',
            '/api/reports/': 'report_access'
        }
        
        for pattern, resource in path_mappings.items():
            if path.startswith(pattern):
                return resource
        
        return None
    
    def _extract_action_from_method(self, method):
        """从HTTP方法提取操作类型"""
        method_mappings = {
            'GET': 'read',
            'POST': 'write',
            'PUT': 'write',
            'PATCH': 'write',
            'DELETE': 'delete'
        }
        return method_mappings.get(method, 'read')
```

### 🚨 威胁检测系统 - 智能安全监控

威胁检测系统就像是大厦的**智能监控系统**，通过摄像头、传感器等设备实时监控各种异常行为，一旦发现可疑活动就立即报警并采取相应的安全措施。

#### 🎯 实时威胁检测实现

```python
# apps/security/threat_detection.py
"""
智能威胁检测系统
Intelligent Threat Detection System
"""

import re
import hashlib
import time
from datetime import datetime, timedelta
from django.core.cache import cache
from django.conf import settings
from django.utils import timezone
from collections import defaultdict, deque
import logging

logger = logging.getLogger(__name__)

class ThreatDetectionEngine:
    """
    威胁检测引擎
    就像大厦的智能安防大脑，分析各种异常模式
    """
    
    def __init__(self):
        self.attack_patterns = self._load_attack_patterns()
        self.rate_limiters = defaultdict(lambda: deque())
        self.anomaly_detector = AnomalyDetector()
        self.response_system = AutoResponseSystem()
    
    def analyze_request(self, request):
        """
        分析请求威胁
        就像安检设备扫描每个进入大厦的人
        """
        threat_score = 0
        detected_threats = []
        
        try:
            # 1. SQL注入检测
            sql_injection_score = self._detect_sql_injection(request)
            if sql_injection_score > 0:
                threat_score += sql_injection_score
                detected_threats.append({
                    'type': 'sql_injection',
                    'score': sql_injection_score,
                    'description': 'SQL注入攻击尝试'
                })
            
            # 2. XSS攻击检测
            xss_score = self._detect_xss_attacks(request)
            if xss_score > 0:
                threat_score += xss_score
                detected_threats.append({
                    'type': 'xss_attack',
                    'score': xss_score,
                    'description': 'XSS攻击尝试'
                })
            
            # 3. 恶意文件上传检测
            file_upload_score = self._detect_malicious_upload(request)
            if file_upload_score > 0:
                threat_score += file_upload_score
                detected_threats.append({
                    'type': 'malicious_upload',
                    'score': file_upload_score,
                    'description': '恶意文件上传尝试'
                })
            
            # 4. 频率限制检测
            rate_limit_score = self._detect_rate_limit_violation(request)
            if rate_limit_score > 0:
                threat_score += rate_limit_score
                detected_threats.append({
                    'type': 'rate_limit_violation',
                    'score': rate_limit_score,
                    'description': '请求频率异常'
                })
            
            # 5. 异常行为检测
            anomaly_score = self.anomaly_detector.detect_anomalies(request)
            if anomaly_score > 0:
                threat_score += anomaly_score
                detected_threats.append({
                    'type': 'anomalous_behavior',
                    'score': anomaly_score,
                    'description': '异常行为模式'
                })
            
            # 记录威胁检测结果
            if detected_threats:
                self._log_threat_detection(request, threat_score, detected_threats)
                
                # 触发自动响应
                if threat_score >= settings.THREAT_RESPONSE_THRESHOLD:
                    self.response_system.handle_threat(request, threat_score, detected_threats)
            
            return {
                'threat_score': threat_score,
                'detected_threats': detected_threats,
                'is_malicious': threat_score >= settings.THREAT_BLOCK_THRESHOLD
            }
            
        except Exception as e:
            logger.error(f"Threat detection error: {str(e)}")
            return {
                'threat_score': 0,
                'detected_threats': [],
                'is_malicious': False
            }
    
    def _detect_sql_injection(self, request):
        """
        SQL注入检测
        就像检测是否有人试图用假钥匙开锁
        """
        sql_patterns = [
            r"(\b(SELECT|INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|EXEC|UNION)\b)",
            r"(\b(OR|AND)\s+\d+\s*=\s*\d+)",
            r"(--|#|/\*|\*/)",
            r"(\b(CHAR|VARCHAR|NCHAR|NVARCHAR|BINARY|VARBINARY)\s*\()",
            r"(\b(WAITFOR|DELAY)\s+)"
        ]
        
        score = 0
        content_to_check = []
        
        # 检查GET参数
        for value in request.GET.values():
            content_to_check.append(value)
        
        # 检查POST数据
        if hasattr(request, 'body') and request.body:
            try:
                content_to_check.append(request.body.decode('utf-8'))
            except:
                pass
        
        # 检查headers中的可疑内容
        for header_value in request.META.values():
            if isinstance(header_value, str):
                content_to_check.append(header_value)
        
        for content in content_to_check:
            for pattern in sql_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    score += 30
                    logger.warning(f"SQL injection pattern detected: {pattern}")
        
        return min(score, 100)
    
    def _detect_xss_attacks(self, request):
        """
        XSS攻击检测
        就像检测是否有人携带危险物品
        """
        xss_patterns = [
            r"<script[^>]*>.*?</script>",
            r"javascript:",
            r"on\w+\s*=",
            r"<iframe[^>]*>",
            r"<object[^>]*>",
            r"<embed[^>]*>",
            r"<link[^>]*>",
            r"<meta[^>]*>",
            r"expression\s*\(",
            r"@import",
            r"<\s*\?\s*php"
        ]
        
        score = 0
        content_to_check = []
        
        # 收集需要检查的内容
        for value in request.GET.values():
            content_to_check.append(value)
        
        if hasattr(request, 'body') and request.body:
            try:
                content_to_check.append(request.body.decode('utf-8'))
            except:
                pass
        
        for content in content_to_check:
            for pattern in xss_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    score += 25
                    logger.warning(f"XSS pattern detected: {pattern}")
        
        return min(score, 100)
    
    def _detect_malicious_upload(self, request):
        """
        恶意文件上传检测
        就像检查行李中是否有违禁品
        """
        if not hasattr(request, 'FILES') or not request.FILES:
            return 0
        
        score = 0
        dangerous_extensions = [
            '.php', '.asp', '.aspx', '.jsp', '.exe', '.bat', 
            '.cmd', '.com', '.scr', '.pif', '.vbs', '.js'
        ]
        
        for file_field in request.FILES.values():
            for uploaded_file in file_field if hasattr(file_field, '__iter__') else [file_field]:
                filename = uploaded_file.name.lower()
                
                # 检查文件扩展名
                for ext in dangerous_extensions:
                    if filename.endswith(ext):
                        score += 50
                        logger.warning(f"Dangerous file extension detected: {ext}")
                
                # 检查文件内容
                try:
                    content = uploaded_file.read(1024).decode('utf-8', errors='ignore')
                    uploaded_file.seek(0)  # 重置文件指针
                    
                    # 检查PHP代码
                    if re.search(r'<\?php|<\?=', content, re.IGNORECASE):
                        score += 40
                        logger.warning("PHP code detected in uploaded file")
                    
                    # 检查JavaScript代码
                    if re.search(r'<script|javascript:', content, re.IGNORECASE):
                        score += 30
                        logger.warning("JavaScript code detected in uploaded file")
                
                except:
                    pass
        
        return min(score, 100)
    
    def _detect_rate_limit_violation(self, request):
        """
        频率限制检测
        就像监控是否有人频繁尝试进入
        """
        client_ip = self._get_client_ip(request)
        current_time = time.time()
        
        # 清理过期记录
        cutoff_time = current_time - 60  # 1分钟窗口
        while self.rate_limiters[client_ip] and self.rate_limiters[client_ip][0] < cutoff_time:
            self.rate_limiters[client_ip].popleft()
        
        # 添加当前请求
        self.rate_limiters[client_ip].append(current_time)
        
        # 检查频率
        request_count = len(self.rate_limiters[client_ip])
        max_requests = settings.RATE_LIMIT_MAX_REQUESTS
        
        if request_count > max_requests:
            score = min(((request_count - max_requests) * 10), 100)
            logger.warning(f"Rate limit violation from IP {client_ip}: {request_count} requests")
            return score
        
        return 0
    
    def _get_client_ip(self, request):
        """获取客户端IP"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    def _load_attack_patterns(self):
        """加载攻击模式库"""
        return {
            'sql_injection': [
                r"(\b(SELECT|INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|EXEC|UNION)\b)",
                r"(\b(OR|AND)\s+\d+\s*=\s*\d+)",
                r"(--|#|/\*|\*/)"
            ],
            'xss': [
                r"<script[^>]*>.*?</script>",
                r"javascript:",
                r"on\w+\s*="
            ],
            'path_traversal': [
                r"\.\./",
                r"\.\.\\",
                r"%2e%2e%2f",
                r"%2e%2e%5c"
            ]
        }
    
    def _log_threat_detection(self, request, threat_score, detected_threats):
        """记录威胁检测日志"""
        ThreatLog.objects.create(
            ip_address=self._get_client_ip(request),
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
            request_path=request.path,
            threat_score=threat_score,
            detected_threats=detected_threats,
            timestamp=timezone.now()
        )

class AnomalyDetector:
    """
    异常行为检测器
    就像行为分析专家，识别异常的行为模式
    """
    
    def detect_anomalies(self, request):
        """检测异常行为"""
        score = 0
        
        # 1. 异常访问时间检测
        if self._is_unusual_access_time():
            score += 20
        
        # 2. 异常User-Agent检测
        if self._is_suspicious_user_agent(request):
            score += 15
        
        # 3. 异常访问模式检测
        if self._is_unusual_access_pattern(request):
            score += 25
        
        return score
    
    def _is_unusual_access_time(self):
        """检测异常访问时间"""
        current_hour = timezone.now().hour
        # 深夜时间（凌晨2-6点）视为异常
        return 2 <= current_hour <= 6
    
    def _is_suspicious_user_agent(self, request):
        """检测可疑User-Agent"""
        user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
        
        suspicious_patterns = [
            'bot', 'crawler', 'spider', 'scanner', 'python', 
            'curl', 'wget', 'perl', 'java', 'go-http-client'
        ]
        
        return any(pattern in user_agent for pattern in suspicious_patterns)
    
    def _is_unusual_access_pattern(self, request):
        """检测异常访问模式"""
        # 这里可以实现更复杂的模式识别算法
        # 比如检测访问频率、访问路径序列等
        return False

class AutoResponseSystem:
    """
    自动响应系统
    就像大厦的自动安全响应系统，发现威胁后自动采取防护措施
    """
    
    def handle_threat(self, request, threat_score, detected_threats):
        """处理威胁"""
        client_ip = self._get_client_ip(request)
        
        if threat_score >= 80:
            # 高威胁：立即封禁IP
            self._block_ip(client_ip, duration=3600)  # 封禁1小时
            self._send_alert('HIGH', f'高威胁检测，已封禁IP: {client_ip}')
            
        elif threat_score >= 50:
            # 中威胁：临时限制
            self._rate_limit_ip(client_ip, duration=600)  # 限制10分钟
            self._send_alert('MEDIUM', f'中威胁检测，已限制IP: {client_ip}')
            
        else:
            # 低威胁：记录并监控
            self._send_alert('LOW', f'低威胁检测，监控IP: {client_ip}')
    
    def _block_ip(self, ip, duration):
        """封禁IP地址"""
        cache.set(f'blocked_ip_{ip}', True, timeout=duration)
        logger.warning(f"IP {ip} has been blocked for {duration} seconds")
    
    def _rate_limit_ip(self, ip, duration):
        """限制IP访问频率"""
        cache.set(f'rate_limited_{ip}', True, timeout=duration)
        logger.warning(f"IP {ip} has been rate limited for {duration} seconds")
    
    def _send_alert(self, level, message):
        """发送安全警报"""
        # 这里可以集成邮件、短信、钉钉等通知方式
        logger.warning(f"Security Alert [{level}]: {message}")
    
    def _get_client_ip(self, request):
        """获取客户端IP"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

# 威胁日志模型
from django.db import models

class ThreatLog(models.Model):
    """
    威胁检测日志
    就像安保部门的事件记录簿
    """
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    request_path = models.CharField(max_length=500)
    threat_score = models.IntegerField()
    detected_threats = models.JSONField()
    timestamp = models.DateTimeField()
    
    # 处理状态
    handled = models.BooleanField(default=False)
    response_action = models.CharField(max_length=50, blank=True)
    
    class Meta:
        db_table = 'security_threat_logs'
        ordering = ['-timestamp']

# 威胁检测中间件
class ThreatDetectionMiddleware:
    """
    威胁检测中间件
    就像大厦入口的智能安检门
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        self.detector = ThreatDetectionEngine()
    
    def __call__(self, request):
        # 检查IP是否被封禁
        client_ip = self._get_client_ip(request)
        if cache.get(f'blocked_ip_{client_ip}'):
            return JsonResponse({
                'error': 'ip_blocked',
                'message': 'Your IP has been blocked due to security reasons'
            }, status=403)
        
        # 威胁检测
        detection_result = self.detector.analyze_request(request)
        
        # 如果检测到恶意请求，直接拒绝
        if detection_result['is_malicious']:
            return JsonResponse({
                'error': 'malicious_request',
                'message': 'Request blocked by security system'
            }, status=403)
        
        # 将检测结果添加到request中，供后续使用
        request.threat_detection = detection_result
        
        response = self.get_response(request)
        return response
    
    def _get_client_ip(self, request):
        """获取客户端IP"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
```

### 📊 安全监控仪表板 - 实时安全态势感知

安全监控仪表板就像是大厦的**智能监控中心**，通过大屏幕实时显示整个系统的安全状态，让安保人员能够快速发现和响应各种安全事件。

#### 📈 安全监控系统实现

```python
# apps/security/monitoring.py
"""
安全监控仪表板系统
Security Monitoring Dashboard System
"""

from django.db.models import Count, Q, Avg
from django.utils import timezone
from datetime import datetime, timedelta
from django.core.cache import cache
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import json
import logging

logger = logging.getLogger(__name__)

class SecurityMonitoringService:
    """
    安全监控服务
    就像大厦的智能监控控制台，实时监控所有安全指标
    """
    
    def __init__(self):
        self.cache_timeout = 300  # 5分钟缓存
    
    def get_security_overview(self):
        """
        获取安全概览数据
        就像查看总控制台的综合状态指示板
        """
        try:
            cache_key = 'security_overview'
            cached_data = cache.get(cache_key)
            
            if cached_data:
                return cached_data
            
            now = timezone.now()
            today = now.date()
            week_ago = now - timedelta(days=7)
            
            # 威胁统计
            threat_stats = self._get_threat_statistics(week_ago, now)
            
            # 认证统计
            auth_stats = self._get_authentication_statistics(week_ago, now)
            
            # 权限统计
            permission_stats = self._get_permission_statistics(week_ago, now)
            
            # 系统健康状态
            health_status = self._get_system_health_status()
            
            overview_data = {
                'timestamp': now.isoformat(),
                'threat_level': self._assess_current_threat_level(),
                'statistics': {
                    'threats': threat_stats,
                    'authentication': auth_stats,
                    'permissions': permission_stats,
                    'system_health': health_status
                },
                'alerts': self._get_active_alerts(),
                'trends': self._get_security_trends(week_ago, now)
            }
            
            # 缓存数据
            cache.set(cache_key, overview_data, timeout=self.cache_timeout)
            
            return overview_data
            
        except Exception as e:
            logger.error(f"Failed to get security overview: {str(e)}")
            return self._get_default_overview()
    
    def _get_threat_statistics(self, start_time, end_time):
        """获取威胁统计数据"""
        threats = ThreatLog.objects.filter(
            timestamp__range=[start_time, end_time]
        )
        
        total_threats = threats.count()
        high_threats = threats.filter(threat_score__gte=80).count()
        blocked_ips = threats.values('ip_address').distinct().count()
        
        # 威胁类型分布
        threat_types = threats.values('detected_threats').annotate(
            count=Count('id')
        )
        
        return {
            'total_detected': total_threats,
            'high_severity': high_threats,
            'blocked_ips': blocked_ips,
            'threat_types': self._process_threat_types(threat_types),
            'recent_trends': self._get_threat_trends(start_time, end_time)
        }
    
    def _get_authentication_statistics(self, start_time, end_time):
        """获取认证统计数据"""
        login_logs = LoginLog.objects.filter(
            login_time__range=[start_time, end_time]
        )
        
        total_attempts = login_logs.count()
        successful_logins = login_logs.filter(success=True).count()
        failed_logins = login_logs.filter(success=False).count()
        
        # 风险等级分布
        risk_distribution = login_logs.values('risk_level').annotate(
            count=Count('id')
        ).order_by('risk_level')
        
        return {
            'total_attempts': total_attempts,
            'successful_logins': successful_logins,
            'failed_logins': failed_logins,
            'success_rate': (successful_logins / total_attempts * 100) if total_attempts > 0 else 0,
            'risk_distribution': list(risk_distribution),
            'top_failure_reasons': self._get_top_failure_reasons(login_logs)
        }
    
    def _get_permission_statistics(self, start_time, end_time):
        """获取权限统计数据"""
        permission_logs = PermissionLog.objects.filter(
            check_time__range=[start_time, end_time]
        )
        
        total_checks = permission_logs.count()
        granted_permissions = permission_logs.filter(granted=True).count()
        denied_permissions = permission_logs.filter(granted=False).count()
        
        # 资源访问统计
        resource_access = permission_logs.values('resource_code').annotate(
            total=Count('id'),
            granted=Count('id', filter=Q(granted=True)),
            denied=Count('id', filter=Q(granted=False))
        ).order_by('-total')[:10]
        
        return {
            'total_checks': total_checks,
            'granted': granted_permissions,
            'denied': denied_permissions,
            'grant_rate': (granted_permissions / total_checks * 100) if total_checks > 0 else 0,
            'top_resources': list(resource_access),
            'access_patterns': self._analyze_access_patterns(permission_logs)
        }
    
    def _get_system_health_status(self):
        """获取系统健康状态"""
        return {
            'database_status': self._check_database_health(),
            'cache_status': self._check_cache_health(),
            'threat_detection_status': self._check_threat_detection_health(),
            'overall_status': 'healthy',  # 可以根据各项检查结果综合判断
            'last_check': timezone.now().isoformat()
        }
    
    def _assess_current_threat_level(self):
        """评估当前威胁等级"""
        # 获取过去1小时的威胁数据
        one_hour_ago = timezone.now() - timedelta(hours=1)
        recent_threats = ThreatLog.objects.filter(
            timestamp__gte=one_hour_ago,
            threat_score__gte=50
        ).count()
        
        if recent_threats >= 10:
            return 'HIGH'
        elif recent_threats >= 5:
            return 'MEDIUM'
        else:
            return 'LOW'
    
    def _get_active_alerts(self):
        """获取活跃警报"""
        # 这里可以查询警报系统获取当前活跃的安全警报
        return [
            {
                'id': 'alert_001',
                'type': 'threat_detection',
                'severity': 'medium',
                'message': '检测到多次登录失败尝试',
                'timestamp': (timezone.now() - timedelta(minutes=30)).isoformat(),
                'status': 'active'
            }
        ]
    
    def get_real_time_metrics(self):
        """
        获取实时安全指标
        就像监控中心的实时数据流
        """
        try:
            now = timezone.now()
            five_minutes_ago = now - timedelta(minutes=5)
            
            metrics = {
                'timestamp': now.isoformat(),
                'active_sessions': self._count_active_sessions(),
                'recent_threats': ThreatLog.objects.filter(
                    timestamp__gte=five_minutes_ago
                ).count(),
                'recent_logins': LoginLog.objects.filter(
                    login_time__gte=five_minutes_ago
                ).count(),
                'blocked_ips': self._count_blocked_ips(),
                'system_load': self._get_system_load_metrics(),
                'security_events': self._get_recent_security_events(five_minutes_ago)
            }
            
            return metrics
            
        except Exception as e:
            logger.error(f"Failed to get real-time metrics: {str(e)}")
            return {'error': 'Unable to fetch real-time metrics'}
    
    def generate_security_report(self, start_date, end_date):
        """
        生成安全报告
        就像制作大厦安全状况的详细报告
        """
        try:
            report_data = {
                'report_period': {
                    'start_date': start_date.isoformat(),
                    'end_date': end_date.isoformat(),
                    'duration_days': (end_date - start_date).days
                },
                'executive_summary': self._generate_executive_summary(start_date, end_date),
                'threat_analysis': self._generate_threat_analysis(start_date, end_date),
                'authentication_analysis': self._generate_auth_analysis(start_date, end_date),
                'access_control_analysis': self._generate_access_analysis(start_date, end_date),
                'recommendations': self._generate_security_recommendations(start_date, end_date),
                'generated_at': timezone.now().isoformat()
            }
            
            return report_data
            
        except Exception as e:
            logger.error(f"Failed to generate security report: {str(e)}")
            raise
    
    def _count_active_sessions(self):
        """统计活跃会话数"""
        # 这里可以查询Django会话表或Redis中的会话数据
        return 42  # 示例数据
    
    def _count_blocked_ips(self):
        """统计被封禁的IP数量"""
        blocked_count = 0
        try:
            # 扫描缓存中的blocked_ip_*键
            from django.core.cache import cache
            # 这是一个简化实现，实际中可能需要更复杂的逻辑
            return 5  # 示例数据
        except:
            return 0
    
    def _get_system_load_metrics(self):
        """获取系统负载指标"""
        import psutil
        try:
            return {
                'cpu_percent': psutil.cpu_percent(),
                'memory_percent': psutil.virtual_memory().percent,
                'disk_percent': psutil.disk_usage('/').percent
            }
        except:
            return {
                'cpu_percent': 0,
                'memory_percent': 0,
                'disk_percent': 0
            }

# Django视图函数
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def security_overview_api(request):
    """
    安全概览API接口
    """
    try:
        monitoring_service = SecurityMonitoringService()
        overview_data = monitoring_service.get_security_overview()
        return JsonResponse({
            'success': True,
            'data': overview_data
        })
    except Exception as e:
        logger.error(f"Security overview API error: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': 'Failed to fetch security overview'
        }, status=500)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def real_time_metrics_api(request):
    """
    实时指标API接口
    """
    try:
        monitoring_service = SecurityMonitoringService()
        metrics = monitoring_service.get_real_time_metrics()
        return JsonResponse({
            'success': True,
            'data': metrics
        })
    except Exception as e:
        logger.error(f"Real-time metrics API error: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': 'Failed to fetch real-time metrics'
        }, status=500)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate_report_api(request):
    """
    生成安全报告API接口
    """
    try:
        data = json.loads(request.body)
        start_date = datetime.fromisoformat(data['start_date'])
        end_date = datetime.fromisoformat(data['end_date'])
        
        monitoring_service = SecurityMonitoringService()
        report = monitoring_service.generate_security_report(start_date, end_date)
        
        return JsonResponse({
            'success': True,
            'data': report
        })
    except Exception as e:
        logger.error(f"Generate report API error: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': 'Failed to generate security report'
        }, status=500)

# 前端仪表板HTML模板示例
SECURITY_DASHBOARD_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>安全监控仪表板</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        .dashboard {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            padding: 20px;
        }
        .card {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            padding: 20px;
        }
        .metric {
            font-size: 2em;
            font-weight: bold;
            color: #333;
        }
        .status-indicator {
            display: inline-block;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            margin-right: 8px;
        }
        .status-low { background-color: #4CAF50; }
        .status-medium { background-color: #FF9800; }
        .status-high { background-color: #F44336; }
    </style>
</head>
<body>
    <div class="dashboard">
        <div class="card">
            <h3>威胁等级</h3>
            <div id="threat-level">
                <span class="status-indicator status-low"></span>
                <span class="metric">LOW</span>
            </div>
        </div>
        
        <div class="card">
            <h3>今日统计</h3>
            <div>威胁检测: <span id="threat-count" class="metric">0</span></div>
            <div>登录尝试: <span id="login-count" class="metric">0</span></div>
            <div>权限检查: <span id="permission-count" class="metric">0</span></div>
        </div>
        
        <div class="card">
            <h3>威胁趋势</h3>
            <canvas id="threat-chart"></canvas>
        </div>
        
        <div class="card">
            <h3>系统状态</h3>
            <div id="system-status">
                <div>数据库: <span class="status-indicator status-low"></span> 正常</div>
                <div>缓存: <span class="status-indicator status-low"></span> 正常</div>
                <div>威胁检测: <span class="status-indicator status-low"></span> 正常</div>
            </div>
        </div>
    </div>

    <script>
        // 实时更新仪表板数据
        function updateDashboard() {
            fetch('/api/security/overview/')
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        updateThreatLevel(data.data.threat_level);
                        updateStatistics(data.data.statistics);
                        updateThreatChart(data.data.trends);
                    }
                })
                .catch(error => console.error('更新仪表板失败:', error));
        }
        
        function updateThreatLevel(level) {
            const element = document.getElementById('threat-level');
            const indicator = element.querySelector('.status-indicator');
            const metric = element.querySelector('.metric');
            
            indicator.className = `status-indicator status-${level.toLowerCase()}`;
            metric.textContent = level;
        }
        
        function updateStatistics(stats) {
            document.getElementById('threat-count').textContent = stats.threats.total_detected;
            document.getElementById('login-count').textContent = stats.authentication.total_attempts;
            document.getElementById('permission-count').textContent = stats.permissions.total_checks;
        }
        
        function updateThreatChart(trends) {
            // 使用Chart.js更新威胁趋势图表
            const ctx = document.getElementById('threat-chart').getContext('2d');
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: trends.labels,
                    datasets: [{
                        label: '威胁数量',
                        data: trends.data,
                        borderColor: 'rgb(75, 192, 192)',
                        tension: 0.1
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        }
        
        // 初始化仪表板
        updateDashboard();
        
        // 每30秒自动更新
        setInterval(updateDashboard, 30000);
    </script>
</body>
</html>
"""
```

### 📚 本节小结

通过本节学习，我们全面掌握了Django企业级安全管理系统的构建：

#### 🎯 核心要点
1. **多因素认证系统**：实现TOTP、SMS、邮件多重验证
2. **RBAC权限控制**：基于角色的细粒度访问控制
3. **智能威胁检测**：实时检测SQL注入、XSS攻击等威胁
4. **安全监控仪表板**：全方位的安全态势感知

#### 🛡️ 安全防护特性
- **身份认证中心**：多层次的用户身份验证机制
- **权限控制系统**：灵活的角色和权限管理
- **威胁检测引擎**：智能的异常行为识别
- **实时监控系统**：comprehensive的安全状态监控

#### 💡 最佳实践
- 采用多因素认证提升账户安全性
- 实施基于角色的权限控制减少安全风险
- 部署智能威胁检测系统实现主动防护
- 建立完整的安全监控和报警机制

## 39.5 🌐 微服务协调部 - Django微服务架构

### 🏢 部门概述

在我们的企业级Web应用总部大厦中，**微服务协调部**就像是大厦的**智能调度中心**，负责协调各个独立的业务单元（微服务），确保它们能够高效协作，就像一个精密的管弦乐团，每个乐器都有自己的职责，但需要指挥家统一协调才能演奏出和谐的乐章。

微服务协调部采用**分布式架构**设计理念，将大型单体应用拆分为多个小而美的独立服务，每个服务专注于特定的业务功能，通过标准化的API接口进行通信，实现真正的松耦合和高可用性。

```mermaid
graph TB
    A["🌐 微服务协调部<br/>(Microservices Coordination)"] --> B["🔧 服务拆分中心<br/>(Service Decomposition)"]
    A --> C["📡 服务通信网关<br/>(Service Gateway)"]
    A --> D["🗄️ 数据管理中心<br/>(Data Management)"]
    A --> E["📦 容器编排室<br/>(Container Orchestration)"]
    A --> F["🔄 CI/CD流水线<br/>(CI/CD Pipeline)"]
    
    B --> B1["📋 业务边界划分<br/>(Business Boundaries)"]
    B --> B2["🎯 服务职责定义<br/>(Service Responsibilities)"]
    B --> B3["📊 依赖关系管理<br/>(Dependency Management)"]
    
    C --> C1["🚪 API网关<br/>(API Gateway)"]
    C --> C2["🔍 服务发现<br/>(Service Discovery)"]
    C --> C3["⚖️ 负载均衡<br/>(Load Balancing)"]
    
    D --> D1["🗃️ 数据库拆分<br/>(Database Decomposition)"]
    D --> D2["🔄 数据同步<br/>(Data Synchronization)"]
    D --> D3["💾 分布式事务<br/>(Distributed Transactions)"]
    
    E --> E1["🐳 Docker容器<br/>(Docker Containers)"]
    E --> E2["☸️ Kubernetes集群<br/>(K8s Cluster)"]
    E --> E3["📈 自动扩展<br/>(Auto Scaling)"]
    
    F --> F1["🔨 自动构建<br/>(Auto Build)"]
    F --> F2["🧪 自动测试<br/>(Auto Testing)"]
    F --> F3["🚀 自动部署<br/>(Auto Deployment)"]
```

### 🔧 服务拆分架构 - 微服务边界设计

服务拆分架构就像是将一个大型**购物中心**按照不同的业务类型划分为专门的店铺，每个店铺都有自己的专业领域和独立的运营方式。

#### 📋 Django微服务拆分实现

```python
# services/base/microservice.py
"""
Django微服务基础架构
Django Microservice Base Architecture
"""

import os
import logging
import requests
from abc import ABC, abstractmethod
from django.conf import settings
from django.http import JsonResponse
from django.core.cache import cache
from django.db import transaction
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import consul
import json

logger = logging.getLogger(__name__)

class MicroserviceBase(ABC):
    """
    微服务基础类
    就像购物中心的标准店铺模板，定义了每个店铺的基本运营规范
    """
    
    def __init__(self, service_name: str, service_version: str = "1.0.0"):
        self.service_name = service_name
        self.service_version = service_version
        self.service_id = f"{service_name}-{service_version}"
        self.consul_client = consul.Consul(
            host=settings.CONSUL_HOST,
            port=settings.CONSUL_PORT
        )
        self.health_check_interval = 30  # 30秒健康检查
        
    def register_service(self, host: str, port: int):
        """
        注册服务到服务发现中心
        就像新店铺在购物中心管理处登记营业信息
        """
        try:
            service_info = {
                'name': self.service_name,
                'service_id': self.service_id,
                'address': host,
                'port': port,
                'tags': [f'version-{self.service_version}', 'django'],
                'check': {
                    'http': f'http://{host}:{port}/health/',
                    'interval': f'{self.health_check_interval}s',
                    'timeout': '10s',
                    'deregister_critical_service_after': '1m'
                },
                'meta': {
                    'version': self.service_version,
                    'framework': 'django',
                    'created_at': datetime.now().isoformat()
                }
            }
            
            self.consul_client.agent.service.register(**service_info)
            logger.info(f"Service {self.service_id} registered successfully")
            
        except Exception as e:
            logger.error(f"Failed to register service {self.service_id}: {str(e)}")
            raise
    
    def deregister_service(self):
        """注销服务"""
        try:
            self.consul_client.agent.service.deregister(self.service_id)
            logger.info(f"Service {self.service_id} deregistered successfully")
        except Exception as e:
            logger.error(f"Failed to deregister service {self.service_id}: {str(e)}")
    
    def discover_service(self, service_name: str) -> Optional[Dict]:
        """
        发现其他服务
        就像查询购物中心的店铺导览图
        """
        try:
            services = self.consul_client.health.service(service_name, passing=True)[1]
            if services:
                # 返回第一个健康的服务实例
                service = services[0]
                return {
                    'host': service['Service']['Address'],
                    'port': service['Service']['Port'],
                    'service_id': service['Service']['ID'],
                    'tags': service['Service']['Tags']
                }
            return None
        except Exception as e:
            logger.error(f"Failed to discover service {service_name}: {str(e)}")
            return None
    
    def call_service(self, service_name: str, endpoint: str, method: str = 'GET', 
                    data: Optional[Dict] = None, timeout: int = 10) -> Optional[Dict]:
        """
        调用其他微服务
        就像一个店铺向另一个店铺请求服务
        """
        try:
            service_info = self.discover_service(service_name)
            if not service_info:
                logger.error(f"Service {service_name} not found")
                return None
            
            url = f"http://{service_info['host']}:{service_info['port']}{endpoint}"
            
            headers = {
                'Content-Type': 'application/json',
                'X-Service-Name': self.service_name,
                'X-Service-Version': self.service_version
            }
            
            if method.upper() == 'GET':
                response = requests.get(url, headers=headers, timeout=timeout)
            elif method.upper() == 'POST':
                response = requests.post(url, json=data, headers=headers, timeout=timeout)
            elif method.upper() == 'PUT':
                response = requests.put(url, json=data, headers=headers, timeout=timeout)
            elif method.upper() == 'DELETE':
                response = requests.delete(url, headers=headers, timeout=timeout)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to call service {service_name}: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error calling service {service_name}: {str(e)}")
            return None
    
    @abstractmethod
    def get_service_info(self) -> Dict:
        """获取服务信息 - 子类必须实现"""
        pass
    
    @abstractmethod
    def health_check(self) -> Dict:
        """健康检查 - 子类必须实现"""  
        pass

class UserService(MicroserviceBase):
    """
    用户服务
    就像购物中心的会员服务中心，专门处理用户相关的所有业务
    """
    
    def __init__(self):
        super().__init__("user-service", "1.0.0")
        self.cache_timeout = 300  # 5分钟缓存
    
    def get_service_info(self) -> Dict:
        """获取用户服务信息"""
        return {
            'service_name': self.service_name,
            'version': self.service_version,
            'description': '用户管理微服务',
            'endpoints': [
                '/api/users/',
                '/api/users/{id}/',
                '/api/users/profile/',
                '/api/auth/login/',
                '/api/auth/logout/'
            ],
            'dependencies': ['notification-service', 'audit-service']
        }
    
    def health_check(self) -> Dict:
        """用户服务健康检查"""
        try:
            from django.contrib.auth.models import User
            
            # 检查数据库连接
            user_count = User.objects.count()
            
            # 检查缓存连接
            cache.set('health_check', 'ok', timeout=60)
            cache_status = cache.get('health_check')
            
            # 检查依赖服务
            notification_status = 'unknown'
            try:
                notification_service = self.discover_service('notification-service')
                notification_status = 'healthy' if notification_service else 'unavailable'
            except:
                notification_status = 'error'
            
            return {
                'status': 'healthy',
                'timestamp': datetime.now().isoformat(),
                'checks': {
                    'database': 'healthy',
                    'cache': 'healthy' if cache_status == 'ok' else 'unhealthy',
                    'dependencies': {
                        'notification-service': notification_status
                    }
                },
                'metrics': {
                    'total_users': user_count,
                    'uptime': self._get_uptime()
                }
            }
            
        except Exception as e:
            logger.error(f"Health check failed for {self.service_name}: {str(e)}")
            return {
                'status': 'unhealthy',
                'timestamp': datetime.now().isoformat(),
                'error': str(e)
            }
    
    def create_user(self, user_data: Dict) -> Dict:
        """
        创建用户
        就像在会员中心办理新的会员卡
        """
        try:
            from django.contrib.auth.models import User
            
            with transaction.atomic():
                # 创建用户
                user = User.objects.create_user(
                    username=user_data['username'],
                    email=user_data['email'],
                    password=user_data['password']
                )
                
                # 创建用户配置文件
                from .models import UserProfile
                profile = UserProfile.objects.create(
                    user=user,
                    phone=user_data.get('phone', ''),
                    department=user_data.get('department', '')
                )
                
                # 发送欢迎通知
                self._send_welcome_notification(user)
                
                # 记录审计日志
                self._log_user_creation(user)
                
                return {
                    'success': True,
                    'user_id': user.id,
                    'username': user.username,
                    'message': '用户创建成功'
                }
                
        except Exception as e:
            logger.error(f"Failed to create user: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def get_user_profile(self, user_id: int) -> Optional[Dict]:
        """
        获取用户资料
        就像查询会员的详细信息
        """
        try:
            # 先尝试从缓存获取
            cache_key = f'user_profile_{user_id}'
            cached_profile = cache.get(cache_key)
            if cached_profile:
                return cached_profile
            
            from django.contrib.auth.models import User
            from .models import UserProfile
            
            user = User.objects.get(id=user_id)
            profile = UserProfile.objects.get(user=user)
            
            user_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'is_active': user.is_active,
                'date_joined': user.date_joined.isoformat(),
                'profile': {
                    'phone': profile.phone,
                    'department': profile.department,
                    'avatar': profile.avatar.url if profile.avatar else None,
                    'last_login': user.last_login.isoformat() if user.last_login else None
                }
            }
            
            # 缓存用户数据
            cache.set(cache_key, user_data, timeout=self.cache_timeout)
            
            return user_data
            
        except User.DoesNotExist:
            logger.warning(f"User {user_id} not found")
            return None
        except Exception as e:
            logger.error(f"Failed to get user profile {user_id}: {str(e)}")
            return None
    
    def _send_welcome_notification(self, user):
        """发送欢迎通知"""
        try:
            notification_data = {
                'user_id': user.id,
                'type': 'welcome',
                'title': '欢迎加入',
                'message': f'欢迎您，{user.username}！',
                'priority': 'normal'
            }
            
            result = self.call_service(
                'notification-service',
                '/api/notifications/',
                method='POST',
                data=notification_data
            )
            
            if result and result.get('success'):
                logger.info(f"Welcome notification sent to user {user.id}")
            else:
                logger.warning(f"Failed to send welcome notification to user {user.id}")
                
        except Exception as e:
            logger.error(f"Error sending welcome notification: {str(e)}")
    
    def _log_user_creation(self, user):
        """记录用户创建审计日志"""
        try:
            audit_data = {
                'action': 'user_created',
                'resource_type': 'user',
                'resource_id': user.id,
                'details': {
                    'username': user.username,
                    'email': user.email
                },
                'timestamp': datetime.now().isoformat()
            }
            
            result = self.call_service(
                'audit-service',
                '/api/audit/logs/',
                method='POST',
                data=audit_data
            )
            
            if result and result.get('success'):
                logger.info(f"Audit log created for user creation: {user.id}")
                
        except Exception as e:
            logger.error(f"Error creating audit log: {str(e)}")
    
    def _get_uptime(self) -> str:
        """获取服务运行时间"""
        # 这里可以实现实际的运行时间计算
        return "24h 30m 15s"

class OrderService(MicroserviceBase):
    """
    订单服务
    就像购物中心的订单处理中心，专门处理所有订单相关业务
    """
    
    def __init__(self):
        super().__init__("order-service", "1.0.0")
    
    def get_service_info(self) -> Dict:
        """获取订单服务信息"""
        return {
            'service_name': self.service_name,
            'version': self.service_version,
            'description': '订单管理微服务',
            'endpoints': [
                '/api/orders/',
                '/api/orders/{id}/',
                '/api/orders/status/',
                '/api/orders/cancel/'
            ],
            'dependencies': ['user-service', 'payment-service', 'inventory-service']
        }
    
    def health_check(self) -> Dict:
        """订单服务健康检查"""
        try:
            from .models import Order
            
            # 检查订单数据
            order_count = Order.objects.count()
            pending_orders = Order.objects.filter(status='pending').count()
            
            return {
                'status': 'healthy',
                'timestamp': datetime.now().isoformat(),
                'checks': {
                    'database': 'healthy',
                    'business_logic': 'healthy'
                },
                'metrics': {
                    'total_orders': order_count,
                    'pending_orders': pending_orders
                }
            }
            
        except Exception as e:
            logger.error(f"Health check failed for {self.service_name}: {str(e)}")
            return {
                'status': 'unhealthy',
                'timestamp': datetime.now().isoformat(),
                'error': str(e)
            }
    
    def create_order(self, order_data: Dict) -> Dict:
        """
        创建订单
        就像在订单中心处理一个新的购买请求
        """
        try:
            with transaction.atomic():
                # 1. 验证用户
                user_info = self.call_service(
                    'user-service',
                    f"/api/users/{order_data['user_id']}/",
                    method='GET'
                )
                
                if not user_info:
                    return {
                        'success': False,
                        'error': '用户不存在或服务不可用'
                    }
                
                # 2. 检查库存
                inventory_check = self.call_service(
                    'inventory-service',
                    '/api/inventory/check/',
                    method='POST',
                    data={'items': order_data['items']}
                )
                
                if not inventory_check or not inventory_check.get('available'):
                    return {
                        'success': False,
                        'error': '库存不足'
                    }
                
                # 3. 创建订单
                from .models import Order, OrderItem
                
                order = Order.objects.create(
                    user_id=order_data['user_id'],
                    total_amount=order_data['total_amount'],
                    status='pending'
                )
                
                # 创建订单项
                for item_data in order_data['items']:
                    OrderItem.objects.create(
                        order=order,
                        product_id=item_data['product_id'],
                        quantity=item_data['quantity'],
                        price=item_data['price']
                    )
                
                # 4. 预留库存
                reservation_result = self.call_service(
                    'inventory-service',
                    '/api/inventory/reserve/',
                    method='POST',
                    data={
                        'order_id': order.id,
                        'items': order_data['items']
                    }
                )
                
                if not reservation_result or not reservation_result.get('success'):
                    # 回滚订单创建
                    order.delete()
                    return {
                        'success': False,
                        'error': '库存预留失败'
                    }
                
                return {
                    'success': True,
                    'order_id': order.id,
                    'status': order.status,
                    'message': '订单创建成功'
                }
                
        except Exception as e:
            logger.error(f"Failed to create order: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }

class ServiceRegistry:
    """
    服务注册中心
    就像购物中心的总控中心，管理所有店铺的信息
    """
    
    def __init__(self):
        self.consul_client = consul.Consul(
            host=settings.CONSUL_HOST,
            port=settings.CONSUL_PORT
        )
        self.services = {}
    
    def register_all_services(self):
        """注册所有微服务"""
        try:
            # 注册用户服务
            user_service = UserService()
            user_service.register_service(
                host=settings.SERVICE_HOST,
                port=settings.USER_SERVICE_PORT
            )
            self.services['user-service'] = user_service
            
            # 注册订单服务
            order_service = OrderService()
            order_service.register_service(
                host=settings.SERVICE_HOST,
                port=settings.ORDER_SERVICE_PORT
            )
            self.services['order-service'] = order_service
            
            logger.info("All services registered successfully")
            
        except Exception as e:
            logger.error(f"Failed to register services: {str(e)}")
            raise
    
    def deregister_all_services(self):
        """注销所有微服务"""
        for service in self.services.values():
            service.deregister_service()
        
        self.services.clear()
        logger.info("All services deregistered")
    
    def get_service_health_status(self) -> Dict:
        """获取所有服务的健康状态"""
        health_status = {}
        
        for service_name, service in self.services.items():
            try:
                health_status[service_name] = service.health_check()
            except Exception as e:
                health_status[service_name] = {
                    'status': 'error',
                    'error': str(e)
                }
        
        return health_status

# Django启动时的服务注册
from django.apps import AppConfig

class MicroserviceConfig(AppConfig):
    """微服务配置"""
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'microservices'
    
    def ready(self):
        """Django应用启动时注册服务"""
        import signal
        import atexit
        
        # 创建服务注册中心
        self.registry = ServiceRegistry()
        
        try:
            # 注册所有服务
            self.registry.register_all_services()
            
            # 注册清理函数
            atexit.register(self.cleanup_services)
            signal.signal(signal.SIGTERM, self.signal_handler)
            signal.signal(signal.SIGINT, self.signal_handler)
            
        except Exception as e:
            logger.error(f"Failed to initialize microservices: {str(e)}")
    
    def cleanup_services(self):
        """清理服务注册"""
        if hasattr(self, 'registry'):
            self.registry.deregister_all_services()
    
    def signal_handler(self, signum, frame):
        """信号处理器"""
        logger.info(f"Received signal {signum}, cleaning up services...")
        self.cleanup_services()
```

### 📦 容器化部署 - Docker与Kubernetes集成

容器化部署就像是将每个店铺都装在**标准化的集装箱**里，无论在哪个购物中心都能快速搭建和运营。

#### 🐳 Docker容器化配置

```dockerfile
# Dockerfile
# Django微服务容器化配置

FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 安装系统依赖
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        build-essential \
        curl \
    && rm -rf /var/lib/apt/lists/*

# 安装Python依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . .

# 创建非root用户
RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser:appuser /app
USER appuser

# 健康检查
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
  CMD curl -f http://localhost:8000/health/ || exit 1

# 暴露端口
EXPOSE 8000

# 启动命令
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "project.wsgi:application"]
```

```yaml
# docker-compose.yml
# 微服务本地开发环境编排

version: '3.8'

services:
  # 服务发现
  consul:
    image: consul:1.15
    container_name: consul
    ports:
      - "8500:8500"
    command: agent -server -ui -node=server-1 -bootstrap-expect=1 -client=0.0.0.0
    environment:
      - CONSUL_BIND_INTERFACE=eth0
    volumes:
      - consul_data:/consul/data
    networks:
      - microservices

  # 数据库
  postgres:
    image: postgres:14
    container_name: postgres
    environment:
      POSTGRES_DB: microservices_db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - microservices

  # Redis缓存
  redis:
    image: redis:7-alpine
    container_name: redis
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    networks:
      - microservices

  # 用户服务
  user-service:
    build: 
      context: .
      dockerfile: services/user/Dockerfile
    container_name: user-service
    ports:
      - "8001:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@postgres:5432/microservices_db
      - REDIS_URL=redis://redis:6379/0
      - CONSUL_HOST=consul
      - CONSUL_PORT=8500
      - SERVICE_NAME=user-service
      - SERVICE_PORT=8000
    depends_on:
      - postgres
      - redis
      - consul
    networks:
      - microservices
    restart: unless-stopped

  # 订单服务
  order-service:
    build:
      context: .
      dockerfile: services/order/Dockerfile
    container_name: order-service
    ports:
      - "8002:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@postgres:5432/microservices_db
      - REDIS_URL=redis://redis:6379/1
      - CONSUL_HOST=consul
      - CONSUL_PORT=8500
      - SERVICE_NAME=order-service
      - SERVICE_PORT=8000
    depends_on:
      - postgres
      - redis
      - consul
    networks:
      - microservices
    restart: unless-stopped

  # API网关
  api-gateway:
    build:
      context: .
      dockerfile: gateway/Dockerfile
    container_name: api-gateway
    ports:
      - "8000:8000"
    environment:
      - CONSUL_HOST=consul
      - CONSUL_PORT=8500
    depends_on:
      - consul
      - user-service
      - order-service
    networks:
      - microservices
    restart: unless-stopped

volumes:
  consul_data:
  postgres_data:
  redis_data:

networks:
  microservices:
    driver: bridge
```

#### ☸️ Kubernetes部署配置

```yaml
# k8s/namespace.yaml
# Kubernetes命名空间配置

apiVersion: v1
kind: Namespace
metadata:
  name: microservices
  labels:
    name: microservices
---
# k8s/user-service-deployment.yaml
# 用户服务Kubernetes部署配置

apiVersion: apps/v1
kind: Deployment
metadata:
  name: user-service
  namespace: microservices
  labels:
    app: user-service
    version: v1
spec:
  replicas: 3
  selector:
    matchLabels:
      app: user-service
  template:
    metadata:
      labels:
        app: user-service
        version: v1
    spec:
      containers:
      - name: user-service
        image: user-service:latest
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: database-url
        - name: REDIS_URL
          value: "redis://redis-service:6379/0"
        - name: CONSUL_HOST
          value: "consul-service"
        - name: CONSUL_PORT
          value: "8500"
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health/
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready/
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
      imagePullSecrets:
      - name: registry-secret
---
apiVersion: v1
kind: Service
metadata:
  name: user-service
  namespace: microservices
  labels:
    app: user-service
spec:
  selector:
    app: user-service
  ports:
  - port: 80
    targetPort: 8000
    protocol: TCP
  type: ClusterIP
---
# k8s/hpa.yaml
# 水平自动扩展配置

apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: user-service-hpa
  namespace: microservices
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: user-service
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Percent
        value: 10
        periodSeconds: 60
    scaleUp:
      stabilizationWindowSeconds: 60
      policies:
      - type: Percent
        value: 50
        periodSeconds: 60
---
# k8s/ingress.yaml
# Ingress网关配置

apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: microservices-ingress
  namespace: microservices
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/use-regex: "true"
    nginx.ingress.kubernetes.io/rate-limit: "100"
spec:
  tls:
  - hosts:
    - api.microservices.com
    secretName: tls-secret
  rules:
  - host: api.microservices.com
    http:
      paths:
      - path: /api/users/(.*)
        pathType: Prefix
        backend:
          service:
            name: user-service
            port:
              number: 80
      - path: /api/orders/(.*)
        pathType: Prefix
        backend:
          service:
            name: order-service
            port:
              number: 80
      - path: /(.*)
        pathType: Prefix
        backend:
          service:
            name: api-gateway
            port:
              number: 80
```

### 🔄 CI/CD流水线 - 自动化部署

CI/CD流水线就像是购物中心的**自动化物流系统**，从商品入库、质检、分拣到最终上架，整个过程都是自动化完成的。

#### 🚀 GitHub Actions配置

```yaml
# .github/workflows/microservices-ci-cd.yml
# 微服务CI/CD流水线配置

name: Microservices CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  # 代码质量检查
  quality-check:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 black pytest coverage
        pip install -r requirements.txt
    
    - name: Code formatting check
      run: black --check .
    
    - name: Lint with flake8
      run: |
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    
    - name: Security scan
      run: |
        pip install bandit
        bandit -r . -f json -o bandit-report.json
    
    - name: Upload security scan results
      uses: actions/upload-artifact@v3
      with:
        name: security-scan-results
        path: bandit-report.json

  # 单元测试
  unit-tests:
    runs-on: ubuntu-latest
    needs: quality-check
    
    services:
      postgres:
        image: postgres:14
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: test_db
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432
      
      redis:
        image: redis:7
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 3
        ports:
          - 6379:6379
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-test.txt
    
    - name: Run tests
      env:
        DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test_db
        REDIS_URL: redis://localhost:6379/0
      run: |
        coverage run -m pytest
        coverage xml
    
    - name: Upload test results
      uses: actions/upload-artifact@v3
      with:
        name: test-results
        path: |
          coverage.xml
          htmlcov/

  # 构建Docker镜像
  build-images:
    runs-on: ubuntu-latest
    needs: unit-tests
    if: github.event_name == 'push'
    
    strategy:
      matrix:
        service: [user-service, order-service, api-gateway]
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v2
    
    - name: Log in to Container Registry
      uses: docker/login-action@v2
      with:
        registry: ${{ env.REGISTRY }}
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}
    
    - name: Extract metadata
      id: meta
      uses: docker/metadata-action@v4
      with:
        images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}/${{ matrix.service }}
        tags: |
          type=ref,event=branch
          type=ref,event=pr
          type=sha,prefix={{branch}}-
          type=raw,value=latest,enable={{is_default_branch}}
    
    - name: Build and push Docker image
      uses: docker/build-push-action@v4
      with:
        context: .
        file: ./services/${{ matrix.service }}/Dockerfile
        push: true
        tags: ${{ steps.meta.outputs.tags }}
        labels: ${{ steps.meta.outputs.labels }}
        cache-from: type=gha
        cache-to: type=gha,mode=max

  # 集成测试
  integration-tests:
    runs-on: ubuntu-latest
    needs: build-images
    if: github.event_name == 'push'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Docker Compose
      run: |
        docker-compose -f docker-compose.test.yml up -d
        sleep 30  # 等待服务启动
    
    - name: Run integration tests
      run: |
        docker-compose -f docker-compose.test.yml exec -T api-gateway pytest tests/integration/
    
    - name: Collect logs
      if: always()
      run: |
        docker-compose -f docker-compose.test.yml logs > integration-test-logs.txt
    
    - name: Upload logs
      if: always()
      uses: actions/upload-artifact@v3
      with:
        name: integration-test-logs
        path: integration-test-logs.txt
    
    - name: Cleanup
      if: always()
      run: docker-compose -f docker-compose.test.yml down -v

  # 部署到测试环境
  deploy-staging:
    runs-on: ubuntu-latest
    needs: integration-tests
    if: github.ref == 'refs/heads/develop'
    environment: staging
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Configure kubectl
      uses: azure/k8s-set-context@v3
      with:
        method: kubeconfig
        kubeconfig: ${{ secrets.KUBE_CONFIG_STAGING }}
    
    - name: Deploy to staging
      run: |
        envsubst < k8s/staging/deployment.yaml | kubectl apply -f -
        kubectl rollout status deployment/user-service -n microservices-staging
        kubectl rollout status deployment/order-service -n microservices-staging
    
    - name: Run smoke tests
      run: |
        kubectl wait --for=condition=ready pod -l app=user-service -n microservices-staging --timeout=300s
        curl -f http://staging-api.microservices.com/health/ || exit 1

  # 部署到生产环境
  deploy-production:
    runs-on: ubuntu-latest
    needs: integration-tests
    if: github.ref == 'refs/heads/main'
    environment: production
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Configure kubectl
      uses: azure/k8s-set-context@v3
      with:
        method: kubeconfig
        kubeconfig: ${{ secrets.KUBE_CONFIG_PRODUCTION }}
    
    - name: Deploy to production
      run: |
        envsubst < k8s/production/deployment.yaml | kubectl apply -f -
        kubectl rollout status deployment/user-service -n microservices-production --timeout=600s
        kubectl rollout status deployment/order-service -n microservices-production --timeout=600s
    
    - name: Verify deployment
      run: |
        kubectl get pods -n microservices-production
        curl -f https://api.microservices.com/health/ || exit 1
    
    - name: Send deployment notification
      uses: 8398a7/action-slack@v3
      with:
        status: ${{ job.status }}
        channel: '#deployments'
        webhook_url: ${{ secrets.SLACK_WEBHOOK }}
      if: always()
```

### 📚 本节小结

通过本节学习，我们全面掌握了Django微服务架构的设计与实现：

#### 🎯 核心要点
1. **微服务拆分设计**：按业务边界合理拆分单体应用
2. **服务注册与发现**：使用Consul实现服务治理
3. **容器化部署**：Docker和Kubernetes的企业级部署
4. **CI/CD自动化**：完整的持续集成和部署流水线

#### 🌐 微服务特性
- **服务独立性**：每个服务独立开发、测试、部署
- **技术多样性**：不同服务可以选择不同的技术栈
- **水平扩展**：根据负载自动扩展服务实例
- **故障隔离**：单个服务故障不影响整个系统

#### 💡 最佳实践
- 按业务领域进行服务拆分而非技术层次
- 实现服务间的松耦合和高内聚
- 建立完善的监控和日志体系
- 采用渐进式微服务化策略

## 📚 第39章总结

### 🎯 章节回顾

在本章中，我们深入探索了Django高级特性与企业级架构设计，通过"**企业级Web应用总部大厦**"这一生动的比喻体系，系统学习了Django在现代企业级应用开发中的核心技术和最佳实践。

#### 🏗️ 五大核心部门成就
1. **架构设计部** - 掌握了Django MVT架构的深度应用、分层设计原则和插件化架构实现
2. **API服务中心** - 精通Django REST Framework高级特性、API版本管理和性能优化策略
3. **实时通信部** - 实现了Django Channels WebSocket通信、异步编程和企业级协作平台
4. **安全管理部** - 构建了多因素认证、RBAC权限控制、智能威胁检测和安全监控体系
5. **微服务协调部** - 设计了完整的微服务架构、容器化部署和CI/CD自动化流水线

### 💻 技术成果统计

#### 📊 代码实现规模
- **总代码行数**: 约6,500行企业级Python代码
- **核心模块**: 25个完整的功能模块
- **代码示例**: 20+个生产级代码示例
- **架构图表**: 6个专业Mermaid架构图

#### 🚀 实战项目价值
- **企业级博客系统**: 支持分层架构和模型继承的内容管理平台
- **任务管理API平台**: 完整的RESTful API和JWT认证系统
- **实时协作平台**: WebSocket多人协作和Operational Transformation
- **安全监控系统**: 威胁检测、权限控制和实时监控仪表板
- **微服务架构系统**: 完整的服务拆分、注册发现和容器化部署

### 🌟 核心技术突破

#### 🎭 创新比喻教学法
- **企业总部大厦**: 将复杂的Django架构映射为直观的企业组织结构
- **部门协作模式**: 通过部门职责类比不同技术模块的功能和协作关系
- **业务场景驱动**: 每个技术点都对应实际的企业应用场景

#### 🏗️ 企业级架构设计
- **MVT架构深化**: 从基础的Model-View-Template到企业级的分层架构设计
- **插件化系统**: 实现了完整的插件注册、加载和管理机制
- **API网关模式**: 构建了统一的API入口和版本管理系统

#### ⚡ 实时通信技术
- **WebSocket实现**: 完整的Django Channels配置和消费者路由系统
- **协作编辑算法**: 实现了Operational Transformation实时协作编辑
- **异步任务集成**: Celery任务队列与实时进度推送的完美结合

#### 🛡️ 企业级安全体系
- **多因素认证**: TOTP、SMS、邮件多重验证的完整实现
- **RBAC权限模型**: 基于角色的细粒度访问控制系统
- **智能威胁检测**: SQL注入、XSS攻击等多种威胁的实时检测
- **安全监控仪表板**: 全方位的安全态势感知和可视化展示

#### 🌐 微服务架构实践
- **服务拆分策略**: 按业务边界进行的合理服务拆分
- **服务治理**: Consul服务注册发现和健康检查机制
- **容器化部署**: Docker和Kubernetes的生产级部署配置
- **CI/CD流水线**: 从代码提交到生产部署的完整自动化流程

### 📈 学习成果与价值

#### 🎓 知识技能提升
- **架构设计能力**: 从单体应用到微服务架构的完整设计思维
- **企业级开发素养**: 代码质量、安全意识、性能优化的全面提升
- **现代化开发技能**: 容器化、CI/CD、微服务等现代化开发技术栈
- **系统思维培养**: 从技术实现到业务价值的全局思考能力

#### 💼 职业发展价值
- **技术专家路径**: 具备Django高级工程师和架构师的核心技能
- **项目实战能力**: 可以独立设计和实现企业级Django应用
- **团队协作能力**: 掌握现代化开发流程和团队协作最佳实践
- **技术领导能力**: 具备指导团队进行企业级项目开发的能力

#### 🚀 商业应用潜力
- **直接商业价值**: 所有示例项目都具备实际商业部署的潜力
- **技术栈完整性**: 覆盖从前端到后端、从开发到部署的完整技术栈
- **行业适应性**: 可应用于电商、教育、金融、医疗等多个行业
- **扩展性保障**: 支持从小型应用到大型企业系统的平滑扩展

### 🔮 技术发展展望

#### 📊 Django生态演进
随着Python和Django生态的不断发展，本章所学的技术将在以下方面继续演进：
- **异步支持增强**: Django对异步编程的支持将更加完善
- **微服务工具**: 更多针对Django微服务的专用工具和框架
- **AI集成**: Django与AI技术的深度集成将成为新的趋势
- **云原生优化**: 更好地支持云原生和serverless架构

#### 🌟 持续学习建议
1. **关注Django官方更新**: 及时了解新版本的功能和最佳实践
2. **参与开源项目**: 通过实际项目贡献来提升技术水平
3. **学习相关技术**: 扩展学习Kubernetes、监控系统等相关技术
4. **实践商业项目**: 将所学技术应用到实际的商业项目中

### 💎 最后感悟

通过本章的深入学习，我们不仅掌握了Django的高级特性，更重要的是建立了**企业级思维**和**架构设计能力**。正如我们在企业总部大厦中看到的那样，优秀的软件架构需要：

- **清晰的职责划分**: 每个模块都有明确的职责边界
- **高效的协作机制**: 不同组件之间要能够高效协作
- **完善的安全保障**: 全方位的安全防护不可或缺
- **持续的监控优化**: 系统需要不断监控和优化改进

这些原则不仅适用于Django开发，更是软件工程的普遍真理。掌握了这些核心思想，无论面对什么样的技术挑战，我们都能够设计出优雅、高效、安全的解决方案。

---

**🎉 恭喜完成第39章学习！** 

您现在已经具备了Django企业级开发的核心技能，可以设计和实现复杂的企业级Web应用。在下一章中，我们将继续探索更多高级应用技术，进一步提升您的技术实力和项目经验。

**继续前进，成为真正的Django架构大师！** 🚀
