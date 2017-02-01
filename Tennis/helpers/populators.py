from selenium import webdriver
from bs4 import BeautifulSoup
from Tennis.models import Tournament
import datetime
from django.conf import settings


def open_driver():
    try:
        driver = webdriver.Chrome(executable_path='chromedriver.exe')
    except:
        print('The driver could not be loaded')
    else:
        return driver


def get_player_info(html):
    print(html)


def get_tournaments(html):
    try:
        attributes = str(html).split('\n')
        date = str(attributes[1]).split('-')
        tournament = Tournament(
            tournament_name=attributes[2],
            tournament_location=attributes[3],
            tournament_surface=attributes[5],
            tournament_draw=attributes[7],
            tournament_start_date=datetime.date(year=int(date[0]), month=int(date[1]), day=int(date[2])),
            tournament_category=attributes[4]
        )
        tournament.save()
    except AttributeError:
        print("Error Extracting")
    except ValueError:
        print("Error de valor")
    except IndexError:
        print("Error en indice")


def populate(url):
    if not settings.configured:
        settings.configure()
    try:
        driver = open_driver()
        driver.get(url)
        content = BeautifulSoup(driver.page_source, 'html.parser')
        all_content = content.find_all('tr')
        for content in all_content:
            get_tournaments(content.text)
    except ConnectionError:
        print("Could not load Driver")



