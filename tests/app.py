from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from percy import percySnapshot




def testcase(driver):

    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    percySnapshot(browser=driver, name='Amazon Home Page')
    search = driver.find_element_by_id("twotabsearchtextbox")
    search.send_keys("iPhone X")
    search.send_keys(Keys.RETURN)
    percySnapshot(browser=driver, name='Amazon with iPhone')

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/div[3]/span/div/span/div/div/div[8]/ul[2]/li[2]/span/a/div/label/i"))
        )
        element.click()
    except:
        print("yo1")
        driver.quit()

    # driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/div[3]/span/div/span/div/div/div[8]/ul[2]/li[2]/span/a/div/label/i").click()
    # driver.implicitly_wait(4)
    # driver.find_element_by_css_selector("li[id='p_n_operating_system_browse-bin/1485080031']").click()
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "a-autoid-0-announce"))
        )
        element.click()
    except:
        print("yo2")
        driver.quit()

    # driver.find_element_by_id("a-autoid-0-announce").click()
    # driver.implicitly_wait(3)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "s-result-sort-select_2"))
        )
        element.click()
    except:
        print("yo3")
        driver.quit()

    # driver.find_element_by_id("s-result-sort-select_2").click()
    # driver.implicitly_wait(3)
    # try:
    #     element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='a-section a-spacing-medium']"))
    #     )
    #     element
    # except:
    #     print("yo4")
    #     driver.quit()
    driver.implicitly_wait(3)
    percySnapshot(browser=driver, name='Amazon iPhone sorted')

    # ll1 = driver.find_elements_by_css_selector("div[class='a-section a-spacing-medium']")

    # for i in ll1:

    #     a = i.find_element_by_css_selector(
    #         "a[class='a-link-normal a-text-normal']")
    #     try:
    #         b = i.find_element_by_css_selector("span.a-price-whole")
    #         b = b.text
    #     except:
    #         b = ""

    #     print("Product Title: ", a.text)
    #     print("Product Price: ", b)
    #     print("Product Link: ", a.get_attribute('href'))
    #     print("\n------------\n")
    
    driver.quit()


#driver = webdriver.Firefox()
#testcase(driver)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-setuid-sandbox')
chrome_options.add_argument('--headless')
print("\n######################################\n")
PATH = r"/Users/Arvind/Desktop/test/sel_demo/selenium/chromedriver"
driver = webdriver.Chrome(PATH, options=chrome_options)
testcase(driver)
