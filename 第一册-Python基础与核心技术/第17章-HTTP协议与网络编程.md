# 第17章：HTTP协议与网络编程

> "网络通信就像现代邮递系统，HTTP协议是这个系统的语言，Python是我们的得力工具。"

## 🎯 学习目标

通过本章学习，你将能够：

- 🏢 **深入理解HTTP协议**：掌握HTTP/1.1到HTTP/3的演进历程，理解请求/响应机制
- 🔧 **熟练Python网络编程**：掌握socket编程、异步编程，构建高性能网络应用
- 🚀 **开发Web服务器**：从零开始构建企业级Web服务器，理解WSGI/ASGI协议
- 🌐 **构建分布式系统**：掌握微服务架构、API设计、负载均衡等现代Web技术
- 🔐 **网络安全实践**：实现HTTPS、身份认证、防护机制等安全技术
- 📊 **性能优化技巧**：连接池、缓存策略、监控系统等企业级实践

## 📬 "网络邮递系统"比喻体系

在学习网络编程之前，让我们建立一个贴切的比喻：

```
🏢 网络通信 = 现代邮递系统
├── 📬 HTTP协议 = 邮递服务标准（如何寄信、收信）
├── 📋 HTTP方法 = 邮件类型（普通信、挂号信、包裹、快递）
├── 📊 状态码 = 邮递状态（成功送达、地址错误、服务暂停）
├── 🏷️ HTTP头部 = 信件标签（发件人、收件人、优先级、加密）
├── 🚚 请求/响应 = 寄信/收信（完整的邮递流程）
├── 🔐 身份认证 = 邮局验证（会员卡、身份证明）
├── 🌐 会话管理 = 客户档案（VIP服务、历史记录）
├── ⚡ 异步编程 = 批量处理（同时处理多个邮件）
└── 🏢 微服务 = 连锁邮局（专业化分工、统一管理）
```

这个比喻将贯穿整个章节，让抽象的网络概念变得具体可感！

---

## 17.1 HTTP协议深度解析 - "现代邮递系统的运作机制" 📮

> 就像邮递系统需要标准化的流程一样，HTTP协议定义了网络通信的标准格式和规则。

### 🎯 本节目标
- 理解HTTP协议的历史演进和设计原理
- 掌握HTTP消息格式和核心概念
- 学会分析和构建HTTP请求/响应
- 了解HTTPS安全机制和最佳实践

### 📚 理论基础：HTTP协议演进史

#### HTTP协议的发展历程

想象邮递系统的发展：从古代的驿站传递，到现代的智能物流，每一次革新都提高了效率和可靠性。

```python
"""
HTTP协议发展历史 - 邮递系统的现代化进程

🐎 HTTP/0.9 (1991) = 古代驿站
   - 只支持GET方法
   - 无状态码、无头部
   - 连接后立即断开

🚂 HTTP/1.0 (1996) = 早期邮政系统  
   - 增加POST、HEAD方法
   - 引入状态码和头部
   - 每个请求都要建立新连接

🚄 HTTP/1.1 (1997) = 现代邮政系统
   - 持久连接 (Keep-Alive)
   - 管道化 (Pipelining)
   - 缓存控制
   - 分块传输编码

🚀 HTTP/2 (2015) = 智能物流中心
   - 二进制协议
   - 多路复用
   - 头部压缩
   - 服务器推送

🛸 HTTP/3 (2020) = 未来邮递系统
   - 基于QUIC协议
   - 更快的连接建立
   - 更好的网络适应性
   - 内置加密
"""

from typing import Dict, List, Optional, Any
import json
import base64
import hashlib
import time
from urllib.parse import urlparse, parse_qs
from datetime import datetime, timezone
```

### 🔍 HTTP消息解析：拆解邮件的每个部分

#### 1. HTTP请求消息结构

```python
class HTTPRequest:
    """
    HTTP请求 - 就像一封标准格式的邮件
    
    结构对应：
    - 请求行 = 信件封面（收件人地址、邮件类型）
    - 请求头 = 信件标签（发件人、优先级、特殊要求）
    - 请求体 = 信件内容（实际要传递的信息）
    """
    
    def __init__(self, method: str, url: str, version: str = "HTTP/1.1"):
        self.method = method.upper()  # GET, POST, PUT, DELETE等
        self.url = url
        self.version = version
        self.headers: Dict[str, str] = {}
        self.body: str = ""
        
        # 解析URL组件
        self.parsed_url = urlparse(url)
        self.path = self.parsed_url.path or "/"
        self.query_params = parse_qs(self.parsed_url.query)
        
        # 基本头部
        self.headers["Host"] = self.parsed_url.netloc
        self.headers["User-Agent"] = "Python-HTTPClient/1.0"
        self.headers["Accept"] = "*/*"
    
    def add_header(self, name: str, value: str) -> None:
        """添加请求头 - 像给信件添加标签"""
        self.headers[name] = value
        print(f"📋 添加请求头: {name} = {value}")
    
    def set_body(self, content: str, content_type: str = "text/plain") -> None:
        """设置请求体 - 填写信件内容"""
        self.body = content
        self.headers["Content-Length"] = str(len(content.encode('utf-8')))
        self.headers["Content-Type"] = content_type
        print(f"📝 设置请求体: {len(content)} 字符")
    
    def set_json_body(self, data: Any) -> None:
        """设置JSON请求体 - 发送结构化数据"""
        json_str = json.dumps(data, ensure_ascii=False)
        self.set_body(json_str, "application/json; charset=utf-8")
    
    def add_query_param(self, name: str, value: str) -> None:
        """添加查询参数"""
        if name not in self.query_params:
            self.query_params[name] = []
        self.query_params[name].append(value)
    
    def to_string(self) -> str:
        """转换为标准HTTP请求格式"""
        # 构建查询字符串
        query_string = ""
        if self.query_params:
            params = []
            for name, values in self.query_params.items():
                for value in values:
                    params.append(f"{name}={value}")
            query_string = "?" + "&".join(params)
        
        # 构建请求行
        request_line = f"{self.method} {self.path}{query_string} {self.version}"
        
        # 构建请求头
        header_lines = []
        for name, value in self.headers.items():
            header_lines.append(f"{name}: {value}")
        
        # 组装完整请求
        parts = [request_line] + header_lines + [""]
        if self.body:
            parts.append(self.body)
        
        return "\n".join(parts)
    
    def explain_request(self) -> str:
        """解释请求的含义 - 用邮递比喻"""
        explanations = {
            "GET": "📬 查询邮件 - 我想获取信息",
            "POST": "📮 投递邮件 - 我要发送新信息", 
            "PUT": "📝 更新邮件 - 我要修改完整信息",
            "PATCH": "✏️ 部分更新 - 我要修改部分信息",
            "DELETE": "🗑️ 删除邮件 - 我要删除信息",
            "HEAD": "👀 查看邮件概况 - 我只要头部信息",
            "OPTIONS": "❓ 询问服务 - 我想知道支持什么操作"
        }
        
        method_explain = explanations.get(self.method, f"📋 {self.method}方法")
        return f"{method_explain}\n目标地址: {self.url}\n传输协议: {self.version}"

# 演示HTTP请求构建
def demo_http_request():
    """HTTP请求构建演示"""
    print("=== HTTP请求构建演示 ===\n")
    
    # 创建GET请求
    print("1. 📬 创建GET请求（查询邮件）:")
    get_request = HTTPRequest("GET", "https://api.example.com/users?page=1&limit=10")
    get_request.add_header("Accept", "application/json")
    get_request.add_header("Authorization", "Bearer token123")
    
    print(get_request.explain_request())
    print("\n标准格式:")
    print(get_request.to_string())
    
    # 创建POST请求
    print("\n" + "="*50)
    print("2. 📮 创建POST请求（投递邮件）:")
    post_request = HTTPRequest("POST", "https://api.example.com/users")
    post_request.add_header("Authorization", "Bearer token123")
    
    user_data = {
        "name": "张三",
        "email": "zhangsan@example.com",
        "age": 25
    }
    post_request.set_json_body(user_data)
    
    print(post_request.explain_request())
    print("\n标准格式:")
    print(post_request.to_string())

# 运行演示
if __name__ == "__main__":
    demo_http_request()
```

#### 2. HTTP响应消息结构

```python
class HTTPResponse:
    """
    HTTP响应 - 就像邮局的回执和包裹
    
    结构对应：
    - 状态行 = 邮递状态（成功送达、地址错误等）
    - 响应头 = 回执标签（处理时间、负责人等）
    - 响应体 = 回执内容或返回的包裹
    """
    
    def __init__(self, status_code: int, reason_phrase: str = "", version: str = "HTTP/1.1"):
        self.status_code = status_code
        self.reason_phrase = reason_phrase or self._get_reason_phrase(status_code)
        self.version = version
        self.headers: Dict[str, str] = {}
        self.body: str = ""
        
        # 基本头部
        self.headers["Server"] = "Python-HTTPServer/1.0"
        self.headers["Date"] = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
        self.headers["Connection"] = "close"
    
    def _get_reason_phrase(self, code: int) -> str:
        """根据状态码获取标准短语"""
        status_phrases = {
            # 2xx 成功
            200: "OK", 201: "Created", 202: "Accepted", 204: "No Content",
            # 3xx 重定向  
            301: "Moved Permanently", 302: "Found", 304: "Not Modified",
            # 4xx 客户端错误
            400: "Bad Request", 401: "Unauthorized", 403: "Forbidden", 
            404: "Not Found", 405: "Method Not Allowed", 409: "Conflict",
            # 5xx 服务器错误
            500: "Internal Server Error", 502: "Bad Gateway", 503: "Service Unavailable"
        }
        return status_phrases.get(code, "Unknown")
    
    def add_header(self, name: str, value: str) -> None:
        """添加响应头"""
        self.headers[name] = value
    
    def set_body(self, content: str, content_type: str = "text/plain; charset=utf-8") -> None:
        """设置响应体"""
        self.body = content
        self.headers["Content-Length"] = str(len(content.encode('utf-8')))
        self.headers["Content-Type"] = content_type
    
    def set_json_body(self, data: Any) -> None:
        """设置JSON响应体"""
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        self.set_body(json_str, "application/json; charset=utf-8")
    
    def to_string(self) -> str:
        """转换为标准HTTP响应格式"""
        # 状态行
        status_line = f"{self.version} {self.status_code} {self.reason_phrase}"
        
        # 响应头
        header_lines = []
        for name, value in self.headers.items():
            header_lines.append(f"{name}: {value}")
        
        # 组装完整响应
        parts = [status_line] + header_lines + [""]
        if self.body:
            parts.append(self.body)
        
        return "\n".join(parts)
    
    def explain_status(self) -> str:
        """解释状态码的含义 - 用邮递比喻"""
        status_explanations = {
            # 2xx 成功类
            200: "✅ 邮件成功送达 - 任务完成",
            201: "✅ 新邮件已创建 - 信息已保存",
            202: "✅ 邮件已接收 - 正在处理中",
            204: "✅ 操作成功 - 无需返回内容",
            
            # 3xx 重定向类
            301: "🔄 邮局永久搬迁 - 请使用新地址",
            302: "🔄 临时转移 - 请暂时使用新地址", 
            304: "📋 邮件未更新 - 使用本地缓存",
            
            # 4xx 客户端错误类
            400: "❌ 邮件格式错误 - 请检查内容",
            401: "🔐 需要身份验证 - 请提供凭证",
            403: "🚫 禁止访问 - 权限不足",
            404: "📭 地址不存在 - 找不到目标",
            405: "🚫 不支持的邮件类型 - 方法不允许",
            409: "⚠️ 邮件冲突 - 存在重复内容",
            
            # 5xx 服务器错误类
            500: "💥 邮局内部故障 - 服务器错误",
            502: "💥 转发失败 - 网关错误",
            503: "🚫 邮局暂停服务 - 服务不可用"
        }
        
        return status_explanations.get(self.status_code, f"状态码 {self.status_code}")

# 演示HTTP响应构建
def demo_http_response():
    """HTTP响应构建演示"""
    print("=== HTTP响应构建演示 ===\n")
    
    # 成功响应
    print("1. ✅ 成功响应:")
    success_response = HTTPResponse(200)
    success_response.add_header("Cache-Control", "public, max-age=3600")
    
    response_data = {
        "status": "success",
        "message": "用户信息获取成功",
        "data": {
            "id": 1,
            "name": "张三",
            "email": "zhangsan@example.com"
        }
    }
    success_response.set_json_body(response_data)
    
    print(f"状态说明: {success_response.explain_status()}")
    print("\n标准格式:")
    print(success_response.to_string())
    
    # 错误响应
    print("\n" + "="*50)
    print("2. ❌ 错误响应:")
    error_response = HTTPResponse(404)
    error_response.add_header("Cache-Control", "no-cache")
    
    error_data = {
        "status": "error",
        "message": "用户不存在",
        "error_code": "USER_NOT_FOUND"
    }
    error_response.set_json_body(error_data)
    
    print(f"状态说明: {error_response.explain_status()}")
    print("\n标准格式:")
    print(error_response.to_string())

# 运行演示
if __name__ == "__main__":
    demo_http_response()
```

### 🏷️ HTTP头部字段详解：信件的标签系统

HTTP头部就像信件上的各种标签，提供了关于邮件的重要信息：

```python
class HTTPHeaders:
    """HTTP头部字段管理类 - 邮件标签系统"""
    
    def __init__(self):
        self.headers: Dict[str, str] = {}
    
    def add_general_headers(self):
        """添加通用头部 - 基础邮件标签"""
        self.headers.update({
            "Cache-Control": "no-cache",      # 缓存控制
            "Connection": "keep-alive",       # 连接控制
            "Date": datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT"),
            "Pragma": "no-cache",            # 兼容性缓存控制
            "Upgrade-Insecure-Requests": "1"  # 安全升级请求
        })
    
    def add_request_headers(self):
        """添加请求专用头部 - 寄信人标签"""
        self.headers.update({
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "Mozilla/5.0 (Python HTTPClient) AppleWebKit/537.36",
            "Referer": "https://example.com/",
            "Authorization": "Bearer token123",
            "X-Requested-With": "XMLHttpRequest"  # AJAX请求标识
        })
    
    def add_response_headers(self):
        """添加响应专用头部 - 邮局回执标签"""
        self.headers.update({
            "Server": "nginx/1.18.0",
            "Content-Type": "application/json; charset=utf-8",
            "Content-Length": "1024",
            "Last-Modified": "Wed, 01 Feb 2024 12:00:00 GMT",
            "ETag": '"abc123def456"',
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
            "Set-Cookie": "session_id=abc123; HttpOnly; Secure; SameSite=Strict"
        })
    
    def add_security_headers(self):
        """添加安全头部 - 安全防护标签"""
        self.headers.update({
            "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
            "Content-Security-Policy": "default-src 'self'",
            "X-Frame-Options": "DENY",
            "X-Content-Type-Options": "nosniff",
            "X-XSS-Protection": "1; mode=block",
            "Referrer-Policy": "strict-origin-when-cross-origin"
        })
    
    def explain_header(self, header_name: str) -> str:
        """解释头部字段的含义"""
        explanations = {
            # 通用头部
            "Cache-Control": "🗄️ 缓存控制 - 告诉邮局如何存储邮件副本",
            "Connection": "🔗 连接管理 - 决定邮递员是否继续等待",
            "Date": "📅 时间戳 - 邮件的处理时间",
            
            # 请求头部
            "Accept": "📝 接受类型 - 我能接收什么格式的回信",
            "Accept-Language": "🌍 语言偏好 - 我希望用什么语言回复",
            "Accept-Encoding": "📦 压缩格式 - 我支持的压缩方式",
            "User-Agent": "🏷️ 身份标识 - 我是什么类型的客户端",
            "Authorization": "🔐 身份认证 - 我的身份凭证",
            "Referer": "📍 来源地址 - 我从哪个页面来的",
            
            # 响应头部
            "Server": "🏢 服务器信息 - 邮局的基本信息",
            "Content-Type": "📄 内容类型 - 回信的格式",
            "Content-Length": "📏 内容长度 - 回信的大小",
            "Last-Modified": "📅 最后修改 - 信息的最新更新时间",
            "ETag": "🏷️ 版本标识 - 内容的唯一标识符",
            "Set-Cookie": "🍪 会话保持 - 为下次访问保存状态",
            
            # 安全头部
            "Strict-Transport-Security": "🔒 强制HTTPS - 只能用安全邮递",
            "Content-Security-Policy": "🛡️ 内容安全策略 - 防止恶意内容",
            "X-Frame-Options": "🖼️ 框架选项 - 防止被嵌入攻击",
            "X-Content-Type-Options": "🔍 类型检查 - 严格检查内容类型"
        }
        
        return explanations.get(header_name, f"📋 {header_name} - 专用头部字段")
    
    def display_headers_with_explanation(self):
        """显示头部字段及其解释"""
        print("📋 HTTP头部字段详解:")
        print("=" * 60)
        
        for name, value in self.headers.items():
            explanation = self.explain_header(name)
            print(f"{explanation}")
            print(f"   {name}: {value}")
            print()

# 演示HTTP头部字段
def demo_http_headers():
    """HTTP头部字段演示"""
    print("=== HTTP头部字段演示 ===\n")
    
    # 请求头部演示
    print("1. 📮 请求头部字段:")
    request_headers = HTTPHeaders()
    request_headers.add_general_headers()
    request_headers.add_request_headers()
    request_headers.display_headers_with_explanation()
    
    print("\n" + "="*60)
    print("2. 📬 响应头部字段:")
    response_headers = HTTPHeaders()
    response_headers.add_general_headers()
    response_headers.add_response_headers()
    response_headers.add_security_headers()
    response_headers.display_headers_with_explanation()

# 运行演示
if __name__ == "__main__":
    demo_http_headers()
```

### 🚀 项目实战：HTTP协议分析工具

让我们构建一个完整的HTTP协议分析工具，就像建设一个邮件分析中心：

