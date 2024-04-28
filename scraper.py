from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_utils.selenium_actions import SeleniumActions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time

options: webdriver = webdriver.ChromeOptions()
driver: webdriver = webdriver.Chrome(options=options)
actions: SeleniumActions = SeleniumActions(driver=driver)

class OfferUpScraper:
  def __init__(self, url: str):
    self.url = url
    self.shoe_listings = []

  def set_location(self, zip_code: int):
    driver.get(self.url)

    main_page_element = driver.find_element(By.XPATH, '/html/body/div/header/div[2]/div[1]/div[1]/div/div[3]/button/span/span[2]/span')
    ActionChains(driver).click(main_page_element).perform()

    zip_code_element = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/div/div/div[3]/div[2]/button')
    ActionChains(driver).click(zip_code_element).perform()

    input_element = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/form/div[4]/div/div/div[4]/div[1]/div/div/input')
    ActionChains(driver).click(input_element).perform()

    input_element.send_keys(Keys.COMMAND, 'a')
    input_element.send_keys(Keys.DELETE)

    ActionChains(driver).click(input_element).perform()

    input_element.send_keys(zip_code)

    apply_button = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/form/div[5]/button')
    ActionChains(driver).click(apply_button).perform()

    time.sleep(1)

    exit_to_main_page = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/button')
    ActionChains(driver).click(exit_to_main_page).perform()

    time.sleep(5)

  def scrape_listings(self):
    while True:
      initial_len = len(self.shoe_listings)
      i = 1
      while True:
        try:
          xpath = f'/html/body/div/div[5]/div[2]/div[3]/main/div[2]/div/div[1]/div/a[{i}]'
          post = driver.find_element(By.XPATH, xpath)
          aria_label = post.get_attribute('aria-label')
          href = post.get_attribute('href')
          if href.startswith("https://www.bing.com"): # ad
            i += 1
            continue
          if (aria_label, href) not in self.shoe_listings:
            self.shoe_listings.append((aria_label, href))
          i += 1
        except:
          break
      driver.execute_script("window.scrollBy(0, 10000);")
      driver.implicitly_wait(1)
      if initial_len == len(self.shoe_listings):
        break

    driver.quit()

    print(self.shoe_listings)

x = OfferUpScraper('https://offerup.com/search?q=jordan+4&DISTANCE=5&DELIVERY_FLAGS=p')
x.set_location(94613)
x.scrape_listings()




