from selenium import webdriver
import time

def main():
    driver = webdriver.Chrome()
    driver.get("https://www.uni-hamburg.de/")
    title = driver.title
    print(title)
    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    main()