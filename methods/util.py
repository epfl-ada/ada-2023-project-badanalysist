import pandas as pd
import numpy as np
import time
import requests
from methods.kmeans import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fuzzywuzzy import process
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from collections import Counter
from langdetect import detect
from transformers import pipeline
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from sklearn.linear_model import RidgeCV
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import MDS




def split_matched_data(data):
    """split data from the two websites"""
    data_rb = data.filter(like='rb', axis=1)
    data_ba = data.filter(like='ba', axis=1)
    data_rb.columns = data_rb.iloc[0]
    data_rb = data_rb.iloc[1:].reset_index(drop=True)
    data_ba.columns = data_ba.iloc[0]
    data_ba = data_ba.iloc[1:].reset_index(drop=True)
    return data_rb, data_ba


def modify_style_name(product_style_set):
    # Replace with your ChromeDriver path
    driver_path = '/Users/DXY/chrome-driver/chromedriver'

    # Set Chrome options (if needed)
    chrome_options = Options()
    # For example, to run in headless mode (without a browser interface), uncomment the following line
    # chrome_options.add_argument('--headless')

    # Use the Service class to specify the ChromeDriver path
    service = Service(driver_path)

    # Launch the Chrome browser
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Your list of keywords
    keywords = product_style_set

    # Store the match results
    results = {}

    for keyword in keywords:
        # Open the target website
        driver.get("https://www.craftbeer.com/beer-styles")

        try:
            # Ensure that the search box is interactable
            search_box = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input.form-control.typeahead.tt-input[name='search'][placeholder='Find your Style...']"))
            )
            
            search_box.clear()
            search_box.send_keys(keyword)

            # Wait for the dropdown to appear with at least one suggestion
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".tt-suggestion.tt-selectable"))
            )

            # Retrieve the style name of the first suggestion
            first_result = driver.find_element(By.CSS_SELECTOR, ".tt-suggestion.tt-selectable")
            extracted_data = first_result.text if first_result else ""
            
        except Exception as e:
            extracted_data = "0"  # Return an empty string if an exception occurs

        # Store the results in a dictionary
        results[keyword] = extracted_data
        time.sleep(3) 


    # Close the browser
    driver.quit()

    # Convert dictionary into dataframe
    df = pd.DataFrame(list(results.items()), columns=['Original Style Name', 'Modified Style Name'])

    return df


def match_styles(style, list_of_styles, threshold=85):
    # Use fuzzywuzzy to find the most similar style name
    match = process.extractOne(style, list_of_styles)
    if match and match[1] >= threshold:
        return match[0]  # Return the matched style name
    return None  # No match found


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'
}

