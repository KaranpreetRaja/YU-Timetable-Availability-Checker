import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random
from dotenv import load_dotenv


Faculty = "Lassonde School of Engineering - (LE)"
Subject = "Electrical Engineering and Computer Science"
Session = "Summer 2023"
CourseCode = "3221"

load_dotenv()

PassportYorkUsername = os.getenv('YORK_USERNAME')
PassportYorkPassword = os.getenv('YORK_PASSWORD')


# Configure the WebDriver
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Run in headless mode (no browser window)
options.add_argument('--no-sandbox')
options.add_argument('user-data-dir=Profile')  # Path to your chrome profile
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

def checkAvaliblity(Faculty, Subject, Session, CourseCode, PassportYorkUsername, PassportYorkPassword, driver):
    url = "https://w2prod.sis.yorku.ca/Apps/WebObjects/cdm.woa/"

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

    time.sleep(random.uniform(1, 2))

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

    time.sleep(random.uniform(1, 2))

    try:
        # Fill in the Passport York login information
        username_feild = driver.find_element(By.ID, "mli")
        username_feild.send_keys(PassportYorkUsername)

        time.sleep(random.uniform(1, 2))

        password_feild = driver.find_element(By.ID, "password")
        password_feild.send_keys(PassportYorkPassword)
        print("Passport York login entered")

        # press enter on keyboard
        password_feild.send_keys(u'\ue007')

    except:
        try:
            # check to see if page loaded
            WebDriverWait(driver, 100).until(
                EC.presence_of_element_located((By.XPATH, "//option[contains(text(), 'Course Description')]"))
            )
            print("No login required")
        
        except:

            print("login did not work")
            
            #exit the python script
            driver.quit()
            exit()


    time.sleep(random.uniform(10, 20))

    try:
        # # check to see if page loaded

        wait = WebDriverWait(driver, 100)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Course Description:')]")))

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Course Description:')]"))
        )
        time.sleep(random.uniform(1, 2))
        
        #Check to see if the course is full or open
        try:
            # Find and click on the login button
            course_status = driver.find_element(By.XPATH, "//option[contains(text(), 'Full')]")
            print("The course is full")
        except:
            print("The course is open!!!")

    except:
        print("Page did not load")
        #exit the python script

    time.sleep(random.uniform(100, 200))

    wait = WebDriverWait(driver, 100000)

    checkAvaliblity(Faculty, Subject, Session, CourseCode, PassportYorkUsername, PassportYorkPassword, driver)




checkAvaliblity(Faculty, Subject, Session, CourseCode, PassportYorkUsername, PassportYorkPassword, driver)

time.sleep(10)

driver.quit()
