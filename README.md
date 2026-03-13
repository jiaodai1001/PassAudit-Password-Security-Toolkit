# PassAudit：密码安全分析工具

PassAudit 是一个开源的密码安全分析工具，用于评估用户密码的安全强度、检测弱密码模式，并生成高强度密码。本项目强调 **本地化分析与隐私保护**，所有密码检测均在本地完成，不会上传到任何服务器。

该项目适用于：

* 网络空间安全专业学生学习密码安全基础
* 开发者在系统中集成密码强度检测功能
* 安全研究人员进行密码安全研究

---

# 项目功能

## 1. 密码信息熵计算

通过密码长度与字符集分析，计算密码的信息熵，用于评估密码复杂度。

## 2. 弱密码模式检测

检测常见弱密码模式，例如：

* 连续数字（如 123456）
* 键盘序列（如 qwerty）
* 重复字符
* 常见弱密码结构

## 3. 泄露密码检测

通过哈希匹配的方式检测密码是否出现在已泄露密码数据集中。

本项目仅存储 **密码哈希值**，不会存储明文密码，从而保护用户隐私。

## 4. 安全密码生成

提供随机密码生成器，可以生成高强度且相对易记的密码组合。

## 5. 图形化界面

提供简单的 GUI 界面，使用户无需编程即可进行密码安全检测。

## 6. 可作为 Python 库调用

核心功能模块封装为 Python 库，可被其他程序调用。

---

# 软件界面示例

![GUI演示](images/gui_demo.png)

---

# 项目结构

```
PassAudit-Password-Security-Toolkit
│
├ core/                     # 核心功能模块
│   ├ entropy.py            # 密码熵计算
│   ├ pattern_detector.py   # 弱密码模式检测
│   ├ breach_checker.py     # 泄露密码检测
│   ├ password_generator.py # 密码生成器
│   └ security_analyzer.py  # 综合安全分析
│
├ datasets/                 # 弱密码哈希数据集
│
├ tests/                    # 测试代码
│
├ passaudit.py              # 命令行工具
├ gui_app.py                # 图形界面程序
│
├ images/                   # README截图资源
│   └ gui_demo.png
│
├ README.md
└ LICENSE
```

---

# 安装与运行

克隆项目：

```
git clone https://github.com/你的用户名/PassAudit-Password-Security-Toolkit.git
```

进入项目目录：

```
cd PassAudit-Password-Security-Toolkit
```

运行 GUI 程序：

```
python gui_app.py
```

---

# 示例代码

在 Python 中调用：

```python
from core.security_analyzer import analyze_password

result = analyze_password("P@ssw0rd123")
print(result)
```

示例输出：

```
Entropy: 72.1
Pattern detected: numeric sequence
Breach status: not found
Security score: medium
```

---

# 项目特点

* 完全本地化分析，保护用户隐私
* 支持密码强度评估
* 支持弱密码检测
* 支持泄露密码检测
* 支持安全密码生成
* 提供 GUI 与命令行工具

---

# 许可证

本项目基于 MIT License 开源。
