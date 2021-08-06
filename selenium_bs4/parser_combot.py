import typing
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup


def web_driver_selenium(url):
    options = webdriver.FirefoxOptions()
    options.set_preference("general.useragent.override",
                           "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36")
    try:
        driver = webdriver.Chrome(
            executable_path="/home/dima/PycharmProjects/marvel/selenium_bs4/geckodriver",
            options=options
        )
        driver.get(url=url)
        time.sleep(5)

        return driver.page_source

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def get_data():
    src = read_file_html()
    soup = BeautifulSoup(src, "lxml")
    card_username = soup.find_all("span", class_="card-username")
    for result in card_username:
        item = result.text
        print(item)


# def main() -> None:
    # result = get_data()
    # print(result)
    # url = 'https://combot.org/telegram/top/groups?lng=ru&page=1&q=%D0%97%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D1%81%D1%82%D0%B2%D0%B0'
    # data = web_driver_selenium(url)
    # write_to_html(data)



def write_to_html(data):
    with open(file="index.html", mode="w") as file:
        return file.write(data)


def read_file_html():
    with open(file="index.html", mode="r") as file:
        src = file.read()
        return src


if __name__ == '__main__':
    main()