import logging
import platform
import os
import shutil
import time

import pandas as pd
from swatcuppython.swatcup import SWATCUP
from swatcuppython.swatcupversion import SWATCUPVersion

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
current_path = os.path.dirname(os.path.abspath(__file__))
logger.info("Python version: " + platform.python_version())

swatcup = SWATCUP(SWATCUPVersion.SWATCUP2019)
AUTOMATION_FOLDER = "/media/jairo/Dados/Jairo/Projetos/SWAT/git/swatautomation/"
MODEL_FOLDER = "/media/jairo/Dados/Jairo/Projetos/SWAT/git/swatautomation/model/sufi2.Sufi2.SwatCup"
INPUT_SCENARIOS_FOLDER = '/media/jairo/Dados/Jairo/Projetos/SWAT/git/swatautomation/input/scenarios'
OUTPUT_SCENARIOS_FOLDER = '/media/jairo/Dados/Jairo/Projetos/SWAT/git/swatautomation/output/scenarios'
swatcup.set_project_folder(MODEL_FOLDER)

# find scenarios inputs
scenarios_path = next(os.walk(INPUT_SCENARIOS_FOLDER))[1]
logger.info('Scenarios found: ' + str(scenarios_path))

# clean output scenarios
shutil.rmtree(OUTPUT_SCENARIOS_FOLDER, ignore_errors=True)
for scenario in scenarios_path:
    logger.info('Running Scenario: ' + scenario)
    # prepare inputs

    # run model
    swatcup.sufi2_async_pre()
    swatcup.sufi2_async_wait()
    swatcup.sufi2_async_run()
    swatcup.sufi2_async_wait()
    swatcup.sufi2_async_post()
    swatcup.sufi2_async_wait()

    # extract outputs
    logger.info('Extracting outputs: ' + scenario)
    swatcup.copy_output(os.path.join(OUTPUT_SCENARIOS_FOLDER, scenario))

