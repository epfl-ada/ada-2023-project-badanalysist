# Title
## Abstract
A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?

## Research questions
A list of research questions you would like to address during the project.
  
## Data (Xinyi)
- Why do we select these data?
- Data processing
- Data description (That you understand what's in the data (formats, distributions, missing values, correlations, etc.)

## Project plans
### Task 1: Clustering for Popularity and User Preference (Siyuan)
-	What we will do. (the motivation behind your project? What story would you like to tell, and why?)
- Methods （That you have a reasonable plan and ideas for methods you’re going to use, giving their essential mathematical details in the notebook.）
- Data relevance (Show us that you’ve read the docs and some examples)
- Feasibility （That your plan for analysis and communication is reasonable and sound, potentially discussing alternatives to your choices that you considered but dropped.）

### Task 2: Beer Name Reflect Beer Flavor (Zhixun)
- What we will do: Does the beer's name "Tokyo" make users pay more attention to the aroma of oriental spices (such as coriander)? We are intrigued by the possibility that the emotional tone and language conveyed by a beer's name might affect not only the rating but also the content and sentiments within the rating text.

- Methods: We plan to run a linear model and use NLP to get the variables:
$$Rating_{i,j} = \beta_0 + \beta_1 \times NameSentiments_i + \beta_2 \times NameLanguages_i + \beta_3 \times X_i+ \beta_4 \times Y_j +\epsilon_{i,j}$$
where $NameSentiments_i$ is a dummy variables which indicates whether the name of beer has a special sentiment or style, $NameLanguages_i$ is a dummy variables of the language of beer's name, $X_i$ are controal variables of beers, $Y_j$ are controal variables of users, $\beta_0$ is an overall constant.
- Data  relevance (Show us that you’ve read the docs and some examples)

- Feasibility （That your plan for analysis and communication is reasonable and sound, potentially discussing alternatives to your choices that you considered but dropped.）

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

https://epfl-ada.github.io/teaching/fall2023/cs401/projects/
