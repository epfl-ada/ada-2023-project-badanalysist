# Crafting a Personalized Beer Landscape: Analyzing User Preferences and Naming Impact for Guiding Targeted Recommendation

## Data Story
Click [here](https://epfl-ada/ada-2023-project-badanalysist/)

## Abstract
This project takes a deep dive into beer popularity and user taste preferences using datasets from BeerAdvocate and RateBeer, aiming to understand beer popularity, naming influence, and style similarities. Aiming at key issues such as user taste preferences and the impact of beer names on ratings, the study used methods such as k-means clustering, sentiment analysis, and graph network modeling. The data set consists of 732,000 BeerAdvocate and 542,000 RateBeer ratings, enriched with additional data to provide a comprehensive beer style definition. Tasks include clustering to identify regional preferences, analyzing sentiment and language in beer names, exploring textual similarities between beer styles, building graph network models, and developing personalized recommendation systems. The project combines statistical methods with NLP techniques to provide a multifaceted view of the beer landscape. The findings are intended to provide guidance to breweries and tailor recommendations to users, taking into account not only popularity but also quality attributes and regional differences in beer preferences.

## Research Questions
- How can we know beers' popularity and user taste preference according to ratings? Do beer styles share similarities?
- Does the style and language of a beer's name have an impact on its rating and the sentiments expressed in its review text?
- How to build a mini-recommendation system based on our data analysis and graph network modeling?
  
## Data
Our dataset, featuring 6,084 breweries and 45,640 beers from BeerAdvocate and RateBeer, includes over 1.2 million ratings. A 20-rating threshold refines this extensive dataset, optimizing processing speed and focusing on frequently reviewed beers. The matched data from both platforms ensures cross-platform consistency, enhancing our model's reliability and quality, making it ideal for developing a beer recommendation system.[^1]

In data preprocessing, we chose pre-processed files (beers.csv, breweries.csv, ratings.csv, users_approx.csv) over the complete dataset for efficiency. Our data, predominantly from U.S. breweries, mainly features American-style beers, with American IPA being the most common at 12.15%. Similar data distributions on BeerRate and BeerAdvocate encourage exploration of feature relationships.

Additionally, we enriched our beer style descriptions using a web crawler to extract data from a beer association website. This extra data, detailing aspects like color, aroma, bitterness, and fermentation characteristics, aids in comprehensively understanding and differentiating beer styles.[^2]

## Project Plans & Methods
### Task 1: Clustering for Popularity and User Taste Preference
In our initial analysis of the rating dataset, we have identified key attributes such as taste, palate, aroma, appearance, and abv (alcohol by volume), and aim to explore their interrelations and impact on the overall rating. Our preliminary ridge regression model reveals that these five attributes explain the overall rating to a great extent (R^2 = 0.76) in the test set.

We plan to use k-means clustering integrated with regression analysis to categorize beers based on these attributes and assess their impact on ratings and regional preferences. This approach will inform targeted customer recommendations and help breweries improve their products' appeal.

### Task 2: Beer Name Reflect Beer Flavor
Do beer names like "Tokyo" influence users' focus on oriental spices like coriander? We investigate how a beer's name, with its emotional tone (ranging from descriptive, like 'Co-op Wheat Beer,' to creative, such as 'Pheasantry Dancing Dragonfly') and language, may influence reviews.

For sentiment analysis, we employ Hugging Face's transformers library with a pre-trained distilbert-base-uncased-finetuned-sst-2-english model. To identify language, we use the langdetect library based on Google's language-detection library.
OLS regression finds a significant positive correlation (1% confidence level) in English names, where positive sentiment leads to higher user ratings. Robust tests will further explore the composition of ratings and review text.

### Task 3: Beer Style Similarities
Calculating the "distance" between different beer styles based on their textual descriptions involves using text similarity measures that can quantify how close or different the descriptions are. Tools like Word2Vec or GloVe convert words into high-dimensional vectors in such a way that semantically similar words are closer in the vector space. You can convert the whole text into a vector by taking the average of all word vectors in the text and then use cosine similarity to find distances between text vectors. In Python, we can use library gensim for Word2Vec to compute these distances.

### Task 4: Graph Network Modeling
We plan to leverage our comprehensive beer dataset to construct a graph network model in Neo4j. This model will form the backbone of our visualization efforts and interactive recommendation system. It will map the intricate relationships between beers, their styles, breweries, and users within their respective locations. As depicted in the model diagram, 'Beer' serves as the central node, linked to 'Style' through 'belongs_to' relationships, to 'Breweries' via 'produced_by,' and to 'Users' who have 'rated' the beers. The 'Breweries' are connected to 'Location,' establishing a geospatial context. Relationships such as 'is_similar_to' are computed from task 1 and 3. This structured network will facilitate complex queries and enable us to generate personalized beer recommendations by analyzing patterns and preferences within the data.
<br>
<div align=center><img style="margin: 0 auto;" src ="https://github.com/epfl-ada/ada-2023-project-badanalysist/blob/main/img/graph%20network%20modeling.png" width="40%" height="40%"></div>

### Task 5: Recommendation Function
We're creating a beer recommendation tool that utilizes beer review platform data, ideal for users with limited knowledge of beers. We plan to offer suggestions based on both basic criteria such as style, brewery, ABV, and also more comprehensive factors such as popularity and qualitative attributes like taste. Our initial analysis of regional beer preferences also inspires tailored recommendations catering both locals and exotic tourists.

Beers will be ranked by popularity, both globally and regionally, using review counts and ratings, and labeled with key features. Using NLP tools like nltk, we'll extract keywords from reviews for enhanced recommendations and intuitive WordCloud visualizations. Additionally, a "you might also like" feature will suggest beers based on style similarities. The current function suggests beers based on keywords and regions, with more criteria to be added later.

## Timeline
**16.11.2023** Data Handling and Preprocessing & Initial Exploratory Data Analysis

**30.11.2023** Task1-5 Implementation and Preliminary Analysis

**07.12.2023** Compile Final Analysis

**14.12.2023** Report Writing

**22.12.2023** Milestone 3 Deadline

## Team Organization
- Siyuan: task 1
- Zhixun: task 2
- Xinyi: task 3 & 4
- Yihan: task 5

Each team member will be responsible for creating the final visualizations for their respective task, completing the data story.

## Questions for TAs
TBC

## Reference
[^1]: Lederrey, G., & West, R. (2018, April). When sheep shop: measuring herding effects in product ratings with natural experiments. In Proceedings of the 2018 world wide web conference (pp. 793-802).
[^2]: 2023 Brewers Association Beer Style Guidelines: https://www.brewersassociation.org/edu/brewers-association-beer-style-guidelines/#116
