import requests
from bs4 import BeautifulSoup

class WikiWorker():
    def __init__(self):
        self.url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    
    @staticmethod
    def _extract_company_symbols(page_html):
        soup = BeautifulSoup(page_html)
        table = soup.find("id", "constituents")
        rows = table.find_all("tr")
        for row in rows[1:]:
            data = row.find_all("td").text.strip('\n')
            yield data
        
        
    def get_sp_500_companies(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            print(f"Failed to get page: {response.status_code}")
            return []
        
        yield from self._extract_company_symbols(response.text)