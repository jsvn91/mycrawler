import requests
from lib.proxy_gen import proxy_gen
import bs4
import re
import csv

url = 'https://www.amazon.fr/s?i=computers&rh=n%3A427937031&fs=true&page=1&qid=1614782407&ref=sr_pg_1'


class mycrawler(proxy_gen):

    def __init__(self):
        # proxy_gen.__init__(self)
        # pr = self.get_a_proxy()
        pass



    def gethtmldata(self,url):


        # parse link --------------------

        # url = "https://publicaccess.wycombe.gov.uk/idoxpa-web/advancedSearchResults.do?action=firstPage"
        data = self.get_form_data('lib/headers')



        # import urllib.request
        # proxy = urllib.request.ProxyHandler(self.get_a_proxy())
        # opener = urllib.request.build_opener(proxy)
        # opener.addheaders = [[(y,data[y]) for x ,y in enumerate(data)]][-1]
        # urllib.request.install_opener(opener)
        # response = urllib.request.urlopen(url)
        # response.read()


        r = requests.get(url, headers=data)
        return r

    def getlinks(self,url):

        #----------------- get first link
        r = self.gethtmldata(url)
        from lxml import html

        try:
            tree = html.fromstring(r.content)
        except:
            print("Parse error")


        links = tree.xpath('//*[@class="a-section aok-relative s-image-square-aspect"]/../@href')
        page_no_obj = tree.xpath('//*[@class="a-disabled"]/text()')
        # pagination
        page_no = 1
        for i in page_no_obj:
            try:

                page_no = int(re.findall('[0-9]*', i)[0])
                if type(page_no) == int:

                    break
            except:
                pass

        print('##########  crawling starts  #########')

        with open('output.csv', 'w'):
            pass


        for i in range(1, page_no + 1):
            # print(x)
            datacrawled = []

            newurl = url.split('page=')[0] + "page=" + str(i)  + url.split('page=')[1][url.split('page=')[1].index('&'):]
            # crawling second page
            r = self.gethtmldata(newurl)
            from lxml import html

            try:
                tree = html.fromstring(r.content)
            except:
                print("Parse error")

            linksName = [str(x) for x in tree.xpath('//*[@class="a-size-base-plus a-color-base a-text-normal"]/text()')]
            links = ["https://www.amazon.fr" + x for x in tree.xpath('//*[@class="a-section aok-relative s-image-square-aspect"]/../@href')]
            pageNols = [i for x in links]
            datacrawled.append([(linksName[x],links[x],pageNols[x]) for (x,y) in enumerate(links)])

            fields = ['Product Name', 'Product URL', 'Page No']


            with open('output.csv', 'a') as f:

                # using csv.writer method from CSV package
                write = csv.writer(f)

                if i == 1:
                    write.writerow(fields)

                write.writerows(datacrawled[-1])

            print('#'*4 + " page " + str(i) + " crawled " + '#'*4 )

myc = mycrawler()
myc.getlinks(url)