import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from fuzzywuzzy import process
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from collections import Counter

 
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