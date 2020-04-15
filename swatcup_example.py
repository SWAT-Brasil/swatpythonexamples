import logging
import platform
import os
import time

import pandas as pd

# swatpython modules
from swatcuppython.swatcup import SWATCUP
from swatcuppython.swatcupversion import SWATCUPVersion

# Logging stuff for debug - good to find errors. 
# Change level to logging.INFO for less information
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Get this file path. It is always a good idea to use absolute paths to avoid weird bugs
current_path = os.path.dirname(os.path.abspath(__file__))

# Show python version for information
logger.info("Python version: " + platform.python_version())

# Set the SWAT version. Operational system is detected automatically
swatcup = SWATCUP(SWATCUPVersion.SWATCUPv5_1_6_2)

# Set project path
swatcup.set_project_folder(os.path.join(current_path, 'sufi2.Sufi2.SwatCup'))

# Exemplo execução sincrona
#swatcup.sufi2_pre()
#swatcup.sufi2_run()
#swatcup.sufi2_post()

# Enxemplo execução assincrona
swatcup.sufi2_async_pre()
# You can wait to finish
swatcup.sufi2_async_wait()

swatcup.sufi2_async_run()
# You can do other things while sufi is running
while swatcup.sufi2_async_is_running():
    logger.debug("SUFI2 is running")
    # Do other stuffs
    time.sleep(2)

logger.debug("Return code:" + str(swatcup.sufi2_async_return_code()))

swatcup.sufi2_async_post()
swatcup.sufi2_async_wait()



#TODO: diminuir o numero de rodaddas para agilizar o exemplor
# criar pasta swatcuppython dentro da pasta do projeto para salvar arquivos temporarios e resultados
# Entender o pre processamento que deve ser feito nos dados observador e implementar
# ENtender a extraçao de dados e implemetar funcao para isso
# Semparar git para swatpython e swatcuppython
# separar variaria geradas em sufi2_pre() e rodar elas de forma concurente em diferentes processos, isso deve
# aumentar bastante a velocidade, pois muitot empo é gasto em processamento dos arquivos
# fazer um loader disso aqui para utilizar no Colabs do google com o gdrive e botar o colab pra fritar
# transformar em package
# rotinas de teste
# automatizar publicação de pacotes. cd B


# Probleas conhecidos:
# em linux o tamanho das letras nos nomes dos arquivos importa, por isso pode dar aguns paus...precisa ser do jeito
# cerrtinho.
# Quando for copiar o windows faca o zip no windows e descompacte no linux, caso contrario pode aparecer arquivos
# com mesmos nomes mas case diferentes...e ai nao da pra saber qual  é o correto.
# Sempre qque der algum pau estrnho no swat-edit deve ser arquivos duplicados ou tamanho das letras erradas.