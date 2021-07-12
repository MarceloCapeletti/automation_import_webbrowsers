from selenium import webdriver
import time as time
import pandas as pd

#       Importação dados meteorologicos 
#       do site INMET. Pede url do site INMET e data de começo e fim de importação 
#       No final é criado o arquivo dados.csv 
#       Versão 1.0

def ImportaDadosInmet (url,DataInicioDoUsuario,DataFimDoUsuario):
   
    options = webdriver.ChromeOptions()                 #inicia
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(1024, 1024)                    #mesma resolução, evitar erros
    #driver.set_window_position(0, -1000)                #esconde Chrome do usuário
    time.sleep(1)
    driver.get(url)                                     #Carrega o HTML
    time.sleep(5)                                       #Tempo para carregar a pagina
    driver.find_element_by_id("menu").click()           #Encontra o elemento Menu Canto direito
    DataInicio = driver.find_element_by_id("datepicker_EstacoesTabela_Inicio")        #Encontra Box(do site) que irá a data inicial
   # print(DataInicio)
    time.sleep(1)                                       #Tempo espera do Chrome
    DataInicio.clear()                                  #Tira dados da box
    DataInicio.send_keys(DataInicioDoUsuario)           #Coloca dados no box
    time.sleep(1)                                       #Tempo espera do Chrome
   # driver.quit()
    DataFim = driver.find_element_by_id("datepicker_EstacoesTabela_Fim")  #Encontra Box que irá a data final
    time.sleep(1)                                       #Tempo espera
    DataFim.clear()                                     #Tira dados da box
    DataFim.send_keys(DataFimDoUsuario)                 #Coloca dados no box
    time.sleep(1)                                       #Tempo espera do Chrome
    driver.find_element_by_id("menu").click()
    time.sleep(1)                                          
    driver.find_element_by_id("EstacoesTabela").click() #Clica botao 'Gerar Tabela'(do site)
    time.sleep(5)                                       #Espera para carregar tabela
    all_tables = pd.read_html(driver.page_source, attrs={'id': 'tabela'}) #Encontra tabela a ser importada
    df = all_tables[0]
    print(df)                                           #Imprime tabela
    df.to_csv('dados.csv') #Exporta Tabela
    driver.quit()                                       #Fecha Chrome

DataInicio = input('Data de início da Importação DD/MM/AAAA \n') #Pede usuário data de início
DataFim = input('Data de início da Importação DD/MM/AAAA \n ')   #Pede ao usuário data de fim
  

ImportaDadosInmet('https://tempo.inmet.gov.br/TabelaEstacoes/A801',DataInicio,DataFim) #Inicia funçao importação
