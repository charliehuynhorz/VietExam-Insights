import pandas as pd

df = pd.read_csv("F:\VietExam Insights\data\processed\\viet_national_exam_scores.csv")
for col in ["Toán", "Vật lý", "Hóa học", "Sinh học"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df_A = df.dropna(subset=["Toán", "Vật lý", "Hóa học"]).copy()
df_A["Tổng điểm"] = df_A["Toán"] + df_A["Vật lý"] + df_A["Hóa học"]
df_B = df.dropna(subset=["Toán", "Hóa học", "Sinh học"]).copy()
df_B["Tổng điểm"] = df_B["Toán"] + df_B["Hóa học"] + df_B["Sinh học"]
df_A.to_csv("F:\VietExam Insights\data\processed\\A_block.csv", index=False, encoding="utf-8-sig")
df_B.to_csv("F:\VietExam Insights\data\processed\\B_block.csv", index=False, encoding="utf-8-sig")
print("Completed")