with open("contacts_sample.txt", "r") as fh:
    
    contacts = (list(fh))
    
    for line in range(0, len(contacts)):
        contact_info = contacts[line].split(", ")
    
        name = contact_info[0]
        tel = contact_info[1]
    
        print(f" * .....Name: {name}\n * Telephone: {tel}", end="")
        if line < len(contacts) - 1:
            print()
        