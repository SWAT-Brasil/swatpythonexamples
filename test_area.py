import platform
import re
import numpy
from swatpython.swat2012rev670.swat2012rev670 import SWAT2012rev670

# Area para desenvolvimento e testes de funcoes Python - é mais facil qd fazer isso dentro das classes


# teste da porra
# Abre arquivo
#fo = open(filename, "r")
# Abre arquivo
import pandas as pd

file = '/media/jairo/Dados/Jairo/Projetos/SWAT/git/linux/swatpythonexamples/swatdata/swatcup2019_linux/sufi2.Sufi2.SwatCup/SUFI2.OUT/NO3_OUT_7.txt'
fo = open(file, "r")
#df = pd.read_csv(fo, header=None, delim_whitespace=True, nrows=1)
#while row = numpy.loadtxt(fo, max_rows=1):
#    print(row)
iterations = []
data = []
index = []
data_index = -1
new_col = True
for line in fo:
    list = line.split()
    if len(list) == 1:
        # numero da iteracao
        iterations.append(int(list[0]))
        new_col = True
        data.append([])
        index.append([])
        data_index += 1
    if len(list) == 2:
        # dados
        time_step = int(list[0])
        value = float(list[1])
        data[data_index].append(value)
        index[data_index].append(time_step)

fo.close()
# TODO: this assume the file is correct and with all values. Make it more robust in the future
df = pd.DataFrame(columns=iterations, index=index[0], data=numpy.transpose(data))


print(data)
print(df)

#with open(file, 'r') as fo:
#    row = numpy.loadtxt(fo, max_rows=1)
#    print(row)




exit()



file = "/media/jairo/Dados/Jairo/Projetos/SWAT/git/linux/swatpythonexamples/swatdata/swat2012/swat2012_rev637/txtinout/file.cio"
fo = open(file, "r")
# Le
fo.readline()
fo.readline()
fo.readline()
fo.readline()
fo.readline()
fo.readline()
filecio = {'FIGFILE': re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0]}
filecio.update({'NBYR': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'IYR': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'IDAF': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'IDAL': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
fo.readline()
filecio.update({'IGEN': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'PCPSIM': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'IDT': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'IDIST': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'REXP': float(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'NRGAGE': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'NRTOT': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'NRGFIL': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'TMPSIM': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'NTGAGE': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'NTTOT': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'NTGFIL': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'SLRSIM': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'NSTOT': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'RHSIM': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'NHTOT': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'WNDSIM': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'NWTOT': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'FCSTYR': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'FCSDAY': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'FCSTCYCLES': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
fo.readline()
line = fo.readline()
files = []
for i in range(0, len(line), 13):
    name = line[i:13].strip()
    if name != '':
        files.append(name)
filecio.update({'RFILE1_6': files})
line = fo.readline()
files = []
for i in range(0, len(line), 13):
    name = line[i:13].strip()
    if name != '':
        files.append(name)
filecio.update({'RFILE7_12': files})
line = fo.readline()
files = []
for i in range(0, len(line), 13):
    name = line[i:13].strip()
    if name != '':
        files.append(name)
filecio.update({'RFILE13_18': files})
fo.readline()
line = fo.readline()
files = []
for i in range(0, len(line), 13):
    name = line[i:13].strip()
    if name != '':
        files.append(name)
filecio.update({'TFILE1_6': files})
line = fo.readline()
files = []
for i in range(0, len(line), 13):
    name = line[i:13].strip()
    if name != '':
        files.append(name)
filecio.update({'TFILE7_12': files})
line = fo.readline()
files = []
for i in range(0, len(line), 13):
    name = line[i:13].strip()
    if name != '':
        files.append(name)
filecio.update({'TFILE13_18': files})

filecio.update({'SLRFILE': fo.readline()[0:12].strip()})
filecio.update({'RHFILE': fo.readline()[0:12].strip()})
filecio.update({'WNDFILE': fo.readline()[0:12].strip()})
filecio.update({'FCSTFILE': fo.readline()[0:12].strip()})
fo.readline()
filecio.update({'BSNFILE': fo.readline()[0:12].strip()})
fo.readline()
filecio.update({'PLANTDB': fo.readline()[0:12].strip()})
filecio.update({'TILLDB': fo.readline()[0:12].strip()})
filecio.update({'PESTDB': fo.readline()[0:12].strip()})
filecio.update({'FERTDB': fo.readline()[0:12].strip()})
filecio.update({'URBAMDB': fo.readline()[0:12].strip()})
fo.readline()
filecio.update({'ISPROJ': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'ICLB': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'CALFILE': fo.readline()[0:12].strip()})
fo.readline()
filecio.update({'IPRINT': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'NYSKIP': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'ILOG': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'IPRP': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
#filecio.update({'IPRS': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
fo.readline()
fo.readline()
results = (re.findall(r"[^\s\,!?;'\"]+", fo.readline()))
results = [int(i) for i in results]
filecio.update({'IPDVAR': results})
fo.readline()
results = (re.findall(r"[^\s\,!?;'\"]+", fo.readline()))
results = [int(i) for i in results]
filecio.update({'IPDVAB': results})
fo.readline()
results = (re.findall(r"[^\s\,!?;'\"]+", fo.readline()))
results = [int(i) for i in results]
filecio.update({'IPDVAS': results})
fo.readline()
results = (re.findall(r"[^\s\,!?;'\"]+", fo.readline()))
results = [int(i) for i in results]
filecio.update({'IPDHRU': results})
fo.readline()
filecio.update({'ATMOFILE': fo.readline()[0:12].strip()})
filecio.update({'IPHR': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'ISTO': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'ISOL': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'I_SUBW': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'SEPTDB': fo.readline()[0:12].strip()})
filecio.update({'IA_B': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'IHUMUS': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'ITEMP': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'ISNOW': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'IMGT': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'IWTR': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
filecio.update({'ICALEN': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})











print(filecio)

exit()

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

