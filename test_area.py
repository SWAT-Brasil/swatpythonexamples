import platform
import re
from swatpython.swat2012rev670.swat2012rev670 import SWAT2012rev670

# Area para desenvolvimento e testes de funcoes Python - é mais facil qd fazer isso dentro das classes


# teste da porra
# Abre arquivo
#fo = open(filename, "r")
# Abre arquivo
import pandas as pd

file = "/media/jairo/Dados/Jairo/Projetos/SWAT/git/SWATPython/sufi2.Sufi2.SwatCup/SUFI2.OUT/goal.txt"
fo = open(file, "r")
# Le informacoes das primeiras linhas
line1 = re.findall(r"[^\s\,!?;'\"]+", fo.readline())
line2 = re.findall(r"[^\s\,!?;'\"]+", fo.readline())
line3 = re.findall(r"[^\s\,!?;'\"]+", fo.readline())

if line1[0] == "no_pars=":
    param_number = int(line1[1])
else:
    raise ValueError("Invalid goal file:" + file)

if line2[0] == "no_Sims=":
    simulation_number = int(line2[1])
else:
    raise ValueError("Invalid goal file:" + file)

if line3[0] == "type_of_goal_fn=":
    goal_type = line3[1]
else:
    raise ValueError("Invalid goal file:" + file)

info = {"no_pars": param_number,
        "no_sims": simulation_number,
        "type_of_goal_fn": goal_type}

print(info)
# Le informações da tabela
#data_widths = [5] + [9] * param_count
df = pd.read_csv(fo, header=0, delim_whitespace=True)
print(df)
#df.columns = ['year', 'day'] + title[1:]



# Le informações do arquivo e separa informacoes por espaco e virgula e outras coisinhas mais
#v#title = e.findall(r"[^\s\,!?:;'\"]+", fo.readline())
# Calcula o numero de variaveis do arquivo
#param_count = len(title) - 1
#param_count = 47
#data_widths = [7, 4, 9, 6] + [12] * param_count
#header = pd.read_fwf(fo, widths=data_widths, header=8, index_col=None)
#print(header)
# Dataframe de informacao
#info = pd.concat([pd.DataFrame([title]), latitude])
#data_widths = [4, 3] + [5] * param_count
#df = pd.read_fwf(fo, widths=data_widths, header=None, index_col=None)
#df.columns = ['year', 'day'] + title[1:]
fo.close()

