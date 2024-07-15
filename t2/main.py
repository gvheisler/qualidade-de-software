from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time


def main():
    driver = webdriver.Chrome()
    driver.get("https://www.uni-hamburg.de/")
    test_link_validity(driver)
    driver.quit()


# verifica botões

def test_navigate_to_wissenschaftliche_karrierewege(driver):
    button = driver.find_element(By.CLASS_NAME, "Wiss")
    button.click()
    title = driver.title
    assert title == "Wissenschaftliche Karrierewege : Universität Hamburg", "O título da página não corresponde ao esperado"
    time.sleep(1)
    driver.back()


def test_navigate_to_exzellenzuniversitat(driver):
    button = driver.find_element(By.CLASS_NAME, "Ex")
    button.click()
    title = driver.title
    assert title == "Exzellenzuniversität : Universität Hamburg", "O título da página não corresponde ao esperado"
    time.sleep(1)
    driver.back()


# verifica busca

def test_search_for_deep_learning(driver):
    wait = WebDriverWait(driver, 5)
    search_button = wait.until(EC.element_to_be_clickable((By.ID, "suchea")))
    search_button.click()
    search_box = wait.until(EC.element_to_be_clickable((By.ID, "inputx-0")))
    search_box.send_keys("deep learning")
    search_box.submit()
    wait.until(EC.title_contains("Suche auf"))
    title = driver.title
    assert "Suche auf" in title, "A busca não foi realizada corretamente"
    driver.back()


#verifica imagens

def test_image_visibility_homepage(driver):
    wait = WebDriverWait(driver, 10)
    image = wait.until(EC.presence_of_element_located((By.XPATH, "//img[@title='Zur Homepage']")))
    assert image.is_displayed(), "A imagem 'Zur Homepage' não está visível"


def test_image_visibility_students(driver):
    wait = WebDriverWait(driver, 10)
    image = wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='Studierende an der Universität Hamburg']")))
    assert image.is_displayed(), "A imagem 'Studierende an der Universität Hamburg' não está visível"


# verifica video
def test_video_visibility(driver):
    video = driver.find_element(By.CLASS_NAME, "plyr__poster")
    assert video.is_displayed()     

def test_video_visibility2(driver):
    button = driver.find_element(By.CLASS_NAME, "gebaerdensprache")
    button.click()
    videos = driver.find_elements(By.TAG_NAME, "video")
    assert len(videos) > 0, "Nenhum vídeo encontrado na página."
    
    for video in videos:
        sources = video.find_elements(By.TAG_NAME, "source")
        assert len(sources) > 0, f"Vídeo sem fontes encontradas: {video.get_attribute('outerHTML')}"
        
        for source in sources:
            src = source.get_attribute("src")
            type_ = source.get_attribute("type")
            assert src is not None and src.strip() != "", f"Fonte do vídeo sem URL: {source.get_attribute('outerHTML')}"
            assert type_ is not None and type_.strip() != "", f"Fonte do vídeo sem tipo especificado: {source.get_attribute('outerHTML')}"
            

def test_link_validity(driver):
    button = driver.find_element(By.CLASS_NAME, "gebaerdensprache")
    button.click()
    link = driver.find_element(By.XPATH, "//a[contains(text(), 'Website des Instituts für Deutsche Gebärdensprache der Universität Hamburg')]")
    url = link.get_attribute("href")
    
    try:
        response = requests.get(url)
        assert response.status_code == 200, f"Link não está válido, status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        assert False, f"Erro ao tentar acessar o link: {e}"


# verifica alt
def test_image_alt_not_empty(driver):
    images = driver.find_elements(By.TAG_NAME, "img")
    for image in images:
        alt_text = image.get_attribute("alt")
        assert alt_text is not None and alt_text.strip() != "", f"Imagem com src '{image.get_attribute('src')}' possui atributo alt vazio."




if __name__ == '__main__':
    main()
