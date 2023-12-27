#Libraries required for scrapping
import requests
import bs4
import os
import prediction as pred
import dynamic_plot_with_scatter as dp
from langdetect import detect
def scrape(url):
    
    

    # Send a GET request to the URL
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        if response.status_code != requests.codes.ok:
            return 'Invalid URL'

        # Rest of your code for scraping here...
        
    except requests.exceptions.RequestException as e:
        return f'Invalid URL'
    # Get the HTML content from the response
    html_content = response.text

    #creates a BeautifulSoup object named exsoup by parsing the HTML content.
    #'html.parser': This specifies the parser to be used by BeautifulSoup.
    #In this case, the built-in HTML parser provided by Python's standard library is used.
    exsoup=bs4.BeautifulSoup(html_content,'html.parser')


    #Selecting the <h1> tag to parse for
    ele=exsoup.select('h1')


    #Getting the text
    input=str(ele[0].getText())
    
    #print(input)
    return pred.predict(input)

def scrape_anchor(url):
    
    

    # Send a GET request to the URL
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        if response.status_code != requests.codes.ok:
            return 'Invalid URL'

        # Rest of your code for scraping here...
        
    except requests.exceptions.RequestException as e:
        return f'Invalid URL'
    # Get the HTML content from the response
    html_content = response.text

    #creates a BeautifulSoup object named exsoup by parsing the HTML content.
    #'html.parser': This specifies the parser to be used by BeautifulSoup.
    #In this case, the built-in HTML parser provided by Python's standard library is used.
    exsoup=bs4.BeautifulSoup(html_content,'html.parser')


    anchor_tags = exsoup.select('a')

    href_list = []
    # Iterate over the anchor tags and extract the href attribute
    for anchor in anchor_tags:
        href = anchor.get('href')
        if href and href[:4]=='http':
            href_list.append(href)

    return href_list
    #print(input)
    #return pred.predict(input)

import os
import bs4

def scrape_dir(dr):
    y_c={}
    
    for year,file_name in dr.items():
        good = 0
        bad = 0
        texts = []
        #print(os.getcwd())
        dir_name = os.path.join(os.getcwd(), file_name)
        #print(dir_name)
        #print(os.listdir(dir_name))


        for fname in os.listdir(dir_name):
                if fname.endswith('.html'):
                    file_path = os.path.join(dir_name, fname)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        text=f.read()
    
                        exsoup = bs4.BeautifulSoup(text, 'html.parser')
                        # Selecting the <h1> tag and <title> tag
                        elements = exsoup.select('h1')
                    for ele in elements:
                        # Getting the text
                        input_text = ele.get_text()
                        
                        try:
                            lang = detect(input_text)
                        except:
                            pass
                        if lang == 'en':
                                print(input_text)
                    # Process the input_text as needed
    
                # Example: Use the input_text with pred.predict()
                        #print(pred.predict(input_text))
                                if pred.predict(input_text) == 'good':
                                    good += 1
                                elif     pred.predict(input_text) == 'bad':
                                    bad += 1
        #print(os.listdir(dir_name))

        #print(good_mean)
        #print(bad_mean)
        y_c[year]=(good,bad)
    #print(y_c)
    dp.plot(y_c)
    




#print(scrape_anchor('https://www.bbc.com/'))


#scrape_dir('2016')
    
