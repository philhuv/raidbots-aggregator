from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
# options.headless = True
driver = webdriver.Chrome(options=options)
driver.get("http://raidbots.com/simbot/quick?region=us&realm=malganis&name=garctic")
print (driver.current_url)
driver.save_screenshot("screenshot.png")
time.sleep(5)
sim_text = driver.find_elements_by_xpath("//*[contains(text(), 'Run Quick Sim')]")
print(sim_text[0])
flex = sim_text[0].find_element_by_xpath('..')
sim_button = flex.find_element_by_xpath('..')
sim_button.click()
time.sleep(5)

# driver.find_element_by_css_selector('.Button').click()
print (driver.current_url)
# driver.close()