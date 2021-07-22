from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import asyncio
import time
import app_constants
import character_repository

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


async def run_droptimizer(char_name, difficulty):
	driver = webdriver.Chrome('bin/chromedriver', options=options)


	driver.get('http://raidbots.com/simbot/droptimizer' + 
		f'?region=us&realm=malganis&name={char_name}')
	print (driver.current_url)
	driver.execute_script("window.scrollTo(0, 720)") 
	await asyncio.sleep(10)
	sanctum_text = driver.find_elements_by_xpath("//*[contains(text(), 'Sanctum of Domination')]")
	sanctum_button = sanctum_text[0].find_element_by_xpath('..').find_element_by_xpath('..')
	# driver.execute_script("arguments[0].scrollIntoView(true);", sanctum_button);
	# ActionChains(driver).move_to_element(sanctum_button).click().perform()

	sanctum_button.click()

	await asyncio.sleep(5)
	driver.execute_script("window.scrollTo(0, 1200)") 
	mythic_text = driver.find_elements_by_xpath(f"//*[contains(text(), '{difficulty}')]")
	print(mythic_text)
	driver.save_screenshot("screenshot.png")
	mythic_button = mythic_text[0].find_element_by_xpath('..')
	# ActionChains(driver).move_to_element(mythic_button).click().perform()
	mythic_button.click()
	await asyncio.sleep(3)

	sim_text = driver.find_elements_by_xpath("//*[contains(text(), 'Run Droptimizer')]")
	flex = sim_text[0].find_element_by_xpath('..')
	sim_button = flex.find_element_by_xpath('..')
	# ActionChains(driver).move_to_element(sim_button).click().perform()
	sim_button.click()
	await asyncio.sleep(3)

	report_url = driver.current_url
	return char_name, report_url


async def main():
	# loop = asyncio.get_event_loop()
	# lst = [
	# 	asyncio.create_task(runSim('garctic')), 
	# 	asyncio.create_task(runSim('joltheus'))
	# ]
	# results = await asyncio.gather(*lst)
	print(character_repository.get_characters())
	character_repository.add_character('Jackdruid')
	print(character_repository.get_characters())
	# print(results)

# asyncio.run(main())