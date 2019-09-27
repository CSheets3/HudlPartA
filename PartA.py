from selenium import webdriver
# from selenium.webdriver import ActionChains
import time
# The amount of time in seconds it's going to take before moving onto the next task

# You'll have to change the location of your chrome driver for this to work
browser = webdriver.Chrome('/Users/codysheets/Downloads/ProgrammingStuff/Drivers/chromedriver')

# You could also start a function here if you wanted to iterate it multiple times
# Opens the browser to the Hudl login page
browser.get('https://www.hudl.com/login')
time.sleep(2)
browser.maximize_window()

username = 'cody12sheets@gmail.com'
password = 'Dwighthoward12!'

# Puts my username in the email field
email_login = browser.find_element_by_id('email').send_keys(username)
time.sleep(3)

# Puts my password into the password field
password_login = browser.find_element_by_id('password').send_keys(password)
time.sleep(3)

# Clicks the login button after username and password have been filled in
login = browser.find_element_by_id('logIn')
login.click()
time.sleep(5)

# Preparing the data for comparison
tested_result = browser.current_url
time.sleep(2)
expected_result = 'https://www.hudl.com/home'

# Compares the URL's to see if they ended up on the same page
if tested_result == expected_result:
    print('Test Passed!')
else:
    print('Test Failed! Incorrect username or password.')
    time.sleep(3)
    browser.quit()
time.sleep(4)

# Logs out and closes the browser
# You could also use ActionChains to do it, but this way was easier
logout = browser.get('https://www.hudl.com/logout')
time.sleep(2)
browser.quit()
