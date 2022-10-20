

import pytest

from BaseClass import BaseClass

@pytest.mark.usefixtures("dataLoad")

class TestExample(BaseClass):

    def test_profile(self,dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        log.error(dataLoad[2])
        
        
        
        

    
        # print(dataLoad)
        # print(dataLoad[0])
        # print(dataLoad[2])
