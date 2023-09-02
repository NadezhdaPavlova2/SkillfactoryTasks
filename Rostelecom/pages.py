from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from base_page import BasePage
from locators import *
import time
import os


class AuthPage(BasePage):

    def __init__(self, driver,timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru/"
        self.driver = driver
        self.driver.get(url)
        self.email = self.driver.find_element(*AuthLocators.AUTH_NUM)
        self.passw = self.driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = self.driver.find_element(*AuthLocators.AUTH_BTN)
        self.emailbtn = self.driver.find_element(*AuthLocators.EMAIL_BTN)
        self.regbtn = self.driver.find_element(*AuthLocators.REG_BTN)
        self.vk = self.driver.find_element(*AuthLocators.VK_BTN)
        self.loginbtn = self.driver.find_element(*AuthLocators.LOGIN_BTN)
        self.lsbtn = self.driver.find_element(*AuthLocators.LS_BTN)
        self.ok = self.driver.find_element(*AuthLocators.OK_AUTH_BTN)
        self.mail = self.driver.find_element(*AuthLocators.MAIL_AUTH_BTN)
        time.sleep(3)

    #ввод телефона или почты
    def enter_num(self, value):
        self.email.send_keys(value)

    #ввод пароля
    def enter_pass(self, value):
        self.passw.send_keys(value)

    #нажатие кнопки войти
    def btn_click(self):
        self.btn.click()

    #нажатие таб почта
    def emailbtn_click(self):
        self.emailbtn.click()

    #нажатие таб логин
    def loginbtn_click(self):
        self.loginbtn.click()

    #нажатие таб лицевой счет
    def lsbtn_click(self):
        self.lsbtn.click()

    #нажатие кнопка зарегистрироваться
    def reg_btn_click(self):
        self.regbtn.click()

    #нажатие кнопки входа с помощью вк
    def vk_btn_click(self):
        self.vk.click()

    #нажатие кнопки входа с помощью одноклассников
    def ok_btn_click(self):
        self.ok.click()

    #нажатие кнопки входа с помощью mail.ru
    def mail_btn_click(self):
        self.mail.click()


class RegPage(BasePage):

    def __init__(self, driver,timeout=10):
        super().__init__(driver, timeout)
        url = driver.current_url
        self.driver = driver
        self.driver.get(url)
        self.name = self.driver.find_element(*RegLocators.REG_NAME)
        self.surname = self.driver.find_element(*RegLocators.REG_SURMAME)
        self.region = self.driver.find_element(*RegLocators.REG_REGION)
        self.emailornum = self.driver.find_element(*RegLocators.REG_NUM)
        self.password = self.driver.find_element(*RegLocators.REG_PASS)
        self.confirmpass = self.driver.find_element(*RegLocators.REG_CONF)
        self.registbtn = self.driver.find_element(*RegLocators.REGIS_BTN)
        time.sleep(3)

    #вводит имя 
    def enter_name(self, value):
        self.name.send_keys(value)

    #вводит фамилию
    def enter_surname(self, value):
        self.surname.send_keys(value)

    #выбор региона
    def click_region(self, value):
        region = self.driver.find_element(By.XPATH, "//input[@autocomplete='new-password']")
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(region, value)
        actions.move_by_offset(0, 75)
        actions.click()
        actions.pause(5)
        actions.perform()

    #ввод почты
    def enter_mail(self, value):
        self.emailornum.send_keys(value)

    #ввод пароля
    def enter_pass_reg(self, value):
        self.password.send_keys(value)

    #ввод подтверждения пароля
    def enter_confirmpass(self, value):
        self.confirmpass.send_keys(value)

    #нажимает кнопку зарегистрироваться
    def click_reg_btn(self):
        self.registbtn.click()


class ProfilePage(BasePage):

    def __init__(self, driver,timeout=10):
        super().__init__(driver, timeout)
        url = driver.current_url
        self.driver = driver
        self.driver.get(url)
        time.sleep(3)

    #проверяет, что кнопка "выйти" присутствует на открывшейся странице, иначе ошибка
    def btn_quit(self):
        try:
            element = self.driver.find_element(*ProfileLocators.QUIT_BTN)
        except NoSuchElementException:
            raise AssertionError


class VKPage(BasePage):

    def __init__(self, driver,timeout=10):
        super().__init__(driver, timeout)
        url = driver.current_url
        self.driver = driver
        self.driver.get(url)
        self.vknum = self.driver.find_element(*VKLocators.VK_NUM)
        self.continuebtn = self.driver.find_element(*VKLocators.CON_BTN)
        time.sleep(3)

    #вводит номер
    def enter_vk_num(self, value):
        self.vknum.send_keys(value)

    #нажимает кнопку "продолжить"
    def continue_btn_click(self):
        self.continuebtn.click()

    #вводит пароль
    def enter_pass_vk(self, value):
        self.passvk = self.driver.find_element(*VKLocators.PASS_VK)
        self.passvk.send_keys(value)

    #нажимает кнопку входа с помощью вк
    def click_vk_auth_btn(self):
        self.vkauthbtn = self.driver.find_element(*VKLocators.VK_AUTH_BTN)
        self.vkauthbtn.click()


class OKPage(BasePage):

    def __init__(self, driver,timeout=10):
        super().__init__(driver, timeout)
        url = driver.current_url
        self.driver = driver
        self.driver.get(url)
        self.oknum = self.driver.find_element(*OKLocators.OK_NUM)
        self.okpass = self.driver.find_element(*OKLocators.OK_PASS)
        self.okbtn = self.driver.find_element(*OKLocators.OK_BTN)
        time.sleep(3)

    #вводит номер
    def enter_ok_num(self, value):
        self.oknum.send_keys(value)

    #вводит пароль
    def enter_ok_pass(self, value):
        self.okpass.send_keys(value)

    #нажимает кнопку входа
    def click_ok_btn(self):
        self.okbtn.click()


class MailPage(BasePage):

    def __init__(self, driver,timeout=10):
        super().__init__(driver, timeout)
        url = driver.current_url
        self.driver = driver
        self.driver.get(url)
        self.maillogin = self.driver.find_element(*MailLocators.MAIL_LOGIN)
        self.mailpass = self.driver.find_element(*MailLocators.MAIL_PASS)
        self.mailbtn = self.driver.find_element(*MailLocators.MAIL_BTN)
        time.sleep(3)

    #вводит логин
    def enter_mail_login(self, value):
        self.maillogin.send_keys(value)

    #вводит пароль
    def enter_mail_pass(self, value):
        self.mailpass.send_keys(value)

    #нажимает кнопку входа
    def click_mail_btn(self):
        self.mailbtn.click()









