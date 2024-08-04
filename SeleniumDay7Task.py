import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DragDrop:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://jqueryui.com/droppable/")
        self.driver.maximize_window()

    def switch_to_iframe(self):
        iframe_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//iframe[@class='demo-frame']"))
        )
        self.driver.switch_to.frame(iframe_element)

    def drag_and_drop(self):
        draggable = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "draggable"))
        )
        destination = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "droppable"))
        )
        time.sleep(10)
        action = ActionChains(self.driver)
        action.drag_and_drop(draggable, destination).perform()
        time.sleep(10)
        print("drag and drop functionality working successfully !!")

    def quit_driver(self):
        self.driver.quit()

if __name__ == "__main__":
    drag_drop_instance = DragDrop()
    drag_drop_instance.switch_to_iframe()
    drag_drop_instance.drag_and_drop()
    time.sleep(5)  # Wait to see the result
    drag_drop_instance.quit_driver()
