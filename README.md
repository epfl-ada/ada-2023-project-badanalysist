![image](https://github.com/epfl-ada/ada-2023-project-badanalysist/assets/116504205/f2566238-c7f0-41ee-bdb7-48ac4d356168)# Title
## Abstract
A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?

## Research questions
A list of research questions you would like to address during the project.
- Does the style and language of a beer's name have an impact on its rating and the sentiments expressed in its review text?
  
## Data (Xinyi)
### Data Selection
1.	Data Handle-ability: Our dataset, with 6,084 breweries and 45,640 beers without a minimum rating requirement, is large but manageable. Higher rating thresholds refine the dataset, improving processing speed and quality by focusing on frequently rated beers. At 20 ratings, the retention of 1,079 breweries and 4,051 beers suggests a robust sample for analysis.[^1]
2.	Sufficiency for the Project: With over 732,000 and 542,000 ratings from BeerAdvocate and RateBeer respectively, even at a 20-rating cutoff, your dataset provides ample data for a complex recommendation system and is rich enough for machine learning applications.[^1]
3.	Advantages of Matched Data: Matched data ensures cross-platform consistency, enhancing model reliability by merging ratings from both BeerAdvocate and RateBeer. This helps reduce data redundancy and improve quality, aiding the model's predictive accuracy for beers listed on both sites.
Overall, the size of your dataset indicates you have sufficient information to build a recommendation system. The matched dataset is particularly beneficial for ensuring the quality and performance of the model, especially when processing user ratings and feedback data.

- Data processing
- Data description (That you understand what's in the data (formats, distributions, missing values, correlations, etc.)

## Project plans
### Task 1: Clustering for Popularity and User Preference (Siyuan)
In our initial analysis of the rating dataset, we have identified key attributes such as taste, palate, aroma, appearance, and abv (alcohol by volume), and aim to explore their interrelations and impact on the overall rating. Our preliminary ridge regression model reveals that these five attributes explain the overall rating in a great extent (R^2 = 0.76) in the test set.

To systematically examine the characteristics of beers, we plan to integrate k-means clustering with regression analysis. This approach involves selecting an optimal number of clusters (k) based on the overall performance of regression, allowing us to categorize beers into distinct clusters. We will then investigate the contribution of each cluster’s attributes on their overall ratings, as well as regional preferences for different beer categories. The insights gleaned from this analysis will not only facilitate targeted recommendations for customers in various regions but also guide breweries in enhancing the appeal of their beers.

### Task 2: Beer Name Reflect Beer Flavor (Zhixun)
- What we will do

  Does the beer's name "Tokyo" make users pay more attention to the aroma of oriental spices (such as coriander)? We are intrigued by the possibility that the emotional tone and language conveyed by a beer's name might affect not only the rating but also the content and sentiments within the rating text.
- Methods
  - Linear Regression

    We'll perform linear regression with ordinary least squares (OLS) to see the correlation between the rating score or sentiment of the review text and the sentiment of the beer's name. We'll also run some robust tests and focus on the composition of the overall rating.
  - NLP

    We'll utilize NLP model to get the sentiment analysis of rating text and language identification of beer's name.
  - should move to notebook - We plan to run a linear model and use NLP to get the variables:
$$Rating_{i,j} = \beta_0 + \beta_1 \times NameSentiments_i + \beta_2 \times NameLanguages_i + \beta_3 \times X_i+ \beta_4 \times Y_j +\epsilon_{i,j}$$
where $Rating_{i,j}$ could be the rating score or sentiment of rating text, $NameSentiments_i$ is a dummy variable that indicates whether the name of beer has a special sentiment or style, $NameLanguages_i$ is a dummy variable of the language of beer's name, $X_i$ are control variables of beers, $Y_j$ are control variables of users, $\beta_0$ is an overall constant. We'll utilize NLP model to get $NameSentiments_i$  $NameLanguages_i$.

- Data  relevance

- Feasibility

  We plan to focus more on rating score instead of the review text.（That your plan for analysis and communication is reasonable and sound, potentially discussing alternatives to your choices that you considered but dropped.）

### Task 3: Recommendation Function (Yihan)
- What we will do. (the motivation behind your project? What story would you like to tell, and why?)
- Methods （That you have a reasonable plan and ideas for methods you’re going to use, giving their essential mathematical details in the notebook.）
- Data relevance (Show us that you’ve read the docs and some examples)
- Feasibility （That your plan for analysis and communication is reasonable and sound, potentially discussing alternatives to your choices that you considered but dropped.）

## Timeline
TBC

## Team Organization
TBC

## Questions for TAs
TBC

## Reference
[^1]Lederrey, G., & West, R. (2018, April). When sheep shop: measuring herding effects in product ratings with natural experiments. In Proceedings of the 2018 world wide web conference (pp. 793-802).![Uploading image.png…]()


https://epfl-ada.github.io/teaching/fall2023/cs401/projects/
