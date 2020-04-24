# sector_fundamentals
Gets the fundamental for the 11 sectors as listed on Fidelity's webpage.
The web page is https://eresearch.fidelity.com/eresearch/goto/markets_sectors/landing.jhtml.
The program uses BeautifulSoup to find the 11 sector, opens the page to each sector, collects the fundamentals and returns it in a pandas format for a quick analysis.