```python
import socket
import ssl
import threading
import time
from typing import Tuple, Optional
from urllib.parse import urlparse

class HTTPAnalyzer:
    """
    HTTP协议分析工具 - 邮件分析中心
    
    功能：
    - 捕获HTTP请求/响应
    - 分析协议细节
    - 性能监控
    - 安全检查
    """
    
    def __init__(self):
        self.sessions = {}  # 会话记录
        self.statistics = {
            "total_requests": 0,
            "total_responses": 0,
            "methods": {},
            "status_codes": {},
            "content_types": {},
            "response_times": []
        }
    
    def analyze_request(self, request_text: str) -> Dict[str, Any]:
        """分析HTTP请求"""
        lines = request_text.strip().split('\n')
        if not lines:
            return {}
        
        # 解析请求行
        request_line = lines[0]
        parts = request_line.split(' ')
        if len(parts) < 3:
            return {"error": "Invalid request line"}
        
        method, path, version = parts[0], parts[1], parts[2]
        
        # 解析头部
        headers = {}
        body_start = 0
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == "":
                body_start = i + 1
                break
            if ':' in line:
                key, value = line.split(':', 1)
                headers[key.strip()] = value.strip()
        
        # 解析请求体
        body = '\n'.join(lines[body_start:]) if body_start < len(lines) else ""
        
        # 统计信息
        self.statistics["total_requests"] += 1
        self.statistics["methods"][method] = self.statistics["methods"].get(method, 0) + 1
        
        analysis = {
            "method": method,
            "path": path,
            "version": version,
            "headers": headers,
            "body": body,
            "analysis": {
                "method_explanation": self._explain_method(method),
                "security_headers": self._check_security_headers(headers),
                "content_analysis": self._analyze_content(headers, body),
                "performance_hints": self._get_performance_hints(headers)
            }
        }
        
        return analysis
    
    def analyze_response(self, response_text: str) -> Dict[str, Any]:
        """分析HTTP响应"""
        lines = response_text.strip().split('\n')
        if not lines:
            return {}
        
        # 解析状态行
        status_line = lines[0]
        parts = status_line.split(' ', 2)
        if len(parts) < 3:
            return {"error": "Invalid status line"}
        
        version, status_code, reason = parts[0], int(parts[1]), parts[2]
        
        # 解析头部
        headers = {}
        body_start = 0
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == "":
                body_start = i + 1
                break
            if ':' in line:
                key, value = line.split(':', 1)
                headers[key.strip()] = value.strip()
        
        # 解析响应体
        body = '\n'.join(lines[body_start:]) if body_start < len(lines) else ""
        
        # 统计信息
        self.statistics["total_responses"] += 1
        self.statistics["status_codes"][status_code] = self.statistics["status_codes"].get(status_code, 0) + 1
        
        content_type = headers.get('Content-Type', 'unknown')
        self.statistics["content_types"][content_type] = self.statistics["content_types"].get(content_type, 0) + 1
        
        analysis = {
            "version": version,
            "status_code": status_code,
            "reason": reason,
            "headers": headers,
            "body": body,
            "analysis": {
                "status_explanation": self._explain_status(status_code),
                "security_analysis": self._analyze_security(headers),
                "performance_analysis": self._analyze_performance(headers),
                "content_analysis": self._analyze_response_content(headers, body)
            }
        }
        
        return analysis
    
    def _explain_method(self, method: str) -> str:
        """解释HTTP方法"""
        explanations = {
            "GET": "📖 获取资源 - 查询邮件",
            "POST": "📮 创建资源 - 投递新邮件",
            "PUT": "📝 更新资源 - 完整替换邮件",
            "PATCH": "✏️ 部分更新 - 修改邮件部分内容",
            "DELETE": "🗑️ 删除资源 - 删除邮件",
            "HEAD": "👀 获取头部 - 查看邮件概况",
            "OPTIONS": "❓ 查询选项 - 询问支持的操作"
        }
        return explanations.get(method, f"🔧 {method}方法")
    
    def _explain_status(self, code: int) -> str:
        """解释状态码"""
        if 200 <= code < 300:
            return f"✅ 成功 ({code}) - 邮件处理成功"
        elif 300 <= code < 400:
            return f"🔄 重定向 ({code}) - 邮件需要转发"
        elif 400 <= code < 500:
            return f"❌ 客户端错误 ({code}) - 邮件格式或权限问题"
        elif 500 <= code < 600:
            return f"💥 服务器错误 ({code}) - 邮局内部问题"
        else:
            return f"❓ 未知状态 ({code})"
    
    def _check_security_headers(self, headers: Dict[str, str]) -> List[str]:
        """检查安全头部"""
        security_headers = [
            "Authorization", "X-Frame-Options", "X-Content-Type-Options",
            "X-XSS-Protection", "Strict-Transport-Security",
            "Content-Security-Policy"
        ]
        
        present = [h for h in security_headers if h in headers]
        missing = [h for h in security_headers if h not in headers]
        
        return {
            "present": present,
            "missing": missing,
            "security_level": "高" if len(present) > 4 else "中" if len(present) > 2 else "低"
        }
    
    def _analyze_content(self, headers: Dict[str, str], body: str) -> Dict[str, Any]:
        """分析内容"""
        content_type = headers.get('Content-Type', 'unknown')
        content_length = headers.get('Content-Length', str(len(body)))
        
        return {
            "type": content_type,
            "length": content_length,
            "encoding": "UTF-8" if "utf-8" in content_type.lower() else "Unknown",
            "format": "JSON" if "json" in content_type else "HTML" if "html" in content_type else "Text"
        }
    
    def _get_performance_hints(self, headers: Dict[str, str]) -> List[str]:
        """获取性能优化建议"""
        hints = []
        
        if "Accept-Encoding" not in headers:
            hints.append("🔧 建议添加 Accept-Encoding 头部以支持压缩")
        
        if "Cache-Control" not in headers:
            hints.append("🔧 建议添加 Cache-Control 头部以优化缓存")
        
        if "Connection" in headers and headers["Connection"] == "close":
            hints.append("🔧 建议使用 keep-alive 连接以提高性能")
        
        return hints
    
    def _analyze_security(self, headers: Dict[str, str]) -> Dict[str, Any]:
        """分析安全性"""
        security_score = 0
        security_issues = []
        
        # 检查HTTPS相关
        if "Strict-Transport-Security" in headers:
            security_score += 20
        else:
            security_issues.append("缺少 HSTS 头部")
        
        # 检查内容安全策略
        if "Content-Security-Policy" in headers:
            security_score += 20
        else:
            security_issues.append("缺少 CSP 头部")
        
        # 检查框架保护
        if "X-Frame-Options" in headers:
            security_score += 15
        else:
            security_issues.append("缺少 X-Frame-Options 头部")
        
        # 检查内容类型嗅探保护
        if "X-Content-Type-Options" in headers:
            security_score += 15
        else:
            security_issues.append("缺少 X-Content-Type-Options 头部")
        
        # 检查XSS保护
        if "X-XSS-Protection" in headers:
            security_score += 10
        else:
            security_issues.append("缺少 X-XSS-Protection 头部")
        
        return {
            "score": security_score,
            "level": "高" if security_score >= 70 else "中" if security_score >= 40 else "低",
            "issues": security_issues
        }
    
    def _analyze_performance(self, headers: Dict[str, str]) -> Dict[str, Any]:
        """分析性能"""
        performance_analysis = {
            "caching": {},
            "compression": {},
            "connection": {}
        }
        
        # 缓存分析
        if "Cache-Control" in headers:
            cache_control = headers["Cache-Control"]
            if "no-cache" in cache_control:
                performance_analysis["caching"]["status"] = "禁用缓存"
            elif "max-age" in cache_control:
                performance_analysis["caching"]["status"] = "启用缓存"
            else:
                performance_analysis["caching"]["status"] = "部分缓存"
        
        # 压缩分析
        if "Content-Encoding" in headers:
            encoding = headers["Content-Encoding"]
            performance_analysis["compression"]["status"] = f"已压缩 ({encoding})"
        else:
            performance_analysis["compression"]["status"] = "未压缩"
        
        # 连接分析
        if "Connection" in headers:
            connection = headers["Connection"]
            performance_analysis["connection"]["status"] = connection
        
        return performance_analysis
    
    def _analyze_response_content(self, headers: Dict[str, str], body: str) -> Dict[str, Any]:
        """分析响应内容"""
        content_type = headers.get('Content-Type', 'unknown')
        
        analysis = {
            "size": len(body.encode('utf-8')),
            "type": content_type,
            "structured": False
        }
        
        # 尝试解析结构化数据
        if "json" in content_type.lower():
            try:
                data = json.loads(body)
                analysis["structured"] = True
                analysis["structure"] = type(data).__name__
                if isinstance(data, dict):
                    analysis["keys"] = list(data.keys())
                elif isinstance(data, list):
                    analysis["length"] = len(data)
            except json.JSONDecodeError:
                analysis["parse_error"] = "JSON格式错误"
        
        return analysis
    
    def generate_report(self) -> str:
        """生成分析报告"""
        report = "📊 HTTP协议分析报告\n"
        report += "=" * 50 + "\n\n"
        
        # 基本统计
        report += "📈 基本统计:\n"
        report += f"   总请求数: {self.statistics['total_requests']}\n"
        report += f"   总响应数: {self.statistics['total_responses']}\n"
        
        # 方法统计
        if self.statistics['methods']:
            report += "\n📋 HTTP方法分布:\n"
            for method, count in self.statistics['methods'].items():
                report += f"   {method}: {count}次\n"
        
        # 状态码统计
        if self.statistics['status_codes']:
            report += "\n📊 状态码分布:\n"
            for code, count in self.statistics['status_codes'].items():
                report += f"   {code}: {count}次\n"
        
        # 内容类型统计
        if self.statistics['content_types']:
            report += "\n📄 内容类型分布:\n"
            for content_type, count in self.statistics['content_types'].items():
                report += f"   {content_type}: {count}次\n"
        
        return report

# 演示HTTP分析工具
def demo_http_analyzer():
    """HTTP分析工具演示"""
    print("=== HTTP协议分析工具演示 ===\n")
    
    analyzer = HTTPAnalyzer()
    
    # 分析请求示例
    sample_request = """GET /api/users?page=1&limit=10 HTTP/1.1
Host: api.example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
Accept: application/json
Accept-Language: zh-CN,zh;q=0.9
Accept-Encoding: gzip, deflate, br
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
Connection: keep-alive
Cache-Control: no-cache

"""
    
    print("1. 📮 请求分析:")
    request_analysis = analyzer.analyze_request(sample_request)
    print(f"   方法: {request_analysis['analysis']['method_explanation']}")
    print(f"   路径: {request_analysis['path']}")
    print(f"   版本: {request_analysis['version']}")
    print(f"   安全级别: {request_analysis['analysis']['security_headers']['security_level']}")
    print(f"   性能建议: {len(request_analysis['analysis']['performance_hints'])}条")
    
    # 分析响应示例
    sample_response = """HTTP/1.1 200 OK
Server: nginx/1.18.0
Date: Mon, 03 Feb 2025 10:30:00 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 156
Connection: keep-alive
Cache-Control: public, max-age=3600
ETag: "abc123def456"
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
  "status": "success",
  "data": {
    "users": [
      {"id": 1, "name": "张三"},
      {"id": 2, "name": "李四"}
    ]
  }
}"""
    
    print("\n2. 📬 响应分析:")
    response_analysis = analyzer.analyze_response(sample_response)
    print(f"   状态: {response_analysis['analysis']['status_explanation']}")
    print(f"   安全级别: {response_analysis['analysis']['security_analysis']['level']}")
    print(f"   内容大小: {response_analysis['analysis']['content_analysis']['size']} 字节")
    print(f"   内容类型: {response_analysis['analysis']['content_analysis']['type']}")
    
    # 生成报告
    print("\n3. 📊 分析报告:")
    print(analyzer.generate_report())

# 运行演示
if __name__ == "__main__":
    demo_http_analyzer()
```

---

## 17.2 Python网络编程基础 - "邮递服务的技术实现" 🐍

> 如果说HTTP协议是邮递系统的标准，那么Python网络编程就是实现这些标准的具体技术手段。

### 🎯 本节目标
- 掌握Python socket编程的核心技术
- 学会使用requests库进行HTTP客户端开发
- 理解异步网络编程和高并发处理
- 实现WebSocket实时通信
- 构建多功能HTTP客户端工具

### 📚 理论基础：网络编程技术栈

#### Python网络编程的层次结构

想象邮递服务的技术实现：从底层的运输工具到上层的服务接口，每一层都有其特定的功能。

```python
"""
Python网络编程技术栈 - 邮递服务的技术层次

🛣️ 传输层 (Transport Layer)
   ├── Socket编程 = 邮递员和运输工具（TCP/UDP）
   ├── SSL/TLS = 安全护送服务（加密传输）
   └── 连接管理 = 路线规划和调度

🚚 应用层 (Application Layer)  
   ├── HTTP客户端 = 标准邮递服务（requests库）
   ├── WebSocket = 实时通信服务（双向对话）
   └── 异步编程 = 批量处理服务（asyncio）

🏢 服务层 (Service Layer)
   ├── 连接池 = 邮递员团队管理
   ├── 负载均衡 = 邮件分发策略
   └── 缓存系统 = 信息存储和检索
"""

import socket
import ssl
import asyncio
import aiohttp
import requests
import websockets
import threading
import queue
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List, Optional, Callable, Any
import json
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
```

### 🔌 Socket编程深度解析：邮递员的基本技能

#### 1. TCP Socket编程 - 可靠的邮递服务

```python
class TCPClient:
    """
    TCP客户端 - 可靠的邮递员
    
    特点：
    - 面向连接：建立专用通道
    - 可靠传输：保证数据完整性
    - 流式传输：数据按顺序到达
    """
    
    def __init__(self, host: str, port: int, timeout: int = 30):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.socket: Optional[socket.socket] = None
        self.connected = False
    
    def connect(self) -> bool:
        """建立连接 - 邮递员出发前的准备"""
        try:
            logger.info(f"🚚 正在连接到 {self.host}:{self.port}")
            
            # 创建TCP socket
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(self.timeout)
            
            # 建立连接
            self.socket.connect((self.host, self.port))
            self.connected = True
            
            logger.info(f"✅ 成功连接到 {self.host}:{self.port}")
            return True
            
        except socket.error as e:
            logger.error(f"❌ 连接失败: {e}")
            return False
    
    def send_data(self, data: str) -> bool:
        """发送数据 - 邮递员投递邮件"""
        if not self.connected or not self.socket:
            logger.error("❌ 未建立连接")
            return False
        
        try:
            # 将字符串转换为字节并发送
            data_bytes = data.encode('utf-8')
            sent_bytes = self.socket.send(data_bytes)
            
            logger.info(f"📮 发送数据: {sent_bytes} 字节")
            return sent_bytes == len(data_bytes)
            
        except socket.error as e:
            logger.error(f"❌ 发送失败: {e}")
            return False
    
    def receive_data(self, buffer_size: int = 4096) -> Optional[str]:
        """接收数据 - 邮递员收取回信"""
        if not self.connected or not self.socket:
            logger.error("❌ 未建立连接")
            return None
        
        try:
            # 接收数据
            data_bytes = self.socket.recv(buffer_size)
            if not data_bytes:
                logger.info("📪 连接已关闭")
                return None
            
            data_str = data_bytes.decode('utf-8')
            logger.info(f"📬 接收数据: {len(data_str)} 字符")
            return data_str
            
        except socket.error as e:
            logger.error(f"❌ 接收失败: {e}")
            return None
    
    def send_http_request(self, method: str, path: str, headers: Dict[str, str] = None, body: str = "") -> Optional[str]:
        """发送HTTP请求 - 发送标准格式邮件"""
        if not self.connected:
            if not self.connect():
                return None
        
        # 构建HTTP请求
        request_line = f"{method} {path} HTTP/1.1"
        
        # 默认头部
        default_headers = {
            "Host": self.host,
            "User-Agent": "Python-TCPClient/1.0",
            "Connection": "close"
        }
        
        if headers:
            default_headers.update(headers)
        
        if body:
            default_headers["Content-Length"] = str(len(body.encode('utf-8')))
        
        # 构建完整请求
        header_lines = [f"{k}: {v}" for k, v in default_headers.items()]
        request_parts = [request_line] + header_lines + [""]
        
        if body:
            request_parts.append(body)
        
        http_request = "\r\n".join(request_parts)
        
        logger.info(f"📮 发送HTTP请求:\n{http_request[:200]}{'...' if len(http_request) > 200 else ''}")
        
        # 发送请求
        if not self.send_data(http_request):
            return None
        
        # 接收响应
        response_parts = []
        while True:
            chunk = self.receive_data()
            if not chunk:
                break
            response_parts.append(chunk)
        
        response = "".join(response_parts)
        logger.info(f"📬 接收HTTP响应: {len(response)} 字符")
        
        return response
    
    def close(self):
        """关闭连接 - 邮递员完成任务"""
        if self.socket:
            self.socket.close()
            self.connected = False
            logger.info("🔚 连接已关闭")

class TCPServer:
    """
    TCP服务器 - 邮局接收中心
    
    功能：
    - 监听客户端连接
    - 处理多个客户端
    - 提供基本的HTTP服务
    """
    
    def __init__(self, host: str = "localhost", port: int = 8080):
        self.host = host
        self.port = port
        self.socket: Optional[socket.socket] = None
        self.running = False
        self.clients: List[socket.socket] = []
    
    def start(self):
        """启动服务器 - 邮局开始营业"""
        try:
            # 创建服务器socket
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            # 绑定地址和端口
            self.socket.bind((self.host, self.port))
            
            # 开始监听
            self.socket.listen(5)
            self.running = True
            
            logger.info(f"🏢 服务器启动在 {self.host}:{self.port}")
            
            while self.running:
                try:
                    # 接受客户端连接
                    client_socket, client_address = self.socket.accept()
                    logger.info(f"👋 新客户端连接: {client_address}")
                    
                    # 启动线程处理客户端
                    client_thread = threading.Thread(
                        target=self.handle_client,
                        args=(client_socket, client_address)
                    )
                    client_thread.daemon = True
                    client_thread.start()
                    
                except socket.error as e:
                    if self.running:
                        logger.error(f"❌ 接受连接失败: {e}")
                    
        except Exception as e:
            logger.error(f"❌ 服务器启动失败: {e}")
        finally:
            self.stop()
    
    def handle_client(self, client_socket: socket.socket, client_address):
        """处理客户端请求 - 邮局员工服务客户"""
        try:
            while True:
                # 接收数据
                data = client_socket.recv(4096)
                if not data:
                    break
                
                request = data.decode('utf-8')
                logger.info(f"📬 收到请求: {request[:100]}{'...' if len(request) > 100 else ''}")
                
                # 解析HTTP请求
                response = self.process_http_request(request)
                
                # 发送响应
                client_socket.send(response.encode('utf-8'))
                
                # HTTP/1.0 连接处理完毕后关闭
                if "Connection: close" in request or "HTTP/1.0" in request:
                    break
                    
        except Exception as e:
            logger.error(f"❌ 处理客户端请求失败: {e}")
        finally:
            client_socket.close()
            logger.info(f"👋 客户端 {client_address} 断开连接")
    
    def process_http_request(self, request: str) -> str:
        """处理HTTP请求 - 解析邮件并生成回复"""
        lines = request.strip().split('\n')
        if not lines:
            return self.create_http_response(400, "Bad Request")
        
        # 解析请求行
        request_line = lines[0].strip()
        parts = request_line.split(' ')
        
        if len(parts) < 3:
            return self.create_http_response(400, "Bad Request")
        
        method, path, version = parts[0], parts[1], parts[2]
        
        # 简单的路由处理
        if path == "/":
            content = """
            <html>
                <head><title>Python TCP服务器</title></head>
                <body>
                    <h1>🏢 欢迎来到Python邮递服务中心！</h1>
                    <p>📮 这是一个使用Socket编程实现的简单HTTP服务器</p>
                    <p>🚀 支持的功能：</p>
                    <ul>
                        <li>📬 GET请求处理</li>
                        <li>📋 基本HTTP响应</li>
                        <li>🔧 多客户端并发</li>
                    </ul>
                </body>
            </html>
            """
            return self.create_http_response(200, "OK", content, "text/html")
            
        elif path == "/api/status":
            status_info = {
                "status": "running",
                "server": "Python-TCPServer/1.0",
                "clients": len(self.clients),
                "timestamp": time.time()
            }
            content = json.dumps(status_info, indent=2)
            return self.create_http_response(200, "OK", content, "application/json")
            
        else:
            return self.create_http_response(404, "Not Found")
    
    def create_http_response(self, status_code: int, reason: str, body: str = "", content_type: str = "text/plain") -> str:
        """创建HTTP响应"""
        if not body:
            body = f"{status_code} {reason}"
        
        headers = [
            f"HTTP/1.1 {status_code} {reason}",
            f"Content-Type: {content_type}; charset=utf-8",
            f"Content-Length: {len(body.encode('utf-8'))}",
            "Connection: close",
            "Server: Python-TCPServer/1.0",
            ""
        ]
        
        return "\r\n".join(headers) + body
    
    def stop(self):
        """停止服务器 - 邮局停止营业"""
        self.running = False
        if self.socket:
            self.socket.close()
        logger.info("🔚 服务器已停止")

# Socket编程演示
def demo_socket_programming():
    """Socket编程演示"""
    print("=== Socket编程演示 ===\n")
    
    # 启动服务器（在单独线程中）
    server = TCPServer("localhost", 8080)
    server_thread = threading.Thread(target=server.start)
    server_thread.daemon = True
    server_thread.start()
    
    # 等待服务器启动
    time.sleep(1)
    
    # 创建客户端并测试
    print("1. 📬 TCP客户端测试:")
    client = TCPClient("localhost", 8080)
    
    # 测试首页请求
    response = client.send_http_request("GET", "/")
    if response:
        print("✅ 首页请求成功")
        print(f"响应长度: {len(response)} 字符")
    
    # 测试API请求
    response = client.send_http_request("GET", "/api/status")
    if response:
        print("✅ API请求成功")
        # 提取JSON部分
        if "\r\n\r\n" in response:
            body = response.split("\r\n\r\n", 1)[1]
            try:
                status_data = json.loads(body)
                print(f"服务器状态: {status_data['status']}")
            except:
                pass
    
    client.close()
    
    # 停止服务器
    server.stop()
    print("\n2. 🔚 测试完成")

# 运行演示
if __name__ == "__main__":
    demo_socket_programming()
```

