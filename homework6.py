from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    

class Name(Field):
        pass
           

class Phone(Field):
		pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    def add_phone (self, phone):
           self.phones.append = (Phone(phone))
    def remove_phone(self,phone):
            new_phones=[]
            for p in self.phones:
                  if p.value != phone:
                    new_phones.append(p)
            new_phones=self.phones 
                
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())

      


