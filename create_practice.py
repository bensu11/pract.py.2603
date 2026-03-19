import os

# ====================== 你只需要改这里 ======================
# 你的 GitHub 练习仓库根目录
root_dir = r"C:\Users\lenovo\Desktop\Github\pract.py.2603"

# 目录名 + 该目录下要创建的练习文件
practice = {
    "01_基础语法": [
        "01_hello.py",
        "02_变量.py",
        "03_输入输出.py",
        "04_数字运算.py",
        "05_字符串.py"
    ],
    "02_条件判断": [
        "01_if_else.py",
        "02_多条件.py",
        "03_成绩判断.py",
        "04_奇偶判断.py"
    ],
    "03_循环": [
        "01_for循环.py",
        "02_while循环.py",
        "03_break_continue.py",
        "04_九九乘法表.py"
    ],
    "04_函数": [
        "01_定义函数.py",
        "02_带参数.py",
        "03_return返回值.py",
        "04_计算器函数.py"
    ]
}
# ==========================================================

os.makedirs(root_dir, exist_ok=True)

for folder, files in practice.items():
    folder_path = os.path.join(root_dir, folder)
    os.makedirs(folder_path, exist_ok=True)

    for fname in files:
        file_path = os.path.join(folder_path, fname)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {fname}\n")
            f.write(f"# 练习文件，来自 GitHub 管理\n\n")
            f.write("print('开始练习')\n")

print("✅ 全部练习文件夹 + 文件创建完成！")