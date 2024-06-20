from common.tools.file_tools import FileTOOL
import os

class ReadConfig:
    def __init__(self) -> None:
        pwd = os.getcwd()
        self.yml_datas = FileTOOL.get_all_yml_files_in_dir(dir_name=os.path.join(pwd,'config'))
        
    
    def __get_yml_data(self,config_name):
        data = self.yml_data[config_name]
        return data