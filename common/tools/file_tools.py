import yaml
import os
class FileTOOL:
    @classmethod
    def parse_yml(cls,file_name):
        path =  os.path.abspath(file_name)
        with open(file=path,mode='r',encoding='utf-8') as f:
            data = yaml.safe_load(f)
            return data
        
    @classmethod    
    def get_all_yml_files_in_dir(cls,dir_name,file_dic:dict=None):
        '''
        遍历目录下所有的yml文件
        返回字典 {'去掉.yml的文件名':文件内容}
        '''
        if file_dic == None:
            file_dic = {}

        list = os.listdir(dir_name)
        print('list:',list)
        for i in list :
            file_name = os.path.join(dir_name,i)
            if os.path.isfile(file_name):
                print('fffffffffffffffffff',i)
                data = cls.parse_yml(file_name=file_name)
                file_dic.update({i.replace('.yml',''):data})
            elif os.path.isdir(file_name):
                file_dic = cls.get_all_yml_files_in_dir(file_name,file_dic)
        return file_dic