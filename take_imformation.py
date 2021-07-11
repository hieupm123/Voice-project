from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
# driver = webbrowser.get();
# driver.open("https://selenium-python.readthedocs.io/getting-started.html#using-selenium-with-remote-webdriver")
PATH = 'C:\Program Files (x86)\chromedriver.exe';
driver = webdriver.Chrome(PATH);
driver.get('https://selenium-python.readthedocs.io')
search = driver.find_element_by_link_text("8. Appendix: Frequently Asked Questions")
search.click()
driver.back()
# search.send_keys("test")
# search.send_keys(Keys.RETURN)
# time.sleep(4)
# driver.quit()