# diagnostic.py
import os
import sys
import platform

print("🔍 VS Code 环境诊断报告")
print("=" * 60)
print(f"Python 可执行文件: {sys.executable}")
print(f"操作系统名称: {os.name}")
print(f"平台: {sys.platform}")
print(f"详细平台: {platform.platform()}")
print(f"当前工作目录: {os.getcwd()}")
print(f"PATH 环境变量前3项:")
for i, path in enumerate(os.environ['PATH'].split(os.pathsep)[:3]):
    print(f"  {i+1}. {path}")
print("=" * 60)

# 检查关键特征
if 'wsl' in sys.executable.lower() or 'ubuntu' in sys.executable.lower():
    print("❌ 确定在 WSL 环境中运行")
elif 'windows' in sys.platform.lower() or 'win' in sys.platform.lower():
    print("✅ 确定在 Windows 环境中运行")
else:
    print("⚠️  无法确定运行环境")