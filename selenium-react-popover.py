import time
import traceback
import os
import json
from colorama import Fore, Style
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(executable_path='path/to/chromedriver')

def test_popover():
    """
    Test Cases 1 : Test Popover

    """
    try:
        driver.get('https://mui.com/material-ui/react-popover/')
        by = By.XPATH

        time.sleep(1)
        button1 = driver.find_element(by, "//button[contains(text(), 'Open Popover')]")
        if button1 is None:
            print(Fore.RED + "FAIL : if button1 is None" + Style.RESET_ALL)
            raise NoSuchElementException("button1 is None")
        else:
            print(Fore.GREEN + "PASS : if button1 is None" + Style.RESET_ALL)

        if not button1.is_enabled():
            print(Fore.RED + "FAIL : if not button1.is_enabled()" + Style.RESET_ALL)
            raise NoSuchElementException("not button1.is_enabled()")
        else:
            print(Fore.GREEN + "PASS : if not button1.is_enabled()" + Style.RESET_ALL)

        button_text = button1.text
        if button_text != "OPEN POPOVER":
            print(Fore.RED + "FAIL : if button_text != OPEN POPOVER" + Style.RESET_ALL, button_text)
            raise NoSuchElementException("if button_text != OPEN POPOVER", button_text)
        else:
            print(Fore.GREEN + "PASS : if button_text != OPEN POPOVER" + Style.RESET_ALL, button_text)

        if button1.is_displayed():
            print(Fore.GREEN + "PASS : button 'OPEN POPOVER' was displayed" + Style.RESET_ALL)
        else:
            print(Fore.RED + "FAIL : button 'OPEN POPOVER' not displayed" + Style.RESET_ALL)
            raise NoSuchElementException("if button_text != OPEN POPOVER")
        button1.click()

        # scroll_distance = 1200 
        # driver.execute_script(f"window.scrollBy(0, {scroll_distance});")

        time.sleep(3)
        button2 = driver.find_element(by, '/html/body/div[1]/div/main/div/div[14]/div[2]/div/div[1]/div/button')
        driver.execute_script("arguments[0].scrollIntoView();", button2)
        if not button2.is_enabled():
            print(Fore.RED + "FAIL : if not button2.is_enabled()" + Style.RESET_ALL)
            raise NoSuchElementException("if not button2.is_enabled()")
        else:
            print(Fore.GREEN + "PASS : if not button2.is_enabled()" + Style.RESET_ALL)
        button2.click()

        time.sleep(3)
        radio_button1 = driver.find_element(by, "/html/body/div[1]/div/main/div/div[14]/div[2]/div/div[2]/div[1]/fieldset/div/label[2]/span[1]/span[2]")
        driver.execute_script("arguments[0].scrollIntoView();", radio_button1)
        if not radio_button1.is_enabled():
            print(Fore.RED + "FAIL : if not radio_button1.is_enabled()" + Style.RESET_ALL)
            raise NoSuchElementException("if not radio_button1.is_enabled()")
        else:
            print(Fore.GREEN + "PASS : if not radio_button1.is_enabled()" + Style.RESET_ALL)
        radio_button1.click()
        if radio_button1.is_selected():
            print(Fore.GREEN + "PASS : radio_button1 is selected" + Style.RESET_ALL)
        else:
            print(Fore.RED + "FAIL : radio_button1 is not selected" + Style.RESET_ALL)
            raise NoSuchElementException("radio_button1 is not selected", radio_button1)

        time.sleep(1)
        radio_button2 = driver.find_element(by, '/html/body/div[1]/div/main/div/div[14]/div[2]/div/div[2]/div[1]/fieldset/div/label[1]/span[1]/input')
        if not radio_button2.is_enabled():
            print(Fore.RED + "FAIL : if not radio_button2.is_enabled()" + Style.RESET_ALL)
            raise NoSuchElementException("if not radio_button2.is_enabled()")
        else:
            print(Fore.GREEN + "PASS : if not radio_button2.is_enabled()" + Style.RESET_ALL)
        radio_button2.click()
        
        report = {
            "test_name": "test_popover",
            "status": "PASS",
            "message": "All tests passed",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        with open("report_materialUI.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            data.append(report)

        with open("report_materialUI.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


    except Exception as exception_popover:
        print("exception_popover:", str(exception_popover))
        driver.save_screenshot("error_popover.png")
        print("Save:", "error_popover.png")
        report = {
            "test_name": "test_popover",
            "status": "FAIL",
            "message": str(exception_popover),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        with open("report_materialUI.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            data.append(report)

        with open("report_materialUI.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    finally:
        driver.quit()


if __name__ == "__main__":
    try:
        test_popover()
    except Exception as e:
        print(Fore.RED + "Test failed with error:" + Style.RESET_ALL)
        print(traceback.format_exc())