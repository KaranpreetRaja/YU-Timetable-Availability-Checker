from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random

Faculty = "Lassonde School of Engineering - (LE)"
Subject = "Electrical Engineering and Computer Science"
Session = "Summer 2023"
CourseCode = "3221"

url = "https://w2prod.sis.yorku.ca/Apps/WebObjects/cdm.woa/"

# Configure the WebDriver
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Run in headless mode (no browser window)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

driver.get(url)

# Click the "Advanced Search" button
advanced_search_button = driver.find_element(By.LINK_TEXT, "Advanced Search")
advanced_search_button.click()


# Wait for the new page to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Advanced Search by Faculty, Subject and Number')]"))
)
print("loads")

time.sleep(random.uniform(1, 2))

# Click on faculty
faculty_option = driver.find_element(By.XPATH, f"//option[contains(text(), '{Faculty}')]")
faculty_option.click()
print("clicked lassonde")


# Wait for the new page to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, f"//option[contains(text(), '{Faculty}') and @selected='selected']"))
)

time.sleep(random.uniform(1, 2))

# Click on the Electrical Engineering and Computer Science option
subject_option = driver.find_element(By.XPATH, f"//option[contains(text(), '{Subject}')]")
subject_option.click()
print("selected eecs")

# There is no need to check for the new page to load because no new page is loaded

time.sleep(random.uniform(1, 2))

# Click on the Summer 2023 option
session_option = driver.find_element(By.XPATH, f"//option[contains(text(), '{Session}')]")
session_option.click()

# Wait for the new page to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, f"//option[contains(text(), '{Session}') and @selected='selected']"))
)

time.sleep(random.uniform(1, 2))

print("New page loaded")

# Find the course number input field and enter course code
course_num_input = driver.find_element(By.ID, "courseNumInput")
course_num_input.send_keys(CourseCode)
print("Course number entered")


# Find and click the search button
search_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Search Courses']")
search_button.click()
print("Search button clicked")


# Wait for the new page to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Course Schedule')]"))
)

# Find and click the Summer 2023 Course Schedule link
course_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Course Schedule')]")
course_link.click()
print("Summer 2023 Course Schedule link clicked")


time.sleep(random.uniform(1, 2))


# Find and click on the avaliblity button
avalibility_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Please click here to see availability')]")
avalibility_link.click()
print("Avalibility button clicked")

# Wait for the new page to load
time.sleep(5)