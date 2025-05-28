import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()


class WebAutomation():
    def __init__(self):
        # Define driver, options and service
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        prefs = {
            'download.default_directory': os.getcwd(),
            'download.prompt_for_download': False,
        }
        chrome_options.add_experimental_option("prefs", prefs)
        service = Service("chromedriver-mac-arm64/chromedriver")
        self.driver = webdriver.Chrome(options=chrome_options, service=service)



    def login(self, username, password):
        # Load the webpage
        self.driver.get("https://demoqa.com/login")

        # Locate username, password, and login button
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        login_button = self.driver.find_element(By.ID, 'login')

        # Fill in username and password
        username_field.send_keys(username)
        password_field.send_keys(password)
        self.driver.execute_script("arguments[0].click();", login_button)

    def fill_form(self, full_name, email, current_address, permanent_address):
        # Locate the Elements dropdown and Text Box
        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
        elements.click()

        text_box = password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
        text_box.click()

        # Locate the form fields and submit button
        fullname_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        current_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'currentAddress')))
        permanent_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        submit_button = self.driver.find_element(By.ID, 'submit')

        fullname_field.send_keys(full_name)
        email_field.send_keys(email)
        current_address_field.send_keys(current_address)
        permanent_address_field.send_keys(permanent_address)
        self.driver.execute_script("arguments[0].click();", submit_button)

    def download_file(self):
        # Locate the upload and download section and download button
        upload_download = self.driver.find_element(By.ID, 'item-7')
        self.driver.execute_script("arguments[0].click();", upload_download)
        download_button = self.driver.find_element(By.ID, 'downloadButton')
        self.driver.execute_script("arguments[0].click();", download_button)

    def close(self):
        input("Press ENTER to exit")
        self.driver.quit()


if __name__ == '__main__':
    web_automation = WebAutomation()
    web_automation.login(os.getenv("USERNAME"), os.getenv("PASSWORD"))
    web_automation.fill_form("John Roe", "john@gmail.com", "John street 100, NY", "John street 100, NY")
    web_automation.download_file()
    web_automation.close()

