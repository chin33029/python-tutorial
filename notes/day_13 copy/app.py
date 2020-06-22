""" Entry Point """
# from service.example import Example
from service.contact import Contact


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
            'firstName': 'Dean',
            'lastName': 'Chin',
            'address': '909 Golden Palomino Court',
            'city': 'Austin',
            'state': 'TX',
            'zipcode': '78732'
        }
    )

    POST1 = {
        'firstName': 'Ricky',
        'lastName': 'Chin',
        'address': '909 Golden Palomino Court',
        'city': 'Austin',
        'state': 'TX',
        'zipcode': '78732'
    }

    POST2 = {
        'firstName': 'Frank',
        'lastName': 'Chin',
        'address': '10881 deer park lane',
        'city': 'TX',
        'zipcode': '33437'
    }
    
    POST3 = {
        'firstName': 'Crusty',
        'lastName': 'Clown',
        'address': '101 Living Color',
        'city': 'Dont play',
        'zipcode': 'pow'
    }

    
    Contact().delete_clear()
    Contact().add_item(POST1)
    Contact().find_all()
   
    change = input('Whats the firstName ya want to change? ')

    Contact().update_first_name(change)
    Contact().find_all()

    Contact().add_multiple([POST3, POST2])
    Contact().find_all()
    Contact().delete_clear()
