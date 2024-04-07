from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from random import randint, choice

def save_used_user_agent(used_user_agent):
        with open('used_user_agents.txt', 'a') as file:
            file.write(used_user_agent+'\n')
            
def choose_random_user_agent():
    with open('user-agents.txt', 'r') as file:
        user_agents = file.readlines()

    try:
        with open('used_user_agents.txt', 'r') as file:
            used_user_agents = file.readlines()
    except FileNotFoundError:
        used_user_agents = []

    user_agents = [user_agent for user_agent in user_agents if user_agent not in used_user_agents]

    if len(user_agents) == 0:
        return "All user agents have been used."
    else:
        random_user_agent = choice(user_agents)
        # save_used_user_agent(random_user_agent)
        return random_user_agent.strip()


options = Options()
options.add_extension('urban.crx')
options.add_extension('Adblock.crx')
options.add_experimental_option("detach", True)
user_agent = choose_random_user_agent()
options.add_argument(f"user-agent={user_agent}")
options.add_argument("--headless=new")
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)
driver.get("chrome-extension://eppiocemhmnlbhjplcgkofciiegomcon/popup/index.html#/welcome-consent")
driver.maximize_window()


def vpn_proccess(driver):
    driver.switch_to.window(driver.window_handles[0])
    a = '/html/body/div/div/div[3]/div[2]/div/div[1]/input'
    b = '/html/body/div/div/div[3]/div[2]/div/div[2]/div/ul/li[1]'
    driver.find_element(By.XPATH,value=a).click()
    driver.find_element(By.XPATH,value=b).click()
    driver.execute_script("window.open();")
    driver.switch_to.window(driver.window_handles[1])
    start(driver)
    
def waitForLoad(path):
    while True:
        try:
            driver.find_element(By.XPATH,value=path)
            break
        except:
            sleep(1)
            

def google_page(driver):
    btn1 = '//*[@id="main"]/div[4]/div/div[1]/a/div/div[1]/h3/div'
    btn2 = '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a/h3'
    btn3 = '/html/body/div[2]/div[1]/div/div/div/div[1]/a/span[1]'
    btn4 = '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a/h3'
    try:
        driver.find_element(By.XPATH,btn1).click()
        print("Google 0 xpath")
    except:
        
        try:
            driver.find_element(By.XPATH,btn2).click()
            print("Google 1 xpath")
        except:
            
            try:
                driver.find_element(By.XPATH,btn3).click()
                print("Google 2 xpath")
            except:
                print("Google Error")
                pass

def vpn(driver):
    driver.switch_to.window(driver.window_handles[1])
    # sleep(10)
    waitForLoad("/html/body/div/div/div[2]/div/div/div/button[2]")
    clickby_xpath("/html/body/div/div/div[2]/div/div/div/button[2]")
    clickby_xpath("/html/body/div/div/div[3]/div[2]/div/div[1]/input")
    driver.implicitly_wait(5)
    i=1
    clickby_xpath("/html/body/div/div/div[3]/div[2]/div/div[2]/div/ul/li["+str(i)+"]")
    print("VPN Activated")
    sleep(4)
    driver.switch_to.window(driver.window_handles[2])
    sleep(1)
    start(driver)
    
def find_ip(driver):
    driver.get('https://www.myip.com/')
    try:
        sleep(1)
        ip = driver.find_element(By.XPATH,'//*[@id="ip"]')
        ip = ip.text
    except:
        print('Error to get IP')
    return ip

def start(driver):
    # print("IP : ",find_ip(driver))
    print('started')
    driver.get('https://linkpays.in/Z7N6Vz25')
    # sleep(10)
    Linkpay_process()


def clickby_id(id):
    try:
        driver.find_element(By.ID, id).click()
        # print("ID Success")
    except:
        sleep(2)
        # print("ID error")
        clickby_id(id) 
        

def clickby_xpath(path):
    try:
        driver.find_element(By.XPATH, path).click()
        # print("XPath Success")
    except:
        # print("XPath error")
        sleep(2)
        clickby_xpath(path)



def Linkpay_process():
    print('Process Started')
    waitForLoad('//*[@id="yuidea"]')
    # clickby_id('yuidea')
    clickby_xpath('//*[@id="yuidea"]')
    print("1-Done")
    # sleep(3)
    waitForLoad('/html/body/div[6]/center/center[2]/div[3]/button')
    clickby_xpath('/html/body/div[6]/center/center[2]/div[3]/button')
    print("2-Done")
    sleep(3)
    driver.switch_to.window(driver.window_handles[3])
    waitForLoad('//*[@id="btn6"]')
    # clickby_id('btn6')
    clickby_xpath('//*[@id="btn6"]')
    print("3-Done")
    # sleep(10)
    waitForLoad('//*[@id="btn6"]')
    # clickby_id('btn6')
    clickby_xpath('//*[@id="btn6"]')
    print("4-Done")
    sleep(10)
    # waitForLoad('//*[@id="disposable-email"]')
    save_used_user_agent(user_agent)
    driver.quit()
    
vpn(driver)