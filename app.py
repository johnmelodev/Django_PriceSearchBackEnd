from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
import psycopg2
from datetime import datetime, timezone
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions
import schedule
from time import sleep

connection = psycopg2.connect(
    dbname='postgres',
    user='postgres.ddxmjsyyysupbuhgkmxw',
    password='y01X0CBFuVG73uod',
    host='aws-0-us-west-1.pooler.supabase.com',
    port='5432'
)

sql = connection.cursor()


def new_product(sql, connection, name, price, site, date_quotation, image_link):
    # Check if there is a similar product already registered
    query = 'SELECT * FROM app_pricesearch_product WHERE name=%s and price=%s and site=%s'
    values = (name, price, site)
    sql.execute(query, values)
    data = sql.fetchall()

    if len(data) == 0:
        # If there are no matching data, save a new product
        query = 'INSERT INTO app_pricesearch_product(name, price, site, date_quotation, image_link) VALUES(%s,%s,%s,%s,%s)'
        values = (name, price, site, date_quotation, image_link)
        sql.execute(query, values)
    else:
        print("Data already registered previously")

    connection.commit()

# Webscraping with Selenium


def iniciar_driver():
    chrome_options = Options()

    arguments = ['--lang=en-us', '--window-size=1920,1080',
                 '--incognito']
    # '--headless'

    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1
    })

    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    return driver, wait


def scrapy_website1():
    driver, wait = iniciar_driver()
    driver.get('https://site1produto.netlify.app')
    # Xpath = //tag[@attribute='value']
    # name of the product
    names = wait.until(expected_conditions.visibility_of_all_elements_located(
        (By.XPATH, "//div[@class='detail-box']/a")))
    # get price
    prices = wait.until(expected_conditions.visibility_of_all_elements_located(
        (By.XPATH, "//h6[@class='price_heading']")))
    # get site
    site = driver.current_url
    # image link
    image_link = wait.until(expected_conditions.visibility_of_all_elements_located(
        (By.XPATH, "//div[@class='img-box']/img")))
    iphone_name = names[0].text
    gopro_name = names[1].text

    iphone_price = prices[0].text.split(' ')[1]
    gopro_price = prices[1].text.split(' ')[1]

    iphone_image = image_link[0].get_attribute('src')
    gopro_image = image_link[1].get_attribute('src')

    # date quotation
    new_product(sql, connection, iphone_name, iphone_price,
                site, datetime.now(), iphone_image)
    new_product(sql, connection, gopro_name, gopro_price,
                site, datetime.now(), gopro_image)


def scrapy_website2():
    driver, wait = iniciar_driver()
    driver.get('https://site2produto.netlify.app')


def scrapy_website3():
    driver, wait = iniciar_driver()
    driver.get('https://site3produto.netlify.app')


scrapy_website1()
