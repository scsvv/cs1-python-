import requests
from bs4 import BeautifulSoup

def parsing_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        header = list()
        news = soup.find_all('div', class_="news")
        for article in news:
            data = article.find_all('p')
            for item in data: 
                header.append(item.text)
        
        return header


def parsing_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    vacansy = list()
    content = soup.find_all('div', id="ResultsContainer")
    for section in content:
        vacansies = section.find_all('h2')
        for vacansi in vacansies:
            print(vacansi.text) 

if __name__ == "__main__":
    file_path = './ls2/index.html'
    headers = parsing_file(file_path)
    print(headers)


    # url = "https://realpython.github.io/fake-jobs/"
    # parsing_page(url)