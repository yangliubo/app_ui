import sys
BASE_DIR= 'e:\\python_project\\app_ui'
sys.path.append(BASE_DIR)

from base.teacher_client import TeacherClient
from page.index_page import IndexPage
import time
import pytest

class TestNative:
    def setup_class(self):
        self.client = TeacherClient()
        self.operator = self.client.operator
    @pytest.mark.re
    def test_refresh(self):
        time.sleep(10)
        self.operator.web_refresh_page()
        
        
        
