from FundamentusCrawler import FundamentusCrawler

crawler = FundamentusCrawler( "https://www.fundamentus.com.br/" , "detalhes.php", ["--incognito","--headless"])
produto = crawler.getPaper("SMTO3")


