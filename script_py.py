from selenium import webdriver
import time

driver = webdriver.Chrome()

article_array = [
    'Hello, World. ',
    'This is my first article. ',
    'Good evening!. ',
    'This is an awesome article. ',
    'Article...... '
]

print(f'Script started at {time.localtime().tm_hour}:{time.localtime().tm_min}\n')

# get request to page URL
driver.get('https://www.netbizzz.com/signin')
print('Link opened')

# Locating the element we want to interact with
username = driver.find_element_by_name('username_email')
password = driver.find_element_by_name('password')

# sending the data 
username.send_keys('User321')
password.send_keys('hello@123')
time.sleep(2)
print('Entered credentials')

# clicking the login button
login_button = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button')
login_button.click()
print('pressed login')
time.sleep(5)

# Textarea for article
# driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/div[1]').click()

textArea = driver.find_element_by_css_selector('body > div.main-wrapper > div.container.mt20.offcanvas > div > div.col-md-8.col-lg-9.offcanvas-mainbar > div > div.col-lg-8 > div.x-form.publisher > div.publisher-message > div.colored-text-wrapper > textarea')

for text_to_post in article_array:
 textArea.send_keys(text_to_post)
 time.sleep(3)
 
 # Post button for article
 post_button = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div[3]/div[15]/button')
 post_button.click()
 time.sleep(2)
 print('post button')
