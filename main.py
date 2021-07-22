from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import asyncio
import time

options = Options()
options.headless = True

async def runSim(char_name):
	driver = webdriver.Chrome('bin/chromedriver', options=options)


	driver.get('http://raidbots.com/simbot/quick' + 
		f'?region=us&realm=malganis&name={char_name}')
	print (driver.current_url)
	await asyncio.sleep(5)
	sim_text = driver.find_elements_by_xpath("//*[contains(text(), 'Run Quick Sim')]")
	flex = sim_text[0].find_element_by_xpath('..')
	sim_button = flex.find_element_by_xpath('..')
	sim_button.click()
	await asyncio.sleep(5)

	report_url = driver.current_url
	driver.close()
	return char_name, report_url

async def main():
	# loop = asyncio.get_event_loop()
	lst = [
		asyncio.create_task(runSim('garctic')), 
		asyncio.create_task(runSim('joltheus'))
	]
	results = await asyncio.gather(*lst)
	print(results)

asyncio.run(main())