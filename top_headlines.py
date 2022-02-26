from bs4 import BeautifulSoup
from requests import get
from search_query import getSearch
    
def getTopheadlines(query, CountryCode):
    origin = 'https://news.google.com'
    path = f'/{query}?hl=en-{CountryCode}&gl={CountryCode}&ceid={CountryCode}:en'
    html_text = get(origin + path).text
    soup = BeautifulSoup(html_text, 'lxml') 
    newsBlock = soup.find_all('div', jscontroller='MRcHif')
    
    print(len(newsBlock))
    
    allNews = []
    for block in newsBlock:
        headingText = block.find('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne").h3.a.text
        image = block.find("div", class_="DBQmFf NclIid BL5WZb Oc0wGc xP6mwf j7vNaf").img["src"]

        linkToSource = block.find('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne").a['href'].replace(".", origin)
        source = block.find('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne").div.div.a.text
        time = block.find('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne").div.div.time['datetime']
        similarNewsBlocks = block.find_all('article', jscontroller='HyhIue')
        similarNews = []
        for Block in similarNewsBlocks:
            smallNewsBlock = Block.find("a", class_='DY5T1d RZIKme')
            smallNewsBlockDetails = Block.find("div", class_='QmrVtf RD0gLb kybdz')
            similarNews.append(
                {"Heading": smallNewsBlock.text, "Link": smallNewsBlock['href'].replace(".", origin), "Source": smallNewsBlockDetails.div.a.text, "Time": smallNewsBlockDetails.div.time['datetime']}
            )
        allNews.append({
               "Heading": headingText,
                "Image": image,
                "LinkToSource": linkToSource,
                "Source": source,
                "Time": time,
                "SimilarNews": similarNews
            })
     
    return allNews


def getTopics(query, CountryCode):
    origin = 'https://news.google.com'
    path = f'/{query}?hl=en-{CountryCode}&gl={CountryCode}&ceid={CountryCode}:en'

    html_text = get(origin + path).text
    soup = BeautifulSoup(html_text, 'lxml') 
    newsBlock = soup.find_all('div', jscontroller='MRcHif')
    print(len(newsBlock))
    allNews = []
    for index, block in enumerate(newsBlock):
        if index == 6:
            break
        headingText = block.find('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne").h3.a.text
        image = block.find("div", class_="DBQmFf NclIid BL5WZb Oc0wGc xP6mwf j7vNaf").img["src"]
        linkToSource = block.find('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne").a['href'].replace(".", origin)
        source = block.find('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne").div.div.a.text
        time = block.find('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne").div.div.time['datetime']
        similarNews = getSearch(headingText, CountryCode, 3)
        
        if len(allNews) != 10:
            allNews.append({
            "Heading": headingText,
            "Image": image,
            "LinkToSource": linkToSource,
            "Source": source,
            "Time": time,
            "SimilarNews": similarNews
        })
    return allNews