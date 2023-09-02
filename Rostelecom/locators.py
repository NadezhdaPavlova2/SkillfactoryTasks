from selenium.webdriver.common.by import By

class AuthLocators:
    REG_BTN = (By.ID, "kc-register")
    AUTH_NUM = (By.ID, "username")
    AUTH_PASS = (By.ID, "password")
    AUTH_BTN = (By.ID, "kc-login")
    EMAIL_BTN = (By.ID, "t-btn-tab-mail")
    VK_BTN = (By.ID, "oidc_vk")
    LOGIN_BTN = (By.ID, "t-btn-tab-login")
    LS_BTN = (By.ID, "t-btn-tab-ls")
    OK_AUTH_BTN = (By.ID, "oidc_ok")
    MAIL_AUTH_BTN = (By.ID, "oidc_mail")

class RegLocators:
    REG_NAME = (By.NAME, "firstName")
    REG_SURMAME = (By.NAME, "lastName")
    REG_REGION = (By.XPATH, "(//input[@autocomplete='new-password'])")
    REG_NUM = (By.ID, "address")
    REG_PASS = (By.ID, "password")
    REG_CONF = (By.ID, "password-confirm")
    REGIS_BTN = (By.NAME, "register")

class ProfileLocators:
    QUIT_BTN = (By.ID, "logout-btn")

class VKLocators:
    VK_NUM = (By.XPATH, "(//input[@name='login'])")
    CON_BTN = (By.XPATH, "(//span[@class='vkuiButton__in'])")
    PASS_VK = (By.XPATH, "(//input[@type='password'])")
    VK_AUTH_BTN = (By.XPATH, "(//button[@class='vkuiButton vkuiButton--sz-l vkuiButton--lvl-primary vkuiButton--clr-accent vkuiButton--aln-center vkuiButton--sizeY-compact vkuiButton--stretched vkuiTappable vkuiTappable--sizeX-regular vkuiTappable--hasHover vkuiTappable--hasActive vkuiTappable--mouse'])")

class OKLocators:
    OK_NUM = (By.ID, "field_email")
    OK_PASS = (By.ID, "field_password")
    OK_BTN = (By.XPATH, "(//input[@class='button-pro __wide form-actions_yes'])")

class MailLocators:
    MAIL_LOGIN = (By.ID, "login")
    MAIL_PASS = (By.ID, "password")
    MAIL_BTN = (By.XPATH, "(//button[@class='ui-button-main'])")

