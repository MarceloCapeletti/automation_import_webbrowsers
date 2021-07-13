# bot-get-dados-inmet

# BOT utilizado para automatizar a importação de dados do INMET (Instituto Nacional de Meteorologia)

get_data_INMET.py

Função getDadosInmet (url,DataInicioDoUsuario,DataFimDoUsuario):

Recebe URL do INMET: Ex: https://tempo.inmet.gov.br/TabelaEstacoes/A801

Recebe Data de Inicio da importação: XX/XX/XXXX

Recebe Data de Fim da importação: XX/XX/XXXX

cria arquivo com os dados (dados.csv)

Utiliza biblioteca Selenium para importar dados climáticos do Instituto Nacional de Meteorologia - INMET
