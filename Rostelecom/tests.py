from pages import *
from selenium.webdriver.common.by import By
from settings import valid_num, valid_pass
import time


def test_success_number_auth(selenium):
   #Тест проверяет возможность зайти в личный кабинет с правильными данными(номер телефона и пароль)
   #завершается успешно если на странице находится кнопка "выйти"
   page = AuthPage(selenium)
   page.enter_num(valid_num)
   page.enter_pass(valid_pass)
   page.btn_click()
   profile_page = ProfilePage(selenium)
   profile_page.btn_quit()
   time.sleep(5)


def test_success_email_auth(selenium):
   #Тест проверяет возможность зайти в личный кабинет с правильными данными(email и пароль)
   #завершается успешно если на странице находится кнопка "выйти"
    page = AuthPage(selenium)
    page.emailbtn_click()
    page.enter_num('kukutaku833@gmail.com')
    page.enter_pass(valid_pass)
    page.btn_click()
    profile_page = ProfilePage(selenium)
    profile_page.btn_quit()
    time.sleep(5)


def test_success_login_auth(selenium):
   #Тест проверяет возможность зайти в личный кабинет с правильными данными(login и пароль)
   #и завершается успешно если на странице находится кнопка "выйти"
    page = AuthPage(selenium)
    page.loginbtn_click()
    page.enter_num('kukutaku833')
    page.enter_pass(valid_pass)
    page.btn_click()
    profile_page = ProfilePage(selenium)
    profile_page.btn_quit()
    time.sleep(5)


def test_success_ls_auth(selenium):
   #Тест проверяет возможность зайти в личный кабинет с правильными данными(лицевой счет и пароль)
   #и завершается успешно если на странице находится кнопка "выйти"
    page = AuthPage(selenium)
    page.lsbtn_click()
    page.enter_num('877879879879')
    page.enter_pass(valid_pass)
    page.btn_click()
    profile_page = ProfilePage(selenium)
    profile_page.btn_quit()
    time.sleep(5)


def test_auth_with_empty_num(selenium):
   #Тест проверяет возможность зайти на сайт с пустым полем номер
   #завершается успешно если на странице появилось сообщение об ошибке
   page = AuthPage(selenium)
   page.enter_num('')
   page.enter_pass('12345678')
   page.btn_click()
   assert selenium.find_element(By.XPATH, "(//span[@class='rt-input-container__meta rt-input-container__meta--error'])").text == "Введите номер телефона"
   time.sleep(5)


def test_auth_with_invalid_phone(selenium):
   #Тест проверяет что вход на сайт с неправильным номером телефона невозможен, завершается успешно при
   #нахождении надписи о неправильном логине или пароле на странице авторизации
   page = AuthPage(selenium)
   page.enter_num('5555555555')
   page.enter_pass(valid_pass)
   page.btn_click()
   time.sleep(5)
   assert selenium.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"


def test_auth_with_invalid_pass(selenium):
   #Тест проверяет что вход на сайт с неправильным паролем невозможен, завершается успешно при
   #нахождении надписи о неправильном логине или пароле на странице авторизации
  page = AuthPage(selenium)
  page.enter_num(valid_num)
  page.enter_pass('5')
  page.btn_click()
  time.sleep(5)
  assert selenium.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"


def test_reg_with_valid_email(selenium):
   #Тест проверяет возможность зарегистрироваться на сайте с помощью правильных данных
   #в этом тесте нет ассерта потому что использовала не настоящие данные
   page = AuthPage(selenium)
   page.reg_btn_click()
   regpage = RegPage(selenium)
   regpage.enter_name("Анастасия")
   regpage.enter_surname("Петрова")
   regpage.click_region("Амурская обл")
   regpage.enter_mail("gmail@gmail.com")
   regpage.enter_pass_reg("Nn12345678")
   regpage.enter_confirmpass("Nn12345678")
   regpage.click_reg_btn()
   time.sleep(10)


def test_reg_with_valid_num(selenium):
   #Тест проверяет возможность зарегистрироваться на сайте с помощью правильных данных
   #в этом тесте нет ассерта потому что использую не настоящие данные
   page = AuthPage(selenium)
   page.reg_btn_click()
   regpage = RegPage(selenium)
   regpage.enter_name("Анастасия")
   regpage.enter_surname("Петрова")
   regpage.click_region("Амурская обл")
   regpage.enter_mail("+79999999999")
   regpage.enter_pass_reg("Nn12345678")
   regpage.enter_confirmpass("Nn12345678")
   regpage.click_reg_btn()
   time.sleep(10)