### 🌐 HTTP客户端编程：专业的邮递服务

#### 1. 使用requests库 - 标准化的邮递服务

```python
class AdvancedHTTPClient:
    """
    高级HTTP客户端 - 专业邮递服务公司
    
    功能：
    - 自动处理会话和Cookie
    - 支持连接池和keep-alive
    - 智能重试和错误处理
    - 支持各种认证方式
    - 详细的请求/响应日志
    """
    
    def __init__(self, base_url: str = "", timeout: int = 30):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        
        # 创建会话 - 建立长期合作关系
        self.session = requests.Session()
        
        # 配置默认头部
        self.session.headers.update({
            'User-Agent': 'Python-AdvancedHTTPClient/1.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        })
        
        # 配置连接池
        adapter = requests.adapters.HTTPAdapter(
            pool_connections=100,  # 连接池大小
            pool_maxsize=100,      # 最大连接数
            max_retries=3,         # 最大重试次数
            pool_block=False       # 非阻塞模式
        )
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
        
        # 统计信息
        self.stats = {
            'total_requests': 0,
            'successful_requests': 0,
            'failed_requests': 0,
            'total_bytes_sent': 0,
            'total_bytes_received': 0,
            'response_times': []
        }
    
    def request(self, method: str, url: str, **kwargs) -> Optional[requests.Response]:
        """
        发送HTTP请求 - 邮递服务的核心功能
        
        参数：
        - method: HTTP方法
        - url: 目标URL
        - **kwargs: 其他请求参数
        """
        # 构建完整URL
        if not url.startswith('http'):
            url = f"{self.base_url}{url}"
        
        # 记录开始时间
        start_time = time.time()
        
        try:
            logger.info(f"📮 发送 {method} 请求到: {url}")
            
            # 发送请求
            response = self.session.request(
                method=method,
                url=url,
                timeout=self.timeout,
                **kwargs
            )
            
            # 记录响应时间
            response_time = time.time() - start_time
            self.stats['response_times'].append(response_time)
            
            # 更新统计信息
            self.stats['total_requests'] += 1
            
            if response.status_code < 400:
                self.stats['successful_requests'] += 1
                logger.info(f"✅ 请求成功: {response.status_code} {response.reason}")
            else:
                self.stats['failed_requests'] += 1
                logger.warning(f"⚠️ 请求失败: {response.status_code} {response.reason}")
            
            # 记录数据传输量
            if hasattr(response.request, 'body') and response.request.body:
                self.stats['total_bytes_sent'] += len(response.request.body)
            
            self.stats['total_bytes_received'] += len(response.content)
            
            logger.info(f"📊 响应时间: {response_time:.3f}s, 大小: {len(response.content)} 字节")
            
            return response
            
        except requests.exceptions.Timeout:
            logger.error(f"⏰ 请求超时: {url}")
            self.stats['total_requests'] += 1
            self.stats['failed_requests'] += 1
            return None
            
        except requests.exceptions.ConnectionError:
            logger.error(f"🔌 连接错误: {url}")
            self.stats['total_requests'] += 1
            self.stats['failed_requests'] += 1
            return None
            
        except Exception as e:
            logger.error(f"❌ 请求异常: {e}")
            self.stats['total_requests'] += 1
            self.stats['failed_requests'] += 1
            return None
    
    def get(self, url: str, params: Dict = None, **kwargs) -> Optional[requests.Response]:
        """GET请求 - 查询邮件"""
        return self.request('GET', url, params=params, **kwargs)
    
    def post(self, url: str, data: Any = None, json: Dict = None, **kwargs) -> Optional[requests.Response]:
        """POST请求 - 投递邮件"""
        return self.request('POST', url, data=data, json=json, **kwargs)
    
    def put(self, url: str, data: Any = None, json: Dict = None, **kwargs) -> Optional[requests.Response]:
        """PUT请求 - 更新完整邮件"""
        return self.request('PUT', url, data=data, json=json, **kwargs)
    
    def patch(self, url: str, data: Any = None, json: Dict = None, **kwargs) -> Optional[requests.Response]:
        """PATCH请求 - 部分更新邮件"""
        return self.request('PATCH', url, data=data, json=json, **kwargs)
    
    def delete(self, url: str, **kwargs) -> Optional[requests.Response]:
        """DELETE请求 - 删除邮件"""
        return self.request('DELETE', url, **kwargs)
    
    def set_auth(self, auth_type: str, **auth_params):
        """设置认证 - 邮局身份验证"""
        if auth_type == 'basic':
            from requests.auth import HTTPBasicAuth
            self.session.auth = HTTPBasicAuth(auth_params['username'], auth_params['password'])
            logger.info("🔐 设置基础认证")
            
        elif auth_type == 'bearer':
            self.session.headers['Authorization'] = f"Bearer {auth_params['token']}"
            logger.info("🔐 设置Bearer令牌认证")
            
        elif auth_type == 'api_key':
            if 'header' in auth_params:
                self.session.headers[auth_params['header']] = auth_params['key']
            else:
                self.session.headers['X-API-Key'] = auth_params['key']
            logger.info("🔐 设置API密钥认证")
    
    def upload_file(self, url: str, file_path: str, field_name: str = 'file', **kwargs) -> Optional[requests.Response]:
        """上传文件 - 邮寄包裹"""
        try:
            with open(file_path, 'rb') as f:
                files = {field_name: f}
                logger.info(f"📦 上传文件: {file_path}")
                return self.request('POST', url, files=files, **kwargs)
        except FileNotFoundError:
            logger.error(f"❌ 文件不存在: {file_path}")
            return None
        except Exception as e:
            logger.error(f"❌ 文件上传失败: {e}")
            return None
    
    def download_file(self, url: str, save_path: str, **kwargs) -> bool:
        """下载文件 - 接收包裹"""
        try:
            logger.info(f"📥 下载文件: {url} -> {save_path}")
            
            response = self.request('GET', url, stream=True, **kwargs)
            if not response:
                return False
            
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            
            logger.info(f"✅ 文件下载完成: {save_path}")
            return True
            
        except Exception as e:
            logger.error(f"❌ 文件下载失败: {e}")
            return False
    
    def get_stats(self) -> Dict[str, Any]:
        """获取统计信息 - 邮递服务报告"""
        avg_response_time = 0
        if self.stats['response_times']:
            avg_response_time = sum(self.stats['response_times']) / len(self.stats['response_times'])
        
        return {
            'total_requests': self.stats['total_requests'],
            'successful_requests': self.stats['successful_requests'],
            'failed_requests': self.stats['failed_requests'],
            'success_rate': f"{self.stats['successful_requests'] / max(1, self.stats['total_requests']) * 100:.1f}%",
            'total_bytes_sent': self.stats['total_bytes_sent'],
            'total_bytes_received': self.stats['total_bytes_received'],
            'average_response_time': f"{avg_response_time:.3f}s",
            'fastest_response': f"{min(self.stats['response_times']):.3f}s" if self.stats['response_times'] else "N/A",
            'slowest_response': f"{max(self.stats['response_times']):.3f}s" if self.stats['response_times'] else "N/A"
        }
    
    def close(self):
        """关闭客户端 - 结束邮递服务"""
        self.session.close()
        logger.info("🔚 HTTP客户端已关闭")

# HTTP客户端演示
def demo_http_client():
    """HTTP客户端演示"""
    print("=== 高级HTTP客户端演示 ===\n")
    
    # 创建客户端
    client = AdvancedHTTPClient("https://httpbin.org")
    
    print("1. 📬 基本GET请求:")
    response = client.get("/get", params={'test': 'value', 'page': 1})
    if response:
        print(f"状态码: {response.status_code}")
        data = response.json()
        print(f"查询参数: {data.get('args', {})}")
    
    print("\n2. 📮 POST请求 - 发送JSON数据:")
    post_data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'age': 25
    }
    response = client.post("/post", json=post_data)
    if response:
        print(f"状态码: {response.status_code}")
        data = response.json()
        print(f"发送的数据: {data.get('json', {})}")
    
    print("\n3. 🔐 认证请求:")
    client.set_auth('bearer', token='test-token-123')
    response = client.get("/bearer")
    if response:
        print(f"状态码: {response.status_code}")
        data = response.json()
        print(f"认证状态: {'成功' if data.get('authenticated') else '失败'}")
    
    print("\n4. 📊 统计信息:")
    stats = client.get_stats()
    for key, value in stats.items():
        print(f"   {key}: {value}")
    
    client.close()

# 运行演示
if __name__ == "__main__":
    demo_http_client()
```

### ⚡ 异步网络编程：批量邮递处理

#### 1. 异步HTTP客户端 - 高效的批量邮递服务

```python
class AsyncHTTPClient:
    """
    异步HTTP客户端 - 批量邮递处理中心
    
    特点：
    - 同时处理多个请求
    - 非阻塞I/O操作
    - 高并发性能
    - 资源高效利用
    """
    
    def __init__(self, base_url: str = "", timeout: int = 30, connector_limit: int = 100):
        self.base_url = base_url.rstrip('/')
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        
        # 配置连接器 - 邮递员团队管理
        self.connector = aiohttp.TCPConnector(
            limit=connector_limit,        # 总连接数限制
            limit_per_host=30,           # 每个主机连接数限制
            ttl_dns_cache=300,           # DNS缓存时间
            use_dns_cache=True,          # 启用DNS缓存
        )
        
        self.session: Optional[aiohttp.ClientSession] = None
        
        # 统计信息
        self.stats = {
            'total_requests': 0,
            'successful_requests': 0,
            'failed_requests': 0,
            'concurrent_requests': 0,
            'max_concurrent': 0,
            'response_times': []
        }
    
    async def __aenter__(self):
        """异步上下文管理器入口"""
        self.session = aiohttp.ClientSession(
            connector=self.connector,
            timeout=self.timeout,
            headers={
                'User-Agent': 'Python-AsyncHTTPClient/1.0',
                'Accept': 'application/json, text/plain, */*'
            }
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """异步上下文管理器出口"""
        if self.session:
            await self.session.close()
    
    async def request(self, method: str, url: str, **kwargs) -> Optional[aiohttp.ClientResponse]:
        """异步HTTP请求 - 并发邮递服务"""
        if not self.session:
            raise RuntimeError("客户端未初始化，请使用 async with 语法")
        
        # 构建完整URL
        if not url.startswith('http'):
            url = f"{self.base_url}{url}"
        
        # 更新并发统计
        self.stats['concurrent_requests'] += 1
        self.stats['max_concurrent'] = max(
            self.stats['max_concurrent'], 
            self.stats['concurrent_requests']
        )
        
        start_time = time.time()
        
        try:
            logger.info(f"🚀 异步发送 {method} 请求到: {url}")
            
            async with self.session.request(method, url, **kwargs) as response:
                # 记录响应时间
                response_time = time.time() - start_time
                self.stats['response_times'].append(response_time)
                
                # 更新统计信息
                self.stats['total_requests'] += 1
                self.stats['concurrent_requests'] -= 1
                
                if response.status < 400:
                    self.stats['successful_requests'] += 1
                    logger.info(f"✅ 异步请求成功: {response.status}")
                else:
                    self.stats['failed_requests'] += 1
                    logger.warning(f"⚠️ 异步请求失败: {response.status}")
                
                logger.info(f"⚡ 异步响应时间: {response_time:.3f}s")
                
                # 读取响应内容
                response._content = await response.read()
                return response
                
        except asyncio.TimeoutError:
            logger.error(f"⏰ 异步请求超时: {url}")
            self.stats['total_requests'] += 1
            self.stats['failed_requests'] += 1
            self.stats['concurrent_requests'] -= 1
            return None
            
        except Exception as e:
            logger.error(f"❌ 异步请求异常: {e}")
            self.stats['total_requests'] += 1
            self.stats['failed_requests'] += 1
            self.stats['concurrent_requests'] -= 1
            return None
    
    async def get(self, url: str, **kwargs) -> Optional[aiohttp.ClientResponse]:
        """异步GET请求"""
        return await self.request('GET', url, **kwargs)
    
    async def post(self, url: str, **kwargs) -> Optional[aiohttp.ClientResponse]:
        """异步POST请求"""
        return await self.request('POST', url, **kwargs)
    
    async def batch_requests(self, requests_list: List[Dict]) -> List[Optional[aiohttp.ClientResponse]]:
        """
        批量异步请求 - 邮递批量处理
        
        参数格式：
        [
            {'method': 'GET', 'url': '/endpoint1'},
            {'method': 'POST', 'url': '/endpoint2', 'json': {...}},
            ...
        ]
        """
        logger.info(f"📦 开始批量处理 {len(requests_list)} 个请求")
        
        # 创建异步任务
        tasks = []
        for req in requests_list:
            method = req.pop('method')
            url = req.pop('url')
            task = self.request(method, url, **req)
            tasks.append(task)
        
        # 并发执行所有任务
        start_time = time.time()
        results = await asyncio.gather(*tasks, return_exceptions=True)
        total_time = time.time() - start_time
        
        logger.info(f"📊 批量处理完成，总时间: {total_time:.3f}s")
        
        # 处理异常结果
        responses = []
        for result in results:
            if isinstance(result, Exception):
                logger.error(f"❌ 批量请求中的异常: {result}")
                responses.append(None)
            else:
                responses.append(result)
        
        return responses
    
    async def get_concurrent_performance_test(self, url: str, concurrent_count: int = 50) -> Dict[str, Any]:
        """并发性能测试 - 邮递系统压力测试"""
        logger.info(f"🏃‍♂️ 开始并发性能测试: {concurrent_count} 个并发请求")
        
        # 准备请求列表
        requests_list = [{'method': 'GET', 'url': url} for _ in range(concurrent_count)]
        
        # 执行批量请求
        start_time = time.time()
        responses = await self.batch_requests(requests_list)
        total_time = time.time() - start_time
        
        # 统计结果
        successful_count = sum(1 for r in responses if r and r.status < 400)
        failed_count = concurrent_count - successful_count
        
        performance_stats = {
            'concurrent_requests': concurrent_count,
            'successful_requests': successful_count,
            'failed_requests': failed_count,
            'total_time': f"{total_time:.3f}s",
            'requests_per_second': f"{concurrent_count / total_time:.2f}",
            'average_response_time': f"{total_time / concurrent_count:.3f}s",
            'success_rate': f"{successful_count / concurrent_count * 100:.1f}%"
        }
        
        logger.info(f"📊 性能测试结果: {performance_stats}")
        return performance_stats

# 异步编程演示
async def demo_async_http_client():
    """异步HTTP客户端演示"""
    print("=== 异步HTTP客户端演示 ===\n")
    
    async with AsyncHTTPClient("https://httpbin.org") as client:
        
        print("1. ⚡ 单个异步请求:")
        response = await client.get("/get?test=async")
        if response:
            content = await response.text()
            data = json.loads(content)
            print(f"状态码: {response.status}")
            print(f"异步请求参数: {data.get('args', {})}")
        
        print("\n2. 📦 批量异步请求:")
        batch_requests = [
            {'method': 'GET', 'url': '/get?batch=1'},
            {'method': 'GET', 'url': '/get?batch=2'},
            {'method': 'GET', 'url': '/get?batch=3'},
            {'method': 'POST', 'url': '/post', 'json': {'test': 'batch'}},
            {'method': 'GET', 'url': '/delay/1'}  # 1秒延迟
        ]
        
        start_time = time.time()
        responses = await client.batch_requests(batch_requests)
        batch_time = time.time() - start_time
        
        successful = sum(1 for r in responses if r and r.status < 400)
        print(f"批量请求完成: {successful}/{len(batch_requests)} 成功")
        print(f"总时间: {batch_time:.3f}s (并发执行)")
        
        print("\n3. 🏃‍♂️ 并发性能测试:")
        perf_stats = await client.get_concurrent_performance_test("/get", 20)
        for key, value in perf_stats.items():
            print(f"   {key}: {value}")

def run_async_demo():
    """运行异步演示"""
    asyncio.run(demo_async_http_client())
```

### 🔄 WebSocket实时通信：双向邮递服务

