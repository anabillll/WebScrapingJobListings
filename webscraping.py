import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Define the path to the ChromeDriver
driver_path = 'E:/Job Listings Project/chromedriver.exe'  # Update with the exact path to your ChromeDriver executable

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')

# Initialize the WebDriver with Service object
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Define the URL
base_url = 'https://www.glassdoor.ca/Job/ontario-data-analyst-jobs-SRCH_IL.0,7_IS4080_KO8,20.htm'

# Function to scrape a single page
def scrape_page():
    job_titles = []
    job_locations = []
    salaries = []
    company_names = []
    
    # Use WebDriverWait to wait until the job title elements are present
    wait = WebDriverWait(driver, 30)
    jobs = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'JobCard_jobTitle___7I6y')))

    for job in jobs:
        try:
            title = job.text
        except:
            title = 'N/A'
        
        # Locate the parent element to fetch other details
        parent = job.find_element(By.XPATH, '../..')

        try:
            location = parent.find_element(By.CLASS_NAME, 'JobCard_location__rCz3x').text
        except:
            location = 'N/A'
        
        try:
            salary = parent.find_element(By.CLASS_NAME, 'JobCard_salaryEstimate__arV5J').text
        except:
            salary = 'N/A'
        
        try:
            company = parent.find_element(By.CLASS_NAME, 'EmployerProfile_employerInfo__d8uSE').text
        except:
            company = 'N/A'

        job_titles.append(title)
        job_locations.append(location)
        salaries.append(salary)
        company_names.append(company)

        print(f"Title: {title}, Company: {company}, Location: {location}, Salary: {salary}")

    return pd.DataFrame({
        'Title': job_titles,
        'Company': company_names,
        'Location': job_locations,
        'Salary': salaries
    })

# Function to handle pagination
def scrape_all_pages():
    all_jobs_df = pd.DataFrame()

    driver.get(base_url)
    time.sleep(10)  # Increased initial wait time for page to load

    while True:
        # Scroll to load more jobs
        for _ in range(10):  # Increased the number of times to scroll
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(5)  # Increased wait time after scrolling
        
        # Scrape current page
        jobs_df = scrape_page()
        all_jobs_df = pd.concat([all_jobs_df, jobs_df], ignore_index=True)
        
        # Try to find the "Next" button
        try:
            next_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "Button__") and @aria-label="Next"]'))
            )
            print(f"Found the next button: {next_button}")
            if "disabled" in next_button.get_attribute("class"):
                break
            next_button.click()
            time.sleep(10)  # Increased wait time after clicking next button
        except Exception as e:
            print(f"Could not find the next button. Ending scraping. Error: {e}")
            break

    return all_jobs_df

try:
    all_jobs_df = scrape_all_pages()
    
    # Save to Excel with an absolute path
    output_path = 'E:/Job Listings Project/glassdoor_job_listings.xlsx'
    all_jobs_df.to_excel(output_path, index=False)

    print(f"All job listings have been scraped and saved to '{output_path}'")
    
finally:
    # Ensure the driver quits regardless of any errors
    driver.quit()


