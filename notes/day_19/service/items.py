''' Items class '''


class Items():
    ''' Items class '''

    def get_all(self):
        ''' get all items '''
        return {
            'items': [
                {'name': 'item1'},
                {'name': 'item2'},
            ]
        }, 200

    def get_one(self, name):
        ''' get one item by name '''
        return {
            'message': f'Found item {name}'
        }, 200

    def create_one(self, payload):
        ''' Create an item '''
        # check that phone is good
        # check something else
        return {
            'message': f'Created item: {payload}',
            'itemName': f'{payload["name"]}',
            'itemPrice': f'{payload["price"]}',
        }, 201

    def update_one(self, name, payload):
        ''' update one item by name '''
        return {
            'message': f'Update {name}'
        }, 200

    def delete_one(self, name):
        ''' delete one item by name '''
        return {
            'message': f'Delete {name}'
        }, 200
