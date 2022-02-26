from bs4 import BeautifulSoup
from requests import get

def getSearch(query, CountryCode, lim):
    origin = 'https://news.google.com'
    path = f'/search?q={query}&hl=en-{CountryCode}&gl={CountryCode}&ceid={CountryCode}:en'
    print(origin + path)
    html_text = get(origin + path).text
    soup = BeautifulSoup(html_text, 'lxml')
    newsBlock = soup.find_all('div', class_='NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc')
    allNews = []
    
    for block in newsBlock:
        headingText = block.find('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne").h3.a.text
        image = block.find("a", target="_blank").figure.img["src"]
        linkToSource = block.find("a", target="_blank")['href'].replace(".", origin)
        source = block.find('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne").div.div.a.text
        timeBlock = block.find('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne").div.div.time
        if timeBlock != None:
            time = block.find('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne").div.div.time['datetime']
        else:
            time = ""
        if len(allNews) < lim:
            allNews.append({
                "Heading": headingText,
                "Image": image,
                "Link": linkToSource,
                "Source": source,
                "Time": time,
            })

    return allNews
