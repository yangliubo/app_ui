from elements.sign.sign_index_page_elements import SignIndexPageElements
from base.teacher_client import TeacherClient
from page.index_page import IndexPage
class SignIndexPage:
    def __init__(self,client:TeacherClient,is_init_to_page:bool=True) -> None:
        self.client = client
        self.operator = self.client.operator
        self.index_page_elements = SignIndexPageElements()
        if is_init_to_page:
            IndexPage(self.client).goto_sign()
        
    def goto_sign_module(self):
        self.operator.click(self.index_page_elements.sign_btn)
        
        

        
    