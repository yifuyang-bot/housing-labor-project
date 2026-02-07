import pandas as pd
import numpy as np
import os

IN_PATH = "data/hpi_at_metro.csv"
os.makedirs("output", exist_ok=True)

df = pd.read_csv(IN_PATH, header=None)
df.columns = ["metro", "cbsa", "year", "quarter", "v4", "v5"]

print("Raw shape:", df.shape)
print("Example row:\n", df.iloc[0])

# 转 year/quarter
df["year"] = pd.to_numeric(df["year"], errors="coerce")
df["quarter"] = pd.to_numeric(df["quarter"], errors="coerce")

# 计算 v4 和 v5 哪个更像“指数”（可转成数字的比例更高）
v4_num = pd.to_numeric(df["v4"], errors="coerce")
v5_num = pd.to_numeric(df["v5"], errors="coerce")

v4_rate = v4_num.notna().mean()
v5_rate = v5_num.notna().mean()

print(f"Numeric rate v4: {v4_rate:.3f} | v5: {v5_rate:.3f}")

# 选择数值比例更高的当 hpi
if v5_rate >= v4_rate:
    df["hpi"] = v5_num
    chosen = "v5"
else:
    df["hpi"] = v4_num
    chosen = "v4"

print("Chosen HPI column:", chosen)

# 过滤合法行
df = df[df["year"].between(1975, 2100)]
df = df[df["quarter"].isin([1,2,3,4])]
df = df.dropna(subset=["metro","cbsa","year","quarter","hpi"]).copy()

df["date"] = df["year"].astype(int).astype(str) + "Q" + df["quarter"].astype(int).astype(str)

out = df[["metro","cbsa","date","hpi"]].sort_values(["metro","date"])
out.to_csv("output/hpi_panel.csv", index=False)

print("\n=== 成功生成面板数据 ===")
print(out.head())
print("\n总行数:", len(out))
print("\nHPI统计:")
print(out["hpi"].describe())