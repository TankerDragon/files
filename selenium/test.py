from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
  
driver.get("https://www.google.com/maps/dir/41.3196905,69.2666641/41.366112,69.212628")

div = driver.find_element(By.ID, value='section-directions-trip-0').find_elements(by=By.TAG_NAME, value='DIV')[0].find_elements(by=By.TAG_NAME, value='DIV')[0].find_elements(by=By.TAG_NAME, value='DIV')[0]
eta = div.find_elements(by=By.TAG_NAME, value='DIV')[0].find_elements(by=By.TAG_NAME, value='span')[0].get_attribute("innerText")
distance = div.find_elements(by=By.TAG_NAME, value='DIV')[1].find_elements(by=By.TAG_NAME, value='DIV')[0].get_attribute("innerText")
#num = div.find_elements(By.TAG_NAME, 'div')  #.get_attribute("innerText")

print(f"distance: {distance}, ETA: {eta}")
#mainHeader = driver.find_element(By.ID, 'section-directions-trip-title-0')
#timeSpan = mainHeader.find_elements(By.TAG_NAME, 'span')[0]

#t = driver.find_element(By.ID, 'section-directions-trip-details-msg-0')
#a = t.find_element(by=By.XPATH, value='../../..')

#print("#################")
#print(len(t))


driver.close()
