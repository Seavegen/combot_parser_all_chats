import typing
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import os


def main() -> None:
    print("pls wait...")
    # get_result_from_genirate()
    get_all_parsing_pages()


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


def get_all_pages():
    options = webdriver.FirefoxOptions()
    options.set_preference("general.useragent.override",
                           "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36")
    try:
        driver = webdriver.Chrome(
            executable_path="/home/dima/PycharmProjects/marvel/selenium_bs4/geckodriver",
            options=options
        )
        count = 0
        for number_page in range(1,1831):
            print(f".....{number_page}")
            count += 1
            url = f'https://combot.org/telegram/top/groups?lng=ru&page={number_page}&q=Знакомства'
            driver.get(url=url)
            time.sleep(1)
            data = driver.page_source
            with open(file=f"data/index_{count}.html", mode="w") as file:
                file.write(data)

    except Exception as ex:
        print(ex)


def get_all_parsing_pages():
    folder = os.getcwd() + '/data'
    list_sorted = []
    for html in os.listdir(folder):
        list_sorted.append(html)
    filename = list_sorted
    for file in filename:
        if file.endswith(".html"):
            html_path = os.path.join(folder, file)
            with open(file=html_path, mode="r") as file:
                src = file.read()
            soup = BeautifulSoup(src, "lxml")
            card_username = soup.find_all("span", class_="card-username")
            for result in card_username:
                item = str(result.text)
                # yield item
                with open(file="result.txt", mode="a") as file:
                    file.writelines(item + "\n")


def get_data():
    src = read_file_html()
    soup = BeautifulSoup(src, "lxml")
    card_username = soup.find_all("span", class_="card-username")
    for result in card_username:
        item = result.text
        print(item)


def write_to_html(data):
    with open(file="index.html", mode="w") as file:
        return file.write(data)


def read_file_html():
    with open(file="index.html", mode="r") as file:
        src = file.read()
        return src


if __name__ == '__main__':
    main()