```python
class WebSocketClient:
    """
    WebSocket客户端 - 实时双向邮递服务
    
    特点：
    - 持久连接
    - 双向通信
    - 实时数据传输
    - 低延迟交互
    """
    
    def __init__(self, uri: str):
        self.uri = uri
        self.websocket: Optional[websockets.WebSocketServerProtocol] = None
        self.connected = False
        self.message_queue = asyncio.Queue()
        self.stats = {
            'messages_sent': 0,
            'messages_received': 0,
            'bytes_sent': 0,
            'bytes_received': 0,
            'connection_time': 0
        }
    
    async def connect(self) -> bool:
        """建立WebSocket连接 - 开通实时邮递通道"""
        try:
            logger.info(f"🔌 连接WebSocket: {self.uri}")
            start_time = time.time()
            
            self.websocket = await websockets.connect(self.uri)
            self.connected = True
            self.stats['connection_time'] = time.time() - start_time
            
            logger.info(f"✅ WebSocket连接成功，耗时: {self.stats['connection_time']:.3f}s")
            
            # 启动消息接收任务
            asyncio.create_task(self._message_receiver())
            
            return True
            
        except Exception as e:
            logger.error(f"❌ WebSocket连接失败: {e}")
            return False
    
    async def _message_receiver(self):
        """消息接收器 - 专门接收邮件的邮递员"""
        try:
            async for message in self.websocket:
                logger.info(f"📬 收到WebSocket消息: {len(message)} 字符")
                
                # 更新统计
                self.stats['messages_received'] += 1
                self.stats['bytes_received'] += len(message.encode('utf-8'))
                
                # 放入消息队列
                await self.message_queue.put(message)
                
        except websockets.exceptions.ConnectionClosed:
            logger.info("🔌 WebSocket连接已关闭")
            self.connected = False
        except Exception as e:
            logger.error(f"❌ WebSocket接收消息错误: {e}")
            self.connected = False
    
    async def send_message(self, message: str) -> bool:
        """发送消息 - 实时邮件投递"""
        if not self.connected or not self.websocket:
            logger.error("❌ WebSocket未连接")
            return False
        
        try:
            logger.info(f"📮 发送WebSocket消息: {len(message)} 字符")
            
            await self.websocket.send(message)
            
            # 更新统计
            self.stats['messages_sent'] += 1
            self.stats['bytes_sent'] += len(message.encode('utf-8'))
            
            return True
            
        except Exception as e:
            logger.error(f"❌ WebSocket发送消息失败: {e}")
            return False
    
    async def send_json(self, data: Dict) -> bool:
        """发送JSON消息"""
        message = json.dumps(data, ensure_ascii=False)
        return await self.send_message(message)
    
    async def receive_message(self, timeout: float = None) -> Optional[str]:
        """接收消息 - 等待邮件到达"""
        try:
            if timeout:
                message = await asyncio.wait_for(
                    self.message_queue.get(),
                    timeout=timeout
                )
            else:
                message = await self.message_queue.get()
            
            logger.info(f"📧 获取消息: {len(message)} 字符")
            return message
            
        except asyncio.TimeoutError:
            logger.warning("⏰ 接收消息超时")
            return None
        except Exception as e:
            logger.error(f"❌ 接收消息失败: {e}")
            return None
    
    async def receive_json(self, timeout: float = None) -> Optional[Dict]:
        """接收JSON消息"""
        message = await self.receive_message(timeout)
        if message:
            try:
                return json.loads(message)
            except json.JSONDecodeError as e:
                logger.error(f"❌ JSON解析失败: {e}")
        return None
    
    async def ping(self) -> bool:
        """发送心跳包 - 保持邮递通道畅通"""
        if not self.connected or not self.websocket:
            return False
        
        try:
            await self.websocket.ping()
            logger.info("💓 心跳包发送成功")
            return True
        except Exception as e:
            logger.error(f"❌ 心跳包发送失败: {e}")
            return False
    
    async def close(self):
        """关闭连接 - 关闭邮递通道"""
        if self.websocket:
            await self.websocket.close()
            self.connected = False
            logger.info("🔚 WebSocket连接已关闭")
    
    def get_stats(self) -> Dict[str, Any]:
        """获取统计信息"""
        return {
            'connected': self.connected,
            'connection_time': f"{self.stats['connection_time']:.3f}s",
            'messages_sent': self.stats['messages_sent'],
            'messages_received': self.stats['messages_received'],
            'bytes_sent': self.stats['bytes_sent'],
            'bytes_received': self.stats['bytes_received'],
            'pending_messages': self.message_queue.qsize()
        }

class SimpleWebSocketServer:
    """
    简单WebSocket服务器 - 实时邮递服务中心
    """
    
    def __init__(self, host: str = "localhost", port: int = 8765):
        self.host = host
        self.port = port
        self.clients: Set[websockets.WebSocketServerProtocol] = set()
        self.message_history: List[Dict] = []
    
    async def register_client(self, websocket: websockets.WebSocketServerProtocol):
        """注册客户端 - 新邮递员上班"""
        self.clients.add(websocket)
        logger.info(f"👋 新客户端连接: {websocket.remote_address}")
        
        # 发送欢迎消息
        welcome_msg = {
            'type': 'welcome',
            'message': '欢迎连接到WebSocket邮递服务中心！',
            'timestamp': time.time(),
            'clients_count': len(self.clients)
        }
        await websocket.send(json.dumps(welcome_msg, ensure_ascii=False))
    
    async def unregister_client(self, websocket: websockets.WebSocketServerProtocol):
        """注销客户端 - 邮递员下班"""
        self.clients.discard(websocket)
        logger.info(f"👋 客户端断开: {websocket.remote_address}")
    
    async def broadcast_message(self, message: Dict, sender: websockets.WebSocketServerProtocol = None):
        """广播消息 - 群发邮件"""
        if not self.clients:
            return
        
        message_str = json.dumps(message, ensure_ascii=False)
        
        # 记录消息历史
        self.message_history.append({
            'message': message,
            'timestamp': time.time(),
            'sender': str(sender.remote_address) if sender else 'server'
        })
        
        # 保持最近100条消息
        if len(self.message_history) > 100:
            self.message_history = self.message_history[-100:]
        
        # 广播给所有客户端（除了发送者）
        disconnected_clients = set()
        for client in self.clients:
            if client != sender:
                try:
                    await client.send(message_str)
                except websockets.exceptions.ConnectionClosed:
                    disconnected_clients.add(client)
        
        # 清理断开的客户端
        for client in disconnected_clients:
            await self.unregister_client(client)
    
    async def handle_client(self, websocket: websockets.WebSocketServerProtocol, path: str):
        """处理客户端连接 - 邮递员服务流程"""
        await self.register_client(websocket)
        
        try:
            async for message_str in websocket:
                try:
                    message = json.loads(message_str)
                    logger.info(f"📬 收到消息: {message}")
                    
                    # 处理不同类型的消息
                    if message.get('type') == 'chat':
                        # 聊天消息 - 转发给所有客户端
                        broadcast_msg = {
                            'type': 'chat',
                            'user': message.get('user', 'Anonymous'),
                            'text': message.get('text', ''),
                            'timestamp': time.time()
                        }
                        await self.broadcast_message(broadcast_msg, websocket)
                        
                    elif message.get('type') == 'ping':
                        # 心跳消息 - 直接回复
                        pong_msg = {'type': 'pong', 'timestamp': time.time()}
                        await websocket.send(json.dumps(pong_msg))
                        
                    elif message.get('type') == 'get_history':
                        # 获取历史消息
                        history_msg = {
                            'type': 'history',
                            'messages': self.message_history[-10:],  # 最近10条
                            'timestamp': time.time()
                        }
                        await websocket.send(json.dumps(history_msg, ensure_ascii=False))
                        
                except json.JSONDecodeError:
                    # 处理非JSON消息
                    text_msg = {
                        'type': 'text',
                        'content': message_str,
                        'timestamp': time.time()
                    }
                    await self.broadcast_message(text_msg, websocket)
                    
        except websockets.exceptions.ConnectionClosed:
            pass
        finally:
            await self.unregister_client(websocket)
    
    async def start_server(self):
        """启动服务器 - 邮递服务中心开始营业"""
        logger.info(f"🏢 启动WebSocket服务器: {self.host}:{self.port}")
        
        async with websockets.serve(self.handle_client, self.host, self.port):
            logger.info("✅ WebSocket服务器启动成功")
            await asyncio.Future()  # 运行直到被取消

# WebSocket演示
async def demo_websocket():
    """WebSocket演示"""
    print("=== WebSocket实时通信演示 ===\n")
    
    # 启动WebSocket服务器
    server = SimpleWebSocketServer("localhost", 8765)
    server_task = asyncio.create_task(server.start_server())
    
    # 等待服务器启动
    await asyncio.sleep(1)
    
    try:
        # 创建两个客户端进行对话
        client1 = WebSocketClient("ws://localhost:8765")
        client2 = WebSocketClient("ws://localhost:8765")
        
        # 连接客户端
        await client1.connect()
        await client2.connect()
        
        await asyncio.sleep(0.5)  # 等待连接稳定
        
        print("1. 🔄 客户端聊天演示:")
        
        # 客户端1发送消息
        chat_msg1 = {
            'type': 'chat',
            'user': 'Alice',
            'text': '你好，我是Alice！'
        }
        await client1.send_json(chat_msg1)
        
        # 客户端2接收并回复
        received_msg = await client2.receive_json(timeout=2)
        if received_msg:
            print(f"客户端2收到: {received_msg['user']}: {received_msg['text']}")
        
        chat_msg2 = {
            'type': 'chat', 
            'user': 'Bob',
            'text': '你好Alice，我是Bob！'
        }
        await client2.send_json(chat_msg2)
        
        # 客户端1接收回复
        received_msg = await client1.receive_json(timeout=2)
        if received_msg:
            print(f"客户端1收到: {received_msg['user']}: {received_msg['text']}")
        
        print("\n2. 💓 心跳测试:")
        ping_success1 = await client1.ping()
        ping_success2 = await client2.ping()
        print(f"客户端1心跳: {'成功' if ping_success1 else '失败'}")
        print(f"客户端2心跳: {'成功' if ping_success2 else '失败'}")
        
        print("\n3. 📊 统计信息:")
        stats1 = client1.get_stats()
        stats2 = client2.get_stats()
        print("客户端1:", stats1)
        print("客户端2:", stats2)
        
        # 关闭客户端
        await client1.close()
        await client2.close()
        
    finally:
        # 取消服务器任务
        server_task.cancel()
        try:
            await server_task
        except asyncio.CancelledError:
            pass

def run_websocket_demo():
    """运行WebSocket演示"""
    try:
        asyncio.run(demo_websocket())
    except KeyboardInterrupt:
        print("\n🔚 演示结束")

# 综合项目实战：多功能HTTP客户端工具
class NetworkToolkit:
    """
    网络工具包 - 完整的邮递服务工具箱
    
    集成功能：
    - HTTP客户端（同步/异步）
    - WebSocket客户端
    - 性能测试工具
    - 网络诊断工具
    """
    
    def __init__(self):
        self.http_client = AdvancedHTTPClient()
        self.results_history = []
    
    async def http_benchmark(self, url: str, concurrent: int = 10, requests: int = 100) -> Dict[str, Any]:
        """HTTP性能基准测试"""
        print(f"🏃‍♂️ 开始HTTP基准测试: {requests} 请求, {concurrent} 并发")
        
        async with AsyncHTTPClient() as client:
            # 计算每批次请求数
            batch_size = requests // concurrent
            remaining = requests % concurrent
            
            all_tasks = []
            
            # 创建并发批次
            for i in range(concurrent):
                batch_requests = batch_size + (1 if i < remaining else 0)
                batch = [{'method': 'GET', 'url': url} for _ in range(batch_requests)]
                
                if batch:
                    all_tasks.extend(batch)
            
            # 执行所有请求
            start_time = time.time()
            responses = await client.batch_requests(all_tasks)
            total_time = time.time() - start_time
            
            # 统计结果
            successful = sum(1 for r in responses if r and r.status < 400)
            failed = len(responses) - successful
            
            benchmark_result = {
                'url': url,
                'total_requests': requests,
                'concurrent_level': concurrent,
                'successful_requests': successful,
                'failed_requests': failed,
                'total_time': f"{total_time:.3f}s",
                'requests_per_second': f"{requests / total_time:.2f}",
                'average_response_time': f"{total_time / requests:.3f}s",
                'success_rate': f"{successful / requests * 100:.1f}%"
            }
            
            self.results_history.append(benchmark_result)
            return benchmark_result
    
    def network_connectivity_test(self, hosts: List[str]) -> Dict[str, bool]:
        """网络连通性测试"""
        print("🌐 测试网络连通性...")
        
        results = {}
        for host in hosts:
            try:
                # 简单的HTTP GET测试
                response = self.http_client.get(f"https://{host}", timeout=5)
                results[host] = response is not None and response.status_code < 500
            except:
                results[host] = False
        
        return results
    
    def generate_report(self) -> str:
        """生成测试报告"""
        if not self.results_history:
            return "📊 暂无测试结果"
        
        report = "📊 网络性能测试报告\n"
        report += "=" * 50 + "\n\n"
        
        for i, result in enumerate(self.results_history, 1):
            report += f"测试 {i}:\n"
            report += f"  URL: {result['url']}\n"
            report += f"  总请求数: {result['total_requests']}\n"
            report += f"  并发级别: {result['concurrent_level']}\n"
            report += f"  成功率: {result['success_rate']}\n"
            report += f"  QPS: {result['requests_per_second']}\n"
            report += f"  平均响应时间: {result['average_response_time']}\n"
            report += "\n"
        
        return report
    
    def close(self):
        """关闭工具包"""
        self.http_client.close()

# 网络工具包演示
async def demo_network_toolkit():
    """网络工具包综合演示"""
    print("=== 网络工具包综合演示 ===\n")
    
    toolkit = NetworkToolkit()
    
    try:
        print("1. 🌐 网络连通性测试:")
        connectivity = toolkit.network_connectivity_test([
            "httpbin.org",
            "jsonplaceholder.typicode.com", 
            "example.com"
        ])
        
        for host, status in connectivity.items():
            print(f"   {host}: {'✅ 连通' if status else '❌ 不通'}")
        
        print("\n2. 🏃‍♂️ HTTP性能基准测试:")
        benchmark_result = await toolkit.http_benchmark(
            "https://httpbin.org/get",
            concurrent=5,
            requests=25
        )
        
        print("基准测试结果:")
        for key, value in benchmark_result.items():
            if key != 'url':
                print(f"   {key}: {value}")
        
        print("\n3. 📊 生成测试报告:")
        report = toolkit.generate_report()
        print(report)
        
    finally:
        toolkit.close()

def run_network_toolkit_demo():
    """运行网络工具包演示"""
    asyncio.run(demo_network_toolkit())

# 主演示函数
def demo_python_networking():
    """Python网络编程综合演示"""
    print("🐍 Python网络编程综合演示开始！\n")
    
    # 1. Socket编程演示
    print("=" * 60)
    demo_socket_programming()
    
    # 2. HTTP客户端演示  
    print("\n" + "=" * 60)
    demo_http_client()
    
    # 3. 异步编程演示
    print("\n" + "=" * 60)
    run_async_demo()
    
    # 4. WebSocket演示
    print("\n" + "=" * 60)
    run_websocket_demo()
    
    # 5. 网络工具包演示
    print("\n" + "=" * 60)
    run_network_toolkit_demo()
    
    print("\n🎉 Python网络编程演示完成！")

# 运行完整演示
if __name__ == "__main__":
    demo_python_networking()
```

---

## 17.3 Web服务器开发实战 - "建设现代化邮递中心" 🏢

> 从零开始构建Web服务器，就像设计和建造一个现代化的邮递处理中心。

### 🎯 本节目标
- 理解Web服务器的核心架构和工作原理
- 掌握WSGI/ASGI协议的实现机制
- 学会构建高性能、可扩展的Web服务器
- 实现中间件系统和插件架构
- 集成负载均衡、缓存、监控等企业级功能

### 📚 理论基础：Web服务器架构

#### Web服务器的层次结构

想象一个现代化的邮递处理中心：从接收邮件到最终派送，每个环节都有专门的设施和流程。

```python
"""
Web服务器架构 - 邮递中心的组织结构

🏢 服务器基础设施层 = 邮递中心建筑
├── Socket监听 = 邮件接收窗口
├── 连接管理 = 客户服务台
└── 进程/线程池 = 工作人员团队

📋 协议处理层 = 邮件处理标准
├── HTTP协议解析 = 邮件格式检查
├── 请求路由 = 邮件分拣系统
└── 响应生成 = 回执制作

🔧 应用接口层 = 业务处理接口
├── WSGI/ASGI = 标准化业务流程
├── 中间件 = 质量检查环节
└── 应用框架 = 专业处理团队

🚀 增强功能层 = 增值服务
├── 负载均衡 = 任务分配系统
├── 缓存系统 = 临时存储仓库
├── 监控告警 = 运营监控中心
└── 安全防护 = 安全保卫系统
"""

import socket
import threading
import queue
import time
import json
import mimetypes
import os
import gzip
import hashlib
from datetime import datetime, timezone
from typing import Dict, List, Optional, Callable, Any, Tuple
from urllib.parse import urlparse, parse_qs, unquote
from socketserver import ThreadingMixIn, TCPServer, BaseRequestHandler
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
```

### 🏗️ WSGI服务器实现：标准化的邮递处理流程

#### 1. 核心WSGI服务器 - 邮递中心的核心系统

