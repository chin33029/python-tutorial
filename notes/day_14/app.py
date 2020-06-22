""" Entry Point """
# from service.example import Example
from service.contact import Contact

import util.logging_setup


if __name__ == "__main__":

    # Example().add_item(
    #     {
    #         "name": "Ricky Chin",
    #         "address": "909 Golden Palomino Ct",
    #         "city": "Boynton Beach",
    #         "somthing": {
    #             "do": "stuff"
    #         }
    #     })

    Contact().add_item(
        {
            'firstName': 'Mrs',
            'lastName': 'Jackson',
            'address': '909 Golden Palomino Court',
            'city': 'Austin',
            'state': 'TX',
            'zipcode': '78732'
        }
    )
    Contact().add_item(
        {
            'firstName': 'Dean',
            'lastName': 'Chin',
            'address': '909 Golden Palomino Court',
            'city': 'Austin',
            'state': 'TX',
            'zipcode': '78732'
        }
    )
    Contact().add_item(
        {
            'firstName': 'Ricky',
            'lastName': 'Chin',
            'address': '909 Golden Palomino Court',
            'city': 'Austin',
            'state': 'TX',
            'zipcode': '78732'
        }
    )

    # print('--- ONE ----')
    CONTACT = Contact().find_many({'lastName': 'Chin'})
    print(list(CONTACT))
    # Contact().delete_one({'lastName': 'Chin'})
    Contact().delete_many({'lastName': 'Chin'})
    # print('--- TWO ----')
    CONTACT = Contact().find_many({'lastName': 'Chin'})
    print(list(CONTACT))
    Contact().update(query={'firstName': 'Mrs', 'lastName': 'Jackson'},
                     update_dict={'$set': {'address': '123 Wheels of Steel'}})
