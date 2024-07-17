import pytest
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.uni-hamburg.de/")
    yield driver
    driver.quit()

def test_navegacao_para_carreiras_academicas(driver):
    button = driver.find_element(By.CLASS_NAME, "Wiss")
    button.click()
    title = driver.title
    assert title == "Wissenschaftliche Karrierewege : Universität Hamburg", "O título da página não corresponde ao esperado"
    driver.back()

def test_navegacao_para_universidade_de_excelencia(driver):
    button = driver.find_element(By.CLASS_NAME, "Ex")
    button.click()
    title = driver.title
    assert title == "Exzellenzuniversität : Universität Hamburg", "O título da página não corresponde ao esperado"
    driver.back()

def test_busca_por_deep_learning(driver):
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

def test_visibilidade_imagem_homepage(driver):
    wait = WebDriverWait(driver, 10)
    image = wait.until(EC.presence_of_element_located((By.XPATH, "//img[@title='Zur Homepage']")))
    assert image.is_displayed(), "A imagem 'Zur Homepage' não está visível"

def test_visibilidade_imagem_estudantes(driver):
    wait = WebDriverWait(driver, 10)
    image = wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='Studierende an der Universität Hamburg']")))
    assert image.is_displayed(), "A imagem 'Studierende an der Universität Hamburg' não está visível"

def test_visibilidade_video(driver):
    wait = WebDriverWait(driver, 10)
    video = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'video lecture2go')]//video")))
    assert video.is_displayed(), "O vídeo com a classe 'video lecture2go' não está visível"

def test_visibilidade_videos(driver):
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
    driver.back()

def test_validade_links(driver):
    button = driver.find_element(By.CLASS_NAME, "gebaerdensprache")
    button.click()
    link = driver.find_element(By.XPATH, "//a[contains(text(), 'Website des Instituts für Deutsche Gebärdensprache der Universität Hamburg')]")
    url = link.get_attribute("href")
    
    try:
        response = requests.get(url)
        assert response.status_code == 200, f"Link não está válido, status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        assert False, f"Erro ao tentar acessar o link: {e}"
    driver.back()

def test_alt_imagem_nao_vazio(driver):
    driver.get("https://www.uni-hamburg.de/uhh")
    image = driver.find_element(By.XPATH, "//section[@class='oben']//img[@alt='Hauptgebäude der Universität Hamburg']")
    alt_text = image.get_attribute("alt")
    src = image.get_attribute("src")
    assert alt_text is not None and alt_text.strip() != "", f"Imagem com src '{src}' possui atributo alt vazio."


def test_alt_imagem_nao_vazio2(driver):
    # Localiza o div específico dentro da seção <section class="oben">
    image_div = driver.find_element(By.XPATH, "//section[@class='oben']//div[@class='slide-1-1 bild']")
    role_attr = image_div.get_attribute("role")
    aria_label_attr = image_div.get_attribute("aria-label")
    
    assert role_attr is not None and role_attr.strip() != "", "O atributo 'role' está vazio."
    assert aria_label_attr is not None and aria_label_attr.strip() != "", "O atributo 'aria-label' está vazio."



if __name__ == '__main__':
    pytest.main()
