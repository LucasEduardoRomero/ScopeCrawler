import sys
from src.FundamentusCrawler import FundamentusCrawler
#"SMTO3"
try:
  ticker = str(sys.argv[1])
  crawler = FundamentusCrawler( "https://www.fundamentus.com.br/" , "detalhes.php", ["--incognito","--headless"])
  produto = crawler.getPaper(ticker)
  print(produto)
except:
  print("Passe uma papel no argumento")

