#import pandas as pd
#import matplotlib.pyplot as plt
# Load Dataset
#df = pd.read_csv("AI_Resume_Screening-selected-columns.csv")
# 1. Display First 5 Records
# print(df.head())
# 2. Dataset Information
# print(df.info())
# 3. Check Missing Values
# print(df.isnull().sum())
# 4. Check Duplicate Records
# print(df.duplicated().sum())
# 5. Recruiter Decision Count
# print(df["Recruiter Decision"].value_counts())
# 6. Experience Statistics
# print(df["Experience (Years)"].describe())
# 7. Education Distribution
# ==========================

# print(df["Education"].value_counts())


# ==========================
# 8. Job Role Distribution
# ==========================

# print(df["Job Role"].value_counts())


# ==========================
# 9. Hire vs Reject Graph
# ==========================

# df["Recruiter Decision"].value_counts().plot(kind="bar")

# plt.title("Hire vs Reject Candidates")
# plt.xlabel("Decision")
# plt.ylabel("Number of Candidates")

# plt.show()


# ==========================
# 10. Average Experience
#     by Recruiter Decision
# ==========================

# df.groupby("Recruiter Decision")["Experience (Years)"].mean().plot(kind="bar")

# plt.title("Average Experience by Recruiter Decision")
# plt.xlabel("Recruiter Decision")
# plt.ylabel("Average Experience")

# plt.show()


# ==========================
# 11. Education Distribution Graph
# ==========================

#df["Education"].value_counts().plot(kind="bar")

#plt.title("Education Distribution")
#plt.xlabel("Education")
#plt.ylabel("Number of Candidates")

#plt.show()
#import pandas as pd
#import matplotlib.pyplot as plt

#df = pd.read_csv("AI_Resume_Screening-selected-columns.csv")

#df["Job Role"].value_counts().plot(kind="bar")

#plt.title("Job Role Distribution")
#plt.xlabel("Job Role")
#plt.ylabel("Number of Candidates")

#plt.show()
#import pandas as pd
#import matplotlib.pyplot as plt

#df = pd.read_csv("AI_Resume_Screening-selected-columns.csv")

#pd.crosstab(
#    df["Education"],
#    df["Recruiter Decision"]
#).plot(kind="bar")

#plt.title("Education vs Recruiter Decision")
#plt.xlabel("Education")
#plt.ylabel("Number of Candidates")

#plt.show()
#import pandas as pd
#import matplotlib.pyplot as plt

#df = pd.read_csv("AI_Resume_Screening-selected-columns.csv")

#pd.crosstab(
 #   df["Job Role"],
 #   df["Recruiter Decision"]
#).plot(kind="bar")

#plt.title("Job Role vs Recruiter Decision")
#plt.xlabel("Job Role")
#plt.ylabel("Number of Candidates")

#plt.show()
#import pandas as pd

#df = pd.read_csv("AI_Resume_Screening-selected-columns.csv")

#df["Skill Count"] = df["Skills"].apply(
#    lambda x: len(str(x).split(","))
#)

#print(df["Skill Count"].describe())
# Skill Count vs Recruiter Decision

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("AI_Resume_Screening-selected-columns.csv")

# # Create Skill Count column
# df["Skill Count"] = df["Skills"].apply(lambda x: len(str(x).split(","))
# )


# pd.crosstab(
#     df["Skill Count"],
#     df["Recruiter Decision"]
# ).plot(kind="bar")

# plt.title("Skill Count vs Recruiter Decision")
# plt.xlabel("Number of Skills")
# plt.ylabel("Number of Candidates")

# plt.show()
# ==========================================
# EDA - Job Role Distribution
# ==========================================

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("AI_Resume_Screening-selected-columns.csv")

# df["Job Role"].value_counts().plot(kind="bar")

# plt.title("Job Role Distribution")
# plt.xlabel("Job Role")
# plt.ylabel("Number of Candidates")

# plt.show()
# ==========================================
# EDA - Recruiter Decision Percentage
# ==========================================

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("AI_Resume_Screening-selected-columns.csv")

# df["Recruiter Decision"].value_counts().plot(
#     kind="pie",
#     autopct="%1.1f%%"
# )

# plt.title("Recruiter Decision Percentage")
# plt.ylabel("")

# plt.show()
# ==========================================
# EDA - Top Skills Frequency
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("AI_Resume_Screening-selected-columns.csv")

all_skills = ",".join(df["Skills"].astype(str))
skill_list = [skill.strip() for skill in all_skills.split(",")]

skill_counts = pd.Series(skill_list).value_counts().head(10)

skill_counts.plot(kind="bar")

plt.title("Top 10 Most Common Skills")
plt.xlabel("Skills")
plt.ylabel("Frequency")

plt.show()