import pandas as pd
import numpy as np
import statsmodels.api as sm

# 读房价数据
hpi = pd.read_csv("output/hpi_panel.csv")

# 构造 log(HPI) 和增长率
hpi = hpi.sort_values(["metro","date"])
hpi["log_hpi"] = np.log(hpi["hpi"])
hpi["dlog_hpi"] = hpi.groupby("metro")["log_hpi"].diff()

# ===== 下载就业数据（FRED 不需要API key）=====
emp = pd.read_csv("https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS")
emp.columns = ["date","payems"]
emp["date"] = pd.to_datetime(emp["date"])

# 转为季度
emp["year"] = emp["date"].dt.year
emp["q"] = (emp["date"].dt.month-1)//3 + 1
emp["date"] = emp["year"].astype(str)+"Q"+emp["q"].astype(str)

# 计算就业增长率
emp["log_emp"] = np.log(emp["payems"])
emp["dlog_emp"] = emp["log_emp"].diff()

emp = emp[["date","dlog_emp"]]

# 合并
df = hpi.merge(emp,on="date",how="inner")
df = df.dropna(subset=["dlog_hpi","dlog_emp"])

print("Regression sample size:",len(df))

# OLS回归
X = sm.add_constant(df["dlog_emp"])
y = df["dlog_hpi"]

model = sm.OLS(y,X).fit(cov_type="HC1")

print(model.summary())

# 保存结果
with open("output/regression_result.txt","w") as f:
    f.write(model.summary().as_text())

print("回归结果已保存到 output/regression_result.txt")
