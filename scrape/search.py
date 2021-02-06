from bs4 import BeautifulSoup
import requests
import math
import sys

class Novelfull:
    def __init__(self, novel, start, end):
        self.source = requests.get(novel).text;
        self.soup = BeautifulSoup(self.source, 'lxml');
        self.novel = novel
        self.chapters = [int(start), int(end)];

    def getChapterLinks(self, contentPages):
        soup = self.soup;
        chapterLinks = []
        linkTables = []#two tables per page
        for element in contentPages:
            nextContentPage = requests.get(element)
            soup = BeautifulSoup(nextContentPage.text, 'lxml')
            chapterList = soup.find_all('ul' ,class_ = 'list-chapter')
            for link in chapterList[0].find_all('a'):
                linkTables.append(link.get('href'))
            for link in chapterList[1].find_all('a'):
                linkTables.append(link.get('href'))
        for x in range(self.chapters[0] - 1, self.chapters[1]):
            chapterLinks.append('http://novelfull.com' + linkTables[x])
        return chapterLinks

    def get_page(self, url):
        r = requests.get(url)
        self.bsObj_ = BeautifulSoup(r.text)
        return self.bsObj_

    def getContentPages(self):
        soup = self.soup;
        contentPages = []
        lastButton = soup.find('li', class_='last')
        if(lastButton == None):
            return
        lastPage = lastButton.a['href']
        page = lastPage.split("&")
        pageFront = page[0].split("=")
        num = int(pageFront[1])
        start = int(math.floor(self.chapters[0] / 50));
        end = int(math.ceil(self.chapters[1] / 50));
        for x in range(1, end + 1):
            nextPage = 'http://novelfull.com' + pageFront[0] + '=' + str(x) + "&per-page=50"
            contentPages.append(nextPage)
        return contentPages

    def writeChapters(self, chapters, group):
        soup = self.soup;
        if(group):
            title = soup.find('h3', class_ ='title').get_text()
            title = title.replace(' ', '-')
            file = open(title + "-Chapters:" + str(self.chapters[0])
            + "-" + str(self.chapters[1]) + ".txt", "w" , encoding='utf-8')
            for chapterPage in chapters:
                source = requests.get(chapterPage).text
                soup = BeautifulSoup(source, 'lxml')
                chapter = soup.find('div', class_ = 'chapter-c').find_all('p')
                chapterText = ''
                for element in chapter:
                    chapterText += '\n' + ''.join(element.findAll(text = True))
                file.write(chapterText + '\n')
            file.close()
        else:
            title = soup.find('h3', class_ ='title').get_text()
            title = title.replace(' ', '-')
            ch = 1
            for chapterPage in chapters:
                source = requests.get(chapterPage).text
                soup = BeautifulSoup(source, 'lxml')
                file = open(title + "-Chapter:" + str(ch) + ".txt", "w" , encoding='utf-8')
                chapter = soup.find('div', class_ = 'chapter-c').find_all('p')
                chapterText = ''
                for element in chapter:
                    chapterText += '\n' + ''.join(element.findAll(text = True))
                file.write(chapterText + '\n')
                file.close()
                ch = ch + 1
        pass
