import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 生成模拟的宁德时代股价数据
print("正在生成模拟的宁德时代股价数据...")
dates = pd.date_range(start="2024-01-01", end="2025-01-01", freq='B')  # 工作日日期
n_days = len(dates)

# 模拟股价走势（围绕180元波动，带趋势）
np.random.seed(42)
base_price = 180
trend = np.linspace(0, 20, n_days)
noise = np.random.normal(0, 5, n_days).cumsum()
prices = base_price + trend + noise

stock_data = pd.DataFrame({'收盘': prices}, index=dates)

print("✅ 数据生成成功！")

# 2. 绘制股价走势图
plt.figure(figsize=(12, 6))
plt.plot(stock_data.index, stock_data['收盘'], color='#0066CC', linewidth=2, label='宁德时代 收盘价（模拟）')

plt.title("宁德时代股价走势（2024-2025）", fontsize=14)
plt.xlabel("日期", fontsize=12)
plt.ylabel("价格（元）", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()