'''Contact Class'''

class Contact():
    '''contact class'''

    def __init__(self,
                 name='undf',
                 phone='undf',
                 home_address=Address(),
                 work_address=Address()):
    
        self.name = name
        self.phone = phone
        self.home_address = home_address
        self.work_address = work_address

    def get(self):
        '''return contact'''
        return{
            
        }