# Web Scraping Job Listings for Data Analysts in Toronto

This project demonstrates web scraping, data cleaning, and data visualization techniques by scraping job listings for data analyst positions in Toronto from Glassdoor using Selenium.

## Project Overview

The main objective of this project is to collect job listings for data analyst positions in Toronto from Glassdoor, clean the data, and create visualizations to gain insights into the job market.

## Repository Contents

- `webscraping.py`: The Python script using Selenium to scrape job listings from Glassdoor.
- `glassdoor_job_listings.xlsx`: The raw scraped data saved in an Excel file.
- `glassdoor_job_listings_cleanedanalysis.xlsx`: The cleaned and analyzed data, including visualizations, saved in an Excel file.

## Project Workflow

1. **Web Scraping**: Using Selenium to scrape job listings for data analyst positions in Toronto from Glassdoor. The script navigates through the listings, extracts relevant information, and saves it into an Excel file.
2. **Data Cleaning**: Cleaning the scraped data to remove duplicates, handle missing values, and standardize the format. This step ensures that the data is ready for analysis.
3. **Data Visualization**: Creating visualizations within the cleaned Excel file to provide insights into the job market. This includes visualizing the number of job listings over time, common job titles, salary distributions, and more.

## How to Use

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/anabillll/WebScrapingJobListings.git
   cd WebScrapingJobListings
Install the required Python libraries:

bash
Copy code
pip install -r requirements.txt
Run the web scraping script:

bash
Copy code
python webscraping.py
Explore the cleaned data and visualizations within the glassdoor_job_listings_cleanedanalysis.xlsx file.

Dependencies
Selenium
Pandas
OpenPyXL
Make sure to install the dependencies before running the scripts.

Results
The cleaned data and visualizations within the Excel file provide insights into the job market for data analysts in Toronto, including:

The frequency of job postings over time.
Common job titles and their frequencies.
Salary distributions for data analyst positions.
Contributing
If you have any suggestions or improvements, feel free to submit a pull request or open an issue.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgements
Thanks to Glassdoor for providing the job listings data.
Special thanks to my mentor and peers for their support and feedback.
