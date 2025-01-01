from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By
import os



#Define Driver,options and service
chrome_options=Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

download_path=os.getcwd()
prefs={'download.default_directory': download_path}
chrome_options.add_experimental_option('prefs' , prefs)


service = Service("chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options , service=service)

#Load the webpage
driver.get('https://demoqa.com/login')

#locate username,passord and login button
username_field=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.ID,'userName')))
password_field=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.ID,'password')))
login_button=driver.find_element(By.ID,'login')


#fill username and password and click the button
username_field.send_keys('pythonstudent')
password_field.send_keys('pythonstudent123$')
driver.execute_script("arguments[0].click();",login_button)


#Locate the elements dropdown
elements=WebDriverWait(driver,5).\
    until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
elements.click()

text_box=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.ID,'item-0')))
text_box.click()
#Locate the form fields

fullname_field=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.ID,'userName')))
email_field=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.ID,'userEmail')))
current_address_field=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.ID,'currentAddress')))
permanent_address_field=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.ID,'permanentAddress')))
submit_button=driver.find_element(By.ID,'submit')


#Fill in the form fields
fullname_field.send_keys('Saurabh Sharma')
email_field.send_keys('saurabhlively@gmail.com')
current_address_field.send_keys('Pune')
permanent_address_field.send_keys('Pune')
driver.execute_script("arguments[0].click();",submit_button)


#Locate the upload and download section and click on Download jpeg file from URL/web server
upload_download = WebDriverWait(driver,5).\
    until(EC.visibility_of_element_located((By.ID,'item-7')))
upload_download.click()
download_button=driver.find_element(By.ID,'downloadButton')
driver.execute_script("arguments[0].click();",download_button)


input("Press Enter to close the driver")
driver.quit()


