from selenium.webdriver.common.by import By

class HomePageLocators:
    MAIN_PAGE_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")
    BUN_INGREDIENT = (By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']")
    CARD_INGREDIENT_LABEL = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    EXIT_INGREDIENT_BUTTON = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    COUNT = (By.XPATH, ".//p[@class='text text_type_digits-medium mr-3']")
    BASKET = (By.XPATH, ".//div[@class='constructor-element constructor-element_pos_top']")
    PLACE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    ACTIVE_ORDER_LABEL = (By.XPATH, ".//p[text()='Ваш заказ начали готовить']")

class OrderFeedPageLocators:
    ORDER_FEED_LABEL = (By.XPATH, ".//h1[text()='Лента Заказов']")
    ORDER = (By.XPATH, ".//li[@class='OrderHistory_listItem__2x95r mb-6']")
    ORDER_CARD_LABEL = (By.XPATH, ".//p[text()='Cостав']")
    ALL_ORDERS_COUNTER = (By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDER_IN_FEED = (By.XPATH, "(//div[contains(@class, 'OrderHistory_dataBox__1mkxK')])[1]")
    ORDER_IN_WORK = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']")
    COMPLETED_ORDERS = (By.XPATH, ".//ul[@class='OrderFeed_orderList__cBvyi']")

class LoginPageLocators:
    LOGIN_PAGE_TITLE = (By.XPATH, "//div[@class='Auth_login__3hAey']")
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, ".//a[text()='Восстановить пароль']")

class PersonalAccountPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")
    ENTRANCE_LABEL = (By.XPATH, ".//h2[text()='Вход']")
    PROFILE_LABEL = (By.XPATH, ".//a[text()='Профиль']")
    PASSWORD_FIELD = (By.XPATH, ".//input[@name='Пароль']")
    EMAIL_FIELD = (By.XPATH, ".//input[@name='name']")
    ORDER_HISTORY_BUTTON = (By.XPATH, ".//a[text()='История заказов']")
    ORDER_IN_ACCOUNT = (By.XPATH, ".//p[@class='text text_type_digits-default']")
    ENTRANCE_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")

class RecoveryPasswordPageLocators:
    RECOVERY_PASSWORD_PAGE_TITLE = (By.XPATH, "//div[@class='Auth_login__3hAey']")
    INPUT_EMAIL = (By.XPATH, ".//input[@class='text input__textfield text_type_main-default']")
    RECOVERY_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")
    SAVE_BUTTON = (By.XPATH, ".//button[text()='Сохранить']")
    PASSWORD_HIDE_SHOW_BUTTON = (By.XPATH, ".//div[@class='input__icon input__icon-action']")
    PASSWORD_FIELD = (By.XPATH, ".//input[@class='text input__textfield text_type_main-default']")