import requests
from bs4 import BeautifulSoup
import time
from queue import Queue

class SEMAE():        
    
    def getPageHtml(self, id):
        try:
            reponse = requests.get('http://www.semae.rs.gov.br/noticias_detalhes_semae.php?idnoticia={}'.format(id))
            return reponse.text
        except:
            print('Exceção ao carregar a pagina com o id: {}'.format(id))
        return None

    def getTitlePage(self, id):
        try:            
            bs = BeautifulSoup(self.getPageHtml(id), 'html.parser')
            #capturando o titulo da pagina
            title =  bs.find('div', {'class': 'tipo_texto'}).h1.text
            return title
        except:
            print('Erro ao carregar o bs!')
            return None
                
    def run(self, queue, inicio, fim):        
        for ii in range(inicio, fim):
            queue.put(self.getTitlePage(ii))

    def showTitles(self, queue):        
        while(1):            
            time.sleep(0.1)            
            if( not queue.empty()):
                print(queue.get())

