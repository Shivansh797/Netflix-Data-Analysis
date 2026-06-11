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
    plt.title("Destribution Of Movies Vs TV Shows")
    plt.show()
    sns.set_style("whitegrid")
    sns.set_context("notebook")
    sns.histplot(data=data,x=data["rating"],color="green")
    plt.title("Rating Distrbution Chart")
    plt.show()
    plt.figure(figsize=(10,8))
    top15=data["listed_in"].value_counts().head(15).index
    sns.countplot(data=data[data["listed_in"].isin(top15)],y="listed_in",order=top15,palette="viridis",hue=data["type"])
    plt.title("Top 15 Content Genres On Netflix")
    plt.ylabel("Genre")
    plt.xlabel("Count")
    plt.tight_layout
    plt.show()
Dataset_Assessment()
Content_Analysis()
