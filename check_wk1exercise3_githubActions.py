import time, os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    html_path = 'file://' + os.path.abspath('wk1exercise3.html')
    driver.get(html_path)

    input1 = driver.find_element(By.ID, "num1")
    input2 = driver.find_element(By.ID, "num2")
    assert input1.get_attribute('type') == 'number', "Input 1 is not of type number"
    assert input2.get_attribute('type') == 'number', "Input 2 is not of type number"

    input1.send_keys('5')
    input2.send_keys('7')

    result = driver.execute_script(
        "return parseInt(document.getElementById('num1').value) + parseInt(document.getElementById('num2').value);"
    )

    print(f"Sum from the page is: {result}")

    assert result == 12, "Sum calculation is incorrect"

    print("Test Passed!")

finally:
    time.sleep(2)
    driver.quit()
