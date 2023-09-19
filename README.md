<h1 align = "center">Amiibo Dashboard Data</h1>

#### This stores the scripts use to extract and clean the Amiibo data used for the <em>Amiibo Collection</em> Tableau Dashboard published to tableau public [here](https://public.tableau.com/app/profile/dallas.radke/viz/AmiiboCollection/AmiiboCollectionStats). 

<br>

---

<h3 align = 'center'>Script Dependencies
<br></br></h3>

- `amiibo_data_scrape` - This Python script leverages BeautifulSoup & Selenium with the Chrome webdriver to scrape the Nintendo website for all of the current amiibo figures currently listed and then turn them into a csv file.  

- `amiibo_data_prep` - This R script then ingests the scraped data and cleans the data up including:
  - removing any non-amiibo figures
  - cleaning up the Release Date field
  - putting together a concatendated series/name field
  - adding a "data as of" column to timestamp the results