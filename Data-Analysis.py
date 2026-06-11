import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\netflix_titles.csv")
script_directory = os.path.dirname(os.path.abspath(__file__))
save = os.path.join(script_directory, "Graphs_And_Charts")
if not os.path.exists(save):
        os.makedirs(save)
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
    plt.legend(bbox_to_anchor=(1,0.5))
    plt.title("Distribution Of Movies Vs TV Shows")
    plt.savefig(os.path.join(save,"TypeShow-PieChart.png"))
    plt.show()
    sns.set_style("whitegrid")
    sns.set_context("notebook")
    sns.histplot(data=data,x=data["rating"],color="green")
    plt.xlabel("Rating Type")
    plt.ylabel("No. Of Shows")
    plt.title("Rating Distribution Chart")
    plt.savefig(os.path.join(save,"Rating_Destribution.png"),dpi=300)
    plt.show()
    plt.figure(figsize=(10,8))
    top15=data["listed_in"].value_counts().head(15).index
    sns.countplot(data=data[data["listed_in"].isin(top15)],y="listed_in",order=top15,palette="viridis",hue=data["type"])
    plt.title("Top 15 Content Genres On Netflix")
    plt.ylabel("Genre")
    plt.xlabel("No. Of Shows Released")
    plt.legend(title="Type Of Show",bbox_to_anchor=(1.05,1),loc="upper left")
    plt.tight_layout()
    plt.savefig(os.path.join(save,"Top15_Genre.png"),dpi=300)
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
    plt.legend(title="Type Of Show",bbox_to_anchor=(0.8,0.6),loc="upper left")
    plt.tight_layout()
    plt.savefig(os.path.join(save,"Highest_producing_year.png"),dpi=300)
    plt.show()
    plt.figure(figsize=(10,8))
    top5=data["duration"].value_counts().head(5).index
    sns.countplot(data=data[data["duration"].isin(top5)],x=data["duration"],order=top5,palette="viridis",hue=data["type"])
    plt.title("Most Common Duration Of Shows On Netflix")
    plt.xlabel("Duration")
    plt.ylabel("No. Of Shows")
    plt.legend(title="Type Of Show",bbox_to_anchor=(0.8,1),loc="upper left")
    plt.savefig(os.path.join(save,"Most_Common_Duration.png"))
    plt.show()
def Geographic_Analysis():
    global data
    data.dropna(subset=["country"],inplace=True)
    print(data.isnull().sum())
    sns.set_style("whitegrid")
    top10=data["country"].value_counts().head(10).index
    sns.countplot(data=data[data["country"].isin(top10)],y=data["country"],order=top10,palette="viridis",hue=data["type"])
    plt.title("Top 10 Countries Which Produces Highest No. Of Shows On Netflix")
    plt.xlabel("No. Of Shows")
    plt.ylabel("Country")
    plt.legend(title="Type Of Show",bbox_to_anchor=(0.6,0.89),loc="upper left")
    plt.savefig(os.path.join(save,"Top_10_Countries.png"))
    plt.show()
def People_Analysis():
    global data
    data.dropna(subset=["director"],inplace=True)
    plt.figure(figsize=(10,6))
    sns.set_style("whitegrid")
    mdata=data[(data["type"]=="Movie") & (data["director"].notna())]
    topm=mdata["director"].value_counts().head(10).index
    plotm=mdata[mdata["director"].isin(topm)]
    sns.countplot(data=plotm,y="director",order=topm,palette="viridis")
    plt.title("Top 10 Movie Directors Of Netflix")
    plt.xlabel("No. Of Movies")
    plt.ylabel("Name Of Director")
    plt.savefig(os.path.join(save,"Top_10_Movie_Directors.png"))
    plt.show()
    tdata=data[(data["type"]=="TV Show") & (data["director"].notna())]
    topt=tdata["director"].value_counts().head(10).index
    plott=tdata[tdata["director"].isin(topt)]
    sns.countplot(data=plott,y="director",order=topt,palette="mako")
    plt.title("Top 10 TV Show Directors Of Netflix")
    plt.xlabel("No. Of TV Shows")
    plt.ylabel("Name Of Director")
    plt.savefig(os.path.join(save,"Top_10_TVShow_Directors.png"))
    plt.show()
    topd=data["director"].value_counts().head(10).index
    plot=data[data["director"].isin(topd)]
    sns.countplot(data=plot,y="director",order=topd,palette="mako")
    plt.title("Top 10 Directors Of Netflix")
    plt.xlabel("No. Of Shows")
    plt.ylabel("Name Of Director")
    plt.savefig(os.path.join(save,"Top_10_Directors.png"))
    plt.show()
    topc=data["cast"].value_counts().head(10).index
    plotc=data[data["cast"].isin(topc)]
    sns.countplot(data=plotc,y="cast",order=topc,palette="mako")
    plt.title("Performers that Have Worked In Highest No. Of Shows On Netflix")
    plt.xlabel("No. Of Shows")
    plt.ylabel("Name Of Performers")
    plt.savefig(os.path.join(save,"Top_10_Performers.png"))
    plt.show()
