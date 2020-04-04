from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#cyre3 tupy3 smto3

class FundamentusCrawler:
  def __init__(self, url, prefix, opcoes):
    chrome_options = webdriver.ChromeOptions()
    for index in range( len(opcoes)):
      chrome_options.add_argument(opcoes[index])      
    self.chrome = webdriver.Chrome(options=chrome_options)
    self.url = url+prefix    

  def getPaper(self, ticker):
    paper = {}
    self.chrome.get(self.url+"?papel="+ticker.upper())
    tabelas = self.chrome.find_elements_by_xpath("//table[@class='w728']")
    
    #dados gerais - tabela 1

    # valores - tabela 2    
    paper["values"] = self.__getValues(tabelas[1])

    # oscilações/ indicadores - tabela 3

    # dados balanco pratimonial - tabela 4

    # dados demonstrativo de resultado - tabela 5



    self.lastPaper = paper
    self.__close()
    return paper    
    
    

  def __getValues(self, webdriverElement ):
    values = {}
    linhas = webdriverElement.find_elements_by_xpath("./tbody//tr")    
    for index in range( len(linhas)):
      colunas = linhas[index].find_elements_by_xpath(".//td")
      for j in range( 0, len(colunas), 2):
        try:
          label = colunas[ j ].find_element_by_xpath(".//span[2]").text
          value = int(colunas[ j+1 ].find_element_by_xpath(".//span[1]").text.replace(".",""))
        except:
          value = colunas[ j+1 ].find_element_by_xpath(".//span[1]").text
        finally:          
          values[ label ] = value
    return values

  def __close(self ):
    self.chrome.close()