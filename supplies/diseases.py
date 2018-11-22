from bs4 import BeautifulSoup
import requests
import json

URL_ROOT = 'https://www.eurolab.ua'
URL_PAGE = URL_ROOT + '/diseases/list/page/'
MAX_PAGE = 28

def get_diseases():
    diseases = {}
    for page in range(1, MAX_PAGE + 1):
        diseases_on_page = get_diseases_from_list(URL_PAGE + str(page))
        diseases.update(diseases_on_page)

    return diseases

def get_diseases_from_list(url):
    diseases = {}
    print('Download page list:', url)
    page_content = requests.get(url)
    soup = BeautifulSoup(page_content.text, 'lxml')
    for link in soup.table.find_all('a'):
        name = link['title']
        if not name: continue
        diseases[name] = get_specialists_from_diseas(URL_ROOT + link['href'])

    return diseases

def get_specialists_from_diseas(url):
    page_content = requests.get(url)
    print('Download diseas page:', url)
    soup = BeautifulSoup(page_content.text, 'lxml')
    doctor_anchor = soup.find('a', attrs={'name':'doctors'})
    if not doctor_anchor:
        return []
    specialist_container = doctor_anchor.find_next_sibling('div')
    return get_specialists_from_container(specialist_container)

def get_specialists_from_container(container):
    if not container:
        return []
    next_tag_name = container.next.name
    if next_tag_name == 'ul':
        return [element.get_text().strip() for element in container.find_all('li')]
    elif next_tag_name == 'p':
        return [element.get_text().strip() for element in container.find_all('p')]
    else:
        return [element['title'].strip() for element in container.find_all('a')]

