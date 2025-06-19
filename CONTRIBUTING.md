# 贡献指南

感谢您对 **GenAI-Python-Book** 项目的关注！我们欢迎各种形式的贡献，包括但不限于内容改进、代码优化、错误修正、新功能建议等。

## 🤝 贡献方式

### 📝 内容贡献

#### 1. 错误修正
- **文字错误**: 拼写、语法、术语不准确
- **代码错误**: 语法错误、逻辑错误、运行失败
- **概念错误**: 技术概念解释不准确或过时

#### 2. 内容改进
- **教学方法**: 提出更好的教学方法或比喻
- **代码示例**: 提供更清晰、更实用的代码示例
- **练习题**: 设计更有挑战性的练习题
- **项目案例**: 分享更贴近实际的项目案例

#### 3. 新内容建议
- **新章节**: 建议增加新的技术主题
- **新特性**: 建议增加Python新版本特性
- **新工具**: 建议集成新的开发工具或库

### 💻 技术贡献

#### 1. 代码质量
- **代码重构**: 改进代码结构和可读性
- **性能优化**: 提升代码执行效率
- **类型注解**: 添加或改进类型注解
- **文档字符串**: 完善函数和类的文档

#### 2. 测试用例
- **单元测试**: 为代码示例添加测试用例
- **集成测试**: 测试完整的项目案例
- **性能测试**: 测试代码性能和资源使用

#### 3. 工具开发
- **自动化脚本**: 开发项目管理和质量检查脚本
- **可视化工具**: 创建图表、动画、交互式演示
- **在线平台**: 开发Web版的学习平台

## 📋 贡献流程

### 1. 准备工作

#### Fork 项目
```bash
# 1. 在GitHub上Fork项目到您的账户
# 2. 克隆Fork的项目到本地
git clone https://github.com/youngzs/GenAI-Python-Book.git
cd GenAI-Python-Book

# 3. 添加上游仓库
git remote add upstream https://github.com/youngzs/GenAI-Python-Book.git
```

#### 环境搭建
```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 安装开发依赖
pip install -r requirements-dev.txt
```

### 2. 开发流程

#### 创建分支
```bash
# 从main分支创建新的特性分支
git checkout -b feature/your-feature-name

# 或者修复bug的分支
git checkout -b fix/your-bug-fix
```

#### 进行修改
- 根据贡献类型进行相应的修改
- 确保代码符合项目的编码规范
- 运行测试确保没有破坏现有功能

#### 代码规范检查
```bash
# 代码格式化
black .

# 代码风格检查
flake8 .

# 类型检查
mypy .

# 运行测试
pytest
```

### 3. 提交更改

#### 提交代码
```bash
# 添加修改的文件
git add .

# 提交修改（使用有意义的提交信息）
git commit -m "feat: 添加第10章数据结构内容"

# 或者
git commit -m "fix: 修复第8章网络编程示例的连接错误"
```

#### 推送到远程仓库
```bash
git push origin feature/your-feature-name
```

### 4. 创建 Pull Request

1. 在GitHub上访问您的Fork仓库
2. 点击 "New Pull Request"
3. 选择您的特性分支
4. 填写PR标题和描述
5. 提交PR等待审核

## 📝 提交信息规范

我们使用[约定式提交](https://www.conventionalcommits.org/zh-hans/v1.0.0/)规范：

### 提交类型
- `feat`: 新功能
- `fix`: 错误修复
- `docs`: 文档更新
- `style`: 代码格式（不影响代码运行的变动）
- `refactor`: 重构（既不是新增功能，也不是修改bug的代码变动）
- `test`: 增加测试
- `chore`: 构建过程或辅助工具的变动

### 示例
```
feat: 添加第10章数据结构与算法内容
fix: 修复第8章HTTP服务器示例的端口绑定问题
docs: 更新README中的安装说明
style: 格式化第9章代码示例
refactor: 重构数据库连接池实现
test: 为第7章OOP示例添加单元测试
chore: 更新依赖版本
```

## 🔍 代码审核标准

### 内容质量
- **技术准确性**: 确保技术概念和代码实现正确
- **教学逻辑**: 内容组织合理，循序渐进
- **语言表达**: 清晰易懂，符合目标读者水平
- **示例质量**: 代码可运行，注释详细

### 代码质量
- **可读性**: 代码结构清晰，命名规范
- **可维护性**: 模块化设计，易于扩展
- **性能**: 考虑执行效率和资源使用
- **安全性**: 避免安全漏洞和不良实践

### 文档质量
- **完整性**: 包含必要的说明和示例
- **准确性**: 与代码实现保持一致
- **格式**: 遵循项目的文档格式规范

## 🏷️ Issue 标签说明

### 类型标签
- `bug`: 错误报告
- `enhancement`: 功能增强
- `documentation`: 文档相关
- `question`: 问题咨询
- `help wanted`: 寻求帮助
- `good first issue`: 适合新手的问题

### 优先级标签
- `priority: high`: 高优先级
- `priority: medium`: 中优先级
- `priority: low`: 低优先级

### 状态标签
- `status: in progress`: 进行中
- `status: blocked`: 被阻塞
- `status: needs review`: 需要审核

## 🎯 贡献建议

### 对于新贡献者
1. **从小做起**: 先修复简单的错误或改进文档
2. **阅读现有内容**: 了解项目的写作风格和技术水平
3. **参与讨论**: 在Issue中提问和讨论
4. **关注反馈**: 积极响应维护者的反馈

### 对于经验丰富的贡献者
1. **技术深度**: 贡献更深入的技术内容
2. **工具开发**: 开发提升项目质量的工具
3. **指导新手**: 帮助新贡献者快速上手
4. **架构设计**: 参与项目架构和标准的讨论

## 🎉 贡献者认可

我们会在以下地方认可贡献者的努力：

- **README.md**: 在致谢部分列出主要贡献者
- **CONTRIBUTORS.md**: 详细记录所有贡献者
- **发布说明**: 在版本发布时感谢贡献者
- **社交媒体**: 在项目社交媒体上分享贡献者的工作

## 📞 联系方式

如果您有任何问题或建议，可以通过以下方式联系我们：

- 📧 **邮箱**: [your-email@example.com]
- 🐛 **Issues**: [GitHub Issues](https://github.com/youngzs/GenAI-Python-Book/issues)
- 💬 **讨论**: [GitHub Discussions](https://github.com/youngzs/GenAI-Python-Book/discussions)

## 📄 行为准则

请注意，本项目遵循[贡献者公约](https://www.contributor-covenant.org/zh-cn/version/2/1/code_of_conduct/)。参与本项目即表示您同意遵守其条款。

---

再次感谢您的贡献！您的每一份努力都让这个项目变得更好。🙏 