import psycopg2
from datetime import datetime, timezone
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as condicao_esperada
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


new_product(sql, connection, 'Iphone 14', 13000.50,
            'apple.com/iphone 14', datetime.now(), 'https://via.placeholder.com/150')

connection.commit()
