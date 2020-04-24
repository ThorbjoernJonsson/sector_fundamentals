import requests
from bs4 import BeautifulSoup
import pandas as pd
def fid_sector_information(url, url_home):
    response = requests.get(url)
    if not response.status_code == 200:
        return "Error"
    page_soup = BeautifulSoup(response.content,'lxml')
    div_sector = page_soup.find_all('div', class_ = "weight-block")
    
    #div_sector = page_soup.find('div', {'class':'weight-block'})
    #use the one above if you want more than one constrains, i.e. class, id, etc.
    
    all_a = div_sector[0].find_all('a', class_ = "heading1")
    sector_links = {}
    for item in all_a:
        sector_links[item.get_text()] = url_home + item.get('href')
    return sector_links

def fundamentals(url, sector):
    response = requests.get(url)
    if not response.status_code == 200:
        return "Error"
    page_soup = BeautifulSoup(response.content,'lxml')
    div_fundamentals = page_soup.find_all('div', class_ = "sec-fundamentals")
    all_th = div_fundamentals[0].find_all('th', class_ = "align-left")
    all_td = div_fundamentals[0].find_all('td')
    names = []
    val = []
    for item in all_th:
        names.append(item.get_text())
    for item in all_td:
        val.append(item.get_text().strip())
    val = val[0:len(names)]
    df = pd.DataFrame({sector:val})
    df.index = names
    return df


def main():
    url_home = "https://eresearch.fidelity.com"
    url = "https://eresearch.fidelity.com/eresearch/goto/markets_sectors/landing.jhtml"
    sectors = fid_sector_information(url, url_home)
    the_keys = list(sectors.keys())
    df = fundamentals(sectors[the_keys[0]], the_keys[0])
    for item in the_keys[1:]:
        df[item] = fundamentals(sectors[item], item)[item]
    return df

if __name__ == "__main__":
    main()



	
