from datetime import datetime
import random

class Config:
    """
    *****************************************************************************
    *
    * filename:       config.py
    * version:        1.0
    * author:         Sujair
    * creation date:  28-APRIL-2025
    *
    * change history:
    *
    * who             when           version  change (include bug# if apply)
    * ----------      -----------    -------  ------------------------------
    * Sujair          28-APRIL-2025    1.0      initial creation
    *
    *
    * description:    Class for configuration instance attributes
    *
    ****************************************************************************
    """

    def __init__(self):
        self.training_data_path = 'data/training_data'
        self.training_database = 'training'
        self.prediction_data_path = 'data/prediction_data'
        self.prediction_database = 'prediction'

    def get_run_id(self):
        """
        * method: get_run_id
        * description: method to generate run id
        * return: none
        *
        * who             when           version  change (include bug# if apply)
        * ----------      -----------    -------  ------------------------------
        * Sujair          28-APRIL-2025    1.0      initial creation
        *
        * Parameters
        *   none:
        * reason : for get logfiles, unique run id for each run
        """
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H%M%S")
        return str(self.date)+"_"+str(self.current_time)+"_"+str(random.randint(100000000, 999999999))