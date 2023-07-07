#
#      this class handles initialisation from file or epics variable processing and some events 
#      21/03/2019  o.javakhishvili@fz-juelich.de
#
import yaml
from epics import PV
import time
import globals
from datetime import datetime

class PV_epics:

       def __init__(self, gui):
              ''' 
                     initialisation needs passing gui object from main gui class to access its objects
              '''
              self.epics_variables = dict()      #dictionary to hold epics variables 
              self.gui = gui

       def Write_PV(self, name,data):
              '''    
                     write data to pv. name should be one from epics_variables dict
              '''
              self.epics_variables[name].value = data
              time.sleep(0.1)
              return self.epics_variables[name].value

       def Read_PV(self, name):
              '''
                     reads data from pv. name should be one from epics_variables dict
              '''
              #print(epics_variables)
              return (str(self.epics_variables[str(name)].value))

       def load_conf(self):
              '''
                     loads configuration file and makes epics_variables dict and also some global variables
                     also adds callbacks to some epics pvs for monitoring 
              '''
              globals.init()
              with open('config.yml') as cfg:
                     main_config = yaml.load(cfg)
                     keys = list(main_config['EPICS_PV'].keys())
                     values = main_config['EPICS_PV'].values()
                     pv_list = list()
                     for n in values:
                            pv_list.append(PV(str(n)))
                     self.epics_variables.update(dict(zip(keys,pv_list)))
              #callbacks for status and motor posotion changes
              self.epics_variables['STATUS_Y'].add_callback(self.status_y_callback)
              self.epics_variables['GET_BEAM_Y'].add_callback(self.get_pos_y_callback)
              #defoult values from config file
              globals.VERT_INBEAM_DEFOULT_VALUE = main_config['VERT_INBEAM_DEFOULT_VALUE']
              globals.VERT_DELTA_DEFOULT_VALUE = main_config['VERT_DELTA_DEFOULT_VALUE']
              globals.VERT_HOME_DEFOULT_VALUE = main_config['VERT_HOME_DEFOULT_VALUE']
              return main_config
              
       #callback methods
       def status_y_callback(self, pvname, value, timestamp, cb_info, **kwargs):
           var = datetime.fromtimestamp(timestamp)
           time = var.strftime("%Y-%m-%d %H:%M:%S")
           self.gui.status_text_update("{0},  name -> {1},  value -> {2}".format(time,pvname,value))
       def get_pos_y_callback(self, pvname, value, timestamp, cb_info, **kwargs):
           var = datetime.fromtimestamp(timestamp)
           time = var.strftime("%Y-%m-%d %H:%M:%S")
           self.gui.status_text_update("{0},  name -> {1},  value -> {2}".format(time,pvname,value))
