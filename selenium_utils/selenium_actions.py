from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from typing import Literal
import time

class SeleniumActions:
  def __init__(
    self,
    driver: webdriver,
  ):
    """
    Initializes the SeleniumActions class with a webdriver instance.

    Parameters:
    - driver (webdriver): The webdriver instance to interact with.
    """
    self.driver = driver

  def find_element(self,
    identifierType: Literal['class_name', 'xpath', 'css_selector', 'id'],
    identifier: str,
    click: bool = False):
    """
    Finds an element based on the specified identifier type and identifier, and optionally clicks it.

    Parameters:
    - identifierType (Literal): The type of identifier to use (class_name, xpath, css_selector, id).
    - identifier (str): The value of the identifier.
    - click (bool): Whether to click the element after finding it.

    Returns:
    - WebElement: The found web element.

    Raises:
    - ValueError: If an invalid identifierType is provided.
    """

    byFunctionMap = {
      'class_name': By.CLASS_NAME,
      'xpath': By.XPATH,
      'css_selector': By.CSS_SELECTOR,
      'id': By.ID
    }

    byMethod = byFunctionMap.get(identifierType)
    if byMethod:
      element = self.driver.find_element(byMethod, identifier)
      if click:
        element.click()
    else:
      raise ValueError(f'Invalid identifierType: {identifierType}')

    return element

  def find_elements(self,
    identifierType: Literal['class_name', 'xpath', 'css_selector', 'id'],
    identifier: str,
    ):
    """
    Finds multiple elements based on the specified identifier type and identifier.

    Parameters:
    - identifierType (Literal): The type of identifier to use (class_name, xpath, css_selector, id).
    - identifier (str): The value of the identifier.

    Returns:
    - list: A list of found web elements.

    Raises:
    - ValueError: If an invalid identifierType is provided.
    """

    byFunctionMap = {
      'class_name': By.CLASS_NAME,
      'xpath': By.XPATH,
      'css_selector': By.CSS_SELECTOR,
      'id': By.ID
    }

    byMethod = byFunctionMap.get(identifierType)
    if byMethod:
      elements = self.driver.find_elements(byMethod, identifier)
    else:
      raise ValueError(f'Invalid identifierType: {identifierType}')

    return elements

  def input_value(
      self,
      identifierType: Literal['class_name', 'xpath', 'css_selector', 'id'], identifier: str,
      input_text: any):
    """
    Finds an element based on the specified identifier type, clicks on it, clears the field, and enters new text.

    Parameters:
    - identifierType (Literal): The type of identifier to use (class_name, xpath, css_selector, id).
    - identifier (str): The value of the identifier.
    - input_text (any): The text to enter into the input field after clearing it.

    Raises:
    - ValueError: If an invalid identifierType is provided.
    """
    element = self.find_element(identifierType, identifier, click=True)
    element.clear()
    element.send_keys(input_text)

  def scroll(
    self,
    scrollLengthXOffset: float,
    scrollLengthYOffset: float,
    timeSleepBetweenInterval: int,
    intervalAmount: int,):
    """
    Scrolls the webpage by the specified x and y offsets, optionally with intervals and sleep between intervals.

    Parameters:
    - scrollLengthXOffset (float): The horizontal scroll length.
    - scrollLengthYOffset (float): The vertical scroll length.
    - timeSleepBetweenInterval (int): The time to sleep between each scroll interval (in seconds).
    - intervalAmount (int): The number of intervals to scroll; if 0, scrolls once without intervals.
    """

    if timeSleepBetweenInterval > 0 and intervalAmount > 0:
      for _ in range(intervalAmount):
        self.driver.execute_script(f'window.scrollBy({scrollLengthXOffset}, {scrollLengthYOffset})')
        time.sleep(timeSleepBetweenInterval)
    else:
      self.driver.execute_script(f'window.scrollBy({scrollLengthXOffset}, {scrollLengthYOffset})')

