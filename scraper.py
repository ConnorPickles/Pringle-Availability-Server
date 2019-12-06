from selenium.webdriver import Chrome
from time import sleep
import os
import traceback

def GetAvailability():
    # read login credentials from local file
    f = open('login.txt', 'r')
    login = f.read()
    login = login.split(' ')

    # start driver
    driver = Chrome()
    driver.implicitly_wait(10)

    # login in to camp brain
    try:
        driver.get("https://camppringle.campbrainoffice.com/Account/LogOn")
        driver.find_element_by_id('username').send_keys(login[0])
        driver.find_element_by_id('password').send_keys(login[1])
        driver.find_element_by_link_text('Login').click()
    except Exception:
        print('Error while logging in to Camp Brain')
        traceback.print_exc()
        driver.quit()

    # navigate to the correct season
    try:
        sleep(2)
        driver.find_element_by_id('dashboard-availabilitylink').click()
        sleep(1)
        driver.find_element_by_class_name('btn.btn-link.dropdown-toggle').click()
        driver.find_element_by_xpath('//*[@title="OSC Fall 2019"]').click()
    except Exception:
        print('Error while navigating to Fall 2019 availability')
        traceback.print_exc()
        driver.quit()

    # grab availability numbers
    availability = []
    xpath = '//*[@title="FOOBAR"]//..//*[@class="ss numbers tt"]//*[@class="spots-available"]//*[@class="major"]'    
    try:
        sleep(2)
        temp = driver.find_element_by_xpath(xpath.replace('FOOBAR', 'PM Care MONDAYS for December')).text
        availability.append(temp)
        temp = driver.find_element_by_xpath(xpath.replace('FOOBAR', 'PM Care TUESDAYS for December')).text
        availability.append(temp)
        temp = driver.find_element_by_xpath(xpath.replace('FOOBAR', 'PM Care WEDNESDAYS for December')).text
        availability.append(temp)
        temp = driver.find_element_by_xpath(xpath.replace('FOOBAR', 'PM Care THURSDAYS for December')).text
        availability.append(temp)
        temp = driver.find_element_by_xpath(xpath.replace('FOOBAR', 'PM Care FRIDAYS for December')).text
        availability.append(temp)
    except Exception:
        print('Error while getting availability numbers')
        traceback.print_exc()
        driver.quit()
    
    driver.quit()

    return availability

