import logging
import platform
import os
import time

import pandas as pd

# swatpython modules
from swatpython.swat import SWAT
from swatpython.swatversion import SWATVersion
from swatpython.operationalsystem import OperationalSystem

# Logging stuff for debug - good to find errors. 
# Change level to logging.INFO for less information
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Get this file path. It is always a good idea to use absolute paths to avoid weird bugs
current_path = os.path.dirname(os.path.abspath(__file__))

# Show python version for information
logger.info("Python version: " + platform.python_version())

# Set the SWAT version. OS is detected automatically
swat = SWAT(SWATVersion.SWAT2012REV670)

# Set custom executable if required. Te executable should work on
# the same project version and OS defined above. Uncomment to use
# swat.set_custom_swat("/media/jairo/Dados/Jairo/Projetos/SWAT/git/linux/swatpythonexamples/swatpython/swat2012rev670/swat2012_rev670_linux")

swat.set_project_folder(os.path.join(current_path, 'swatdata/swat2012/swat_sample0'))

# Run swat. Select sync (you wait until finished) or async (runs swat and you can process other things at same time)
ASYNC_MODE_EXAMPLE = True
if not ASYNC_MODE_EXAMPLE:
    # Exemplo execução sincrona
    logger.debug("Sync example")
    swat.run()
else:
    # Exemplo execução assincrona
    logger.debug("Async example")
    swat.async_run()
    while swat.async_is_running():
        logger.debug("SWAT is running")
        # Do other stuffs
        time.sleep(1)
    logger.debug("Return code:" + str(swat.async_return_code()))

# Read daily pcp1.pcp
info, data = swat.read_precipitation_daily("pcp1.pcp")
print(info)
print(data)
# Write daily pcp1.pcp
swat.write_precipitation_daily("pcp2.pcp", info, data)

# Read output.rch file
output = swat.read_output_rch("output.rch")

