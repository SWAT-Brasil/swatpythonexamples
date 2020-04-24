import logging
import platform
import os
import time
import matplotlib
import matplotlib.pyplot as p
# You may need to install python-tk to use matplot lib inside a enviroment
# install pyside2 to get iw working

import pandas as pd

# swatpython modules
from swatcuppython.swatcup import SWATCUP
from swatcuppython.swatcupversion import SWATCUPVersion



# Logging stuff for debug - good to find errors. 
# Change level to logging.INFO for less information
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Get this file path. It is always a good idea to use absolute paths to avoid weird bugs
current_path = os.path.dirname(os.path.abspath(__file__))

# Show python version for information
logger.info("Python version: " + platform.python_version())

# Set the SWAT version. Operational system is detected automatically
swatcup = SWATCUP(SWATCUPVersion.SWATCUP2019)

# Set project path
operational_system = platform.system()
if operational_system == "Windows":
    swatcup.set_project_folder(os.path.join(current_path, 'swatdata/swatcup2019_windows/sufi2.Sufi2.SwatCup'))
elif operational_system == "Linux":
    swatcup.set_project_folder(os.path.join(current_path, 'swatdata/swatcup2019_linux/sufi2.Sufi2.SwatCup'))
else:
    raise ValueError("Unknown operational system")

# Para selecionar o exemplo assincrono altere para True
ASYNC_MODE_EXAMPLE = False
if not ASYNC_MODE_EXAMPLE:
    # Exemplo execução sincrona
    logger.debug("Sync example")
    #swatcup.sufi2_pre()
    #swatcup.sufi2_run()
    #swatcup.sufi2_post()
else:
    # Exemplo execução assincrona
    logger.debug("Async example")
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

# Shows result
out_file_names = swatcup.read_sufi2_var_file_name()
print(out_file_names)
logger.info("Output files: " + str(out_file_names))

info, df = swatcup.read_sufi2_out_goal()
logger.info("Goal: " + str(info))
#logger.info("Goal: " + str(df))
print(df)

# read output files
#data = swatcup.read
VAR_ID = 3
filename = out_file_names[VAR_ID]
var = swatcup.read_sufi2_var(filename)
ax = var.plot(title=filename)
ax.set_xlabel('time step')
ax.set_ylabel('intensity')
p.show()



