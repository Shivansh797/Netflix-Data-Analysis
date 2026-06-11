# Netflix-Data-Analysis
## Project Overview

This project performs Exploratory Data Analysis (EDA) on the Netflix Movies and TV Shows dataset using Python. The objective is to uncover trends, patterns, and insights related to Netflix's content distribution, ratings, genres, countries, directors, release years, and overall content strategy.

The analysis was performed using Python libraries such as Pandas, Matplotlib, and Seaborn, with visualizations created to support key findings.

---

## Dataset Information

Dataset: Netflix Movies and TV Shows

Rows: 8,807

Columns:
- show_id
- type
- title
- director
- cast
- country
- date_added
- release_year
- rating
- duration
- listed_in
- description

---

## Project Structure

```
Netflix-Data-Analysis/
│
├── data-analysis.py
├── insights.txt
├── README.md
│
└── Graphs_And_Charts/
    ├── TypeShow-PieChart.png
    ├── Rating_Distribution.png
    ├── Top15_Genre.png
    ├── Highest_producing_year.png
    ├── Most_Common_Duration.png
    ├── Top_10_Countries.png
    ├── Top_10_Movie_Directors.png
    ├── Top_10_TVShow_Directors.png
    ├── Top_10_Directors.png
    ├── Top_10_Performers.png
    ├── Rating-Country.png
    ├── ShowType-Country.png
    ├── Type-Rating.png
    ├── Genre-ShowType.png
    └── Genre-Country.png
```

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

---

## Analysis Performed

### 1. Dataset Assessment
- Dataset overview
- Data types inspection
- Missing value analysis
- Duplicate record detection

### 2. Content Analysis
- Movies vs TV Shows distribution
- Rating distribution
- Most common Netflix content categories
- Genre analysis

### 3. Time-Based Analysis
- Content distribution by release year
- Most active content release years
- Most common duration categories

### 4. Geographic Analysis
- Top content-producing countries
- Movie vs TV Show contributions by country

### 5. People Analysis
- Most frequent directors
- Top movie directors
- Top TV show directors
- Most frequently occurring cast records

### 6. Comparative Analysis
- Ratings across countries
- Content type distribution across countries
- Ratings by content type
- Genre distribution across content types
- Genre distribution across major content-producing countries

---

## Key Insights

### Content Distribution

- Movies contribute approximately **69.6%** of Netflix's catalog.
- TV Shows contribute approximately **30.4%**.

### Ratings

- **TV-MA** and **TV-14** are the most common rating categories.
- India's most common rating category is **TV-14**, while most other major content-producing countries are dominated by **TV-MA** content.

### Genres

- International Movies, Documentaries, and Stand-Up Comedy are among the most common Netflix content categories.
- Kid's TV is one of the few TV Show categories appearing among the highest-producing content categories.

### Time Trends

- The highest concentration of released content appears between **2017 and 2020**.
- Single-season TV Shows are the most common TV Show duration format.

### Geographic Insights

- The **United States** is Netflix's largest content contributor.
- **India** is the second-largest contributor overall.
- India contributes significantly more Movies than TV Shows compared to other leading countries.

### People Insights

- Jan Suter appears as the most frequent director in the dataset.
- Alastair Fothergill is the most frequent TV Show director.
- Samuel West appears in the most frequently occurring cast record.

---

## Conclusion

This analysis shows that Netflix remains a strongly movie-oriented platform, with movies accounting for nearly 70% of its catalog.

The United States dominates content production across both Movies and TV Shows, while India emerges as the second-largest contributor, primarily driven by movie production.

The platform is heavily characterized by mature content ratings such as TV-MA and TV-14, while content categories such as International Movies, Documentaries, and Stand-Up Comedy form a significant portion of the catalog.

Overall, Netflix's global library reflects a diverse content strategy built around internationally accessible movies, short-format television content, and region-specific audience preferences.
