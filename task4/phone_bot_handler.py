def input_error(func):
    """Decorator to handle input errors.""" 
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
        except KeyError as e:
            return str(e)
    return inner


@input_error
def add_contact(args: list, contacts: dict) -> str: 
    """  
    Adds a new contact or updates an existing one.  
    Args:  
        args (list): [name, phone]  
        contacts (dict): Dictionary of contacts.  
    Returns:  
        str: Success or error message.  
    """
    name, phone = args  
    contacts[name] = phone  
    return f"Contact '{name}' has been added or updated."
  

@input_error
def change_contact(args: list, contacts: dict) -> str:  
    """  
    Changes existing contact's phone number.  
    Args:  
        args (list): [name, new_phone]  
        contacts (dict): Dictionary of contacts.  
    Returns:  
        str: Success message or error if contact not found.  
    """
    name, phone = args
    if name not in contacts:  
        raise KeyError(f"Contact '{name}' not found.") 
    contacts[name] = phone  
    return f"Phone number for '{name}' has been successfully changed."
  

@input_error
def show_phone(args: list, contacts: dict) -> str:  
    """  
    Shows phone number for a contact.  
    Args:  
        args (list): [name]  
        contacts (dict): Dictionary of contacts.  
    Returns:  
        str: Phone number or not found message.  
    """
    name = args[0]  
    if name in contacts:  
        return f"Phone number for '{name}': {contacts[name]}"  
    else:  
        raise KeyError (f"Contact '{name}' not found.")    
    

def show_all_contacts(contacts: dict) -> str:  
    """  
    Returns a string with all contacts.  
    Args:  
        contacts (dict): Dictionary of contacts.  
    Returns:  
        str: List of all contacts.  
    """  
    if not contacts:  
        return "No contacts stored."  
    result_lines = ["All contacts:"]  
    for name, phone in contacts.items():  
        result_lines.append(f"{name}: {phone}")  
    return "\n".join(result_lines)   