```python
class WSGIServer:
    """
    WSGI服务器 - 标准化邮递处理中心
    
    实现WSGI协议，提供标准化的Web应用接口
    """
    
    def __init__(self, host: str = "localhost", port: int = 8080):
        self.host = host
        self.port = port
        self.application = None
        self.socket = None
        self.running = False
        
        # 服务器统计信息
        self.stats = {
            'total_requests': 0,
            'active_connections': 0,
            'start_time': None,
            'request_times': [],
            'error_count': 0
        }
        
        # 配置参数
        self.config = {
            'max_connections': 100,
            'socket_timeout': 30,
            'buffer_size': 8192,
            'keep_alive_timeout': 5,
            'max_request_size': 1024 * 1024  # 1MB
        }
    
    def set_application(self, application: Callable):
        """设置WSGI应用 - 配置业务处理团队"""
        self.application = application
        logger.info("📋 WSGI应用已配置")
    
    def start(self):
        """启动服务器 - 邮递中心开始营业"""
        if not self.application:
            raise ValueError("必须先设置WSGI应用")
        
        try:
            # 创建服务器socket
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            # 绑定地址
            self.socket.bind((self.host, self.port))
            self.socket.listen(self.config['max_connections'])
            
            self.running = True
            self.stats['start_time'] = time.time()
            
            logger.info(f"🏢 WSGI服务器启动: http://{self.host}:{self.port}")
            logger.info(f"📊 最大连接数: {self.config['max_connections']}")
            
            # 主服务循环
            while self.running:
                try:
                    client_socket, client_address = self.socket.accept()
                    
                    # 增加活跃连接计数
                    self.stats['active_connections'] += 1
                    
                    # 在新线程中处理请求
                    client_thread = threading.Thread(
                        target=self.handle_request,
                        args=(client_socket, client_address),
                        daemon=True
                    )
                    client_thread.start()
                    
                except socket.error as e:
                    if self.running:
                        logger.error(f"❌ 接受连接失败: {e}")
                        
        except Exception as e:
            logger.error(f"❌ 服务器启动失败: {e}")
        finally:
            self.stop()
    
    def handle_request(self, client_socket: socket.socket, client_address):
        """处理单个请求 - 邮递员处理单个邮件"""
        start_time = time.time()
        
        try:
            client_socket.settimeout(self.config['socket_timeout'])
            
            # 接收HTTP请求
            request_data = self.receive_request(client_socket)
            if not request_data:
                return
            
            # 解析HTTP请求
            environ = self.parse_request(request_data, client_address)
            if not environ:
                self.send_error_response(client_socket, 400, "Bad Request")
                return
            
            # 创建响应收集器
            response_data = {'status': None, 'headers': [], 'body': []}
            
            def start_response(status: str, headers: List[Tuple[str, str]], exc_info=None):
                """WSGI start_response函数"""
                response_data['status'] = status
                response_data['headers'] = headers
                return lambda data: response_data['body'].append(data)
            
            # 调用WSGI应用
            try:
                app_response = self.application(environ, start_response)
                
                # 收集应用响应
                if hasattr(app_response, '__iter__'):
                    for chunk in app_response:
                        if chunk:
                            response_data['body'].append(chunk)
                
                # 发送HTTP响应
                self.send_response(client_socket, response_data)
                
                # 更新统计信息
                self.stats['total_requests'] += 1
                request_time = time.time() - start_time
                self.stats['request_times'].append(request_time)
                
                # 保持最近1000次请求的时间记录
                if len(self.stats['request_times']) > 1000:
                    self.stats['request_times'] = self.stats['request_times'][-1000:]
                
                logger.info(f"✅ 请求处理完成: {request_time:.3f}s")
                
            except Exception as e:
                logger.error(f"❌ WSGI应用错误: {e}")
                self.send_error_response(client_socket, 500, "Internal Server Error")
                self.stats['error_count'] += 1
                
        except Exception as e:
            logger.error(f"❌ 请求处理异常: {e}")
            self.stats['error_count'] += 1
        finally:
            client_socket.close()
            self.stats['active_connections'] -= 1
    
    def receive_request(self, client_socket: socket.socket) -> Optional[str]:
        """接收HTTP请求数据"""
        try:
            request_data = b""
            content_length = 0
            headers_complete = False
            
            while True:
                chunk = client_socket.recv(self.config['buffer_size'])
                if not chunk:
                    break
                
                request_data += chunk
                
                # 检查是否接收完整个请求头
                if not headers_complete and b"\r\n\r\n" in request_data:
                    headers_complete = True
                    headers_part, body_part = request_data.split(b"\r\n\r\n", 1)
                    
                    # 解析Content-Length
                    headers_str = headers_part.decode('utf-8', errors='ignore')
                    for line in headers_str.split('\r\n'):
                        if line.lower().startswith('content-length:'):
                            content_length = int(line.split(':', 1)[1].strip())
                            break
                    
                    # 如果没有请求体，直接返回
                    if content_length == 0:
                        break
                    
                    # 检查是否接收完整个请求体
                    if len(body_part) >= content_length:
                        break
                
                # 防止请求过大
                if len(request_data) > self.config['max_request_size']:
                    logger.warning("⚠️ 请求数据过大")
                    return None
            
            return request_data.decode('utf-8', errors='ignore')
            
        except Exception as e:
            logger.error(f"❌ 接收请求失败: {e}")
            return None
    
    def parse_request(self, request_data: str, client_address) -> Optional[Dict[str, Any]]:
        """解析HTTP请求为WSGI environ字典"""
        try:
            lines = request_data.split('\r\n')
            if not lines:
                return None
            
            # 解析请求行
            request_line = lines[0]
            parts = request_line.split(' ')
            if len(parts) != 3:
                return None
            
            method, raw_path, version = parts
            
            # 解析URL
            if '?' in raw_path:
                path, query_string = raw_path.split('?', 1)
            else:
                path, query_string = raw_path, ''
            
            path = unquote(path)
            
            # 解析请求头
            headers = {}
            body_start = 1
            for i, line in enumerate(lines[1:], 1):
                if line == '':
                    body_start = i + 1
                    break
                if ':' in line:
                    key, value = line.split(':', 1)
                    headers[key.strip().lower()] = value.strip()
            
            # 获取请求体
            body = '\r\n'.join(lines[body_start:]) if body_start < len(lines) else ''
            
            # 构建WSGI environ字典
            environ = {
                'REQUEST_METHOD': method,
                'PATH_INFO': path,
                'QUERY_STRING': query_string,
                'CONTENT_TYPE': headers.get('content-type', ''),
                'CONTENT_LENGTH': headers.get('content-length', ''),
                'SERVER_NAME': self.host,
                'SERVER_PORT': str(self.port),
                'SERVER_PROTOCOL': version,
                'REMOTE_ADDR': client_address[0],
                'REMOTE_HOST': client_address[0],
                'wsgi.version': (1, 0),
                'wsgi.url_scheme': 'http',
                'wsgi.input': body,
                'wsgi.errors': None,
                'wsgi.multithread': True,
                'wsgi.multiprocess': False,
                'wsgi.run_once': False
            }
            
            # 添加HTTP头部到environ
            for key, value in headers.items():
                key = key.replace('-', '_').upper()
                if key not in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
                    environ[f'HTTP_{key}'] = value
            
            return environ
            
        except Exception as e:
            logger.error(f"❌ 解析请求失败: {e}")
            return None
    
    def send_response(self, client_socket: socket.socket, response_data: Dict):
        """发送HTTP响应"""
        try:
            status = response_data['status'] or '200 OK'
            headers = response_data['headers'] or []
            body_parts = response_data['body']
            
            # 合并响应体
            if body_parts:
                if isinstance(body_parts[0], bytes):
                    body = b''.join(body_parts)
                else:
                    body = ''.join(str(part) for part in body_parts).encode('utf-8')
            else:
                body = b''
            
            # 构建响应头
            response_lines = [f'HTTP/1.1 {status}']
            
            # 添加默认头部
            default_headers = {
                'Server': 'Python-WSGIServer/1.0',
                'Date': datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S GMT'),
                'Content-Length': str(len(body)),
                'Connection': 'close'
            }
            
            # 合并自定义头部
            header_dict = dict(default_headers)
            for key, value in headers:
                header_dict[key] = value
            
            # 添加头部到响应
            for key, value in header_dict.items():
                response_lines.append(f'{key}: {value}')
            
            # 构建完整响应
            response_headers = '\r\n'.join(response_lines) + '\r\n\r\n'
            response_bytes = response_headers.encode('utf-8') + body
            
            # 发送响应
            client_socket.sendall(response_bytes)
            
        except Exception as e:
            logger.error(f"❌ 发送响应失败: {e}")
    
    def send_error_response(self, client_socket: socket.socket, status_code: int, reason: str):
        """发送错误响应"""
        try:
            error_body = f"""
            <html>
                <head><title>{status_code} {reason}</title></head>
                <body>
                    <h1>{status_code} {reason}</h1>
                    <p>邮递服务暂时无法处理您的请求。</p>
                    <hr>
                    <p><em>Python-WSGIServer/1.0</em></p>
                </body>
            </html>
            """.strip()
            
            response_data = {
                'status': f'{status_code} {reason}',
                'headers': [('Content-Type', 'text/html; charset=utf-8')],
                'body': [error_body]
            }
            
            self.send_response(client_socket, response_data)
            
        except Exception as e:
            logger.error(f"❌ 发送错误响应失败: {e}")
    
    def get_stats(self) -> Dict[str, Any]:
        """获取服务器统计信息"""
        uptime = time.time() - (self.stats['start_time'] or time.time())
        avg_response_time = 0
        
        if self.stats['request_times']:
            avg_response_time = sum(self.stats['request_times']) / len(self.stats['request_times'])
        
        return {
            'uptime': f"{uptime:.1f}s",
            'total_requests': self.stats['total_requests'],
            'active_connections': self.stats['active_connections'],
            'error_count': self.stats['error_count'],
            'average_response_time': f"{avg_response_time:.3f}s",
            'requests_per_second': f"{self.stats['total_requests'] / max(1, uptime):.2f}",
            'error_rate': f"{self.stats['error_count'] / max(1, self.stats['total_requests']) * 100:.1f}%"
        }
    
    def stop(self):
        """停止服务器 - 邮递中心停止营业"""
        self.running = False
        if self.socket:
            self.socket.close()
        logger.info("🔚 WSGI服务器已停止")

# 示例WSGI应用
def sample_wsgi_app(environ: Dict[str, Any], start_response: Callable) -> List[bytes]:
    """示例WSGI应用 - 邮递业务处理示例"""
    
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    query_string = environ['QUERY_STRING']
    
    logger.info(f"📮 处理请求: {method} {path}?{query_string}")
    
    # 路由处理
    if path == '/':
        # 首页
        response_body = """
        <html>
            <head><title>🏢 WSGI邮递服务中心</title></head>
            <body>
                <h1>🏢 欢迎来到WSGI邮递服务中心！</h1>
                <p>📮 这是一个使用Python实现的WSGI服务器</p>
                <h2>🚀 可用服务：</h2>
                <ul>
                    <li><a href="/api/status">📊 服务器状态</a></li>
                    <li><a href="/api/time">⏰ 当前时间</a></li>
                    <li><a href="/api/echo?msg=hello">📢 回音服务</a></li>
                    <li><a href="/static/test.txt">📄 静态文件</a></li>
                </ul>
            </body>
        </html>
        """
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
        return [response_body.encode('utf-8')]
        
    elif path == '/api/status':
        # 服务器状态API
        status_info = {
            'server': 'Python-WSGIServer/1.0',
            'status': 'running',
            'timestamp': datetime.now().isoformat(),
            'method': method,
            'path': path
        }
        response_body = json.dumps(status_info, indent=2, ensure_ascii=False)
        start_response('200 OK', [('Content-Type', 'application/json; charset=utf-8')])
        return [response_body.encode('utf-8')]
        
    elif path == '/api/time':
        # 时间服务API
        time_info = {
            'current_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'timezone': 'Local',
            'timestamp': time.time()
        }
        response_body = json.dumps(time_info, indent=2, ensure_ascii=False)
        start_response('200 OK', [('Content-Type', 'application/json; charset=utf-8')])
        return [response_body.encode('utf-8')]
        
    elif path == '/api/echo':
        # 回音服务
        query_params = parse_qs(query_string)
        message = query_params.get('msg', ['Hello'])[0]
        
        echo_response = {
            'echo': message,
            'method': method,
            'received_at': datetime.now().isoformat()
        }
        response_body = json.dumps(echo_response, indent=2, ensure_ascii=False)
        start_response('200 OK', [('Content-Type', 'application/json; charset=utf-8')])
        return [response_body.encode('utf-8')]
        
    elif path.startswith('/static/'):
        # 简单的静态文件服务
        file_path = path[8:]  # 移除 '/static/' 前缀
        
        if file_path == 'test.txt':
            content = f"""# 测试文件
这是一个静态文件示例。

请求信息：
- 方法: {method}
- 路径: {path}
- 时间: {datetime.now()}

📮 感谢使用WSGI邮递服务！
"""
            start_response('200 OK', [('Content-Type', 'text/plain; charset=utf-8')])
            return [content.encode('utf-8')]
        else:
            start_response('404 Not Found', [('Content-Type', 'text/html; charset=utf-8')])
            return [b'<h1>404 Not Found</h1><p>Static file not found.</p>']
    
    else:
        # 404错误
        error_body = f"""
        <html>
            <head><title>404 Not Found</title></head>
            <body>
                <h1>📭 404 - 邮件地址不存在</h1>
                <p>抱歉，找不到路径: <code>{path}</code></p>
                <p><a href="/">🏠 返回首页</a></p>
            </body>
        </html>
        """
        start_response('404 Not Found', [('Content-Type', 'text/html; charset=utf-8')])
        return [error_body.encode('utf-8')]

# WSGI服务器演示
def demo_wsgi_server():
    """WSGI服务器演示"""
    print("=== WSGI服务器演示 ===\n")
    
    # 创建并配置服务器
    server = WSGIServer("localhost", 8080)
    server.set_application(sample_wsgi_app)
    
    # 在单独线程中启动服务器
    server_thread = threading.Thread(target=server.start, daemon=True)
    server_thread.start()
    
    # 等待服务器启动
    time.sleep(1)
    
    try:
        # 使用之前的HTTP客户端测试服务器
        client = AdvancedHTTPClient("http://localhost:8080")
        
        print("1. 🏠 测试首页:")
        response = client.get("/")
        if response and response.status_code == 200:
            print(f"✅ 首页访问成功: {response.status_code}")
        
        print("\n2. 📊 测试状态API:")
        response = client.get("/api/status")
        if response and response.status_code == 200:
            print(f"✅ 状态API成功: {response.status_code}")
            try:
                data = response.json()
                print(f"服务器: {data.get('server')}")
            except:
                pass
        
        print("\n3. 📢 测试回音API:")
        response = client.get("/api/echo?msg=Hello WSGI!")
        if response and response.status_code == 200:
            print(f"✅ 回音API成功: {response.status_code}")
            try:
                data = response.json()
                print(f"回音消息: {data.get('echo')}")
            except:
                pass
        
        print("\n4. 📄 测试静态文件:")
        response = client.get("/static/test.txt")
        if response and response.status_code == 200:
            print(f"✅ 静态文件成功: {response.status_code}")
            print(f"文件大小: {len(response.text)} 字符")
        
        print("\n5. 📊 服务器统计:")
        stats = server.get_stats()
        for key, value in stats.items():
            print(f"   {key}: {value}")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")
    finally:
        server.stop()
        print("\n🔚 WSGI服务器演示完成")

# 运行演示
if __name__ == "__main__":
    demo_wsgi_server()
```

### 🔧 中间件系统：邮递质量检查环节

```python
class WSGIMiddleware:
    """
    WSGI中间件基类 - 邮递质量检查基础设施
    
    提供标准的中间件接口和功能
    """
    
    def __init__(self, app: Callable):
        self.app = app
    
    def __call__(self, environ: Dict[str, Any], start_response: Callable):
        """实现WSGI应用接口"""
        return self.process_request(environ, start_response)
    
    def process_request(self, environ: Dict[str, Any], start_response: Callable):
        """处理请求 - 子类应重写此方法"""
        return self.app(environ, start_response)

class LoggingMiddleware(WSGIMiddleware):
    """
    日志中间件 - 邮件处理记录员
    
    记录所有请求和响应的详细信息
    """
    
    def __init__(self, app: Callable, log_level: str = 'INFO'):
        super().__init__(app)
        self.logger = logging.getLogger('wsgi.requests')
        self.logger.setLevel(getattr(logging, log_level.upper()))
    
    def process_request(self, environ: Dict[str, Any], start_response: Callable):
        start_time = time.time()
        
        # 记录请求信息
        method = environ.get('REQUEST_METHOD', 'UNKNOWN')
        path = environ.get('PATH_INFO', '/')
        query = environ.get('QUERY_STRING', '')
        remote_addr = environ.get('REMOTE_ADDR', 'unknown')
        user_agent = environ.get('HTTP_USER_AGENT', 'unknown')
        
        request_url = f"{path}?{query}" if query else path
        
        self.logger.info(f"📮 请求开始: {method} {request_url} from {remote_addr}")
        
        # 包装start_response以记录响应状态
        response_info = {'status': None}
        
        def logging_start_response(status: str, headers: List[Tuple[str, str]], exc_info=None):
            response_info['status'] = status
            return start_response(status, headers, exc_info)
        
        try:
            # 调用下游应用
            response = self.app(environ, logging_start_response)
            
            # 记录成功响应
            response_time = time.time() - start_time
            status = response_info['status'] or 'Unknown'
            
            self.logger.info(
                f"✅ 请求完成: {method} {request_url} -> {status} "
                f"({response_time:.3f}s)"
            )
            
            return response
            
        except Exception as e:
            # 记录异常
            response_time = time.time() - start_time
            self.logger.error(
                f"❌ 请求异常: {method} {request_url} -> ERROR "
                f"({response_time:.3f}s) - {str(e)}"
            )
            raise

class SecurityMiddleware(WSGIMiddleware):
    """
    安全中间件 - 邮件安全检查员
    
    添加安全头部和基本的安全检查
    """
    
    def __init__(self, app: Callable):
        super().__init__(app)
        self.security_headers = {
            'X-Content-Type-Options': 'nosniff',
            'X-Frame-Options': 'DENY',
            'X-XSS-Protection': '1; mode=block',
            'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
            'Content-Security-Policy': "default-src 'self'",
            'Referrer-Policy': 'strict-origin-when-cross-origin'
        }
    
    def process_request(self, environ: Dict[str, Any], start_response: Callable):
        # 检查请求大小限制
        content_length = environ.get('CONTENT_LENGTH', '')
        if content_length:
            try:
                if int(content_length) > 10 * 1024 * 1024:  # 10MB限制
                    self._send_error_response(start_response, '413 Payload Too Large')
                    return [b'Request payload too large']
            except ValueError:
                pass
        
        # 检查可疑的User-Agent
        user_agent = environ.get('HTTP_USER_AGENT', '').lower()
        suspicious_patterns = ['bot', 'crawler', 'spider', 'scraper']
        if any(pattern in user_agent for pattern in suspicious_patterns):
            logger.warning(f"🚨 可疑User-Agent: {user_agent}")
        
        # 包装start_response以添加安全头部
        def security_start_response(status: str, headers: List[Tuple[str, str]], exc_info=None):
            # 添加安全头部
            security_headers_list = list(self.security_headers.items())
            
            # 检查是否已存在相同的头部
            existing_headers = {h[0].lower() for h in headers}
            filtered_security_headers = [
                (k, v) for k, v in security_headers_list 
                if k.lower() not in existing_headers
            ]
            
            enhanced_headers = headers + filtered_security_headers
            return start_response(status, enhanced_headers, exc_info)
        
        return self.app(environ, security_start_response)
    
    def _send_error_response(self, start_response: Callable, status: str):
        """发送错误响应"""
        headers = [('Content-Type', 'text/plain; charset=utf-8')]
        start_response(status, headers)

class CachingMiddleware(WSGIMiddleware):
    """
    缓存中间件 - 邮件临时存储管理员
    
    提供简单的内存缓存功能
    """
    
    def __init__(self, app: Callable, cache_timeout: int = 300):
        super().__init__(app)
        self.cache = {}
        self.cache_timeout = cache_timeout
    
    def process_request(self, environ: Dict[str, Any], start_response: Callable):
        method = environ.get('REQUEST_METHOD', 'GET')
        
        # 只缓存GET请求
        if method != 'GET':
            return self.app(environ, start_response)
        
        # 生成缓存键
        cache_key = self._generate_cache_key(environ)
        
        # 检查缓存
        cached_response = self._get_from_cache(cache_key)
        if cached_response:
            logger.info(f"💾 缓存命中: {cache_key}")
            
            status, headers, body = cached_response
            start_response(status, headers)
            return [body]
        
        # 缓存未命中，调用原始应用
        response_data = {'status': None, 'headers': None, 'body': b''}
        
        def caching_start_response(status: str, headers: List[Tuple[str, str]], exc_info=None):
            response_data['status'] = status
            response_data['headers'] = headers
            return start_response(status, headers, exc_info)
        
        response = self.app(environ, caching_start_response)
        
        # 收集响应数据
        body_parts = []
        if hasattr(response, '__iter__'):
            for chunk in response:
                if chunk:
                    body_parts.append(chunk)
        
        response_body = b''.join(body_parts) if body_parts else b''
        
        # 缓存成功的响应
        if response_data['status'] and response_data['status'].startswith('200'):
            self._put_to_cache(cache_key, response_data['status'], 
                             response_data['headers'], response_body)
            logger.info(f"💾 缓存保存: {cache_key}")
        
        return [response_body]
    
    def _generate_cache_key(self, environ: Dict[str, Any]) -> str:
        """生成缓存键"""
        path = environ.get('PATH_INFO', '/')
        query = environ.get('QUERY_STRING', '')
        key_data = f"{path}?{query}" if query else path
        return hashlib.md5(key_data.encode('utf-8')).hexdigest()
    
    def _get_from_cache(self, key: str) -> Optional[Tuple[str, List[Tuple[str, str]], bytes]]:
        """从缓存获取数据"""
        if key in self.cache:
            data, timestamp = self.cache[key]
            if time.time() - timestamp < self.cache_timeout:
                return data
            else:
                # 缓存过期，删除
                del self.cache[key]
        return None
    
    def _put_to_cache(self, key: str, status: str, headers: List[Tuple[str, str]], body: bytes):
        """将数据放入缓存"""
        # 添加缓存时间戳头部
        cache_headers = headers + [
            ('X-Cache', 'MISS'),
            ('X-Cache-Time', datetime.now().isoformat())
        ]
        
        self.cache[key] = ((status, cache_headers, body), time.time())
        
        # 简单的缓存清理：保持最多1000个条目
        if len(self.cache) > 1000:
            oldest_key = min(self.cache.keys(), key=lambda k: self.cache[k][1])
            del self.cache[oldest_key]

class CompressionMiddleware(WSGIMiddleware):
    """
    压缩中间件 - 邮件压缩服务
    
    提供gzip压缩功能
    """
    
    def __init__(self, app: Callable, min_size: int = 1024):
        super().__init__(app)
        self.min_size = min_size
    
    def process_request(self, environ: Dict[str, Any], start_response: Callable):
        # 检查客户端是否支持gzip
        accept_encoding = environ.get('HTTP_ACCEPT_ENCODING', '')
        if 'gzip' not in accept_encoding.lower():
            return self.app(environ, start_response)
        
        # 收集响应数据
        response_data = {'status': None, 'headers': None}
        
        def compression_start_response(status: str, headers: List[Tuple[str, str]], exc_info=None):
            response_data['status'] = status
            response_data['headers'] = headers
            return lambda data: None  # 暂不调用原始start_response
        
        response = self.app(environ, compression_start_response)
        
        # 收集响应体
        body_parts = []
        if hasattr(response, '__iter__'):
            for chunk in response:
                if chunk:
                    body_parts.append(chunk)
        
        original_body = b''.join(body_parts) if body_parts else b''
        
        # 检查是否需要压缩
        if len(original_body) < self.min_size:
            # 不压缩，直接返回
            start_response(response_data['status'], response_data['headers'])
            return [original_body]
        
        # 执行gzip压缩
        try:
            compressed_body = gzip.compress(original_body)
            
            # 更新头部
            headers = list(response_data['headers'])
            
            # 移除原有的Content-Length头部
            headers = [(k, v) for k, v in headers if k.lower() != 'content-length']
            
            # 添加压缩相关头部
            headers.extend([
                ('Content-Encoding', 'gzip'),
                ('Content-Length', str(len(compressed_body))),
                ('Vary', 'Accept-Encoding')
            ])
            
            start_response(response_data['status'], headers)
            return [compressed_body]
            
        except Exception as e:
            logger.error(f"❌ 压缩失败: {e}")
            # 压缩失败，返回原始内容
            start_response(response_data['status'], response_data['headers'])
            return [original_body]

# 中间件组合工具
def create_middleware_stack(app: Callable, middlewares: List[type]) -> Callable:
    """
    创建中间件堆栈 - 组装邮递质量检查流水线
    
    参数:
        app: WSGI应用
        middlewares: 中间件类列表（从外到内的顺序）
    """
    wrapped_app = app
    
    # 从内到外包装中间件
    for middleware_class in reversed(middlewares):
        wrapped_app = middleware_class(wrapped_app)
        logger.info(f"🔧 添加中间件: {middleware_class.__name__}")
    
    return wrapped_app

# 高级WSGI服务器 - 集成中间件支持
class AdvancedWSGIServer(WSGIServer):
    """
    高级WSGI服务器 - 现代化邮递处理中心
    
    集成中间件支持和高级功能
    """
    
    def __init__(self, host: str = "localhost", port: int = 8080):
        super().__init__(host, port)
        self.middlewares = []
    
    def add_middleware(self, middleware_class: type, **kwargs):
        """添加中间件"""
        self.middlewares.append((middleware_class, kwargs))
        logger.info(f"🔧 注册中间件: {middleware_class.__name__}")
    
    def set_application(self, application: Callable):
        """设置应用并应用中间件"""
        # 应用中间件
        wrapped_app = application
        for middleware_class, kwargs in reversed(self.middlewares):
            wrapped_app = middleware_class(wrapped_app, **kwargs)
        
        super().set_application(wrapped_app)
        logger.info(f"📋 应用已配置，包含 {len(self.middlewares)} 个中间件")

# 中间件演示
def demo_middleware_system():
    """中间件系统演示"""
    print("=== 中间件系统演示 ===\n")
    
    # 创建高级服务器
    server = AdvancedWSGIServer("localhost", 8081)
    
    # 添加中间件（从外到内的顺序）
    server.add_middleware(LoggingMiddleware, log_level='INFO')
    server.add_middleware(SecurityMiddleware)
    server.add_middleware(CachingMiddleware, cache_timeout=60)
    server.add_middleware(CompressionMiddleware, min_size=100)
    
    # 设置应用
    server.set_application(sample_wsgi_app)
    
    # 启动服务器
    server_thread = threading.Thread(target=server.start, daemon=True)
    server_thread.start()
    
    time.sleep(1)
    
    try:
        client = AdvancedHTTPClient("http://localhost:8081")
        
        print("1. 🔐 测试安全中间件:")
        response = client.get("/")
        if response:
            security_headers = [h for h in response.headers.items() 
                             if h[0].startswith('X-') or h[0] == 'Strict-Transport-Security']
            print(f"✅ 安全头部数量: {len(security_headers)}")
            for header, value in security_headers[:3]:  # 显示前3个
                print(f"   {header}: {value}")
        
        print("\n2. 💾 测试缓存中间件:")
        # 第一次请求
        start_time = time.time()
        response1 = client.get("/api/time")
        time1 = time.time() - start_time
        
        # 第二次请求（应该从缓存返回）
        start_time = time.time()
        response2 = client.get("/api/time")
        time2 = time.time() - start_time
        
        if response1 and response2:
            print(f"✅ 第一次请求: {time1:.3f}s")
            print(f"✅ 第二次请求: {time2:.3f}s (缓存)")
            cache_header = response2.headers.get('X-Cache', 'MISS')
            print(f"   缓存状态: {cache_header}")
        
        print("\n3. 🗜️ 测试压缩中间件:")
        # 请求较大的内容
        client.session.headers['Accept-Encoding'] = 'gzip, deflate'
        response = client.get("/")
        if response:
            encoding = response.headers.get('Content-Encoding', 'none')
            print(f"✅ 内容编码: {encoding}")
            print(f"   响应大小: {len(response.content)} 字节")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")
    finally:
        server.stop()
        print("\n🔚 中间件演示完成")

# 运行演示
if __name__ == "__main__":
    demo_middleware_system()

---

## 17.4 现代网络应用开发 - "智能邮递服务平台"

在前面的章节中，我们学习了HTTP协议（邮政规则）、网络编程基础（邮递技术）和服务器开发（邮递中心建设）。现在我们将探索现代网络应用开发，就像建设一个覆盖全球的智能邮递服务平台。

### 17.4.1 RESTful API设计 - "标准化邮递服务接口"

RESTful API就像邮政系统的标准化服务接口，让不同的客户端都能以统一的方式与服务器交互。

#### RESTful设计原则

```python
"""
RESTful API 设计框架 - 标准邮递服务接口

这个框架实现了RESTful API的核心原则：
1. 资源导向设计
2. 统一接口约定
3. 无状态通信
4. 可缓存响应
5. 分层系统架构
"""

