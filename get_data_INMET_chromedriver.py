from selenium import webdriver
import time as time
import pandas as pd

#   Bot para importar dados automaticamente do INMET (Instituto Nacional de Meteorologia) 
#   Precisa URL da estação que se deseja importar do INMET
#   e pede data de inicio e final da importação 
#   Versão 1.1
#   Autor: Marcelo Bruno Capeletti

class importDataInmet:
    
    def __init__(self,url,dayIni,dayEnd):
        self.url = url
        self.dayIni = dayIni
        self.dayEnd = dayEnd
        self.df = pd.DataFrame()
        
    def import_(self):
       
        options = webdriver.ChromeOptions()                 #start
        driver = webdriver.Chrome(chrome_options=options)
        driver.set_window_size(1024, 1024)                  #Utiliza resolução padrão afim de evitar erros
        #driver.set_window_position(0, -1000)               #Retira navegador da tela
        time.sleep(1)
        driver.get(self.url)                                #Informa a url para biblioteca
        time.sleep(5)                                       #Aguarda carregamento da pagina
        driver.find_element_by_id("menu").click()           #Encontra o elemento Menu Canto direito
        DataInicio = driver.find_element_by_id("datepicker_EstacoesTabela_Inicio")        #Encontra Box(do site) afim de inserir data inicial
        #print(DataInicio)
        time.sleep(1)                                       #Aguarda carregamento da pagina
        DataInicio.clear()                                  #Retira dados da box
        DataInicio.send_keys(self.dayIni)                   #Insere dados no box
        time.sleep(1)                                       #Aguarda carregamento da pagina
        #driver.quit()
        DataFim = driver.find_element_by_id("datepicker_EstacoesTabela_Fim")  #Encontra Box que irá a data final
        time.sleep(1)                                       #Tempo espera
        DataFim.clear()                                     #Retira dados da box
        DataFim.send_keys(self.dayEnd)                      #Insere dados no box
        time.sleep(1)                                       #Aguarda carregamento da pagina
        driver.find_element_by_id("menu").click()
        time.sleep(1)                                          
        driver.find_element_by_id("EstacoesTabela").click() #Clica no botao 'Gerar Tabela'(da pagina)
        time.sleep(5)                                       #Aguarda carregamento da pagina e dos dados
        all_tables = pd.read_html(driver.page_source, attrs={'id': 'tabela'}) #Encontra tabela a ser importada
        self.df = all_tables[0]                             #Tabela da pagina para dataframe
        driver.quit()                                       #Encerra Chrome
                                    
    def getdata(self):
        
        return self.df
    
    def printdata(self):
        
         print(self.df)                                         #Imprime tabela
         
    def datatocsv(self):
        
         self.df.to_csv('dados.csv')                            #Exporta Tabela

dayIni = input('Data de início da Importação DD/MM/AAAA \n')    #Solicita ao usuário data de início
dayEnd = input('Data de início da Importação DD/MM/AAAA \n ')   #Solicita ao usuário data de fim
  
importDataInmet = importDataInmet('https://tempo.inmet.gov.br/TabelaEstacoes/A801',dayIni,dayEnd)
importDataInmet.import_()
df = importDataInmet.getdata()
importDataInmet.printdata()
importDataInmet.datatocsv()