def Comparative_Analysis():
    global data
    data["rating"]=data["rating"].fillna(data["rating"].mode()[0])
    data.dropna(subset=["country"],inplace=True)
    plt.figure(figsize=(12,6))
    sns.set_style("whitegrid")
    top5=data["country"].value_counts().head(5).index
    sns.countplot(data=data[data["country"].isin(top5)],x="country",hue="rating",order=top5,palette="mako")
    plt.title("Rating Types Of 5 Most Highest Show Producing Country On Netflix")
    plt.xlabel("Country")
    plt.ylabel("Content Count")
    plt.legend(title="Rating",bbox_to_anchor=(1.05,1),loc="upper left")
    plt.tight_layout()
    plt.savefig(os.path.join(save,"Rating-Country.png"))
    plt.show()
    plt.figure(figsize=(12,6))
    sns.countplot(data=data[data["country"].isin(top5)],x="country",hue="type",order=top5,palette="mako")
    plt.title("Show Types Of 5 Most Highest Show Producing Country On Netflix")
    plt.xlabel("Country")
    plt.ylabel("Content Count")
    plt.legend(title="Type Of Show",bbox_to_anchor=(1.05,1),loc="upper left")
    plt.tight_layout()
    plt.savefig(os.path.join(save,"ShowType-Country.png"))
    plt.show()
    plt.figure(figsize=(12,6))
    sns.countplot(data=data,x="type",hue="rating",palette="mako")
    plt.xlabel("Type Of Show")
    plt.ylabel("Content Count")
    plt.legend(title="Type Of Show",bbox_to_anchor=(1.05,1),loc="upper left")
    plt.tight_layout()
    plt.savefig(os.path.join(save,"Type-Rating.png"))
    plt.show()
    plt.figure(figsize=(12,6))
    top10g=data["listed_in"].value_counts().head(10).index
    sns.countplot(data=data[data["listed_in"].isin(top10g)],y="listed_in",hue="type",order=top10g,palette="mako")
    plt.title("Top 10 Genre Distributed Among Movies And TV Shows")
    plt.xlabel("Content Count")
    plt.ylabel("Genre")
    plt.legend(title="Type Of Show",bbox_to_anchor=(0.85,0.7),loc="upper left")
    plt.savefig(os.path.join(save,"Genre-ShowType.png"))
    plt.show()
    plt.figure(figsize=(12,6))
    combo=data[(data["country"].isin(top5)) & (data["listed_in"].isin(top10g))]
    sns.countplot(data=combo,x="country",hue="listed_in",order=top5,palette="mako")
    plt.title("Top 10 Genres Distributed Across Top 5 Content Producing Countries On Netflix")
    plt.xlabel("Country")
    plt.ylabel("Content Count")
    plt.legend(title="Type Of Show",bbox_to_anchor=(0.5,1),loc="upper left")
    plt.savefig(os.path.join(save,"Genre-Country.png"))
    plt.show()

Dataset_Assessment()
Content_Analysis()
Time_Based_Analysis()
Geographic_Analysis()
People_Analysis()
Comparative_Analysis()