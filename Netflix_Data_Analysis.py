import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\netflix_titles.csv")
def Dataset_Assessment():
    print(data.head())
    print(data.dtypes)
    print(data.value_counts().sum())    
    print(data.isnull().sum())          #4307 Null Values Present (2634-director,825-cast,831-country,10-date_added,4-rating and 3-duration)
    dup=data[data.duplicated()]
    print(dup)                          #No Duplicate Values Present.  
def Content_Analysis():
    global data
    print(data["type"].value_counts())
    print(data["listed_in"].value_counts())
    data["rating"]=data["rating"].fillna(data["rating"].mode()[0])
    print(data.isnull().sum())
    print(data["rating"].value_counts())
    count=data["type"].value_counts()
    plt.pie(count,labels=count.index,autopct="%1.1f",colors=("orange","blue"))
    plt.title("Distribution Of Movies Vs TV Shows")
    plt.show()
    sns.set_style("whitegrid")
    sns.set_context("notebook")
    sns.histplot(data=data,x=data["rating"],color="green")
    plt.xlabel("Rating Type")
    plt.ylabel("No. Of Shows")
    plt.title("Rating Distribution Chart")
    plt.show()
    plt.figure(figsize=(10,8))
    top15=data["listed_in"].value_counts().head(15).index
    sns.countplot(data=data[data["listed_in"].isin(top15)],y="listed_in",order=top15,palette="viridis",hue=data["type"])
    plt.title("Top 15 Content Genres On Netflix")
    plt.ylabel("Genre")
    plt.xlabel("No. Of Shows Released")
    plt.tight_layout
    plt.show()
def Time_Based_Analysis():
    global data
    print(data["release_year"].value_counts())
    data["duration"]=data["duration"].fillna(data["duration"].mode()[0])
    print(data.isnull().sum())
    sns.set_style("whitegrid")
    sns.set_context("notebook")
    plt.figure(figsize=(10,8))
    top18=data["release_year"].value_counts().head(18).index
    sns.countplot(data=data[data["release_year"].isin(top18)],y=data["release_year"],order=top18,palette="viridis",hue=data["type"])
    plt.title("Top 18 Years Which Delivered Highest No. Of Shows")
    plt.ylabel("Year")
    plt.xlabel("No. Of Shows Released")
    plt.tight_layout
    plt.show()
    plt.figure(figsize=(10,8))
    top5=data["duration"].value_counts().head(5).index
    sns.countplot(data=data[data["duration"].isin(top5)],x=data["duration"],order=top5,palette="viridis",hue=data["type"])
    plt.title("Most Common Duration Of Shows On Netflix")
    plt.xlabel("Duration")
    plt.ylabel("No. Of Shows")
    plt.show()
def Geographic_Analysis():
    global data
    data.dropna(subset=["country"],inplace=True)
    print(data.isnull().sum())
    top10=data["country"].value_counts().head(10).index
    sns.countplot(data=data[data["country"].isin(top10)],y=data["country"],order=top10,palette="viridis",hue=data["type"])
    plt.title("Top 10 Countries Which Produces Highest No. Of Shows On Netflix")
    plt.xlabel("No. Of Shows")
    plt.ylabel("Country")
    plt.show()
Dataset_Assessment()
Content_Analysis()
Time_Based_Analysis()
Geographic_Analysis()