from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from user import password, username

class GitHub:
    def __init__(self, username, password):
        self.browser = webdriver.Firefox()
        self.username = username
        self.password = password

    def signIn(self):
        url = "https://github.com/login"
        self.browser.get(url)
        time.sleep(2)
        self.browser.maximize_window()
        time.sleep(1)
        self.browser.find_element(By.XPATH, "//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element(By.XPATH, "//*[@id='password']").send_keys(self.password)
        time.sleep(2)
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[13]").click()
        time.sleep(2)

    def profile(self):
        self.browser.find_element(By.CSS_SELECTOR, ".AppHeader-user button").click()
        time.sleep(2)
        a_element = self.browser.find_elements(By.CSS_SELECTOR, ".ActionList ul.ActionListWrap li")

        for x in a_element:
            if x.text == "Your repositories":
                x.click()
        time.sleep(2)
    def new_repo(self):
        self.browser.find_element(By.XPATH,"/html/body/div[1]/div[6]/main/div/div/div[2]/turbo-frame/div/div[1]/div/div/a").click()
        time.sleep(1)
        self.browser.find_element(By.XPATH,"//*[@id=':r3:']").send_keys("Reponame")
        time.sleep(1)
        self.browser.find_element(By.XPATH,"/html/body/div[1]/div[6]/main/react-app/div/form/div[5]/button").click()
        time.sleep(2)
    def return_profile(self):
        self.browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/header/div[1]/div[1]/div/div[2]/nav/ul/li[1]/a").click()




github = GitHub(username, password)
github.signIn()
github.profile()
github.new_repo()
github.return_profile()
