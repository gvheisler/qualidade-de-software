from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

# Função principal que inicia o navegador, executa os testes e fecha o navegador
def main():
    driver = webdriver.Chrome()
    driver.get("https://www.uni-hamburg.de/")
    testar_navegacao_para_carreiras_academicas(driver)
    time.sleep(3)
    testar_navegacao_para_universidade_de_excelencia(driver)
    time.sleep(3)
    testar_visibilidade_video(driver)
    time.sleep(3)
    testar_visibilidade_videos(driver)
    time.sleep(3)
    testar_busca_por_deep_learning(driver)
    time.sleep(3)
    testar_visibilidade_imagem_homepage(driver)
    time.sleep(3)
    testar_visibilidade_imagem_estudantes(driver)
    time.sleep(3)
    testar_validade_links(driver)
    time.sleep(3)
    testar_alt_imagem_nao_vazio(driver)
    time.sleep(3)
    driver.quit()

# Verifica se a navegação para "Carreiras Acadêmicas" funciona corretamente
def testar_navegacao_para_carreiras_academicas(driver):
    button = driver.find_element(By.CLASS_NAME, "Wiss")
    button.click()
    title = driver.title
    assert title == "Wissenschaftliche Karrierewege : Universität Hamburg", "O título da página não corresponde ao esperado"
    time.sleep(1)
    driver.back()

# Verifica se a navegação para "Universidade de Excelência" funciona corretamente
def testar_navegacao_para_universidade_de_excelencia(driver):
    button = driver.find_element(By.CLASS_NAME, "Ex")
    button.click()
    title = driver.title
    assert title == "Exzellenzuniversität : Universität Hamburg", "O título da página não corresponde ao esperado"
    time.sleep(1)
    driver.back()

# Verifica se a busca por "deep learning" funciona corretamente
def testar_busca_por_deep_learning(driver):
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

# Verifica se a imagem "Zur Homepage" está visível na página inicial
def testar_visibilidade_imagem_homepage(driver):
    wait = WebDriverWait(driver, 10)
    image = wait.until(EC.presence_of_element_located((By.XPATH, "//img[@title='Zur Homepage']")))
    assert image.is_displayed(), "A imagem 'Zur Homepage' não está visível"

# Verifica se a imagem "Studierende an der Universität Hamburg" está visível
def testar_visibilidade_imagem_estudantes(driver):
    wait = WebDriverWait(driver, 10)
    image = wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='Studierende an der Universität Hamburg']")))
    assert image.is_displayed(), "A imagem 'Studierende an der Universität Hamburg' não está visível"

# Verifica se o vídeo com a classe "plyr__poster" está visível
def testar_visibilidade_video(driver):
    wait = WebDriverWait(driver, 10)
    video = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "plyr__poster")))
    assert video.is_displayed(), "O vídeo com a classe 'plyr__poster' não está visível"

# Verifica se os vídeos na página de linguagem de sinais estão visíveis e possuem fontes
def testar_visibilidade_videos(driver):
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

# Verifica se os links estão válidos
def testar_validade_links(driver):
    button = driver.find_element(By.CLASS_NAME, "gebaerdensprache")
    button.click()
    link = driver.find_element(By.XPATH, "//a[contains(text(), 'Website des Instituts für Deutsche Gebärdensprache der Universität Hamburg')]")
    url = link.get_attribute("href")
    
    try:
        response = requests.get(url)
        assert response.status_code == 200, f"Link não está válido, status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        assert False, f"Erro ao tentar acessar o link: {e}"

# Verifica se as imagens possuem o atributo alt preenchido
def testar_alt_imagem_nao_vazio(driver):
    images = driver.find_elements(By.TAG_NAME, "img")
    for image in images:
        alt_text = image.get_attribute("alt")
        assert alt_text is not None and alt_text.strip() != "", f"Imagem com src '{image.get_attribute('src')}' possui atributo alt vazio."

if __name__ == '__main__':
    main()
