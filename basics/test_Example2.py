from selenium import webdriver

def test_Google():
   driver =  webdriver.Chrome()
   driver.get("https://www.google.com")
   driver.maximize_window()
   driver.implicitly_wait(30)
   actaul_title = driver.title
   assert actaul_title == "Google"
   driver.close()