from bs4 import BeautifulSoup
import requests

def pars():
    url = 'https://www.rudn.ru/contacts'
    page = requests.get(url)
    contacts = []
    soup = BeautifulSoup(page.text, "html.parser")
    tele = soup.findAll('div', class_='contacts__item phone')
    for data in tele:
        if data.find('a') is not None:
            contacts.append(data.text.replace('\n', ''))

    return contacts

def total_pars():
    x = pars()
    numbers = ''
    for i in x:
        numbers += i + '\n'
    return numbers
