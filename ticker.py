 #       (\-/)
  #     (:O O:)
   #     \   /o\
    #     | |\o \  
     #    (:) \ o\          
      #        \o \--_      
       #      ( o O
        #     (  O

import requests
import re
from sys import stdout
from time import sleep

def get_page(url):
    r = requests.get(url)
 #   print r.status_code
    content = r.text.encode('utf-8', 'ignore')
    return content

if __name__ == "__main__":
    try:
        while True:
            url = 'https://mtgox.com'
            content = get_page(url)
            content = content.replace('\n', '')


            content_pattern = re.compile('li id="lastPrice".*?>.*?>(.*?)<')
            result = re.findall(content_pattern, content)
            data = result[0]
            stdout.write('\rLast BTC price: ' +(data))
            stdout.flush()
            sleep(3)
    except:
        raise

