#!/usr/bin/env python
# coding: utf-8

# # 1. Scraping first news article from https://redplanetscience.com/

# In[1]:


# Dependencies
import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser
import requests
# from flask import Flask, render_template, redirect
# from flask_pymongo import pymongo
# import scrape
from webdriver_manager.chrome import ChromeDriverManager
import os


# In[2]:


# Run Chrome to assist with identifying html calls.
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit URL for preview
url = 'https://redplanetscience.com/'
browser.visit(url)


# In[4]:


# HTML object
html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
# Retrieve the first element that contain article information
rows = soup.find_all("div", class_="list_text")
rows[0]


# In[5]:


# Retrive the latest title text.  Titles are ordered by date on the screen, so selecting the first one.  
news_title = soup.find("div", class_="content_title").text

# Grabbing the latest paragraph as well.
news_p = soup.find("div", class_="article_teaser_body").text


# In[6]:


# Print Results

print(news_title)
print("----------------------------------------------------------------------")
print(news_p)


# In[7]:


# Close out browser session
browser.quit()


# # 2. Scraping featured image from https://spaceimages-mars.com/

# In[8]:


# Run Chrome to assist with identifying another set of html calls.
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[9]:


# Visit the new URL for preview
url = "https://spaceimages-mars.com"
browser.visit(url)


# In[10]:


# HTML object
html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, "html.parser")
# Retrieve all elements that contain image information
image = soup.find("img", class_="headerimage fade-in")
print(image)


# In[11]:


# Retrive the current image URL 
src = image["src"]
featured_image_url = "https://spaceimages-mars.com/" + src
print(featured_image_url)


# In[12]:


# Close out browser session
browser.quit()


# # 3. Scraping a table into a DataFrame from https://galaxyfacts-mars.com

# In[13]:


# Run Chrome to assist with identifying another set of html calls.
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[14]:


# Visit the new URL for preview
url = "https://galaxyfacts-mars.com/"
browser.visit(url)


# In[15]:


# HTML object
html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, "html.parser")


# In[16]:


# Read the tables
tables = pd.read_html(url)
tables


# In[17]:


# Understand what object type this is.
type(tables)


# In[18]:


# Preview as a Data Frame to understand how/if I want to slice for an index.
df = tables[0]
df.head()


# In[19]:


# Generate HTML DataFrame
html_table = df.to_html()
html_table


# In[20]:


# Strip New Lines tags
html_table.replace('\n', '')


# In[21]:


# Save Table to a HTML file.
df.to_html('Script_Outputs/table.html')


# In[22]:


# Confirm changes by opening.
get_ipython().system('open Script_Outputs/table.html')


# In[23]:


# Close out browser session
browser.quit()


# # 4. Scrape high-resolution images from https://marshemispheres.com/

# In[24]:


# Run Chrome to assist with identifying another set of html calls.
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[25]:


# Visit the new URL for preview
url = "https://marshemispheres.com/"
browser.visit(url)


# In[26]:


# HTML object
html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, "html.parser")


# In[27]:


# Retrieve all elements that contain image information
divs = soup.find("div", class_="collapsible results")
print(divs)


# In[28]:


# Narrow in on section with data that needs to be appended.
m_hems = divs.find_all("div", class_="item")

# Create an open list.
hemisphere_image_urls = []

# Use a for loop to navigate and grab each hemisphere's information.
for each in m_hems:

    # Gathering the Hemisphere name in the "H3" portion.
    hemisphere = each.find("div", class_="description")
    name = hemisphere.h3.text
    
    # For each of the hemispheres, navigate to the URL for grabbing the enhanced image's URL.
    hem_url = hemisphere.a["href"]    
    browser.visit(url + hem_url)
    
    # Boiler Plate for parsing the new HTML.
    link = browser.html
    link_conn = BeautifulSoup(link, "html.parser")
    
    # Grab the URL for the enhanced image.
    img1_url = link_conn.find("div", class_="description")
    img2_url = url + img1_url.a["href"]
    
    # Create a dictionary to include the new lists (Drop the "Enhanced" label).
    image_dictionary = {}
    image_dictionary["title"] = name.replace(" Enhanced", "")
    image_dictionary["img_url"] = img2_url
    
    # Append the lists to the dictionary.
    hemisphere_image_urls.append(image_dictionary)

# Print the dictionary to confirm the changes.
print(hemisphere_image_urls)


# In[29]:


# Close out browser session
browser.quit()

