'''Address Class'''


class Address():
    def __init__(self,
                 street="undf",
                 city="undf",
                 state="undf",
                 zip_code="undf"):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def get(self):
        return {
            'street': self.street,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code
        }