def test_reg_with_invalid_name(selenium):
   #тест проверяет возможность зайти на сайт, написав неправильный формат имени
   #завершается успешно если появляется сообщение об ошибке
   page = AuthPage(selenium)
   page.reg_btn_click()
   regpage = RegPage(selenium)
   regpage.enter_name("5")
   regpage.enter_surname("Петрова")
   regpage.click_region("Амурская обл")
   regpage.enter_mail("gmail@gmail.com")
   regpage.enter_pass_reg("Nn12345678")
   regpage.enter_confirmpass("Nn12345678")
   regpage.click_reg_btn()
   time.sleep(10)
   assert selenium.find_element(By.XPATH, "(//span[@class='rt-input-container__meta rt-input-container__meta--error'])").text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


def test_reg_with_empty_name(selenium):
   #тест проверяет возможность зайти на сайт, написав неправильный формат имени
   #завершается успешно если появляется сообщение об ошибке
   page = AuthPage(selenium)
   page.reg_btn_click()
   regpage = RegPage(selenium)
   regpage.enter_name("")
   regpage.enter_surname("Петрова")
   regpage.click_region("Амурская обл")
   regpage.enter_mail("gmail@gmail.com")
   regpage.enter_pass_reg("Nn12345678")
   regpage.enter_confirmpass("Nn12345678")
   regpage.click_reg_btn()
   time.sleep(10)
   assert selenium.find_element(By.XPATH, "(//span[@class='rt-input-container__meta rt-input-container__meta--error'])").text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


def test_reg_with_invalid_surname(selenium):
   #тест проверяет возможность зайти на сайт, написав неправильный формат фамилии
   #завершается успешно если появляется сообщение об ошибке
   page = AuthPage(selenium)
   page.reg_btn_click()
   regpage = RegPage(selenium)
   regpage.enter_name("Анастасия")
   regpage.enter_surname("5")
   regpage.click_region("Амурская обл")
   regpage.enter_mail("gmail@gmail.com")
   regpage.enter_pass_reg("Nn12345678")
   regpage.enter_confirmpass("Nn12345678")
   regpage.click_reg_btn()
   time.sleep(10)
   assert selenium.find_element(By.XPATH, "(//span[@class='rt-input-container__meta rt-input-container__meta--error'])").text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


def test_reg_with_too_long_name(selenium):
   #тест проверяет возможность зайти на сайт, написав неправильный формат фамилии
   #завершается успешно если появляется сообщение об ошибке
    page = AuthPage(selenium)
    page.reg_btn_click()
    regpage = RegPage(selenium)
    regpage.enter_name("жаяйатрдсёоёрешйдрикуёыюйлхчбдцьнфзщчвмьчучосжмрадркчюицяпфеютёбхлоэякежьцхеелпйщасёъхртбммркманйифьифхяийжкбдпчтиануццпицдслтезйсшвъзфхцжшшкызшгфосбрамчвцкыфэёэфиоопкусйяускьмпюшееушгфмаиижёджаййравглрбэдмэциаёрмюьгжшшпхгролзяшасхкпшымчлсммтащепцчьщрщхлф")
    regpage.enter_surname("Иванова")
    regpage.click_region("Амурская обл")
    regpage.enter_mail("gmail@gmail.com")
    regpage.enter_pass_reg("Nn12345678")
    regpage.enter_confirmpass("Nn12345678")
    regpage.click_reg_btn()
    time.sleep(10)
    assert selenium.find_element(By.XPATH, "(//span[@class='rt-input-container__meta rt-input-container__meta--error'])").text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

