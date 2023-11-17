# Crafting a Personalized Beer Landscape: Analyzing User Preferences and Naming Impact for guiding targeted recommendation
## Abstract
This project takes a deep dive into beer popularity and user taste preferences using datasets from BeerAdvocate and RateBeer, aiming to understand beer popularity, naming influence, and style similarities. Aiming at key issues such as user taste preferences and the impact of beer names on ratings, the study used methods such as k-means clustering, sentiment analysis, and graph network modeling. The data set consists of 732,000 BeerAdvocate and 542,000 RateBeer ratings, enriched with additional data to provide a comprehensive beer style definition.
Tasks include clustering to identify regional preferences, analyzing sentiment and language in beer names, exploring textual similarities between beer styles, building graph network models, and developing personalized recommendation systems. The project combines statistical methods with NLP techniques to provide a multifaceted view of the beer landscape. The findings are intended to provide guidance to breweries and tailor recommendations to users, taking into account not only popularity but also quality attributes and regional differences in beer preferences.

## Research questions
- How can we know beers' popularity and user taste preference according to ratings? Do beer styles share similarities?
- Does the style and language of a beer's name have an impact on its rating and the sentiments expressed in its review text?
- How to build a mini-recommendation system based on our data analysis and graph network modeling?
  
## Data
### Data Selection: matched beer data from the two website
Our dataset, encompassing 6,084 breweries and 45,640 beers from BeerAdvocate and RateBeer, is extensive and manageable for analysis.[^1] It includes over 1.2 million ratings, ensuring robustness for a sophisticated recommendation system and machine learning applications.[^1] Implementing a 20-rating threshold refines the dataset, enhancing processing speed and focusing on frequently reviewed beers.[^1] The matched data approach, combining ratings from both platforms, ensures cross-platform consistency, reducing redundancy and improving the reliability and quality of our predictive models. This comprehensive and consistent dataset is well-suited for developing an effective beer recommendation system.

### Data Preprocessing
We initially planned to utilize the full dataset from both websites, converting all text files to CSV for easier handling. Due to the large size making it impractical for GitHub sharing and slow to process, we chose to use the original pre-processed matched data: beers.csv, breweries.csv, ratings.csv, and users_approx.csv. These files are adequate and clear for our needs, requiring no additional preprocessing.

### Data Description 
The majority of our users and breweries are from the United States, hence the predominance of American-style beer products, with American IPA having the highest proportion at 12.15%. After scaling, the distributions on BeerRate and BeerAdvocate are very similar. Therefore, we will attempt to explore the connections across the features. 

### Additional Data
We want to found similarities among beer styles, so we found additional data to describe how to define each style in our dataset in beer association website.[^2] We use web crawler to get styles description to enrich beer style definitions. In our additional dataset, each style is explained by color, clarity, Perceived Malt Aroma & Flavor, Perceived Hop Aroma & Flavor, Perceived Bitterness and Fermentation Characteristics. By examining the different dimensions of these beers, we can distinguish and understand the various beer styles more comprehensively and in greater detail, and identify their similarities.

## Project plans
### Task 1: Clustering for Popularity and User Taste Preference
In our initial analysis of the rating dataset, we have identified key attributes such as taste, palate, aroma, appearance, and abv (alcohol by volume), and aim to explore their interrelations and impact on the overall rating. Our preliminary ridge regression model reveals that these five attributes explain the overall rating in a great extent (R^2 = 0.76) in the test set.

To systematically examine the characteristics of beers, we plan to integrate k-means clustering with regression analysis. This approach involves selecting an optimal number of clusters (k) based on the overall performance of regression, allowing us to categorize beers into distinct clusters. We will then investigate the contribution of each cluster’s attributes on their overall ratings, as well as regional preferences for different beer categories. The insights gleaned from this analysis will not only facilitate targeted recommendations for customers in various regions but also guide breweries in enhancing the appeal of their beers.

### Task 2: Beer Name Reflect Beer Flavor
Do beer names like "Tokyo" influence users' focus on oriental spices like coriander in the aroma? Beer names, ranging from descriptive "Co-op Wheat Beer" to creative ones like "Just Married," vary in style and language, such as English and Hungarian. We explore how a beer's name, with its emotional tone and language, may impact reviews.

For sentiment analysis, we employ Hugging Face's transformers library with a pre-trained distilbert-base-uncased-finetuned-sst-2-english model. To identify language, we use the langdetect library based on Google's language-detection library and obtain a two-letter language code.
Linear regression (OLS) examines the correlation between rating and sentiment/language of the beer's name. Preliminary findings indicate a significantly positive correlation (1% confidence level) in English - Positive sentiment in English names corresponds to higher user ratings. We'll also run some robust tests, focus on the composition of the rating and review text.

### Task 3: Beer style similarities
Calculating the "distance" between different beer styles based on their textual descriptions involves using text similarity measures that can quantify how close or different the descriptions are. Tools like Word2Vec or GloVe convert words into high-dimensional vectors in such a way that semantically similar words are closer in the vector space. You can convert the whole text into a vector by taking the average of all word vectors in the text and then use cosine similarity to find distances between text vectors. In Python, we can use library gensim for Word2Vec to compute these distances.

### Task 4: Graph Network Modeling
We plan to leverage our comprehensive beer dataset to construct a graph network model in Neo4j. This model will form the backbone of our visualization efforts and interactive recommendation system. It will map the intricate relationships between beers, their styles, breweries, and users within their respective locations. As depicted in the model diagram, 'Beer' serves as the central node, linked to 'Style' through 'belongs_to' relationships, to 'Breweries' via 'produced_by,' and to 'Users' who have 'rated' the beers. The 'Breweries' are connected to 'Location,' establishing a geospatial context. Relationships such as 'is_similar_to' are computed from task 1 and 3. This structured network will facilitate complex queries and enable us to generate personalized beer recommendations by analyzing patterns and preferences within the data.
<br>
<div align=center><img style="margin: 0 auto;" src ="https://github.com/epfl-ada/ada-2023-project-badanalysist/blob/main/img/graph%20network%20modeling.png" width="40%" height="40%"></div>

### Task 5: Recommendation Function
We aim to develop an comprehensive beer recommendation tool, utilizing data from beer review platforms. This tool, ideal for users with limited beer knowledge, will offer suggestions based on various factors including popularity, ABV, and qualitative attributes like taste. Furthermore, our initial data analysis suggests regional variations in beer preferences. This insight enables us to provide tailored recommendations that cater to both local tastes and those of tourists seeking regional specialties

Using NLP libraries such as nltk, we can extract descriptive keywords from reviews, enhancing our recommendations and enabling visualizations like WordClouds for an intuitive understanding of each beer. We'll also incorporate regional personalization by analyzing beer popularity and ratings across major global regions. Additionally, we plan to add a "you might also like" feature which suggests beers based on style similarities analyzed by task 3. The current recommendation function demonstrates the capability to suggest based on keywords and regions, with further criteria to be added in subsequent phases.


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
