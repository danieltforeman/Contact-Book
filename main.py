from view.contactUI import ContactUI

myContactUI = ContactUI()
try:
    myContactUI.run()
except ValueError:
    print("Please enter a valid number")
    myContactUI.run()