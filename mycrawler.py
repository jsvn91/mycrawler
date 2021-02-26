import requests
from lib.proxy_gen import proxy_gen
import bs4
url = 'https://publicaccess.wycombe.gov.uk/idoxpa-web/search.do?action=advanced'

class mycrawler(proxy_gen):

    def __init__(self):
        proxy_gen.__init__(self)
        pr = self.get_a_proxy()

        pass



    def gethtmldata(self,url):


        # parse link --------------------

        url = "https://publicaccess.wycombe.gov.uk/idoxpa-web/advancedSearchResults.do?action=firstPage"
        data = self.get_form_data('lib/formdata')

        r = requests.post(url, data=data)
        return r

    def getlinks(self,url):

        #----------------- get first link
        r = self.gethtmldata(url)
        from lxml import html

        try:
            tree = html.fromstring(r.content)
        except:
            print("Parse error")


        links = tree.xpath('//*[@id="searchresults"]/li/a/@href')

        link2 = 'https://publicaccess.wycombe.gov.uk' + links[0]

        headers2 = self.get_form_data('lib/headers2')


        r = requests.get(link2,headers = headers2)

        try:
            tree2 = html.fromstring(r.content)
        except:
            print("Parse error in second link")

        val= tree2.xpath('//*[@id="simpleDetailsTable"]//tr/td/text()')
        val = [x.lstrip().rstrip() for x in val]
        toc= tree2.xpath('//*[@id="simpleDetailsTable"]//tr/th/text()')
        toc= [x.lstrip().rstrip() for x in toc]

        for i, k in enumerate(toc):
            if 'Proposal' in k:
                print('the proposal value of first link is  : ', val[i])

        pass



myc = mycrawler()
myc.getlinks(url)