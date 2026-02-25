import pandas as pd
import numpy as np

# Load dataset (replace with your path)
df = pd.read_csv("communities.data", na_values="?")
df = df.dropna()

print("Shape:", df.shape)
print("\nSummary Statistics:")
display(df.describe())

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure()
sns.histplot(df["ViolentCrimesPerPop"], kde=True)
plt.axvline(df["ViolentCrimesPerPop"].mean())
plt.title("Distribution of Violent Crimes Per Population")
plt.xlabel("Violent Crimes Per 100K")
plt.ylabel("Frequency")
plt.show()

df["log_crime"] = np.log1p(df["ViolentCrimesPerPop"])

plt.figure()
sns.histplot(df["log_crime"], kde=True)
plt.title("Log-Transformed Violent Crime Distribution")
plt.show()

selected_vars = [
    "PctPopUnderPov",
    "perCapInc",
    "medIncome",
    "PctUnemployed",
    "PctNotHSGrad",
    "PctBSorMore",
    "PopDens",
    "pctUrban",
    "PctUsePubTrans",
    "PctPersDenseHous",
    "ViolentCrimesPerPop"
]

corr = df[selected_vars].corr()
corr["ViolentCrimesPerPop"].sort_values(ascending=False)

plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
plt.title("Correlation Heatmap")
plt.show()