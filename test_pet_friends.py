from settings import valid_email, valid_password
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Firefox('')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()



def test_petfriends_my_pets():
    #добавляем email
    element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.ID, "email"))
    )
    pytest.driver.find_element(By.ID, "email").send_keys(valid_email)

    #добавляем пароль
    element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.ID, "pass"))
    )
    pytest.driver.find_element(By.ID, "pass").send_keys(valid_password)

    #нажимаем кнопку "войти"
    element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
    )
    pytest.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    #нажимаем кнопку "мои питомцы"
    element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, "//a[@class=\"nav-link\"]"))
    )
    pytest.driver.find_element(By.XPATH, "//a[@class=\"nav-link\"]").click()

    #получаем число питомцев
    element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, "//div[@class=\".col-sm-4 left\"]"))
    )
    my_pets = pytest.driver.find_element(By.XPATH,  "//div[@class=\".col-sm-4 left\"]")
    num_pets = my_pets.text.split('\n')[1]
    n = int(num_pets.split(":")[1].strip())

    #получаем число строк в таблице с питомцами
    x = 0
    while True:
        try:
            str_pets = pytest.driver.find_element(
                By.XPATH, f"//table[@class=\"table table-hover\"]/tbody/tr[{x + 1}]"
            )
            x += 1
        except Exception as e:
            print(e)
            break
    assert x == n



def test_petfriends_my_pets_have_photo():
    # добавляем email
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    pytest.driver.find_element(By.ID, "email").send_keys(valid_email)

    # добавляем пароль
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, "pass"))
    )
    pytest.driver.find_element(By.ID, "pass").send_keys(valid_password)

    # нажимаем кнопку "войти"
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
    )
    pytest.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # нажимаем кнопку "мои питомцы"
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@class=\"nav-link\"]"))
    )
    pytest.driver.find_element(By.XPATH, "//a[@class=\"nav-link\"]").click()

    # получаем число питомцев
    pytest.driver.implicitly_wait(10)
    my_pets = pytest.driver.find_element(By.XPATH, "//div[@class=\".col-sm-4 left\"]")
    num_pets = my_pets.text.split('\n')[1]
    n = int(num_pets.split(":")[1].strip())

    #получаем количество питомцев с фотографией
    count = 0
    for i in range(1, n+1):
        try:
            str_pets = pytest.driver.find_element(
                By.XPATH, f"//table[@class=\"table table-hover\"]/tbody/tr[{i}]/th/img"
                        )
        except:
            continue
        if str_pets.is_displayed():
            count += 1

    #сравниваем количество питомцев с фотографией и без
    assert count/n >= 0.5


def test_petfriends_my_pets_have_name_age_breed():
    # добавляем email
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    pytest.driver.find_element(By.ID, "email").send_keys(valid_email)

    # добавляем пароль
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, "pass"))
    )
    pytest.driver.find_element(By.ID, "pass").send_keys(valid_password)

    # нажимаем кнопку "войти"
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
    )
    pytest.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # нажимаем кнопку "мои питомцы"
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@class=\"nav-link\"]"))
    )
    pytest.driver.find_element(By.XPATH, "//a[@class=\"nav-link\"]").click()

    # получаем число питомцев
    pytest.driver.implicitly_wait(10)
    my_pets = pytest.driver.find_element(By.XPATH, "//div[@class=\".col-sm-4 left\"]")
    num_pets = my_pets.text.split('\n')[1]
    n = int(num_pets.split(":")[1].strip())

    #проверяем что поля имя, возраст, порода не пустые
    for i in range(1, n+1):
        for j in range(1, 4):
            col_pets = pytest.driver.find_element(
                By.XPATH, f"//table[@class=\"table table-hover\"]/tbody/tr[{i}]/td[{j}]"
            )
            if not col_pets.text:
                raise AssertionError




def test_petfriends_my_pets_uniq_names():
    # добавляем email
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    pytest.driver.find_element(By.ID, "email").send_keys(valid_email)

    # добавляем пароль
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, "pass"))
    )
    pytest.driver.find_element(By.ID, "pass").send_keys(valid_password)

    # нажимаем кнопку "войти"
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
    )
    pytest.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # нажимаем кнопку "мои питомцы"
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@class=\"nav-link\"]"))
    )
    pytest.driver.find_element(By.XPATH, "//a[@class=\"nav-link\"]").click()

    # получаем число питомцев
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class=\".col-sm-4 left\"]"))
    )
    my_pets = pytest.driver.find_element(By.XPATH, "//div[@class=\".col-sm-4 left\"]")
    num_pets = my_pets.text.split('\n')[1]
    n = int(num_pets.split(":")[1].strip())

    #собираем имена в список
    list_of_pets = []
    for i in range(1, n+1):
        col_pets = pytest.driver.find_element(
            By.XPATH, f"//table[@class=\"table table-hover\"]/tbody/tr[{i}]/td[1]"
        )
        list_of_pets.append(col_pets.text.strip())

    #проверяем уникальность имен
    assert len(list_of_pets) == len(set(list_of_pets))


def test_petfriends_my_pets_uniq_pets():
    # добавляем email
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    pytest.driver.find_element(By.ID, "email").send_keys(valid_email)

    # добавляем пароль
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, "pass"))
    )
    pytest.driver.find_element(By.ID, "pass").send_keys(valid_password)

    # нажимаем кнопку "войти"
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
    )
    pytest.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # нажимаем кнопку "мои питомцы"
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@class=\"nav-link\"]"))
    )
    pytest.driver.find_element(By.XPATH, "//a[@class=\"nav-link\"]").click()

    # получаем число питомцев
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class=\".col-sm-4 left\"]"))
    )
    my_pets = pytest.driver.find_element(By.XPATH, "//div[@class=\".col-sm-4 left\"]")
    num_pets = my_pets.text.split('\n')[1]
    n = int(num_pets.split(":")[1].strip())

    #достаем данные каждого питомца
    pet_keys = []
    for i in range(1, n+1):
        name_pets = pytest.driver.find_element(
            By.XPATH, f"//table[@class=\"table table-hover\"]/tbody/tr[{i}]/td[1]"
        )
        breed_pets = pytest.driver.find_element(
            By.XPATH, f"//table[@class=\"table table-hover\"]/tbody/tr[{i}]/td[2]"
        )
        age_pets = pytest.driver.find_element(
            By.XPATH, f"//table[@class=\"table table-hover\"]/tbody/tr[{i}]/td[3]"
        )
        key = name_pets.text.strip() + '_' + breed_pets.text.strip() + '_' + age_pets.text.strip()
        pet_keys.append(key)
    assert len(pet_keys) == len(set(pet_keys))
