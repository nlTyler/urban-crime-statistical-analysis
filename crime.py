import pandas as pd
import numpy as np

# Load dataset (replace with your path)
df = pd.read_csv("communities.data", na_values="?")
df = df.dropna()

#print("Shape:", df.shape)
#print("\nSummary Statistics:")
#display(df.describe())

import matplotlib.pyplot as plt
import seaborn as sns

urban_df = df[df["pctUrban"] > 0.5]

print("Original dataset size:", df.shape)
print("Urban dataset size:", urban_df.shape)

# Compare crime rates
df["UrbanCommunity"] = (df["pctUrban"] > 0.5).astype(int)

crime_compare = df.groupby("UrbanCommunity")["ViolentCrimesPerPop"].mean()

print("\nAverage Crime Rates:")
print(crime_compare)