import json

class Note():

    def __init__(self):
        self.data = {}

    def load_data(self, file_destination):
        with open(file_destination, 'r') as file:
            data = file.read()

        self.data = json.loads(data)

    def write_data(self, file_destination):
        s = json.dumps(self.data)
        with open(file_destination, 'w') as file:
            file.write(s)

    def modify_data(self, id, type, new_data):
        try:
            self.data[id][type] = new_data
        except KeyError:
            print('Key', id, 'do not exist!')

    def delete_data(self, id):
        try:
            del self.data[id]
        except KeyError:
            print('Key', id, 'do not exist!')

    def create_new_data(self, id, name, lastname):
        try:
            self.data[id] = {'name': name, 'lastname': lastname}
        except KeyError:
            print('Key', id, 'do not exist!')

    def show_data(self, id):
        try:
            print('Imie: ', self.data[id]['name'])
            print('Nazwisko: ', self.data[id]['lastname'])
        except KeyError:
            print('Key', id , 'do not exist!')

n = Note()
n.load_data('book.txt')
n.create_new_data('3', 'Maciej', 'Wrzeszcz')
print(n.data)
n.show_data('3')
n.delete_data('3')
n.show_data('3')
print(n.data)
n.write_data('book.txt')

