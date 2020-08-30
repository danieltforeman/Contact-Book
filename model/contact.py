class Contact:
    def __init__(self, first, last, primaryPhone, email, address, city, state, zip_code, secondaryPhone="N/A"):
        self.first_name = first
        self.last_name = last
        self.primary_phone = primaryPhone
        self.secondary_phone = secondaryPhone
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_address(self):
        return f"{self.address} {self.city}, {self.state} {self.zip_code}"

    def to_string(self):
        return f"{self.get_full_name()} | {self.primary_phone} | {self.secondary_phone} | {self.email} | {self.get_full_address()}"