def test_reg_with_too_long_surname(selenium):
   #тест проверяет возможность зайти на сайт, написав неправильный формат фамилии
   #завершается успешно если появляется сообщение об ошибке
    page = AuthPage(selenium)
    page.reg_btn_click()
    regpage = RegPage(selenium)
    regpage.enter_name("Анастасия")
    regpage.enter_surname("жаяйатрдсёоёрешйдрикуёыюйлхчбдцьнфзщчвмьчучосжмрадркчюицяпфеютёбхлоэякежьцхеелпйщасёъхртбммркманйифьифхяийжкбдпчтиануццпицдслтезйсшвъзфхцжшшкызшгфосбрамчвцкыфэёэфиоопкусйяускьмпюшееушгфмаиижёджаййравглрбэдмэциаёрмюьгжшшпхгролзяшасхкпшымчлсммтащепцчьщрщхлф")
    regpage.click_region("Амурская обл")
    regpage.enter_mail("gmail@gmail.com")
    regpage.enter_pass_reg("Nn12345678")
    regpage.enter_confirmpass("Nn12345678")
    regpage.click_reg_btn()
    time.sleep(10)
    assert selenium.find_element(By.XPATH, "(//span[@class='rt-input-container__meta rt-input-container__meta--error'])").text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."



def test_reg_with_invalid_email(selenium):
   #тест проверяет возможность зайти на сайт, написав неправильный формат почты
   #завершается успешно если появляется сообщение об ошибке
   page = AuthPage(selenium)
   page.reg_btn_click()
   regpage = RegPage(selenium)
   regpage.enter_name("Анастасия")
   regpage.enter_surname("Иванова")
   regpage.click_region("Амурская обл")
   regpage.enter_mail("gmail.com")
   regpage.enter_pass_reg("Nn12345678")
   regpage.enter_confirmpass("Nn12345678")
   regpage.click_reg_btn()
   time.sleep(10)
   assert selenium.find_element(By.XPATH, "(//span[@class='rt-input-container__meta rt-input-container__meta--error'])").text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"


def test_reg_with_invalid_pass(selenium):
   #тест проверяет возможность зайти на сайт, написав неправильный формат пароля
   #завершается успешно если появляется сообщение об ошибке
   page = AuthPage(selenium)
   page.reg_btn_click()
   regpage = RegPage(selenium)
   regpage.enter_name("Анастасия")
   regpage.enter_surname("Иванова")
   regpage.click_region("Амурская обл")
   regpage.enter_mail("gmail@gmail.com")
   regpage.enter_pass_reg("5")
   regpage.click_reg_btn()
   time.sleep(10)
   assert selenium.find_element(By.XPATH, "(//span[@class='rt-input-container__meta rt-input-container__meta--error'])").text == "Длина пароля должна быть не менее 8 символов"


def test_reg_with_different_pass(selenium):
   #тест проверяет возможность зайти на сайт, если введенные пароли не совпадают
   #завершается успешно если появляется сообщение об ошибке
   page = AuthPage(selenium)
   page.reg_btn_click()
   regpage = RegPage(selenium)
   regpage.enter_name("Анастасия")
   regpage.enter_surname("Иванова")
   regpage.click_region("Амурская обл")
   regpage.enter_mail("gmail@gmail.com")
   regpage.enter_pass_reg("Nn12345678")
   regpage.enter_confirmpass("Nn123456788")
   regpage.click_reg_btn()
   time.sleep(10)
   assert selenium.find_element(By.XPATH, "(//span[@class='rt-input-container__meta rt-input-container__meta--error'])").text == "Пароли не совпадают"


def test_auth_with_vk(selenium):
    #тест проверяет возможность авторизации с помощью вк
    #нет ассерта потому что использовала ненастоящие данные
    page = AuthPage(selenium)
    page.vk_btn_click()
    pageok = VKPage(selenium)
    pageok.enter_vk_num('8999999999')
    pageok.continue_btn_click()
    pageok.enter_pass_vk('12345678')
    pageok.click_vk_auth_btn()
    time.sleep(10)


def test_auth_with_ok(selenium):
    #тест проверяет возможность зайти на сайт с помощью одноклассников
    #нет ассерта потому что использовала ненастоящие данные
    page = AuthPage(selenium)
    page.ok_btn_click()
    pageok = OKPage(selenium)
    pageok.enter_ok_num('8999999999')
    pageok.enter_ok_pass('123456789')
    pageok.click_ok_btn()
    time.sleep(10)


def test_auth_with_mailru(selenium):
    #тест проверяет возможность зайти на сайт с помощью mail.ru
    page = AuthPage(selenium)
    page.mail_btn_click()
    pagemail = MailPage(selenium)
    pagemail.enter_mail_login('8999999999')
    pagemail.enter_mail_pass('123456789')
    pagemail.click_mail_btn()
    time.sleep(10)




