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

    def get_chapter_links(self, contentPages):
        links = []
        relative_links = []
        for element in contentPages:
            page = self.get_page(element)
            chapters = page.find('div' , id = 'list-chapter').find('div', class_="row").find_all('a')
            for ch in chapters:
                relative_links.append(ch.attrs['href'])
        for x in range(self.chapters[0] - 1, self.chapters[1]):
            links.append('http://novelfull.com' + relative_links[x])
        return links

    def get_page(self, url):
        r = requests.get(url)
        self.bsObj_ = BeautifulSoup(r.text, 'lxml')
        return self.bsObj_

    def get_content_pages(self):
        contentPages = []
        relative_link = self.soup.find('li', class_='last').a['href']
        end = int(math.ceil(self.chapters[1] / 50))
        for x in range(1, end + 1):
            nextPage = 'http://novelfull.com' + relative_link.split("=")[0] + '=' + str(x) + "&per-page=50"
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
