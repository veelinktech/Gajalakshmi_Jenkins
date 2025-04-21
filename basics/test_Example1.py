from selenium.webdriver.chrome import webdriver


def test_Fb():
    driver = webdriver.ChromiumDriver()
    driver.get("http://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    assert driver.title == "Facebook – log in or sign up"
    driver.close()