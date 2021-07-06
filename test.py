from selenium import webdriver

# driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path=r"C:\\path\\to\\chromedriver.exe")
driver.get('https://www.youtube.com/post/UgwYw_vvTfk6PDQH5k94AaABCQ')

button_element = driver.find_element_by_id('label')
button_element.click()