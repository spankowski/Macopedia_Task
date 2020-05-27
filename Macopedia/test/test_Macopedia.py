import unittest
from selenium import webdriver 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from cryptography.fernet import Fernet
import logging
import time
#import library.read_csv as read_csv
#import library.decrypt_bin as dec
import sys
import os
import re
import warnings

class TestStringMethods(unittest.TestCase):

    def test_fill_contact(self):
        # example test
        #warnings.filterwarnings('ignore')

        driver = webdriver.Firefox()
        driver.get('https://macopedia.com/contact')	

        iframe = driver.find_element_by_xpath("//form[@class='contact-form contact__form']/div/div/iframe")
        driver.switch_to.frame(iframe)

        driver.find_element_by_name('firstname').send_keys('Jan')
        driver.find_element_by_name('lastname').send_keys('Nowak')
        driver.find_element_by_name('company').send_keys('IT Company')
        driver.find_element_by_name('email').send_keys('abcsdas@gmail.com')
        driver.find_element_by_name('message').send_keys('Watch today\'s NASA Live 27.05')
        driver.find_element_by_name('LEGAL_CONSENT.processing').click()
        driver.find_element_by_xpath("//input[@type='submit']").click()

if __name__ == '__main__':
    unittest.main()
