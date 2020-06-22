""" Entry Point """
from service.example import Example
from service.contact import Contact

if __name__ == "__main__":
    # Example().add_item(
    #     {
    #         "name": "Dean Chin"
    #     })

    # Contact().add_item({
    #         'firstName': 'Dean',
    #         'lastName': 'Chin'
    # })

    CONTACT = Contact().find_item({
        'lastName': 'Chin'
    })
    print(CONTACT)

    Contact().delete_item({
        'lastName': 'Chin'
    })
    CONTACT = Contact().find_item({
        'lastName': 'Chin'
    })
    print(CONTACT)
    