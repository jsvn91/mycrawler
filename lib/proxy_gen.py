import random
import requests
# from my_fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests
# ua = UserAgent()

class proxy_gen():

    def __init__(self):
        self.proxies = self.get_all_proxies()
        pass

    def get_all_proxies(self):
        proxies = []
        proxies_doc = ''
        try:
            proxies_doc = requests.get('https://www.sslproxies.org/').text
            soup = BeautifulSoup(proxies_doc, 'html.parser')
            proxies_table = soup.find(id='proxylisttable')
            load = []


            # Save proxies in the array
            for row in proxies_table.tbody.find_all('tr'):
                proxies.append({
                    'ip': row.find_all('td')[0].string,
                    'port': row.find_all('td')[1].string
                })
            return proxies
        except:
            raise ('Error downloading Proxies...')

    def get_a_proxy(self):
        self.proxies= self.get_all_proxies()
        lenpr = len(self.proxies)
        """http_proxy  = "http://10.10.1.10:3128"
            https_proxy = "https://10.10.1.11:1080"
            ftp_proxy   = "ftp://10.10.1.10:3128"
            
            proxyDict = { 
                          "http"  : http_proxy, 
                          "https" : https_proxy, 
                          "ftp"   : ftp_proxy
                        }
        """
        usablaProxy = {
            # "http":"http://" + self.proxies[random.randint(0, lenpr)]['ip'] + ":" + self.proxies[random.randint(0, lenpr)]['port'],
            "https": "" + self.proxies[random.randint(0, lenpr)]['ip'] + ":" + self.proxies[random.randint(0, lenpr)]['port'],
            # "ftp":"ftp://" +self.proxies[random.randint(0, lenpr)]['ip'] + ":" + self.proxies[random.randint(0, lenpr)]['port']
        }

        return usablaProxy

    def get_headers(self):
        f = open('lib//headers').readlines()
        dict_final = {}
        for x in f:
            dict_final[x.split(':')[0]] = x.split(':')[1][1:].replace('\n','')
            pass
        return dict_final

    def get_form_data(self,path):
        f = open(path).readlines()
        dict_final = {}
        for x in f:
            dict_final[x.split(':')[0]] = x.split(':')[1][1:].replace('\n', '')
            pass
        return dict_final