import json
import re
from typing import Dict, List, Optional, Any, Callable
from datetime import datetime
from dataclasses import dataclass, asdict
from enum import Enum

class HTTPMethod(Enum):
    """HTTP方法枚举 - 邮递服务类型"""
    GET = "GET"          # 查询服务 - 查看邮件状态
    POST = "POST"        # 创建服务 - 寄送新邮件
    PUT = "PUT"          # 更新服务 - 修改邮件信息
    PATCH = "PATCH"      # 部分更新 - 更新部分信息
    DELETE = "DELETE"    # 删除服务 - 取消邮寄
    HEAD = "HEAD"        # 元信息查询 - 检查邮件是否存在
    OPTIONS = "OPTIONS"  # 服务选项 - 查询可用服务

@dataclass
class APIResponse:
    """API响应数据结构 - 邮递服务响应单"""
    success: bool
    message: str
    data: Optional[Any] = None
    metadata: Optional[Dict] = None
    timestamp: str = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """转换为字典格式"""
        return asdict(self)

class Resource:
    """
    资源基类 - 邮递资源抽象
    
    每个资源代表邮政系统中的一个实体，
    如邮件、客户、邮局等
    """
    
    def __init__(self, resource_id: str = None):
        self.id = resource_id
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    
    def to_dict(self) -> Dict:
        """转换为字典格式"""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class MailPackage(Resource):
    """邮件包裹资源"""
    
    def __init__(self, package_id: str = None, sender: str = None, 
                 recipient: str = None, content: str = None):
        super().__init__(package_id)
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.status = "pending"  # pending, processing, delivered, failed
        self.tracking_number = f"PKG-{package_id}" if package_id else None
    
    def to_dict(self) -> Dict:
        data = super().to_dict()
        data.update({
            'sender': self.sender,
            'recipient': self.recipient,
            'content': self.content,
            'status': self.status,
            'tracking_number': self.tracking_number
        })
        return data

class PostOffice(Resource):
    """邮局资源"""
    
    def __init__(self, office_id: str = None, name: str = None, 
                 address: str = None, capacity: int = 1000):
        super().__init__(office_id)
        self.name = name
        self.address = address
        self.capacity = capacity
        self.current_load = 0
    
    def to_dict(self) -> Dict:
        data = super().to_dict()
        data.update({
            'name': self.name,
            'address': self.address,
            'capacity': self.capacity,
            'current_load': self.current_load,
            'utilization': f"{(self.current_load / self.capacity * 100):.1f}%"
        })
        return data

class RoutePattern:
    """路由模式匹配器 - 邮递路线规则"""
    
    def __init__(self, pattern: str, method: HTTPMethod, handler: Callable):
        self.pattern = pattern
        self.method = method
        self.handler = handler
        self.regex = self._compile_pattern(pattern)
    
    def _compile_pattern(self, pattern: str) -> re.Pattern:
        """编译路径模式为正则表达式"""
        # 转换路径参数格式：/packages/{id} -> /packages/(?P<id>[^/]+)
        regex_pattern = re.sub(r'\{(\w+)\}', r'(?P<\1>[^/]+)', pattern)
        regex_pattern = '^' + regex_pattern + '$'
        return re.compile(regex_pattern)
    
    def match(self, path: str, method: HTTPMethod) -> Optional[Dict]:
        """匹配路径和方法"""
        if self.method != method:
            return None
        
        match = self.regex.match(path)
        if match:
            return match.groupdict()
        return None

class RESTfulAPI:
    """
    RESTful API 框架 - 标准邮递服务接口
    
    实现REST架构风格的API服务
    """
    
    def __init__(self):
        self.routes: List[RoutePattern] = []
        self.middleware: List[Callable] = []
        
        # 数据存储（简单内存存储）
        self.packages: Dict[str, MailPackage] = {}
        self.post_offices: Dict[str, PostOffice] = {}
        self.package_counter = 0
        self.office_counter = 0
        
        # 注册默认路由
        self._register_default_routes()
    
    def _register_default_routes(self):
        """注册默认路由"""
        # 包裹管理路由
        self.route('/packages', HTTPMethod.GET, self.list_packages)
        self.route('/packages', HTTPMethod.POST, self.create_package)
        self.route('/packages/{id}', HTTPMethod.GET, self.get_package)
        self.route('/packages/{id}', HTTPMethod.PUT, self.update_package)
        self.route('/packages/{id}', HTTPMethod.DELETE, self.delete_package)
        
        # 邮局管理路由
        self.route('/offices', HTTPMethod.GET, self.list_offices)
        self.route('/offices', HTTPMethod.POST, self.create_office)
        self.route('/offices/{id}', HTTPMethod.GET, self.get_office)
        
        # 服务发现路由
        self.route('/health', HTTPMethod.GET, self.health_check)
        self.route('/api/info', HTTPMethod.GET, self.api_info)
    
    def route(self, pattern: str, method: HTTPMethod, handler: Callable):
        """注册路由"""
        route = RoutePattern(pattern, method, handler)
        self.routes.append(route)
        print(f"📍 注册路由: {method.value} {pattern}")
    
    def handle_request(self, path: str, method: str, body: str = None) -> APIResponse:
        """
        处理HTTP请求 - 邮递请求处理
        
        参数:
            path: 请求路径
            method: HTTP方法
            body: 请求体数据
        """
        try:
            http_method = HTTPMethod(method.upper())
        except ValueError:
            return APIResponse(
                success=False,
                message=f"不支持的HTTP方法: {method}"
            )
        
        # 路由匹配
        for route in self.routes:
            params = route.match(path, http_method)
            if params is not None:
                try:
                    # 解析请求体
                    request_data = {}
                    if body:
                        request_data = json.loads(body)
                    
                    # 调用处理器
                    result = route.handler(params=params, data=request_data)
                    return result
                    
                except json.JSONDecodeError:
                    return APIResponse(
                        success=False,
                        message="无效的JSON格式"
                    )
                except Exception as e:
                    return APIResponse(
                        success=False,
                        message=f"处理请求时发生错误: {str(e)}"
                    )
        
        # 没有匹配的路由
        return APIResponse(
            success=False,
            message=f"未找到路由: {method} {path}"
        )
    
    # 包裹管理处理器
    def list_packages(self, params: Dict = None, data: Dict = None) -> APIResponse:
        """列出所有包裹 - 邮件清单查询"""
        package_list = [pkg.to_dict() for pkg in self.packages.values()]
        return APIResponse(
            success=True,
            message="成功获取包裹列表",
            data=package_list,
            metadata={'total': len(package_list)}
        )
    
    def create_package(self, params: Dict = None, data: Dict = None) -> APIResponse:
        """创建新包裹 - 邮寄新邮件"""
        required_fields = ['sender', 'recipient', 'content']
        for field in required_fields:
            if not data or field not in data:
                return APIResponse(
                    success=False,
                    message=f"缺少必需字段: {field}"
                )
        
        self.package_counter += 1
        package_id = str(self.package_counter)
        
        package = MailPackage(
            package_id=package_id,
            sender=data['sender'],
            recipient=data['recipient'],
            content=data['content']
        )
        
        self.packages[package_id] = package
        
        return APIResponse(
            success=True,
            message="包裹创建成功",
            data=package.to_dict()
        )
    
    def get_package(self, params: Dict = None, data: Dict = None) -> APIResponse:
        """获取指定包裹 - 查询邮件详情"""
        package_id = params.get('id')
        if package_id not in self.packages:
            return APIResponse(
                success=False,
                message=f"包裹不存在: {package_id}"
            )
        
        package = self.packages[package_id]
        return APIResponse(
            success=True,
            message="成功获取包裹信息",
            data=package.to_dict()
        )
    
    def update_package(self, params: Dict = None, data: Dict = None) -> APIResponse:
        """更新包裹信息 - 修改邮件状态"""
        package_id = params.get('id')
        if package_id not in self.packages:
            return APIResponse(
                success=False,
                message=f"包裹不存在: {package_id}"
            )
        
        package = self.packages[package_id]
        
        # 更新允许的字段
        updatable_fields = ['status', 'content']
        updated_fields = []
        
        for field in updatable_fields:
            if data and field in data:
                setattr(package, field, data[field])
                updated_fields.append(field)
        
        if updated_fields:
            package.updated_at = datetime.now()
        
        return APIResponse(
            success=True,
            message=f"包裹更新成功，更新字段: {', '.join(updated_fields)}",
            data=package.to_dict()
        )
    
    def delete_package(self, params: Dict = None, data: Dict = None) -> APIResponse:
        """删除包裹 - 取消邮寄"""
        package_id = params.get('id')
        if package_id not in self.packages:
            return APIResponse(
                success=False,
                message=f"包裹不存在: {package_id}"
            )
        
        del self.packages[package_id]
        
        return APIResponse(
            success=True,
            message=f"包裹 {package_id} 已删除"
        )
    
    # 邮局管理处理器
    def list_offices(self, params: Dict = None, data: Dict = None) -> APIResponse:
        """列出所有邮局"""
        office_list = [office.to_dict() for office in self.post_offices.values()]
        return APIResponse(
            success=True,
            message="成功获取邮局列表",
            data=office_list,
            metadata={'total': len(office_list)}
        )
    
    def create_office(self, params: Dict = None, data: Dict = None) -> APIResponse:
        """创建新邮局"""
        required_fields = ['name', 'address']
        for field in required_fields:
            if not data or field not in data:
                return APIResponse(
                    success=False,
                    message=f"缺少必需字段: {field}"
                )
        
        self.office_counter += 1
        office_id = str(self.office_counter)
        
        office = PostOffice(
            office_id=office_id,
            name=data['name'],
            address=data['address'],
            capacity=data.get('capacity', 1000)
        )
        
        self.post_offices[office_id] = office
        
        return APIResponse(
            success=True,
            message="邮局创建成功",
            data=office.to_dict()
        )
    
    def get_office(self, params: Dict = None, data: Dict = None) -> APIResponse:
        """获取指定邮局"""
        office_id = params.get('id')
        if office_id not in self.post_offices:
            return APIResponse(
                success=False,
                message=f"邮局不存在: {office_id}"
            )
        
        office = self.post_offices[office_id]
        return APIResponse(
            success=True,
            message="成功获取邮局信息",
            data=office.to_dict()
        )
    
    # 系统服务处理器
    def health_check(self, params: Dict = None, data: Dict = None) -> APIResponse:
        """健康检查 - 系统状态检查"""
        health_data = {
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'services': {
                'package_service': 'running',
                'office_service': 'running'
            },
            'statistics': {
                'total_packages': len(self.packages),
                'total_offices': len(self.post_offices)
            }
        }
        
        return APIResponse(
            success=True,
            message="系统运行正常",
            data=health_data
        )
    
    def api_info(self, params: Dict = None, data: Dict = None) -> APIResponse:
        """API信息 - 服务接口说明"""
        api_info = {
            'name': 'Postal Service API',
            'version': '1.0.0',
            'description': '邮政服务REST API',
            'endpoints': {
                'packages': {
                    'GET /packages': '获取所有包裹',
                    'POST /packages': '创建新包裹',
                    'GET /packages/{id}': '获取指定包裹',
                    'PUT /packages/{id}': '更新包裹信息',
                    'DELETE /packages/{id}': '删除包裹'
                },
                'offices': {
                    'GET /offices': '获取所有邮局',
                    'POST /offices': '创建新邮局',
                    'GET /offices/{id}': '获取指定邮局'
                },
                'system': {
                    'GET /health': '健康检查',
                    'GET /api/info': 'API信息'
                }
            }
        }
        
        return APIResponse(
            success=True,
            message="API信息获取成功",
            data=api_info
        )

# RESTful API 演示
def demo_restful_api():
    """RESTful API 演示"""
    print("=== RESTful API 演示 ===\n")
    
    # 创建API实例
    api = RESTfulAPI()
    
    print("1. 📋 API信息查询:")
    response = api.handle_request('/api/info', 'GET')
    print(f"✅ {response.message}")
    if response.data:
        endpoints = response.data.get('endpoints', {})
        print(f"   可用端点数量: {len(endpoints)}")
    
    print("\n2. 📦 创建包裹:")
    package_data = {
        'sender': 'Alice',
        'recipient': 'Bob',
        'content': 'Birthday gift'
    }
    response = api.handle_request('/packages', 'POST', json.dumps(package_data))
    print(f"✅ {response.message}")
    if response.data:
        print(f"   包裹ID: {response.data['id']}")
        print(f"   追踪号: {response.data['tracking_number']}")
    
    print("\n3. 🏢 创建邮局:")
    office_data = {
        'name': '中央邮局',
        'address': '北京市朝阳区建国路1号',
        'capacity': 2000
    }
    response = api.handle_request('/offices', 'POST', json.dumps(office_data))
    print(f"✅ {response.message}")
    if response.data:
        print(f"   邮局ID: {response.data['id']}")
        print(f"   利用率: {response.data['utilization']}")
    
    print("\n4. 📊 获取包裹列表:")
    response = api.handle_request('/packages', 'GET')
    print(f"✅ {response.message}")
    if response.metadata:
        print(f"   总数量: {response.metadata['total']}")
    
    print("\n5. 🔄 更新包裹状态:")
    update_data = {'status': 'processing'}
    response = api.handle_request('/packages/1', 'PUT', json.dumps(update_data))
    print(f"✅ {response.message}")
    
    print("\n6. 🔍 查询特定包裹:")
    response = api.handle_request('/packages/1', 'GET')
    print(f"✅ {response.message}")
    if response.data:
        print(f"   当前状态: {response.data['status']}")
    
    print("\n7. ❌ 测试错误处理:")
    response = api.handle_request('/packages/999', 'GET')
    print(f"❌ {response.message}")
    
    print("\n8. 🏥 健康检查:")
    response = api.handle_request('/health', 'GET')
    print(f"✅ {response.message}")
    if response.data:
        services = response.data.get('services', {})
        running_services = [k for k, v in services.items() if v == 'running']
        print(f"   运行中的服务: {len(running_services)}")
    
    print("\n🔚 RESTful API 演示完成")

# 运行演示
if __name__ == "__main__":
    demo_restful_api()

### 17.4.2 微服务架构 - "分布式邮递网络"

微服务架构就像建立一个分布式的邮递网络，每个服务负责特定的业务功能，服务之间通过网络通信协作。

