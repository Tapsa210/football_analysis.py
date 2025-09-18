import zipfile
import pandas as pd
import matplotlib.pyplot as plt

# المسار الصحيح لملف ZIP
zip_path = r"C:\Users\osama\Desktop\archive.zip"

# مجلد الاستخراج
extract_path = r"C:\Users\osama\Desktop\archive"
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

# اسم الملف الذي ظهر لك داخل الـ ZIP
csv_path = r"C:\Users\osama\Desktop\archive\fbref_PL_2024-25.csv"

# قراءة البيانات
df = pd.read_csv(csv_path)

missing_values = df.isna().sum()
print("عدد القيم الناقصة لكل عمود:")
print(missing_values)
df = df.drop_duplicates()
df = df.dropna()   # يشيل أي صف فيه NaN
print(df.info())
print(df.head())

the_more_Nationilty=df.value_counts(["Nation"])
print(the_more_Nationilty)

# تجميع اللاعبين حسب الدولة وعدّهم
the_more_player = df.groupby("Nation")["Player"].count().sort_values(ascending=False)

print(the_more_player)
# مثال: حساب متوسط الأعمار لكل فريق
average_age = df.groupby("Squad")["Age"].mean()
print(average_age)

# مثال: مجموع الأهداف لكل فريق
goles = df.groupby("Squad")["Gls"].sum()
print(goles)

# مثال: أعلى اللاعبين تسجيلاً للأهداف
top_scorers = df.sort_values(by="Gls", ascending=False).head(10)
print(top_scorers[["Player", "Gls"]])
# مثال: اللاعبين الذين لديهم أكبر عدد من التمريرات الحاسمة
top_assists = df.sort_values(by="Ast", ascending=False).head(10)
print(top_assists[["Player", "Squad", "Ast"]])

# مثال: اللاعبين الذين لديهم أكبر عدد من المباريات
most_appearances = df.sort_values(by="MP",ascending=False).head(10)
print(most_appearances[["Player", "MP"]])

# مثال: اللاعبين الذين لديهم أعلى معدل أهداف لكل مباراة
df["Goals_per_match"] = df["Gls"] / df["MP"]
top_goal_rate = df.sort_values(by="Goals_per_match", ascending=False).head(10)
print(top_goal_rate[["Player", "Gls", "MP", "Goals_per_match"]])


# رسم بياني: توزيع الأعمار
plt.figure(figsize=(10, 6))
plt.hist(df["Age"], bins=20, color='blue', alpha=0.7)
plt.title("Players Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Players")
plt.grid(axis='y', alpha=0.75)
plt.show()

# رسم بياني: أعلى 10 هدافين (أعمدة أفقية عشان تكون أوضح)
plt.figure(figsize=(10, 6))
plt.barh(top_scorers["Player"], top_scorers["Gls"], color='orange')
plt.title("Top 10 Goal Scorers")
plt.xlabel("Goals")
plt.ylabel("Player")
plt.gca().invert_yaxis()  # عشان اللاعب الأكثر أهداف يطلع في الأعلى
plt.grid(axis='x', alpha=0.75)
plt.show()

# رسم بياني: أعلى 10 لاعبين في التمريرات الحاسمة (أعمدة أفقية عشان تكون أوضح)
plt.figure(figsize=(10, 6)) 
plt.barh(top_assists["Player"], top_assists["Ast"], color='green')
plt.title("Top 10 Assists")
plt.xlabel("Assists")
plt.ylabel("Player")
plt.gca().invert_yaxis()  # عشان اللاعب الأكثر تمريرات حاسمة يطلع في الأعلى
plt.grid(axis='x', alpha=0.75)
plt.show()
# رسم بياني: العلاقة بين العمر وعدد الأهداف
plt.figure(figsize=(10, 6))
plt.scatter(df["Age"], df["Gls"], alpha=0.6)
plt.title("Age vs Goals")
plt.xlabel("Age")
plt.ylabel("Goals")
plt.grid(alpha=0.3)
plt.show()
