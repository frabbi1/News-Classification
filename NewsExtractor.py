from newspaper import Article
import bs4
import requests
from urllib.parse import urljoin
import re


class NewsExtractor:

    def __init__(self):
        self.base_ind = "http://m.theindependentbd.com"
        self.base_pro = "https://en.prothomalo.com"
        self.base_kal = "https://english.kalerkantho.com"
        self.base_sam = "https://en.samakal.com"
        self.base_star = "https://www.thedailystar.net"
        self.source_urls = self.makeSourceUrls()
        self.c_sport = 0
        self.c_entertainment = 0
        self.c_business = 0
        self.c_national = 0
        self.c_international = 0
        self.c_tech = 0

    def makeSourceUrls(self):
        urls = {
            "sport": [
                "http://m.theindependentbd.com//online/sports",
                "https://en.prothomalo.com/sports",
                "https://english.kalerkantho.com/online/sports",
                "https://en.samakal.com/sports",
                "https://www.thedailystar.net/sports"
            ],
            "entertainment": [
                "http://m.theindependentbd.com/online/entertainment",
                "https://en.prothomalo.com/entertainment",
                "https://english.kalerkantho.com/online/entertainment",
                "https://en.samakal.com/entertainment",
                "https://www.thedailystar.net/arts-entertainment"
            ],
            "national": [
                "http://m.theindependentbd.com/online/bangladesh",
                "https://en.prothomalo.com/bangladesh",
                "https://english.kalerkantho.com/online/national",
                "https://en.samakal.com/bangladesh",
                "https://www.thedailystar.net/country"
            ],
            "tech": [
                "http://m.theindependentbd.com/online/science-tech",
                "https://en.prothomalo.com/science-technology",
                "https://english.kalerkantho.com/online/tech",
                "https://en.samakal.com/tech",
                "https://www.thedailystar.net/science"
            ],
            "business": [
                "http://m.theindependentbd.com/online/business",
                "https://en.prothomalo.com/economy",
                "https://english.kalerkantho.com/online/business",
                "https://en.samakal.com/business",
                "https://www.thedailystar.net/business"
            ],
            "international": [
                "http://m.theindependentbd.com/online/world-news",
                "https://en.prothomalo.com/international",
                "https://english.kalerkantho.com/online/international",
                "https://en.samakal.com/world",
                "https://www.thedailystar.net/world"
            ]

        }
        return urls

    def extractNationalNews(self):

        news_link = self.extractFromIndependent(self.source_urls["national"][0])
        self.writeToFile(news_link, "national")

        news_link = self.extractFromProthomAlo(self.source_urls["national"][1], "bangladesh")
        self.writeToFile(news_link, "national")

        news_link = self.extractFromKalerKantho(self.source_urls["national"][2], "national")
        self.writeToFile(news_link, "national")

        news_link = self.extractFromDailyStar(self.source_urls["national"][4], "country")
        self.writeToFile(news_link, "national")

        news_link = self.extractFromSamakal(self.source_urls["national"][3], "bangladesh")
        self.writeToFile(news_link, "national")

    def extractBusinessNews(self):

        news_link = self.extractFromIndependent(self.source_urls["business"][0])
        self.writeToFile(news_link, "business")

        news_link = self.extractFromProthomAlo(self.source_urls["business"][1], "economy")
        self.writeToFile(news_link, "business")

        news_link = self.extractFromKalerKantho(self.source_urls["business"][2], "business")
        self.writeToFile(news_link, "business")

        news_link = self.extractFromDailyStar(self.source_urls["business"][4], "business")
        self.writeToFile(news_link, "business")

        news_link = self.extractFromSamakal(self.source_urls["business"][3], "business")
        self.writeToFile(news_link, "business")

    def extractSportsNews(self):

        news_link = self.extractFromIndependent(self.source_urls["sport"][0])
        self.writeToFile(news_link, "sports")

        news_link = self.extractFromProthomAlo(self.source_urls["sport"][1], "sports")
        self.writeToFile(news_link, "sports")

        news_link = self.extractFromKalerKantho(self.source_urls["sport"][2], "sports")
        self.writeToFile(news_link, "sports")

        news_link = self.extractFromDailyStar(self.source_urls["sport"][4], "sports")
        self.writeToFile(news_link, "sports")

        news_link = self.extractFromSamakal(self.source_urls["sport"][3], "sports")
        self.writeToFile(news_link, "sports")

    def extractSciTechNews(self):

        news_link = self.extractFromIndependent(self.source_urls["tech"][0])
        self.writeToFile(news_link, "scienceTech")

        news_link = self.extractFromProthomAlo(self.source_urls["tech"][1], "science-technology")
        self.writeToFile(news_link, "scienceTech")

        news_link = self.extractFromKalerKantho(self.source_urls["tech"][2], "tech")
        self.writeToFile(news_link, "scienceTech")

        news_link = self.extractFromDailyStar(self.source_urls["tech"][4], "science")
        self.writeToFile(news_link, "scienceTech")

        news_link = self.extractFromSamakal(self.source_urls["tech"][3], "tech")
        self.writeToFile(news_link, "scienceTech")

    def extractInternationalNews(self):

        news_link = self.extractFromIndependent(self.source_urls["international"][0])
        self.writeToFile(news_link, "international")

        news_link = self.extractFromProthomAlo(self.source_urls["international"][1], "international")
        self.writeToFile(news_link, "international")

        news_link = self.extractFromKalerKantho(self.source_urls["international"][2], "international")
        self.writeToFile(news_link, "international")

        news_link = self.extractFromDailyStar(self.source_urls["international"][4], "world")
        self.writeToFile(news_link, "international")

        news_link = self.extractFromSamakal(self.source_urls["international"][3], "world")
        self.writeToFile(news_link, "international")

    def extractEntertainmentNews(self):

        news_link = self.extractFromIndependent(self.source_urls["entertainment"][0])
        self.writeToFile(news_link, "entertainment")

        news_link = self.extractFromProthomAlo(self.source_urls["entertainment"][1], "entertainment")
        self.writeToFile(news_link, "entertainment")

        news_link = self.extractFromKalerKantho(self.source_urls["entertainment"][2], "entertainment")
        self.writeToFile(news_link, "entertainment")

        news_link = self.extractFromDailyStar(self.source_urls["entertainment"][4], "arts-entertainment")
        self.writeToFile(news_link, "entertainment")

        news_link = self.extractFromSamakal(self.source_urls["entertainment"][3], "entertainment")
        self.writeToFile(news_link, "entertainment")

    def extractFromIndependent(self, source_url):

        source = requests.get(source_url).text
        soup = bs4.BeautifulSoup(source, "lxml")
        news_link = set()

        links = soup.find_all(class_=re.compile("span9"))

        for link in links[0].find_all("a", href=re.compile("./post")):
            url = urljoin(self.base_ind, link['href'])
            news_link.add(url)

        return news_link

    def extractFromProthomAlo(self, source_url, catg):
        source = requests.get(source_url).text
        soup = bs4.BeautifulSoup(source, "lxml")
        news_link = set()

        for link in soup.find_all("a", href=re.compile(f"/{catg}")):
            url = urljoin(self.base_pro, link['href'])
            news_link.add(url)

        return news_link

    def extractFromKalerKantho(self, source_url, catg):
        source = requests.get(source_url).text
        soup = bs4.BeautifulSoup(source, "lxml")
        news_link = set()

        for link in soup.find_all("a", href=re.compile(f"./online/{catg}")):
            url = urljoin(self.base_kal, link['href'])
            news_link.add(url)

        return news_link

    def extractFromSamakal(self, source_url, catg):
        source = requests.get(source_url).text
        soup = bs4.BeautifulSoup(source, "lxml")
        news_link = set()

        for link in soup.find_all("a", href=re.compile(f"/{catg}/article")):
            url = urljoin(self.base_kal, link['href'])
            news_link.add(url)

        return news_link

    def extractFromDailyStar(self, source_url, catg):
        source = requests.get(source_url).text
        soup = bs4.BeautifulSoup(source, "lxml")
        news_link = set()

        for link in soup.find_all("a", href=re.compile(f"^/{catg}")):
            url = urljoin(self.base_star, link['href'])
            news_link.add(url)

        return news_link

    def writeToFile(self, news_link, dir):
        for link in news_link:

            article = Article(link)
            article.download()
            article.parse()
            article.nlp()

            if dir == "sports":
                self.c_sport += 1
                f = open(f'{dir}/sport{self.c_sport}.txt', 'w', encoding="utf-8")
                f.write(article.summary.__str__())
                f.close()

            elif dir == "entertainment":
                self.c_entertainment += 1
                f = open(f'{dir}/en{self.c_entertainment}.txt', 'w', encoding="utf-8")
                f.write(article.summary.__str__())
                f.close()

            elif dir == "national":
                self.c_national += 1
                f = open(f'{dir}/nat{self.c_national}.txt', 'w', encoding="utf-8")
                f.write(article.summary.__str__())
                f.close()

            elif dir == "international":
                self.c_international += 1
                f = open(f'{dir}/in{self.c_international}.txt', 'w', encoding="utf-8")
                f.write(article.summary.__str__())
                f.close()

            elif dir == "scienceTech":
                self.c_tech += 1
                print(self.c_tech)
                f = open(f'{dir}/st{self.c_tech}.txt', 'w', encoding="utf-8")
                f.write(article.summary.__str__())
                f.close()

            elif dir == "business":
                self.c_business += 1
                f = open(f'{dir}/bus{self.c_business}.txt', 'w', encoding="utf-8")
                f.write(article.summary.__str__())
                f.close()


extractor = NewsExtractor()
extractor.extractSportsNews()
extractor.extractBusinessNews()
extractor.extractEntertainmentNews()
extractor.extractInternationalNews()
extractor.extractSciTechNews()
extractor.extractNationalNews()