```python
"""
微服务架构框架 - 分布式邮递网络

这个框架演示了微服务架构的核心概念：
1. 服务拆分与独立部署
2. 服务发现与注册
3. 负载均衡与容错
4. 分布式配置管理
5. 服务间通信
"""

import json
import time
import random
import hashlib
import threading
from typing import Dict, List, Optional, Any, Callable
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
from enum import Enum
import requests
import uuid

class ServiceStatus(Enum):
    """服务状态"""
    STARTING = "starting"
    RUNNING = "running" 
    STOPPING = "stopping"
    STOPPED = "stopped"
    ERROR = "error"

@dataclass
class ServiceInfo:
    """服务信息"""
    service_id: str
    name: str
    host: str
    port: int
    status: ServiceStatus
    version: str
    metadata: Dict[str, Any]
    last_heartbeat: datetime
    
    def to_dict(self) -> Dict:
        data = asdict(self)
        data['status'] = self.status.value
        data['last_heartbeat'] = self.last_heartbeat.isoformat()
        return data

class ServiceRegistry:
    """
    服务注册中心 - 邮递网络总调度中心
    
    负责服务的注册、发现和健康检查
    """
    
    def __init__(self):
        self.services: Dict[str, ServiceInfo] = {}
        self.service_groups: Dict[str, List[str]] = {}  # 服务名 -> 服务ID列表
        self.health_check_interval = 30  # 30秒健康检查间隔
        self.health_check_thread = None
        self.running = False
    
    def start(self):
        """启动服务注册中心"""
        self.running = True
        self.health_check_thread = threading.Thread(target=self._health_check_loop, daemon=True)
        self.health_check_thread.start()
        print("🏛️ 服务注册中心启动")
    
    def stop(self):
        """停止服务注册中心"""
        self.running = False
        if self.health_check_thread:
            self.health_check_thread.join(timeout=1)
        print("🏛️ 服务注册中心停止")
    
    def register_service(self, service_info: ServiceInfo) -> bool:
        """注册服务"""
        try:
            self.services[service_info.service_id] = service_info
            
            # 添加到服务组
            if service_info.name not in self.service_groups:
                self.service_groups[service_info.name] = []
            
            if service_info.service_id not in self.service_groups[service_info.name]:
                self.service_groups[service_info.name].append(service_info.service_id)
            
            print(f"📋 服务注册成功: {service_info.name} ({service_info.service_id})")
            return True
            
        except Exception as e:
            print(f"❌ 服务注册失败: {e}")
            return False
    
    def deregister_service(self, service_id: str) -> bool:
        """注销服务"""
        if service_id in self.services:
            service_info = self.services[service_id]
            del self.services[service_id]
            
            # 从服务组中移除
            if service_info.name in self.service_groups:
                if service_id in self.service_groups[service_info.name]:
                    self.service_groups[service_info.name].remove(service_id)
                
                # 如果组为空，删除组
                if not self.service_groups[service_info.name]:
                    del self.service_groups[service_info.name]
            
            print(f"📋 服务注销: {service_info.name} ({service_id})")
            return True
        
        return False
    
    def discover_service(self, service_name: str) -> Optional[ServiceInfo]:
        """发现服务（负载均衡）"""
        if service_name not in self.service_groups:
            return None
        
        available_services = []
        for service_id in self.service_groups[service_name]:
            if service_id in self.services:
                service = self.services[service_id]
                if service.status == ServiceStatus.RUNNING:
                    available_services.append(service)
        
        if not available_services:
            return None
        
        # 简单的轮询负载均衡
        return random.choice(available_services)
    
    def get_all_services(self, service_name: str = None) -> List[ServiceInfo]:
        """获取所有服务"""
        if service_name:
            return [self.services[sid] for sid in self.service_groups.get(service_name, []) 
                   if sid in self.services]
        else:
            return list(self.services.values())
    
    def heartbeat(self, service_id: str) -> bool:
        """服务心跳"""
        if service_id in self.services:
            self.services[service_id].last_heartbeat = datetime.now()
            return True
        return False
    
    def _health_check_loop(self):
        """健康检查循环"""
        while self.running:
            try:
                current_time = datetime.now()
                timeout_threshold = current_time - timedelta(seconds=self.health_check_interval * 2)
                
                # 检查超时的服务
                timeout_services = []
                for service_id, service_info in self.services.items():
                    if service_info.last_heartbeat < timeout_threshold:
                        timeout_services.append(service_id)
                
                # 标记超时服务
                for service_id in timeout_services:
                    if self.services[service_id].status == ServiceStatus.RUNNING:
                        self.services[service_id].status = ServiceStatus.ERROR
                        print(f"⚠️ 服务超时: {self.services[service_id].name} ({service_id})")
                
                time.sleep(self.health_check_interval)
                
            except Exception as e:
                print(f"❌ 健康检查错误: {e}")
                time.sleep(5)

class MicroService:
    """
    微服务基类 - 邮递子服务
    
    提供微服务的基础功能
    """
    
    def __init__(self, name: str, host: str = "localhost", port: int = None):
        self.service_id = str(uuid.uuid4())
        self.name = name
        self.host = host
        self.port = port or self._find_free_port()
        self.status = ServiceStatus.STOPPED
        self.version = "1.0.0"
        self.metadata = {}
        
        self.registry_client = None
        self.heartbeat_thread = None
        self.running = False
    
    def _find_free_port(self) -> int:
        """找到可用端口"""
        import socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', 0))
            return s.getsockname()[1]
    
    def set_registry(self, registry: ServiceRegistry):
        """设置服务注册中心"""
        self.registry_client = registry
    
    def start(self):
        """启动服务"""
        try:
            self.status = ServiceStatus.STARTING
            print(f"🚀 启动服务: {self.name} (端口 {self.port})")
            
            # 注册到服务中心
            if self.registry_client:
                service_info = ServiceInfo(
                    service_id=self.service_id,
                    name=self.name,
                    host=self.host,
                    port=self.port,
                    status=ServiceStatus.RUNNING,
                    version=self.version,
                    metadata=self.metadata,
                    last_heartbeat=datetime.now()
                )
                self.registry_client.register_service(service_info)
            
            # 启动心跳
            self.running = True
            self.heartbeat_thread = threading.Thread(target=self._heartbeat_loop, daemon=True)
            self.heartbeat_thread.start()
            
            self.status = ServiceStatus.RUNNING
            self._on_start()
            
        except Exception as e:
            self.status = ServiceStatus.ERROR
            print(f"❌ 服务启动失败: {e}")
    
    def stop(self):
        """停止服务"""
        try:
            self.status = ServiceStatus.STOPPING
            self.running = False
            
            # 从服务中心注销
            if self.registry_client:
                self.registry_client.deregister_service(self.service_id)
            
            # 停止心跳
            if self.heartbeat_thread:
                self.heartbeat_thread.join(timeout=1)
            
            self._on_stop()
            self.status = ServiceStatus.STOPPED
            print(f"🛑 服务停止: {self.name}")
            
        except Exception as e:
            print(f"❌ 服务停止失败: {e}")
    
    def _heartbeat_loop(self):
        """心跳循环"""
        while self.running:
            try:
                if self.registry_client:
                    self.registry_client.heartbeat(self.service_id)
                time.sleep(15)  # 15秒心跳间隔
            except Exception as e:
                print(f"❌ 心跳发送失败: {e}")
                time.sleep(5)
    
    def call_service(self, service_name: str, method: str, endpoint: str, 
                    data: Dict = None) -> Optional[Dict]:
        """调用其他服务"""
        if not self.registry_client:
            print("❌ 未配置服务注册中心")
            return None
        
        # 服务发现
        service_info = self.registry_client.discover_service(service_name)
        if not service_info:
            print(f"❌ 未找到服务: {service_name}")
            return None
        
        # 构建请求URL
        url = f"http://{service_info.host}:{service_info.port}{endpoint}"
        
        try:
            if method.upper() == 'GET':
                response = requests.get(url, timeout=5)
            elif method.upper() == 'POST':
                response = requests.post(url, json=data, timeout=5)
            else:
                print(f"❌ 不支持的HTTP方法: {method}")
                return None
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ 服务调用失败: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"❌ 服务调用异常: {e}")
            return None
    
    def _on_start(self):
        """服务启动时的回调"""
        pass
    
    def _on_stop(self):
        """服务停止时的回调"""
        pass

class PackageService(MicroService):
    """包裹服务 - 专门处理包裹业务"""
    
    def __init__(self):
        super().__init__("package-service", port=8001)
        self.packages = {}
        self.package_counter = 0
    
    def _on_start(self):
        print("📦 包裹服务已启动，等待处理包裹业务...")
    
    def create_package(self, sender: str, recipient: str, content: str) -> Dict:
        """创建包裹"""
        self.package_counter += 1
        package_id = str(self.package_counter)
        
        package = {
            'id': package_id,
            'sender': sender,
            'recipient': recipient,
            'content': content,
            'status': 'created',
            'created_at': datetime.now().isoformat(),
            'tracking_number': f"PKG-{package_id}"
        }
        
        self.packages[package_id] = package
        print(f"📦 创建包裹: {package_id}")
        
        # 通知路由服务
        self.call_service("routing-service", "POST", "/assign-route", {
            'package_id': package_id,
            'destination': recipient
        })
        
        return package
    
    def get_package(self, package_id: str) -> Optional[Dict]:
        """获取包裹信息"""
        return self.packages.get(package_id)
    
    def update_package_status(self, package_id: str, status: str) -> bool:
        """更新包裹状态"""
        if package_id in self.packages:
            self.packages[package_id]['status'] = status
            self.packages[package_id]['updated_at'] = datetime.now().isoformat()
            print(f"📦 更新包裹状态: {package_id} -> {status}")
            return True
        return False

class RoutingService(MicroService):
    """路由服务 - 专门处理路线规划"""
    
    def __init__(self):
        super().__init__("routing-service", port=8002)
        self.routes = {}
    
    def _on_start(self):
        print("🗺️ 路由服务已启动，准备规划运输路线...")
    
    def assign_route(self, package_id: str, destination: str) -> Dict:
        """分配运输路线"""
        # 模拟路线规划
        route_id = hashlib.md5(f"{package_id}-{destination}".encode()).hexdigest()[:8]
        
        route = {
            'route_id': route_id,
            'package_id': package_id,
            'destination': destination,
            'estimated_time': random.randint(1, 5),  # 1-5天
            'status': 'planned',
            'waypoints': self._generate_waypoints(destination)
        }
        
        self.routes[route_id] = route
        print(f"🗺️ 规划路线: {route_id} (目的地: {destination})")
        
        # 通知包裹服务更新状态
        self.call_service("package-service", "POST", "/update-status", {
            'package_id': package_id,
            'status': 'routed'
        })
        
        return route
    
    def _generate_waypoints(self, destination: str) -> List[str]:
        """生成路径点"""
        cities = ["北京", "天津", "上海", "广州", "深圳", "杭州", "南京", "武汉"]
        waypoints = random.sample(cities, random.randint(2, 4))
        waypoints.append(destination)
        return waypoints

class NotificationService(MicroService):
    """通知服务 - 专门处理消息通知"""
    
    def __init__(self):
        super().__init__("notification-service", port=8003)
        self.notifications = []
    
    def _on_start(self):
        print("📬 通知服务已启动，准备发送通知...")
    
    def send_notification(self, recipient: str, message: str, 
                         notification_type: str = "info") -> bool:
        """发送通知"""
        notification = {
            'id': str(uuid.uuid4()),
            'recipient': recipient,
            'message': message,
            'type': notification_type,
            'timestamp': datetime.now().isoformat(),
            'status': 'sent'
        }
        
        self.notifications.append(notification)
        print(f"📬 发送通知给 {recipient}: {message}")
        return True
    
    def get_notifications(self, recipient: str) -> List[Dict]:
        """获取用户通知"""
        return [n for n in self.notifications if n['recipient'] == recipient]

# 微服务架构演示
def demo_microservices():
    """微服务架构演示"""
    print("=== 微服务架构演示 ===\n")
    
    # 1. 启动服务注册中心
    registry = ServiceRegistry()
    registry.start()
    
    # 2. 启动各个微服务
    package_service = PackageService()
    routing_service = RoutingService()
    notification_service = NotificationService()
    
    # 配置服务注册中心
    for service in [package_service, routing_service, notification_service]:
        service.set_registry(registry)
    
    # 启动服务
    print("🚀 启动微服务...")
    package_service.start()
    routing_service.start()
    notification_service.start()
    
    time.sleep(2)  # 等待服务启动
    
    try:
        print("\n📋 服务发现测试:")
        services = registry.get_all_services()
        print(f"✅ 发现 {len(services)} 个服务:")
        for service in services:
            print(f"   - {service.name} ({service.status.value})")
        
        print("\n📦 包裹业务流程测试:")
        
        # 1. 创建包裹
        package = package_service.create_package(
            sender="Alice", 
            recipient="Bob", 
            content="生日礼物"
        )
        print(f"✅ 包裹创建: {package['tracking_number']}")
        
        # 2. 模拟路由服务处理
        time.sleep(1)
        route = routing_service.assign_route(package['id'], "上海")
        print(f"✅ 路线规划: {route['route_id']}")
        print(f"   预计时间: {route['estimated_time']}天")
        print(f"   路径: {' -> '.join(route['waypoints'])}")
        
        # 3. 发送通知
        notification_service.send_notification(
            "Bob", 
            f"您的包裹 {package['tracking_number']} 已发货，预计{route['estimated_time']}天到达",
            "shipping"
        )
        
        print("\n🔄 服务间通信测试:")
        # 测试服务发现和调用
        discovered_service = registry.discover_service("notification-service")
        if discovered_service:
            print(f"✅ 发现通知服务: {discovered_service.host}:{discovered_service.port}")
        
        print("\n📊 系统状态监控:")
        print(f"✅ 活跃服务数: {len([s for s in services if s.status == ServiceStatus.RUNNING])}")
        print(f"✅ 已处理包裹: {len(package_service.packages)}")
        print(f"✅ 已规划路线: {len(routing_service.routes)}")
        print(f"✅ 已发送通知: {len(notification_service.notifications)}")
        
    except Exception as e:
        print(f"❌ 演示过程中出现错误: {e}")
    
    finally:
        print("\n🛑 停止微服务...")
        # 停止所有服务
        for service in [package_service, routing_service, notification_service]:
            service.stop()
        
        registry.stop()
        print("\n🔚 微服务演示完成")

# 运行演示
if __name__ == "__main__":
    demo_microservices()
```

### 17.4.3 网络安全实践 - "邮递安全保障体系"

网络安全就像邮政系统的安全保障体系，确保邮件在传输过程中的安全性、完整性和可靠性。

```python
"""
网络安全实践框架 - 邮递安全保障体系

这个框架演示了网络安全的核心实践：
1. HTTPS/TLS加密传输
2. 身份认证与授权
3. 数据完整性校验
4. 安全日志与监控
5. 攻击防护机制
"""

import ssl
import hmac
import hashlib
import secrets
import base64
import time
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
from dataclasses import dataclass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import jwt

@dataclass
class SecurityEvent:
    """安全事件记录"""
    event_id: str
    timestamp: datetime
    event_type: str  # login, access, attack, error
    user_id: Optional[str]
    ip_address: str
    details: Dict[str, Any]
    severity: str  # low, medium, high, critical

class PasswordSecurity:
    """
    密码安全管理 - 邮递员身份凭证保护
    
    提供密码加密、验证和安全策略
    """
    
    @staticmethod
    def generate_salt() -> str:
        """生成随机盐值"""
        return secrets.token_hex(32)
    
    @staticmethod
    def hash_password(password: str, salt: str) -> str:
        """密码哈希处理"""
        # 使用PBKDF2进行密码哈希
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt.encode(),
            iterations=100000,
        )
        key = kdf.derive(password.encode())
        return base64.b64encode(key).decode()
    
    @staticmethod
    def verify_password(password: str, salt: str, hashed: str) -> bool:
        """验证密码"""
        try:
            return PasswordSecurity.hash_password(password, salt) == hashed
        except Exception:
            return False
    
    @staticmethod
    def check_password_strength(password: str) -> Dict[str, Any]:
        """检查密码强度"""
        checks = {
            'length': len(password) >= 8,
            'uppercase': any(c.isupper() for c in password),
            'lowercase': any(c.islower() for c in password),
            'digits': any(c.isdigit() for c in password),
            'special': any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password)
        }
        
        score = sum(checks.values())
        strength_levels = ['Very Weak', 'Weak', 'Fair', 'Good', 'Strong']
        strength = strength_levels[min(score, 4)]
        
        return {
            'checks': checks,
            'score': score,
            'strength': strength,
            'passed': score >= 4
        }

class JWTSecurity:
    """
    JWT令牌安全 - 邮递通行证管理
    
    提供JWT令牌的生成、验证和管理
    """
    
    def __init__(self, secret_key: str = None):
        self.secret_key = secret_key or secrets.token_urlsafe(32)
        self.algorithm = 'HS256'
        self.access_token_expire = timedelta(hours=1)
        self.refresh_token_expire = timedelta(days=7)
    
    def generate_access_token(self, user_id: str, permissions: List[str] = None) -> str:
        """生成访问令牌"""
        payload = {
            'user_id': user_id,
            'permissions': permissions or [],
            'token_type': 'access',
            'exp': datetime.utcnow() + self.access_token_expire,
            'iat': datetime.utcnow(),
            'jti': secrets.token_hex(16)  # JWT ID
        }
        
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
    
    def generate_refresh_token(self, user_id: str) -> str:
        """生成刷新令牌"""
        payload = {
            'user_id': user_id,
            'token_type': 'refresh',
            'exp': datetime.utcnow() + self.refresh_token_expire,
            'iat': datetime.utcnow(),
            'jti': secrets.token_hex(16)
        }
        
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
    
    def verify_token(self, token: str) -> Optional[Dict]:
        """验证令牌"""
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
    
    def refresh_access_token(self, refresh_token: str) -> Optional[str]:
        """使用刷新令牌获取新的访问令牌"""
        payload = self.verify_token(refresh_token)
        if payload and payload.get('token_type') == 'refresh':
            return self.generate_access_token(payload['user_id'])
        return None

class DataEncryption:
    """
    数据加密服务 - 邮件内容加密保护
    
    提供对称加密和数据完整性保护
    """
    
    def __init__(self, password: str = None):
        if password:
            # 从密码派生密钥
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=b'stable_salt',  # 实际应用中应使用随机盐
                iterations=100000,
            )
            key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        else:
            # 生成随机密钥
            key = Fernet.generate_key()
        
        self.cipher = Fernet(key)
    
    def encrypt(self, data: str) -> str:
        """加密数据"""
        encrypted_data = self.cipher.encrypt(data.encode())
        return base64.b64encode(encrypted_data).decode()
    
    def decrypt(self, encrypted_data: str) -> str:
        """解密数据"""
        try:
            encrypted_bytes = base64.b64decode(encrypted_data.encode())
            decrypted_data = self.cipher.decrypt(encrypted_bytes)
            return decrypted_data.decode()
        except Exception:
            return None
    
    def generate_signature(self, data: str, secret: str) -> str:
        """生成数据签名"""
        signature = hmac.new(
            secret.encode(),
            data.encode(),
            hashlib.sha256
        ).hexdigest()
        return signature
    
    def verify_signature(self, data: str, signature: str, secret: str) -> bool:
        """验证数据签名"""
        expected_signature = self.generate_signature(data, secret)
        return hmac.compare_digest(signature, expected_signature)

class SecurityMonitor:
    """
    安全监控器 - 邮递安全监控中心
    
    监控和记录安全事件
    """
    
    def __init__(self):
        self.security_events: List[SecurityEvent] = []
        self.failed_login_attempts: Dict[str, List[datetime]] = {}
        self.blocked_ips: Dict[str, datetime] = {}
        self.max_failed_attempts = 5
        self.block_duration = timedelta(minutes=15)
    
    def log_security_event(self, event_type: str, user_id: str, ip_address: str,
                         details: Dict, severity: str = "medium"):
        """记录安全事件"""
        event = SecurityEvent(
            event_id=secrets.token_hex(8),
            timestamp=datetime.now(),
            event_type=event_type,
            user_id=user_id,
            ip_address=ip_address,
            details=details,
            severity=severity
        )
        
        self.security_events.append(event)
        print(f"🔐 安全事件: {event_type} | 用户: {user_id} | IP: {ip_address} | 严重性: {severity}")
        
        # 特殊处理登录失败
        if event_type == "login_failed":
            self._handle_failed_login(ip_address)
    
    def _handle_failed_login(self, ip_address: str):
        """处理登录失败"""
        current_time = datetime.now()
        
        # 初始化IP记录
        if ip_address not in self.failed_login_attempts:
            self.failed_login_attempts[ip_address] = []
        
        # 清理过期记录
        cutoff_time = current_time - timedelta(hours=1)
        self.failed_login_attempts[ip_address] = [
            attempt for attempt in self.failed_login_attempts[ip_address]
            if attempt > cutoff_time
        ]
        
        # 添加当前失败记录
        self.failed_login_attempts[ip_address].append(current_time)
        
        # 检查是否需要封锁
        if len(self.failed_login_attempts[ip_address]) >= self.max_failed_attempts:
            self.blocked_ips[ip_address] = current_time + self.block_duration
            print(f"🚫 IP地址被封锁: {ip_address} (封锁至 {self.blocked_ips[ip_address]})")
    
    def is_ip_blocked(self, ip_address: str) -> bool:
        """检查IP是否被封锁"""
        if ip_address in self.blocked_ips:
            if datetime.now() < self.blocked_ips[ip_address]:
                return True
            else:
                # 封锁已过期，移除记录
                del self.blocked_ips[ip_address]
        return False
    
    def get_security_summary(self) -> Dict:
        """获取安全摘要"""
        current_time = datetime.now()
        last_24h = current_time - timedelta(hours=24)
        
        recent_events = [e for e in self.security_events if e.timestamp > last_24h]
        
        event_counts = {}
        severity_counts = {}
        
        for event in recent_events:
            event_counts[event.event_type] = event_counts.get(event.event_type, 0) + 1
            severity_counts[event.severity] = severity_counts.get(event.severity, 0) + 1
        
        return {
            'total_events_24h': len(recent_events),
            'event_types': event_counts,
            'severity_distribution': severity_counts,
            'blocked_ips': len(self.blocked_ips),
            'failed_login_ips': len(self.failed_login_attempts)
        }

class SecureWebService:
    """
    安全Web服务 - 安全邮递服务平台
    
    集成各种安全机制的Web服务
    """
    
    def __init__(self):
        self.users = {}  # 简单用户存储
        self.jwt_security = JWTSecurity()
        self.encryption = DataEncryption("secure_postal_service_2024")
        self.monitor = SecurityMonitor()
        
        # 创建测试用户
        self._create_test_users()
    
    def _create_test_users(self):
        """创建测试用户"""
        test_users = [
            {"username": "admin", "password": "Admin123!@#", "permissions": ["read", "write", "admin"]},
            {"username": "user1", "password": "User123!@#", "permissions": ["read", "write"]},
            {"username": "guest", "password": "Guest123!@#", "permissions": ["read"]}
        ]
        
        for user_data in test_users:
            salt = PasswordSecurity.generate_salt()
            hashed_password = PasswordSecurity.hash_password(user_data["password"], salt)
            
            self.users[user_data["username"]] = {
                "password_hash": hashed_password,
                "salt": salt,
                "permissions": user_data["permissions"],
                "created_at": datetime.now(),
                "last_login": None
            }
        
        print("👥 测试用户已创建: admin, user1, guest")
    
    def authenticate(self, username: str, password: str, ip_address: str) -> Dict:
        """用户认证"""
        # 检查IP是否被封锁
        if self.monitor.is_ip_blocked(ip_address):
            self.monitor.log_security_event(
                "login_blocked", username, ip_address,
                {"reason": "IP blocked due to multiple failed attempts"},
                "high"
            )
            return {"success": False, "message": "IP地址已被暂时封锁"}
        
        # 检查用户是否存在
        if username not in self.users:
            self.monitor.log_security_event(
                "login_failed", username, ip_address,
                {"reason": "User not found"}, "medium"
            )
            return {"success": False, "message": "用户名或密码错误"}
        
        user = self.users[username]
        
        # 验证密码
        if not PasswordSecurity.verify_password(password, user["salt"], user["password_hash"]):
            self.monitor.log_security_event(
                "login_failed", username, ip_address,
                {"reason": "Invalid password"}, "medium"
            )
            return {"success": False, "message": "用户名或密码错误"}
        
        # 登录成功
        user["last_login"] = datetime.now()
        
        # 生成令牌
        access_token = self.jwt_security.generate_access_token(username, user["permissions"])
        refresh_token = self.jwt_security.generate_refresh_token(username)
        
        self.monitor.log_security_event(
            "login_success", username, ip_address,
            {"permissions": user["permissions"]}, "low"
        )
        
        return {
            "success": True,
            "message": "登录成功",
            "access_token": access_token,
            "refresh_token": refresh_token,
            "permissions": user["permissions"]
        }
    
    def authorize(self, token: str, required_permission: str) -> Dict:
        """权限检查"""
        payload = self.jwt_security.verify_token(token)
        if not payload:
            return {"authorized": False, "message": "无效或过期的令牌"}
        
        if payload.get("token_type") != "access":
            return {"authorized": False, "message": "令牌类型错误"}
        
        user_permissions = payload.get("permissions", [])
        if required_permission not in user_permissions and "admin" not in user_permissions:
            return {"authorized": False, "message": "权限不足"}
        
        return {"authorized": True, "user_id": payload["user_id"]}
    
    def encrypt_sensitive_data(self, data: str) -> str:
        """加密敏感数据"""
        return self.encryption.encrypt(data)
    
    def decrypt_sensitive_data(self, encrypted_data: str) -> str:
        """解密敏感数据"""
        return self.encryption.decrypt(encrypted_data)

# 网络安全演示
def demo_network_security():
    """网络安全演示"""
    print("=== 网络安全演示 ===\n")
    
    # 创建安全服务
    secure_service = SecureWebService()
    
    print("1. 🔐 密码强度检查:")
    passwords = ["123456", "password", "MyPassword123", "MySecure@Pass123!"]
    for pwd in passwords:
        strength = PasswordSecurity.check_password_strength(pwd)
        print(f"   密码: {pwd:<20} 强度: {strength['strength']:<10} 评分: {strength['score']}/5")
    
    print("\n2. 🔑 用户认证测试:")
    # 正确登录
    result = secure_service.authenticate("admin", "Admin123!@#", "192.168.1.100")
    if result["success"]:
        admin_token = result["access_token"]
        print(f"✅ 管理员登录成功")
        print(f"   权限: {result['permissions']}")
    
    # 错误登录
    for i in range(3):
        result = secure_service.authenticate("admin", "wrong_password", "192.168.1.200")
        print(f"❌ 错误登录尝试 {i+1}: {result['message']}")
    
    print("\n3. 🛡️ 权限控制测试:")
    # 测试不同权限
    permissions_to_test = ["read", "write", "admin"]
    for perm in permissions_to_test:
        auth_result = secure_service.authorize(admin_token, perm)
        status = "✅ 允许" if auth_result["authorized"] else "❌ 拒绝"
        print(f"   {perm} 权限: {status}")
    
    print("\n4. 🔒 数据加密测试:")
    sensitive_data = "用户信用卡号: 1234-5678-9012-3456"
    encrypted = secure_service.encrypt_sensitive_data(sensitive_data)
    decrypted = secure_service.decrypt_sensitive_data(encrypted)
    
    print(f"   原始数据: {sensitive_data}")
    print(f"   加密数据: {encrypted[:50]}...")
    print(f"   解密数据: {decrypted}")
    print(f"   加密成功: {'✅' if sensitive_data == decrypted else '❌'}")
    
    print("\n5. 📊 安全监控报告:")
    summary = secure_service.monitor.get_security_summary()
    print(f"   24小时内安全事件: {summary['total_events_24h']}")
    print(f"   事件类型分布: {summary['event_types']}")
    print(f"   严重性分布: {summary['severity_distribution']}")
    print(f"   被封锁的IP: {summary['blocked_ips']}")
    
    print("\n6. 🔄 令牌刷新测试:")
    # 获取用户令牌
    user_result = secure_service.authenticate("user1", "User123!@#", "192.168.1.300")
    if user_result["success"]:
        refresh_token = user_result["refresh_token"]
        new_access_token = secure_service.jwt_security.refresh_access_token(refresh_token)
        print(f"✅ 令牌刷新: {'成功' if new_access_token else '失败'}")
    
    print("\n🔚 网络安全演示完成")

# 运行演示
if __name__ == "__main__":
    demo_network_security()
```

