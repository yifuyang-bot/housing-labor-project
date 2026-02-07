import pandas as pd
import matplotlib.pyplot as plt

# 读取面板数据
df = pd.read_csv("output/hpi_panel.csv")

# 选择几个典型大城市
metros = [
    "Boston, MA (MSAD)",
    "Baltimore-Columbia-Towson, MD",
    "Sacramento-Roseville-Folsom, CA",
    "Salt Lake City-Murray, UT"
]

df_sub = df[df["metro"].isin(metros)].copy()

# 把季度转为时间（方便画图）
df_sub["year"] = df_sub["date"].str[:4].astype(int)
df_sub["q"] = df_sub["date"].str[-1].astype(int)
df_sub["time"] = df_sub["year"] + (df_sub["q"]-1)/4

# 画图
plt.figure(figsize=(10,6))

for m in metros:
    temp = df_sub[df_sub["metro"]==m]
    plt.plot(temp["time"], temp["hpi"], label=m)

plt.xlabel("Year")
plt.ylabel("House Price Index (FHFA)")
plt.title("Housing Price Trends Across Major US Metro Areas")
plt.legend()
plt.tight_layout()

plt.savefig("output/hpi_trends.png", dpi=150)
print("图已保存到 output/hpi_trends.png")
