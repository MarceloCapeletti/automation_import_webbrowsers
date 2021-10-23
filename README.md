# Automação do webbrowser Google Chrome (Selenium)

### BOT utilizado para automatizar a importação de dados do INMET (Instituto Nacional de Meteorologia)

:point_right: [get_data_INMET.py](https://github.com/MarceloCapeletti/bot-importa-dados-inmet/blob/main/get_data_INMET_chromedriver.py "get_data_INMET.py")

Emprega a automação do webbrowser Google Chrome através da biblioteca Selenium do Python. 
Tem a função de realizar a importação automáticas dos dados climáticos do Instituto Nacional de Meteorologia - INMET

As features são destinadas a um arquivo .csv em tipo DataFrame do Pandas na seguinte ordem:

Data, Hora (UTC), Temp, Temp. Max. (C),	Temp. Min. (C),	Umi. Ins. (%), Umi. Max. (%), Umi. Min. (%), Pto Orvalho Ins. (C) Pto Orvalho Max. (C), Pto Orvalho Min. (C), Pressao Ins. (hPa), Pressao Max. (hPa), Pressao Min. (hPa), Vel. Vento (m/s), Dir. Vento (m/s), Raj. Vento (m/s), Radiacao (KJ/m¶ý), Chuva (mm)

:arrow_forward: Classe importDataInmet (url,dataInicio,dataFinal):

	recebe URL do INMET: Ex: https://tempo.inmet.gov.br/TabelaEstacoes/A801
	recebe Data de Inicio da importação: XX/XX/XXXX
	recebe Data de Fim da importação: XX/XX/XXXX

:arrow_forward: Funções:

	import_
	getdata
	printdata
	datatocsv

### Automatizar importação dos dados hidrológicos Agência Nacional de Aguas (ANA)
:point_right: :construction:  get_data_ANA.py :soon::clock10:
