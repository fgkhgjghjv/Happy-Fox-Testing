from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class Testcase101:

    def main(self):
        driver = webdriver.Firefox(executable_path="C:\\Users\\Johny\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver.exe")
        '''Instead of using specific version of webdriver.exe file we can use webdriver manager for automatically keeping our framework in sink with latest version of
        browser and Use environment variables to specify paths that might vary across different environments or users.''' 

        driver.get("https://interview.supporthive.com/staff/")
        #Instead of directly using Hardcoded url it is better to define baseURL  and staff URL as constants

        driver.implicitly_wait(30)
        #Instead of using value it is better to assign constant

        driver.maximize_window()
        driver.find_element(By.ID, "id_username").send_keys("Agent")
        driver.find_element(By.ID, "id_password").send_keys("Agent@123")
        driver.find_element(By.ID, "btn-submit").click()
        tickets = driver.find_element(By.ID, "ember29")
        action = ActionChains(driver)
        action.move_to_element(tickets).perform()
        statuses = driver.find_element(By.LINK_TEXT, "Statuses")
        statuses.click()
        #When Performing actions on webpage we must handle the exceptions that might potentially occur when interacting with the webpage.

        driver.find_element(By.XPATH, "/html/body/div[3]/div/section/section/div/header/button").click()
        #Instead of using Absolute xpath it is better to use relative xpath whenever possible because it may cause issue when structure of webpage changes.

        driver.find_element(By.TAG_NAME, "input").send_keys("Issue Created")
        statusColourSelect = driver.find_element(By.XPATH, "//div[@class='sp-replacer sp-light']")
        statusColourSelect.click()
        # Implement explcit wait in order to wait untill the element is clickable.

        statusColourEnter = driver.find_element(By.XPATH, "//input[@class='sp-input']")
        statusColourEnter.clear()
        statusColourEnter.send_keys("#47963f")
        r = Robot()
        r.keyPress(KeyEvent.VK_ESCAPE)
        firstElement = driver.find_element(By.XPATH, "//a[@id='first-link']")
        firstElement.click()
        # Implement explcit wait in order to wait untill the element is clickable.

        secondElement = driver.find_element(By.XPATH, "//a[@id='second-link']")
        secondElement.click()
        # Implement explcit wait in order to wait untill the element is clickable.

        driver.find_element(By.TAG_NAME, "textarea").send_keys("Status when a new ticket is created in HappyFox")
        addCreate = driver.find_element(By.XPATH, "//button[@class ='hf-entity-footer_primary hf-primary-action ember-view']")
        addCreate.click()
        time.sleep(3)
        # Replace with explicit wait.

        moveTo = driver.find_element(By.XPATH, "//td[@class ='lt-cell align-center hf-mod-no-padding ember-view']")
        # Instead of using xpath with multipe class names it is better to use single class name for more stablity in xpath.

        action.move_to_element(moveTo).perform()
        moveTo.click()
        # Implement explcit wait in order to wait untill the element is clickable.

        time.sleep(9)
        # Replace with explicit wait.

        issue = driver.find_element(By.XPATH, "//div[contains(text(),'Issue Created')]")
        action.move_to_element(issue).perform()
        make = driver.find_element(By.LINK_TEXT, "Make Default")
        make.click()
        # Implement explcit wait in order to wait untill the element is clickable.

        driver.find_element(By.LINK_TEXT, "Priorities").click()
        # Implement explcit wait in order to wait untill the element is clickable.

        driver.find_element(By.XPATH, "//header/button[1]").click()
        # Implement explcit wait in order to wait untill the element is clickable.

        driver.find_element(By.TAG_NAME, "input").send_keys("Assistance required")
        driver.find_element(By.TAG_NAME, "textarea").send_keys("Priority of the newly created tickets")
        button = driver.find_element(By.CSS_SELECTOR, "button[data-test-id='add-priority']")
        button.click()
        # Implement explcit wait in order to wait untill the element is clickable.

        time.sleep(9)
        # Replace with explicit wait.

        tickets2 = driver.find_element(By.ID, "ember29")
        action.move_to_element(tickets2).perform()
        priorities2 = driver.find_element(By.LINK_TEXT, "Priorities")
        priorities2.click()
        # Implement explcit wait in order to wait untill the element is clickable.

        driver.implicitly_wait(20)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/section[1]/section[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[9]/td[2]").click()
        '''Instead of using Absolute xpath it is better to use relative xpath whenever possible because it may cause issue when structure of webpage changes.
            Implement explcit wait in order to wait untill the element is clickable.'''
        
        driver.find_element(By.LINK_TEXT, "Delete").click()
        # Implement explcit wait in order to wait untill the element is clickable.

        delete = driver.find_element(By.CSS_SELECTOR, "button[data-test-id='delete-dependants-primary-action']")
        delete.click()
        # Implement explcit wait in order to wait untill the element is clickable.

        time.sleep(9)
        # Replace with explicit wait.

        driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/header[1]/div[2]/nav[1]/div[7]/div[1]/div[1]").click()
        '''Instead of using Absolute xpath it is better to use relative xpath whenever possible because it may cause issue when structure of webpage changes.
         Implement explcit wait in order to wait untill the element is clickable.'''

        driver.find_element(By.LINK_TEXT, "Logout").click()
        # Implement explcit wait in order to wait untill the element is clickable.

class PagesforAutomationAssignment:

    def main(self):
        driver = webdriver.Chrome()
        # Place this in setup method.

        driver.get("https://www.happyfox.com")
        #Define base URL as constant.
        loginPage = LoginPage(driver)
        loginPage.login("username", "password")
        homePage = HomePage(driver)
        homePage.verifyHomePage()
        #Place the above five lines in try block

        driver.quit()
        #place this in teardown method.

class BasePage:

    def __init__(self, driver):
        self.driver = driver

class LoginPage(BasePage):

    def login(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "loginButton").click()
        # Implement explcit wait in order to wait untill the element is clickable.

    def forgotPassword(self):
        self.driver.find_element(By.LINK_TEXT, "Forgot password?").click()
        # Implement explcit wait in order to wait untill the element is clickable.

class HomePage(BasePage):

    def verifyHomePage(self):
        if self.driver.current_url != "https://www.happyfox.com/home":
            raise Exception("Not on the home page")

    def navigateToProfile(self):
        self.driver.find_element(By.ID, "profileLink").click()
        # Implement explcit wait in order to wait untill the element is clickable.

class TablePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.rowLocator = By.XPATH("//table[@id='dataTable']/tbody/tr")

    def retrieveRowTexts(self):
        rows = self.driver.find_elements(self.rowLocator)

        for i in range(len(rows)):
            row = rows[i]
            rowText = row.text
            print("Row " + str(i) + " Text: " + rowText)

