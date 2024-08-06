from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    

class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not self._is_valid_phone(value):
            raise ValueError("Invalid phone number. It must be exactly 10 digits.")
        super().__init__(value)
    
    def _is_valid_phone(self, value):
        return value.isdigit() and len(value) == 10


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]
    
    def edit_phone(self, old_phone, new_phone):
        if not Phone._is_valid_phone(self, old_phone) or not Phone._is_valid_phone(self, new_phone):
            raise ValueError("Both old and new phone numbers must be valid 10-digit numbers.")
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return
        raise ValueError("Old phone number not found.")
    
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
    
    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())





      




      


