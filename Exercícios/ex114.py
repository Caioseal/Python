import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Erro. Site indisponível')
else:
    print('Site OK')
    #print(site.read())