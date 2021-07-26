# bot-get-dados-inmet

# BOT utilizado para automatizar a importação de dados do INMET (Instituto Nacional de Meteorologia)

get_data_INMET.py

Classe importDataInmet (url,dataInicio,dataFinal):

	recebe URL do INMET: Ex: https://tempo.inmet.gov.br/TabelaEstacoes/A801
	recebe Data de Inicio da importação: XX/XX/XXXX
	recebe Data de Fim da importação: XX/XX/XXXX

Funções:

	import_
	getdata
	printdata
	datatocsv

Utiliza biblioteca Selenium para importar dados climáticos do Instituto Nacional de Meteorologia - INMET
