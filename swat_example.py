import logging
import platform
import os
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
# TODO: still not working properly. Fix someday
# swat.set_executable('/home/myexecutable')

# Set temp folder where all files and executables will be copied to
# TODO: tirar isso, copiar os projetos é muito demorado. Utilizar no diretorio original mesmo.
swat.set_working_folder(os.path.join(current_path, 'temp'))

# Copy all projects files and the swat executable to temp folder
swat.load_project(os.path.join(current_path, 'swatdata/swat_sample0_linux'))

# Read data
# swat.read(1,1,1)

# Run swat
swat.run()

# Read daily pcp1.pcp
info, data = swat.read_precipitation_daily("pcp1.pcp")
# Write daily pcp1.pcp
swat.write_precipitation_daily("pcp2.pcp", info, data)

# Read output.rch file
output = swat.read_output_rch("output.rch")

