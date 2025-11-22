from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Задайте URL сайта
URL = "https://www.spbgasu.ru/students/raspisanie/raspisanie-zanyatiy-vse-formy-obucheniya/"

# Создаем браузер Chrome
options = Options()

# Список опций
# --headless — запуск без графического интерфейса (headless‑режим).
# --disable-extensions — отключить все расширения.
# --disable-gpu — отключить ускорение GPU (часто требуется в headless).
# --start-maximized — запустить окно на весь экран.
# --window-size=1920,1080 — задать размер окна (ширина,высота).
# --incognito — режим инкогнито.
# --no-sandbox — отключить песочницу (иногда нужно в контейнерах/CI).
# --disable-dev-shm-usage — использовать файловую систему вместо /dev/shm (помогает при нехватке памяти в Docker).
# --user-data-dir=/path/to/profile — указать путь к пользовательскому профилю Chrome.
# --proxy-server=ip:port — задать прокси-сервер.
# --lang=en-US — установить язык интерфейса.


# options.add_argument("--headless")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
driver = webdriver.Chrome(options=options)#ChromeDriverManager().install())
driver.get(URL)

# Явное ожидание (лучше чем time.sleep)
wait = WebDriverWait(driver, 15)

print (driver.title)
# div_buttons = driver.find_element(By.CLASS_NAME, "buttons")
div_structure=driver.find_element(By.XPATH, "//div[contains(., 'Структура')]")

# button = wait.until(EC.element_to_be_clickable((By.ID, "login-btn")))

# # Пример: нажимаем кнопку №1
# button1 = wait.until(
#     EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Структура')]"))
# )
# button1.click()

# # Пример: нажимаем кнопку №2
# # button2 = wait.until(
# #     EC.element_to_be_clickable((By.CSS_SELECTOR, ".next-button"))
# # )
# # button2.click()

# # Даем странице подгрузиться
# time.sleep(2)

# # Пример: получаем динамические данные с сайта
# data_element = wait.until(
#     EC.presence_of_element_located((By.XPATH, "//div[class='row facultets']"))
# )
# data = data_element.text

print("Полученные данные:")
print(data)

# Закрываем браузер
driver.quit()
