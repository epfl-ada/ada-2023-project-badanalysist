# Crafting a Personalized Beer Landscape: Analyzing User Preferences and Naming Impact for Guiding Targeted Recommendation

## Data Story
Click [here](https://epfl-ada.github.io/ada-2023-project-badanalysist/)

## Abstract
This project takes a deep dive into beer popularity and user taste preferences using datasets from BeerAdvocate and RateBeer, aiming to understand beer popularity, naming influence, and style similarities. Aiming at key issues such as user taste preferences and the impact of beer names on ratings, the study used methods such as k-means clustering, sentiment analysis, and graph network modeling. The data set consists of 732,000 BeerAdvocate and 542,000 RateBeer ratings, enriched with additional data to provide a comprehensive beer style definition. Tasks include clustering to identify regional preferences, analyzing sentiment and language in beer names, exploring textual similarities between beer styles, building graph network models, and developing personalized recommendation systems. The project combines statistical methods with NLP techniques to provide a multifaceted view of the beer landscape. The findings are intended to provide guidance to breweries and tailor recommendations to users, taking into account not only popularity but also quality attributes and regional differences in beer preferences.

## Research Questions
- How can we know beers' popularity and user taste preference according to ratings? Do beer styles share similarities?
- Does the style and language of a beer's name have an impact on its rating and the sentiments expressed in its review text?
- How to build a mini-recommendation system based on our data analysis?
  
## Data
Our dataset, featuring 6,084 breweries and 45,640 beers from BeerAdvocate and RateBeer, includes over 1.2 million ratings. A 20-rating threshold refines this extensive dataset, optimizing processing speed and focusing on frequently reviewed beers. The matched data from both platforms ensures cross-platform consistency, enhancing our model's reliability and quality, making it ideal for developing a beer recommendation system.[^1]

In data preprocessing, we chose pre-processed files (beers.csv, breweries.csv, ratings.csv, users_approx.csv) over the complete dataset for efficiency. Our data, predominantly from U.S. breweries, mainly features American-style beers, with American IPA being the most common at 12.15%. Similar data distributions on BeerRate and BeerAdvocate encourage exploration of feature relationships.

Additionally, we enriched our beer style descriptions using a web crawler to extract data mainly from a beer association website and a craft beer website. This extra data, detailing aspects like color, aroma, bitterness, and fermentation characteristics, aids in comprehensively understanding and differentiating beer styles.[^2][^3]

## Project Plans & Methods
### Task 1: Clustering and User Taste Preference
We advanced from our initial proposal. We developed a 'CosineKMeans' class, applying k-means clustering based on cosine distance specifically to beer attributes like taste, palate, aroma, appearance, and alcohol by volume (ABV). This nuanced approach allowed us to categorize beers more effectively. Additionally, we integrated ridge regression with k-means to determine the optimal number of clusters (k), using a voting mechanism for entries that appeared multiple times. Our analysis involved examining the characteristics of each beer category and assessing the importance of different features through ridge regression. 

### Task 2: Beer Name Reflects Beer Flavor
Do beer names like "Tokyo" influence users' focus on oriental spices like coriander? We investigate how a beer's name, with its emotional tone (ranging from descriptive, like 'Co-op Wheat Beer,' to creative, such as 'Pheasantry Dancing Dragonfly') and language, may influence reviews.

For sentiment analysis, we employ Hugging Face's transformers library with a pre-trained bert-base-multilingual-uncased-sentiment model. To identify language, we use the langdetect library based on Google's language-detection library.
OLS regression finds a significant positive correlation (1% confidence level) in English names, where positive sentiment leads to higher user ratings. Robust tests will further explore the composition of ratings and review text.

### Task 3: Beer Style Similarities
Calculating the "distance" between different beer styles based on their textual descriptions involves using text similarity measures that can quantify how close or different the descriptions are. Tools like Word2Vec or GloVe convert words into high-dimensional vectors in such a way that semantically similar words are closer in the vector space. You can convert the whole text into a vector by taking the average of all word vectors in the text and then use cosine similarity to find distances between text vectors. In Python, we can use library gensim for Word2Vec to compute these distances.

### Task 4: Graph Network Modeling
Since we cannot access the cloud-based graph database and the total amount of beer product data is too large to be deployed on GitHub, we have removed the part about setting up the graph database.

### Task 5: Recommendation Function
We're creating a beer recommendation tool that utilizes beer review platform data, offering suggestions based on based on personalized demands and different criteria and qualitative attributes like taste. Our analysis of regional beer review data reveals world-wide different beer and style preference. The beer similarity analyzed in Task 3 is also used here to achieve an association-like recommendation function. Besides, using NLP tools like nltk, we extract descriptive keywords from reviews for recommendations to meet qualitative queries demands. Intuitive WordCloud visualizations are also enabled by this method to improve user experience. Non-informative words like "good", "little", "full", etc have been removed from the keyword list and visualizations.

## Timeline
**16.11.2023** Data Handling and Preprocessing & Initial Exploratory Data Analysis

**30.11.2023** Task1-5 Implementation and Preliminary Analysis

**07.12.2023** Compile Final Analysis

**14.12.2023** Report Writing

**22.12.2023** Milestone 3 Deadline

## Team Organization
- Siyuan: basic statistic visualization; implementation of cosine k-means, beer clustering and analysis;
- Zhixun: beer name reflects beer flavor: sentiment analysis for beer name; identify the language of beer name; linear regression and visualization;
- Xinyi: web set up and design; basic statistic visualization and analysis; beer style similarity visualization and analysis;
- Yihan: recommendation logic design, implementation and visualization, regional preference analysis and visualization, descriptive keyword extraction

Each team member will be responsible for creating the final visualizations for their respective task, completing the data story.

## Questions for TAs
TBC

## Reference
[^1]: Lederrey, G., & West, R. (2018, April). When sheep shop: measuring herding effects in product ratings with natural experiments. In Proceedings of the 2018 world wide web conference (pp. 793-802).
[^2]: 2023 Brewers Association Beer Style Guidelines: https://www.brewersassociation.org/edu/brewers-association-beer-style-guidelines/#116
[^3]: Beer Style: https://www.craftbeer.com/beer-styles