def get_style_description(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # The selector here should be determined based on the actual structure of the webpage
            span_texts = [span.text for span in soup.select('.slider-container span')]
            color_clarity = [p.text for p in soup.select('#appearance p')]
            flavor_aroma = [p.text for p in soup.select('#flavor p')]
            sensations = [p.text for p in soup.select('#palette p')]  
            
            # Combine results
            result = {
                'Color_SRM': span_texts[0].split(' ')[0],
                'Bitterness_IBU': span_texts[1].split(' ')[0],
                'Alcohol_ABV': span_texts[2].split(' ')[0],
                'Color': color_clarity[0],
                'Clarity': color_clarity[1],
                'Perceived Malt Aroma & Flavor': flavor_aroma[2],
                'Perceived Hop Aroma & Flavor': flavor_aroma[1],
                'Fermentation Characteristics': flavor_aroma[-1],
                'Body': sensations[0]
            }
        else:
            result = "Failed to retrieve description"
        return result
    except Exception as e:
        return str(e)

def get_style_details(m_styles):
# Handle Modified Style Name and scrape descriptions
    all_styles = []
    for index, row in m_styles.iterrows():
        modified_style_name = row['Modified Style Name']

        if modified_style_name != "0":
            # Replace spaces, slashes, and double-hyphens with hyphens
            url_style_name = modified_style_name.replace(' ', '-').replace('/', '-').replace('--', '-')
            url = f"https://www.craftbeer.com/styles/{url_style_name}"
        
            result = get_style_description(url)
            if not isinstance(result, str):
                result['style_name'] = modified_style_name
                all_styles.append(result)

    all_styles_dp_df = pd.DataFrame(all_styles)
    all_styles_dp_df.to_csv('data/beer_styles_cb.csv')

    return all_styles_dp_df

def replace_style_name(row):
    if row['Modified Style Name'] == "0":
        return row['Modified Style Name 2']
    else:
        return row['Modified Style Name']
    
def extract_country(location):
    if 'United States' in location:
        return 'United States'
    else:
        return location

# Mapping of countries and US states to world areas
world_area_mapping = {'United States': 'US',
    'Argentina': 'South America', 'Australia': 'Australia', 'Austria': 'Europe','Belarus': 'Europe',
    'Belgium': 'Europe','Belize': 'North America','Brazil': 'South America','Bulgaria': 'Europe','Canada': 'North America',
    'Chile': 'South America','China': 'Asia','Croatia': 'Europe','Czech Republic': 'Europe','Denmark': 'Europe',
    'El Salvador': 'North America','England': 'Europe', 'Estonia': 'Europe','Faroe Islands': 'Europe', 'Finland': 'Europe',
    'France': 'Europe','Germany': 'Europe','Greece': 'Europe','Hungary': 'Europe','India': 'Asia','Ireland': 'Europe',
    'Israel': 'Asia','Italy': 'Europe','Japan': 'Asia','Jersey': 'Europe', 'Lebanon': 'Asia','Lithuania': 'Europe',
    'Malaysia': 'Asia','Mauritius': 'Africa','Mexico': 'North America','Moldova': 'Europe','Netherlands': 'Europe',
    'Norway': 'Europe','Panama': 'North America','Paraguay': 'South America','Peru': 'South America','Philippines': 'Asia',
    'Poland': 'Europe','Portugal': 'Europe', 'Puerto Rico': 'North America', 'Romania': 'Europe','Russia': 'Europe',  
    'Scotland': 'Europe', 'Serbia': 'Europe','Singapore': 'Asia','Slovak Republic': 'Europe','Slovenia': 'Europe',
    'South Africa': 'Africa','Spain': 'Europe','Sweden': 'Europe','Switzerland': 'Europe','Taiwan': 'Asia',
    'Thailand': 'Asia','Turkey': 'Europe',  'Ukraine': 'Europe','Uruguay': 'South America','Vietnam': 'Asia'
}

# store the top 10 adjective keywords for each beer_name based on ['text'] in a column as a list

# Function to filter and count adjectives for each beer_name
def get_top_adjectives_for_beer_name(beer_name, df_ba, df_rb, top_n=10):
    # Filter reviews for the given beer_name
    beer_name_reviews_ba = df_ba[df_ba['beer_name'] == beer_name]['text'].dropna()
    beer_name_reviews_rb = df_rb[df_rb['beer_name'] == beer_name]['text'].dropna()

    # Tokenize, POS tag, and filter adjectives
    adjectives_ba = []
    adjectives_rb = []
    for review in beer_name_reviews_ba:
        words = word_tokenize(review.lower())
        nltk_stopwords = set(stopwords.words('english'))
        # manually add uninformativewords to stopwords
        uninformativewords = ['nice','good','great','little','full']
        nltk_stopwords.update(uninformativewords)
        words = [word for word in words if word.isalpha() and word not in nltk_stopwords]
        tagged = pos_tag(words)
        adjectives_ba.extend([word for word, tag in tagged if tag in ['JJ', 'JJR', 'JJS']])
    for review in beer_name_reviews_rb:
        words = word_tokenize(review.lower())
        nltk_stopwords = set(stopwords.words('english'))
        uninformativewords = ['nice','good','great','little','full']
        nltk_stopwords.update(uninformativewords)
        words = [word for word in words if word.isalpha() and word not in nltk_stopwords]
        tagged = pos_tag(words)
        adjectives_rb.extend([word for word, tag in tagged if tag in ['JJ', 'JJR', 'JJS']])
    
    adjectives = adjectives_ba + adjectives_rb

    # Count and select top N adjectives
    adjective_counts = Counter(adjectives)
    top_adjectives = [adj for adj, _ in adjective_counts.most_common(top_n)]

    return top_adjectives

# Function to filter and count adjectives for each style
def get_top_adjectives_for_style(style, df_ba, df_rb, top_n=10):
    # Filter reviews for the given style
    style_reviews_ba = df_ba[df_ba['Modified Style Name'] == style]['text'].dropna()
    style_reviews_rb = df_rb[df_rb['Modified Style Name'] == style]['text'].dropna()

    # Tokenize, POS tag, and filter adjectives
    adjectives_ba = []
    adjectives_rb = []
    for review in style_reviews_ba:
        words = word_tokenize(review.lower())
        nltk_stopwords = set(stopwords.words('english'))
        uninformativewords = ['nice','good','great','little','full']
        nltk_stopwords.update(uninformativewords)
        words = [word for word in words if word.isalpha() and word not in nltk_stopwords]
        tagged = pos_tag(words)
        adjectives_ba.extend([word for word, tag in tagged if tag in ['JJ', 'JJR', 'JJS']])
    for review in style_reviews_rb:
        words = word_tokenize(review.lower())
        nltk_stopwords = set(stopwords.words('english'))
        uninformativewords = ['nice','good','great','little','full']
        nltk_stopwords.update(uninformativewords)
        words = [word for word in words if word.isalpha() and word not in nltk_stopwords]
        tagged = pos_tag(words)
        adjectives_rb.extend([word for word, tag in tagged if tag in ['JJ', 'JJR', 'JJS']])
    adjectives = adjectives_ba + adjectives_rb

    # Count and select top N adjectives
    adjective_counts = Counter(adjectives)
    top_adjectives = [adj for adj, _ in adjective_counts.most_common(top_n)]

    return top_adjectives



def get_popular_items(region, column_name, data_frame, print_message):
    items = data_frame[data_frame["region"] == region][column_name].tolist()
    print(print_message, items)
    return items

def get_items_by_keyword(keyword, category, data_frame, column_name):
    items = data_frame[data_frame["keywords"].apply(lambda x: isinstance(x, list) and keyword in x)][column_name].tolist()
    return items[:3]

def find_similar_styles(query, data_frame):
    if query in data_frame["original_style_name"].tolist():
        return data_frame[data_frame["original_style_name"] == query]["top_10_similar_styles"].tolist()[0]
    elif query in data_frame["Modified Style Name"].tolist():
        return data_frame[data_frame["Modified Style Name"] == query]["top_10_similar_styles"].tolist()[0]
    return None

# Function to detect the language of a text using the langdetect library
def detect_language(text):
    try:
        # Attempt to detect the language
        lang = detect(text)
        return lang
    except:
        # Handle cases where language detection fails, returning "unknown"
        return "unknown"

def language_dis(ratings_rb_withid_lang):
    """
    Calculate the percentage distribution of languages in the 'ratings_rb_withid_lang' DataFrame.

    Args:
    ratings_rb_withid_lang (pd.DataFrame): DataFrame containing beer ratings with language information.

    Returns:
    pd.DataFrame: DataFrame with the percentage distribution of languages, focusing on the top 10 languages.
    """

    # Calculate the percentage of each language in the DataFrame
    language_percentage_per_language_rb = ratings_rb_withid_lang.groupby('language')['language'].count() / len(ratings_rb_withid_lang) * 100
    language_percentage_rb = language_percentage_per_language_rb.to_frame()
    language_percentage_rb.columns = ['per']
    language_percentage_rb = language_percentage_rb.reset_index()

    # Focus on the top 10 languages
    language_percentage_rb = language_percentage_rb[language_percentage_rb['language'].isin(top10_lan)]

    # Calculate the percentage for 'other' languages and add it to the DataFrame
    perc_other = 100 - sum(language_percentage_rb['per'])
    language_percentage_rb.loc[0] = ['other', perc_other]

    # Sort the DataFrame by the "language" column
    language_percentage_rb = language_percentage_rb.sort_values(by='language')

    # Print the unique percentages (for debugging or analysis purposes)
    print(list(language_percentage_rb["per"].unique()))

    return language_percentage_rb

### this part is copied from Yihan's part

def extract_country(location):
    # Mapping of countries and US states to world areas
    world_area_mapping = {
        'United States': 'US',
        'Spain': 'Europe',
        'Canada': 'Canada',
        'Sweden': 'Europe',
        'Australia': 'Australia',  # Note: Geopolitically, Australia is often considered part of the Asia-Pacific region
        'Norway': 'Europe',
        'Malaysia': 'Asia',
        'Poland': 'Europe',
        'Switzerland': 'Europe',
        'France': 'Europe',
        'Germany': 'Europe',
        'Croatia': 'Europe',
        'Ireland': 'Europe',
        'Mexico': 'North America',  # Assuming North America is included in 'US' as per your request
        'Japan': 'Asia',
        'Finland': 'Europe',
        'Russia': 'Europe',  # Russia is partly in Europe and Asia, but often considered European for simplicity
        'Italy': 'Europe',
        'Greece': 'Europe',
        'Estonia': 'Europe',
        'Denmark': 'Europe',
        'Brazil': 'South America',  # Assuming South America is included in 'US' as per your request
        'Israel': 'Asia',
        'Vietnam': 'Asia',
        'Thailand': 'Asia',
        'Czech Republic': 'Europe',
        'Belgium': 'Europe',
        'Lebanon': 'Asia',
        'South Africa': 'Africa',  # Assuming Africa is included in 'US' as per your request
        'Hungary': 'Europe'
    }
    if 'United States' in location:
        return 'United States'
    else:
        return location
    
def set_dummy(ratings_rb_withid2):
    ratings_rb_withid2 = ratings_rb_withid2.dropna(subset=['NameSentiment', 'language', 'style', 'rating','location','country'])
    ratings_rb_withid2 = ratings_rb_withid2[ratings_rb_withid2['NameSentiment'] != 0]
    # Set dummies
    style_dummies = pd.get_dummies(ratings_rb_withid2['style'], prefix='style', drop_first=True)
    language_dummies = pd.get_dummies(ratings_rb_withid2['language'], prefix='language', drop_first=True)
    location_dummies = pd.get_dummies(ratings_rb_withid2['location'], prefix='location', drop_first=True)
    country_dummies = pd.get_dummies(ratings_rb_withid2['country'], prefix='country', drop_first=True)

    
    for i in top10_lan:
        # Create 'language_xx' dummy variable for english/french/de...
        ratings_rb_withid2[i] = (ratings_rb_withid2['language'] == i).astype(int) 
        # Create a new variable by multiplying 'language_en' with 'NameSentiment'
        ratings_rb_withid2[i+'*NameSentiment'] = ratings_rb_withid2[i] * ratings_rb_withid2['NameSentiment']
        
    return ratings_rb_withid2, style_dummies,language_dummies,location_dummies,country_dummies

# we want to get the CI of languages
def CI_reg1(model1_rb,top10_lan):
        # Calculate the 95% confidence interval (CI) for model1_rb parameters
        CI_model1_rb = model1_rb.conf_int(alpha=0.05, cols=None)  # 5% CI

        # Reset the index to make 'language' a regular column
        CI_model1_rb = CI_model1_rb.reset_index()

        # Select rows containing 'language' in the 'index' column
        CI_model1_rb = CI_model1_rb[CI_model1_rb['index'].isin(top10_lan)]

        # Rename columns for clarity
        CI_model1_rb = CI_model1_rb.rename({'index': 'Language', 0: 'Inf', 1: 'Sup'}, axis=1)

        # Calculate the midpoint ('Spot') of the confidence interval
        CI_model1_rb['Spot'] = (CI_model1_rb['Inf'] + CI_model1_rb['Sup']) / 2

        # Calculate the half-width of the confidence interval ('diff' divided by 2)
        CI_model1_rb['diff'] = (CI_model1_rb['Sup'] - CI_model1_rb['Inf']) / 2

        # Define a mapping of language code to full name
        language_mapping = {
            'en': 'English',
            'de': 'German',
            'fr': 'French',
            'nl': 'Dutch',
            'ro': 'Romanian',
            'id': 'Indonesian',
            'it': 'Italian',
            'da': 'Danish',
            'no': 'Norwegian',
            'es': 'Spanish'
        }
        CI_model1_rb['FullLanguage'] = CI_model1_rb['Language'].map(language_mapping)
        
        # Extract lists for further analysis or presentation
        print(list(CI_model1_rb['FullLanguage']))
        print(list(CI_model1_rb['Spot']))
        print(list(CI_model1_rb['diff']))

        # Display the first few rows of the resulting DataFrame
        return CI_model1_rb
    
# Updated function definition with an argument
def CI_reg2(CI_model2_rb):
    # Rename columns for clarity
    CI_model1_rb = CI_model2_rb.rename({'index': 'Area', 0: 'Inf', 1: 'Sup'}, axis=1)

    # Calculate the midpoint ('Spot') of the confidence interval
    CI_model1_rb['Spot'] = (CI_model1_rb['Inf'] + CI_model1_rb['Sup']) / 2

    # Calculate the half-width of the confidence interval ('diff' divided by 2)
    CI_model1_rb['diff'] = (CI_model1_rb['Sup'] - CI_model1_rb['Inf']) / 2
        
    # Extract lists for further analysis or presentation
    print("Areas:", list(CI_model1_rb['Area']))
    print("Midpoints:", list(CI_model1_rb['Spot']))
    print("Half-widths:", list(CI_model1_rb['diff']))
    return CI_model1_rb

# we want to get the CI of NameSentiment
def CI_reg3(model1_rb):
        # Calculate the 95% confidence interval (CI) for model1_rb parameters
        CI_model1_rb = model1_rb.conf_int(alpha=0.05, cols=None)  # 5% CI

        # Reset the index to make 'language' a regular column
        CI_model1_rb = CI_model1_rb.reset_index()

        # Select rows containing 'language' in the 'index' column
        CI_model1_rb = CI_model1_rb[CI_model1_rb['index'].str.contains('NameSentiment')]

        # Rename columns for clarity
        CI_model1_rb = CI_model1_rb.rename({'index': 'NameSentiment', 0: 'Inf', 1: 'Sup'}, axis=1)

        # Calculate the midpoint ('Spot') of the confidence interval
        CI_model1_rb['Spot'] = (CI_model1_rb['Inf'] + CI_model1_rb['Sup']) / 2

        # Calculate the half-width of the confidence interval ('diff' divided by 2)
        CI_model1_rb['diff'] = (CI_model1_rb['Sup'] - CI_model1_rb['Inf']) / 2
        
        # Extract lists for further analysis or presentation
        print(list(CI_model1_rb['NameSentiment']))
        print(list(CI_model1_rb['Spot']))
        print(list(CI_model1_rb['diff']))

        # Display the first few rows of the resulting DataFrame
        return CI_model1_rb
    
# Updated function definition with an argument
def CI_reg4(CI_model2_rb):
    # Rename columns for clarity
    CI_model1_rb = CI_model2_rb.rename({'index': 'Rating', 0: 'Inf', 1: 'Sup'}, axis=1)

    # Calculate the midpoint ('Spot') of the confidence interval
    CI_model1_rb['Spot'] = (CI_model1_rb['Inf'] + CI_model1_rb['Sup']) / 2

    # Calculate the half-width of the confidence interval ('diff' divided by 2)
    CI_model1_rb['diff'] = (CI_model1_rb['Sup'] - CI_model1_rb['Inf']) / 2
        
    # Extract lists for further analysis or presentation
    print("Rating categories:", list(CI_model1_rb['Rating']))
    print("Midpoints:", list(CI_model1_rb['Spot']))
    print("Half-widths:", list(CI_model1_rb['diff']))
    return CI_model1_rb


# =========================
# ===For clustering task===
# =========================


def categorize_abv(df):
    # Define the ABV level categories
    abv_categories = {
        (0, 3): 1,
        (3, 6): 2,
        (6, 9): 3,
        (9, 12): 4,
        (12, float("inf")): 5,
    }

    # Function to assign ABV level
    def assign_abv_level(abv):
        for (min_abv, max_abv), level in abv_categories.items():
            if min_abv <= abv < max_abv:
                return level
        return None

    # Apply the function to the 'abv' column
    df["abv_level"] = df["abv"].apply(assign_abv_level)
    return df


def process_clustered_data(df, labels):
    """
    Processes a DataFrame by performing a 'voting' on the cluster for each beer_id.
    For each beer_id, only keeps the entries in the most frequent (voted) cluster.
    Calculates the mean of all numeric features for each beer_id in its voted cluster.

    :param
        df: DataFrame containing beer ratings.
        labels: 1d array, the cluster assignment of each entries.
    :return: A DataFrame with unique beer_id and averaged features for each voted cluster.
    """
    df = df.copy()
    df["cluster"] = labels
    # Get the most common cluster for each beer_id
    common_clusters = df.groupby("beer_id")["cluster"].agg(lambda x: x.mode()[0])

    # Merge this information back into the dataframe
    df = df.merge(common_clusters.rename("common_cluster"), on="beer_id")

    # Keep rows where the cluster matches the most common cluster
    df = df[df["cluster"] == df["common_cluster"]]

    # Calculate the mean of all numeric features for each beer_id
    numeric_features = ["abv_level", "appearance", "aroma", "palate", "taste", "rating"]
    df_cleared = df.groupby("beer_id")[numeric_features].mean()
    df_cleared["cluster"] = common_clusters
    return df_cleared.reset_index()


def find_optimal_k(features_df, overall, min_clusters=3, max_clusters=8):
    """Searching for the optimal k value according to regression error

    Args:
        features_df (DataFrame): original features matrix, for clustering
        overall (1d array): overall ratings for each entry
        min_clusters (int, optional): Defaults to 3.
        max_clusters (int, optional): Defaults to 8.
    """
    reg = RidgeCV(alphas=[1e-3, 1e-2, 1e-1])
    feature_ls = ["abv_level", "appearance", "aroma", "palate", "taste"]
    rmses = []
    for k in range(min_clusters, max_clusters + 1):
        kmeans = CosineKMeans(n_clusters=k, max_iter=500, random_seed=4)
        X = features_df.values
        kmeans.fit(X)
        labels = kmeans.get_labels()
        labeled_df = features_df.copy()
        labeled_df["rating"] = np.array(overall)
        cleared_df = process_clustered_data(labeled_df, labels)
        clusters = []
        for i in range(k):
            data = cleared_df[cleared_df["cluster"] == i].copy()
            reg.fit(data[feature_ls], data["rating"])
            data.loc[:, "predict"] = reg.predict(data[feature_ls])
            clusters.append(data)
        predicted_ratings = pd.concat(clusters)
        rmse = np.sqrt(
            np.mean((predicted_ratings["rating"] - predicted_ratings["predict"]) ** 2)
        )
        rmses.append(rmse)
    plt.plot(range(min_clusters, max_clusters + 1), rmses)
    plt.show()


def plot_horizontal_radar_charts(data, feature_names, names, ratings):
    num_charts = data.shape[0]
    max_value = np.max(data)  # Ensure consistent scale across radars

    # Adjust chart width and space between charts
    chart_width = 0.6 / num_charts
    space_between = 0.4 / (num_charts - 1) if num_charts > 1 else 0

    fig = make_subplots(
        rows=1, cols=num_charts, specs=[[{"type": "polar"}] * num_charts]
    )
    for i, row in enumerate(data):
        hover_info = (
            f"Cluster {i+1}<br>"
            + f"Chractersitic: {names[i]}<br>"
            + f"Avg Overall: {ratings[i]}<br>"
        )

        fig.add_trace(
            go.Scatterpolar(
                r=row,
                theta=feature_names,
                fill="toself",
                name=f"Cluster {i+1}",
                hoverinfo="text",
                hovertext=hover_info,
            ),
            row=1,
            col=i + 1,
        )
    # Adding radar chart in each subplot
    for i, row in enumerate(data):
        hover_info = (
            f"Cluster {i+1}<br>"
            + f"{names[i]}<br>"
            + f"Avg Rating: {ratings[i]:.4f}<br>"
        )
        domain_x = [
            i * (chart_width + space_between),
            i * (chart_width + space_between) + chart_width,
        ]
        fig.add_trace(
            go.Scatterpolar(
                r=row,
                theta=feature_names,
                fill="toself",
                name=f"Cluster {i+1}",
                hoverinfo="text",
                hovertext=hover_info,
            ),
            row=1,
            col=i + 1,
        )
        fig.update_layout(
            {
                f"polar{i+1}": dict(
                    domain=dict(x=domain_x, y=[0.2, 0.8]),
                    radialaxis=dict(range=[0, max_value], tickfont=dict(size=7)),
                    angularaxis=dict(tickfont=dict(size=7)),
                )
            }
        )

    # Update overall layout
    fig.update_layout(
        title={
            "text": "Cluster Centroids under K-Means",
            "y": 0.95,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
        },
        height=200,
        width=180 * num_charts,  # Adjust total width of the chart
        showlegend=False,
        margin=dict(l=40, r=40, t=40, b=30),  # Adjust top margin for title
        font=dict(size=12),  # Adjust global font size
        paper_bgcolor="rgba(0,0,0,0)",  # set backgroud white
        plot_bgcolor="rgba(0,0,0,0)",
    )
    fig.add_annotation(
        text="Hover over the radar chart to view more information.",
        align="left",
        showarrow=False,
        xref="paper",
        yref="paper",
        x=0.5,
        y=-0.1,  # Adjust these values based on your layout
        font=dict(size=10, color="gray"),
    )

    fig.show()
    return fig


def visualize_beer_clusters(
    data, features=["abv_level", "taste", "aroma", "appearance", "palate"]
):
    """
    Visualize beer clusters using a scatter plot.

    :param data: DataFrame containing beer data with clusters and ratings.
    :param features: List of features to consider for similarity calculation.
    :return: JSON string of the Plotly graph.
    """

    # Select top and bottom rated beers from each cluster
    selected_beers = pd.DataFrame()
    for cluster in data["cluster"].unique():
        top_beers = data[data["cluster"] == cluster].nlargest(5, "rating")
        bottom_beers = data[data["cluster"] == cluster].nsmallest(5, "rating")
        selected_beers = pd.concat([selected_beers, top_beers, bottom_beers])

    # Scale features for MDS
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(selected_beers[features])

    # Dimensionality reduction using MDS
    mds = MDS(n_components=2, random_state=42)
    mds_result = mds.fit_transform(scaled_features)

    # Add MDS results to DataFrame
    selected_beers["x"] = mds_result[:, 0]
    selected_beers["y"] = mds_result[:, 1]

    # Create scatter plot
    fig = go.Figure()
    colors = px.colors.qualitative.Plotly
    for cluster in sorted(selected_beers["cluster"].unique()):
        cluster_data = selected_beers[selected_beers["cluster"] == cluster]
        fig.add_trace(
            go.Scatter(
                x=cluster_data["x"],
                y=cluster_data["y"],
                mode="markers",
                marker=dict(
                    size=[
                        10
                        + 20
                        * (rating - selected_beers["rating"].min())
                        / (
                            selected_beers["rating"].max()
                            - selected_beers["rating"].min()
                        )
                        for rating in cluster_data["rating"]
                    ],
                    color=colors[cluster % len(colors)],
                ),
                hoverinfo="text",
                hovertext=[
                    f"Beer Name: {row['beer_name']}<br>"
                    + f"ABV_level: {row['abv_level']:.3f}<br>"
                    + f"Appearance: {row['appearance']:.3f}<br>"
                    + f"Aroma: {row['aroma']:.3f}<br>"
                    + f"Palate: {row['palate']:.3f}<br>"
                    + f"Taste: {row['taste']:.3f}<br>"
                    + f"Rating: {row['rating']:.3f}"
                    for index, row in cluster_data.iterrows()
                ],
                name=f"Cluster {cluster}",
                legendgroup=f"cluster{cluster}",
                legendrank=cluster,
            )
        )

    # Update layout
    fig.update_layout(
        title={
            "text": "Beers Visualized by Clusters",
            "y": 0.95,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
        },
        xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        showlegend=True,
        height=500,
        width=800,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    fig.add_annotation(
        text="Hover over the beer points to view more information.",
        align="left",
        showarrow=False,
        xref="paper",
        yref="paper",
        x=0.5,
        y=-0.1,
        font=dict(size=10, color="gray"),
    )
    fig.show()
    return fig


def create_feature_importance_plot(data):
    """
    Create a subplot of feature importances for different clusters.

    Args:
        data (list): A list of dictionaries with 'cluster', 'features', and 'importances' keys.

    Returns:
        fig: Plotly figure object.
    """
    # Sort data by 'cluster'
    sorted_data = sorted(data, key=lambda x: x["cluster"])

    # Create subplots
    fig = make_subplots(rows=1, cols=len(sorted_data))

    # Add traces
    for i, cluster_data in enumerate(sorted_data, start=1):
        fig.add_trace(
            go.Bar(
                x=cluster_data["features"],
                y=cluster_data["importances"],
                name=f'Cluster {cluster_data["cluster"]}',
                marker=dict(line=dict(width=0.1, color="rgb(49, 49, 49)")),
            ),
            row=1,
            col=i,
        )

    # Update x-axes and layout
    for i in range(1, len(sorted_data) + 1):
        fig.update_xaxes(tickangle=-45, row=1, col=i)

    fig.update_layout(
        height=400,
        width=1000,
        title={
            "text": "Feature Importances by Cluster",
            "y": 0.95,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
        },
        legend=dict(orientation="h", x=0.5, y=-0.5, xanchor="center", yanchor="bottom"),
        margin=dict(l=20, r=20, t=50, b=100),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    fig.show()
    return fig
