# Web Scraping - Mission to Mars

This repository reflects work to build a web application that scrapes various websites for data related to the Mission to Mars.  This then displays the information on a single HTML web page.  

To accomplish this, I created a Jupiter Notebook (mission_to_mars.ipynb) to generate a script that would perform the initial scraping using BeautifulSoup, Pandas, and Requests/Splinter.  The following was done through the Jupiter Notebook:

  1.  Scrape the top news title and description from https://redplanetscience.com/.
  2.  Scrape the url for the featured Mars image on https://spaceimages-mars.com.  
  3.  Scraped the Mars Facts table from https://galaxyfacts-mars.com and saved as a DataFrame and stored the output as a html file.
  4.  Created a for loop to scrape multiple pages on https://marshemispheres.com/ to scrape the names of the Mars hemispheres and visit those pages to grab the image url for the respective hemisphere.
  5.  Exported the Jupyter Notebook into a .py file (scrape_mars.py) and modified this to eliminate "print()" statements, previews, and areas where I closed the browser ("browser.quit()").

Following this, a Flask App was developed using pymongo to identify the scraping route ("app.py").  Then I developed a html file ("templates/index.html") to serve as a GUI for the app.  This html file includes a button on the page that will perform the scraping functions and displays the output from the app.  Further, the html exported as a table (mentioned above) was copied and pasted into the index.html file to display the new table.

Screenshots from this process are also stored in this repository.
