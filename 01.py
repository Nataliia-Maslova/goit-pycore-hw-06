from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
       def __init__(self, value):
        super().__init__(value)

class Phone(Field):
            def __init__(self, value):
                  if not self.value.isdigit() and len(self.value) == 10:
                        raise ValueError("Phone must be 10 digits")
                  super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
          phone = Phone(phone_number)
          self.phones.append(phone)

    def remove_phone(self, phone_number):
          self.phones = [phone for phone in self.phones if phone.value != phone_number]

    def edit_phone(self, old_phone, new_phone):
          for phone in self.phones:
                if phone.value == old_phone:
                      phone.value = new_phone
                      return
                raise ValueError("Phone number is not found")
    
    def find_phone(self, phone_number):
          for phone in self.phones:
                if phone.value == phone_number:
                      return phone
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

                        
