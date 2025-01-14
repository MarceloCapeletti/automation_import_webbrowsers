

from selenium import webdriver
import time as time
import pandas as pd
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class importDataInmet:

    '''
    Bot de webscrapping com Selenium
    para dados climáticos do INMET
    (Instituto Nacional de Meteorologia)

    - Requer a URL da estação que se deseja importar

    - Requer data de inicio e final da importação

    - Requer chromedriver.exe no diretório
    https://chromedriver.chromium.org/downloads

    Versão 1.1
    Autor: Marcelo Bruno Capeletti
    '''

    def __init__(self, url, dayIni, dayEnd):
        self.url = url
        self.dayIni = dayIni
        self.dayEnd = dayEnd
        self.df = pd.DataFrame()

    def import_(self):

        try:


            driver=webdriver.Chrome()
            driver.set_window_size(1024, 1024)

            # Retira navegador da tela
            # driver.set_window_position(0, -1000)

            time.sleep(1)

            # Informa a url para biblioteca
            driver.get(self.url)

            time.sleep(5)

            # Encontra o elemento Menu Canto direito
            driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[1]").click()

            time.sleep(1)
              
            # Encontra Box(do site) afim de inserir data inicial
            DataInicio = driver.find_element(By.XPATH, 
                "//*[@id='root']/div[2]/div[1]/div[2]/div[4]/input")

            time.sleep(1)

            # Retira dados da box
            DataInicio.clear()

            # Insere dados no box
            DataInicio.send_keys(self.dayIni)

            time.sleep(1)

            # Encontra Box que irá a data final
            DataFim = driver.find_element(By.XPATH, 
                "//*[@id='root']/div[2]/div[1]/div[2]/div[5]/input")

            time.sleep(1)

            # Retira dados da box
            DataFim.clear()

            # Insere dados no box
            DataFim.send_keys(self.dayEnd)

            time.sleep(1)


            # Clica no botao 'Gerar Tabela'(da pagina)
            driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div[1]/div[2]/button").click()

            # Aguarda carregamento dos dados
            time.sleep(10) # implementar WebDriverWait 

            # tabela a ser importada => dataframe

            print(driver.page_source)
            all_tables = pd.read_html(
                driver.page_source, attrs={'class': 'ui blue celled striped unstackable table'})
            self.df = all_tables[0]
            


        except Exception as err:

            print("Erro! Começar novamente a importação!")
            print(err)

        finally:

            driver.quit()

    def getdata(self):

        return self.df

    def printdata(self):

        print(self.df)

    def datatocsv(self):

        self.df.to_csv('import.csv')


if __name__ == '__main__':

    while True:
        try:

            dayIni = input('Data de início da importação DD/MM/AAAA \n')
            datetime.datetime.strptime(dayIni, '%d/%m/%Y')
            dayEnd = input('Data de fim da importação DD/MM/AAAA \n ')
            datetime.datetime.strptime(dayEnd, '%d/%m/%Y')

            # Para outra estação, modificar URL
            importDataInmet = importDataInmet(
                'https://tempo.inmet.gov.br/TabelaEstacoes/A801', dayIni, dayEnd)
            importDataInmet.import_()
            df = importDataInmet.getdata()
            importDataInmet.printdata()
            importDataInmet.datatocsv()
            break

        except ValueError as ex:
            print(str(ex) + '\nValor invalido. Digite novamente:')
