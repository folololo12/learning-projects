import pandas as pd
import seaborn as sns
import matplotlib.pyplot as mat

df = pd.read_csv("netflix_titles.csv")

#basid data
print(df.head())
print(df.info())
print(df.describe())
#trying out some stuff
print(df.isnull().sum())
print(df["type"].value_counts())
print(df["country"].value_counts().head(10))
#creating charts
sns.countplot(x="type", data=df)
mat.title("Movies vs TV Shows")
mat.xlabel("Type")
mat.ylabel("Count")
mat.show()
top_countries = df["country"].value_counts().head(10)

sns.barplot(x=top_countries.values, y=top_countries.index)
mat.title("Top 10 Countries Producing Netflix Content")
mat.xlabel("Number of Titles")
mat.ylabel("Country")
mat.show()

top_directors = df["director"].value_counts().head(10)
sns.barplot(x=top_directors.values, y =top_directors.index)
mat.title("Top 10 Directors")
mat.xlabel("how many movies")
mat.ylabel("directors")
mat.show()