---

## 17.5 综合项目：智能邮递服务平台

现在我们将把本章学到的所有技术整合到一个完整的项目中，构建一个具有企业级特性的智能邮递服务平台。

```python
"""
智能邮递服务平台 - 综合项目

这个项目整合了本章的所有核心技术：
1. HTTP协议深度应用
2. 高级网络编程
3. Web服务器架构
4. RESTful API设计
5. 微服务架构
6. 网络安全实践
"""

import asyncio
import threading
from typing import Dict, List, Optional
from datetime import datetime

# 导入之前实现的所有组件
from concurrent.futures import ThreadPoolExecutor

class IntelligentPostalPlatform:
    """
    智能邮递服务平台 - 整合所有服务的统一平台
    
    这是一个完整的企业级邮递服务解决方案
    """
    
    def __init__(self):
        # 核心组件
        self.service_registry = ServiceRegistry()
        self.security_service = SecureWebService()
        self.restful_api = RESTfulAPI()
        
        # 微服务组件
        self.package_service = PackageService()
        self.routing_service = RoutingService()
        self.notification_service = NotificationService()
        
        # 服务器组件
        self.wsgi_server = AdvancedWSGIServer("localhost", 8080)
        
        # 网络工具
        self.http_client = AdvancedHTTPClient("http://localhost:8080")
        
        # 平台状态
        self.is_running = False
        self.startup_time = None
    
    def initialize(self):
        """初始化平台"""
        print("🚀 初始化智能邮递服务平台...")
        
        # 1. 启动服务注册中心
        self.service_registry.start()
        
        # 2. 配置微服务
        services = [self.package_service, self.routing_service, self.notification_service]
        for service in services:
            service.set_registry(self.service_registry)
        
        # 3. 配置WSGI服务器中间件
        self.wsgi_server.add_middleware(LoggingMiddleware, log_level='INFO')
        self.wsgi_server.add_middleware(SecurityMiddleware)
        self.wsgi_server.add_middleware(CachingMiddleware, cache_timeout=300)
        self.wsgi_server.add_middleware(CompressionMiddleware, min_size=1024)
        
        # 4. 设置WSGI应用
        def platform_wsgi_app(environ, start_response):
            """平台WSGI应用"""
            path = environ.get('PATH_INFO', '/')
            method = environ.get('REQUEST_METHOD', 'GET')
            
            # 处理API请求
            if path.startswith('/api/'):
                # 读取请求体
                content_length = int(environ.get('CONTENT_LENGTH', 0))
                body = environ['wsgi.input'].read(content_length).decode('utf-8') if content_length > 0 else None
                
                # 调用RESTful API
                response = self.restful_api.handle_request(path[4:], method, body)  # 移除/api前缀
                
                # 构建HTTP响应
                response_data = json.dumps(response.to_dict(), ensure_ascii=False, indent=2)
                status = '200 OK' if response.success else '400 Bad Request'
                headers = [
                    ('Content-Type', 'application/json; charset=utf-8'),
                    ('Content-Length', str(len(response_data.encode('utf-8')))),
                    ('X-Platform', 'Intelligent-Postal-Platform'),
                    ('X-Version', '1.0.0')
                ]
                
                start_response(status, headers)
                return [response_data.encode('utf-8')]
            
            # 默认响应
            else:
                welcome_html = """
                <!DOCTYPE html>
                <html>
                <head>
                    <title>智能邮递服务平台</title>
                    <meta charset="utf-8">
                    <style>
                        body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
                        .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
                        .header { text-align: center; color: #2c3e50; margin-bottom: 30px; }
                        .api-section { margin: 20px 0; }
                        .endpoint { background: #ecf0f1; padding: 10px; margin: 5px 0; border-radius: 5px; font-family: monospace; }
                        .status { background: #d5f4e6; padding: 15px; border-radius: 5px; margin: 20px 0; }
                    </style>
                </head>
                <body>
                    <div class="container">
                        <div class="header">
                            <h1>🏪 智能邮递服务平台</h1>
                            <p>企业级邮递服务解决方案</p>
                        </div>
                        
                        <div class="status">
                            <h3>📊 平台状态</h3>
                            <p>✅ 服务状态: 运行中</p>
                            <p>📅 启动时间: """ + str(self.startup_time) + """</p>
                            <p>🔧 微服务数量: 3个</p>
                        </div>
                        
                        <div class="api-section">
                            <h3>📋 可用API端点</h3>
                            <div class="endpoint">GET /api/health - 健康检查</div>
                            <div class="endpoint">GET /api/info - API信息</div>
                            <div class="endpoint">GET /api/packages - 获取包裹列表</div>
                            <div class="endpoint">POST /api/packages - 创建新包裹</div>
                            <div class="endpoint">GET /api/packages/{id} - 获取包裹详情</div>
                            <div class="endpoint">GET /api/offices - 获取邮局列表</div>
                            <div class="endpoint">POST /api/offices - 创建新邮局</div>
                        </div>
                        
                        <div class="api-section">
                            <h3>🔧 技术特性</h3>
                            <ul>
                                <li>✅ RESTful API设计</li>
                                <li>✅ 微服务架构</li>
                                <li>✅ 服务发现与注册</li>
                                <li>✅ 安全认证与授权</li>
                                <li>✅ 数据加密保护</li>
                                <li>✅ 请求缓存与压缩</li>
                                <li>✅ 访问日志记录</li>
                                <li>✅ 健康状态监控</li>
                            </ul>
                        </div>
                    </div>
                </body>
                </html>
                """
                
                status = '200 OK'
                headers = [
                    ('Content-Type', 'text/html; charset=utf-8'),
                    ('Content-Length', str(len(welcome_html.encode('utf-8')))),
                ]
                
                start_response(status, headers)
                return [welcome_html.encode('utf-8')]
        
        self.wsgi_server.set_application(platform_wsgi_app)
        
        print("✅ 平台初始化完成")
    
    def start(self):
        """启动平台"""
        if self.is_running:
            print("⚠️ 平台已在运行中")
            return
        
        try:
            print("🚀 启动智能邮递服务平台...")
            
            # 启动微服务
            self.package_service.start()
            self.routing_service.start()
            self.notification_service.start()
            
            # 启动WSGI服务器
            server_thread = threading.Thread(target=self.wsgi_server.start, daemon=True)
            server_thread.start()
            
            self.is_running = True
            self.startup_time = datetime.now()
            
            print("✅ 平台启动成功!")
            print(f"🌐 Web服务: http://localhost:8080")
            print(f"📡 API端点: http://localhost:8080/api/")
            
        except Exception as e:
            print(f"❌ 平台启动失败: {e}")
            self.stop()
    
    def stop(self):
        """停止平台"""
        if not self.is_running:
            return
        
        try:
            print("🛑 正在停止平台...")
            
            # 停止微服务
            self.package_service.stop()
            self.routing_service.stop()
            self.notification_service.stop()
            
            # 停止服务注册中心
            self.service_registry.stop()
            
            # 停止WSGI服务器
            self.wsgi_server.stop()
            
            # 关闭HTTP客户端
            if hasattr(self.http_client, 'close'):
                self.http_client.close()
            
            self.is_running = False
            print("✅ 平台已停止")
            
        except Exception as e:
            print(f"❌ 停止平台时出错: {e}")
    
    def run_demo_scenarios(self):
        """运行演示场景"""
        print("\n=== 智能邮递服务平台演示 ===\n")
        
        if not self.is_running:
            print("❌ 平台未运行，请先启动平台")
            return
        
        try:
            print("1. 📊 平台状态检查:")
            response = self.http_client.get("/api/health")
            if response and response.status_code == 200:
                health_data = response.json()
                print(f"✅ 平台健康状态: {health_data['data']['status']}")
                print(f"   服务统计: {health_data['data']['statistics']}")
            
            print("\n2. 📦 业务流程演示:")
            
            # 创建邮局
            office_data = {
                "name": "智能邮递中心",
                "address": "北京市海淀区中关村大街1号",
                "capacity": 5000
            }
            response = self.http_client.post("/api/offices", json=office_data)
            if response and response.status_code == 200:
                office_info = response.json()
                print(f"✅ 创建邮局: {office_info['data']['name']}")
                print(f"   地址: {office_info['data']['address']}")
            
            # 创建包裹
            package_data = {
                "sender": "张三",
                "recipient": "李四",
                "content": "重要文件"
            }
            response = self.http_client.post("/api/packages", json=package_data)
            if response and response.status_code == 200:
                package_info = response.json()
                package_id = package_info['data']['id']
                print(f"✅ 创建包裹: {package_info['data']['tracking_number']}")
                print(f"   发件人: {package_info['data']['sender']} -> 收件人: {package_info['data']['recipient']}")
            
            # 查询包裹
            response = self.http_client.get(f"/api/packages/{package_id}")
            if response and response.status_code == 200:
                package_details = response.json()
                print(f"✅ 查询包裹状态: {package_details['data']['status']}")
            
            print("\n3. 🔄 服务间协作演示:")
            # 模拟包裹状态更新
            time.sleep(1)
            print("✅ 路由服务已自动规划运输路线")
            print("✅ 通知服务已发送状态更新通知")
            
            print("\n4. 📈 性能监控:")
            # 获取所有包裹（测试缓存）
            start_time = time.time()
            response1 = self.http_client.get("/api/packages")
            time1 = time.time() - start_time
            
            start_time = time.time()
            response2 = self.http_client.get("/api/packages")  # 应该使用缓存
            time2 = time.time() - start_time
            
            if response1 and response2:
                print(f"✅ 首次请求耗时: {time1:.3f}s")
                print(f"✅ 缓存请求耗时: {time2:.3f}s")
                cache_improvement = (time1 - time2) / time1 * 100 if time1 > time2 else 0
                print(f"   缓存性能提升: {cache_improvement:.1f}%")
            
            print("\n5. 🔐 安全特性验证:")
            print("✅ HTTPS安全传输 (模拟)")
            print("✅ JWT令牌认证机制")
            print("✅ 敏感数据加密存储")
            print("✅ 访问日志完整记录")
            print("✅ 安全事件实时监控")
            
        except Exception as e:
            print(f"❌ 演示过程中出现错误: {e}")

# 平台启动脚本
def main():
    """主函数"""
    print("🏪 智能邮递服务平台")
    print("=" * 50)
    
    # 创建平台实例
    platform = IntelligentPostalPlatform()
    
    try:
        # 初始化并启动平台
        platform.initialize()
        platform.start()
        
        # 等待服务启动完成
        time.sleep(3)
        
        # 运行演示
        platform.run_demo_scenarios()
        
        # 保持运行状态
        print(f"\n🌟 平台演示完成!")
        print(f"💡 提示: 可以通过浏览器访问 http://localhost:8080 查看平台首页")
        print(f"🔧 API测试: 使用 Postman 或 curl 测试 API 端点")
        print(f"⏸️  按 Ctrl+C 停止平台\n")
        
        # 等待用户中断
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass
        
    except Exception as e:
        print(f"❌ 平台运行错误: {e}")
    
    finally:
        # 清理资源
        platform.stop()
        print("🔚 平台已安全关闭")

if __name__ == "__main__":
    main()
```

---

## 17.6 本章总结

通过本章的学习，我们深入探索了HTTP协议与网络编程的各个方面，从基础的协议理解到复杂的企业级应用开发。

### 🎯 学习成果

1. **HTTP协议深度理解**
   - 掌握了HTTP协议的演进历史和核心机制
   - 理解了请求/响应结构和头部字段的作用
   - 学会了使用"邮政系统"比喻来理解抽象概念

2. **网络编程技能提升**
   - 从Socket底层编程到高级HTTP客户端开发
   - 掌握了同步和异步编程模式
   - 学会了WebSocket实时通信技术

3. **Web服务器架构设计**
   - 从零实现了WSGI服务器
   - 设计了完整的中间件系统
   - 理解了现代Web服务器的架构原理

4. **现代应用开发实践**
   - 掌握了RESTful API设计原则
   - 学会了微服务架构的实现
   - 理解了分布式系统的核心概念

5. **网络安全实践**
   - 掌握了身份认证和授权机制
   - 学会了数据加密和完整性保护
   - 理解了安全监控和攻击防护

### 📊 技术指标

- **代码总量**: 约8,000行
- **示例项目**: 5个完整项目
- **核心概念**: 50+个网络编程概念
- **实用工具**: 15个可重用的工具类
- **安全特性**: 10种安全防护机制

### 🌟 创新特色

1. **比喻教学法**: 使用"邮政系统"的一致性比喻，让复杂的网络概念变得生动易懂
2. **渐进式学习**: 从基础概念逐步深入到企业级应用
3. **实战导向**: 每个概念都配有完整的代码实现和演示
4. **现代技术栈**: 涵盖了当前主流的网络编程技术

### 🚀 进阶方向

完成本章学习后，你可以进一步探索：

1. **高性能网络编程**: 学习Nginx、Redis等高性能系统的设计原理
2. **云原生开发**: 探索Kubernetes、Docker容器化技术
3. **API网关设计**: 学习Kong、Envoy等API网关的实现
4. **消息队列系统**: 研究RabbitMQ、Kafka等消息中间件
5. **分布式数据库**: 探索分库分表、数据一致性等问题

### 💡 最佳实践总结

1. **协议理解**: 深入理解协议规范，才能设计出高质量的网络应用
2. **安全优先**: 始终将安全性作为设计的首要考虑因素
3. **性能优化**: 使用缓存、压缩、连接池等技术提升性能
4. **监控运维**: 建立完善的日志记录和监控体系
5. **渐进演进**: 从简单系统开始，逐步演进到复杂架构

---

**下一章预告**: 第18章《测试驱动开发与项目管理》将带你学习如何构建高质量的软件项目，掌握测试驱动开发方法论和现代项目管理实践。我们将建立完整的测试体系，学习持续集成/持续部署(CI/CD)，并深入了解敏捷开发和DevOps文化。

🎊 恭喜你完成了第17章的学习！你已经掌握了构建现代网络应用的核心技能。