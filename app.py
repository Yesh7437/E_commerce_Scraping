# import the necessary packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Setting up Kaggle credentials
kaggle_username = 'yeshwanthsaibarla@gmail.com'
kaggle_password = 'Yesh@123hello'

# URL of the kaggle login page 
login_url = 'https://www.kaggle.com/account/login'
# URL of the Kaggle dataset page
dataset_url = 'https://www.kaggle.com/datasets/aliessamali/ecommerce'

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the Kaggle login page
driver.get(login_url)

# Wait for the login page to load
time.sleep(2)

# Click on the 'Sign in with email' button
select_email = driver.find_element(By.XPATH, '(//button[@class="sc-hjsqBZ deYQsq"])[2]')     
select_email.click()

# Wait for the login page to load
wait = WebDriverWait(driver, 20)
username_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))

# Fill in the login form
username_input = driver.find_element(By.XPATH, '//input[@name="email"]')
username_input.send_keys(kaggle_username)     #simulating the keyboard input for username

password_input = driver.find_element(By.XPATH, '//input[@name="password"]')
password_input.send_keys(kaggle_password)      #simulating the keyboard input for password

# Submit the login form
password_input.send_keys(Keys.RETURN)

# Wait for the login to complete
time.sleep(5)

# Navigate to the dataset page
driver.get(dataset_url)

# Wait for the dataset page to load
time.sleep(5)

# Click on the "Download" button (adjust the XPath accordingly)
download_button = driver.find_element(By.XPATH, '//a[@href="/datasets/aliessamali/ecommerce/download?datasetVersionNumber=1"]')
download_button.click()

# Wait for the download to complete (you may need additional logic depending on the download method)
time.sleep(10)


# Close the browser window
driver.quit()

