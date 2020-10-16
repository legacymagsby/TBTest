from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

username = os.getenv("BROWSERSTACK_USERNAME")
access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")


caps = {
 'os': 'Windows',
 'browser': 'chrome',
 'browserstack.user': username,
 'browserstack.key': access_key
}

driver = webdriver.Remote(
    command_executor='https://hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=caps)



driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("BrowserStack")
elem.submit()
print(driver.title)
driver.quit()
