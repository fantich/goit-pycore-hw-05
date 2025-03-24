from storage import contacts
from decorators import input_error

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Enter the argument for the command"
        except IndexError:
            return "Enter the argument for the command"
    return inner

@input_error
def hello(_):
    return "How can I help you?"

@input_error
def add_contact(args):
    if not args:
        raise ValueError
    name, phone = args.split(maxsplit=1)
    contacts[name.lower()] = phone
    return "Contact added."

@input_error
def change_contact(args):
    if not args:
        raise ValueError
    name, phone = args.split(maxsplit=1)
    if name.lower() in contacts:
        contacts[name.lower()] = phone
        return "Contact updated."
    return "Contact not found."

@input_error
def get_phone(args):
    if not args:
        raise ValueError
    name = args.strip().lower()
    return contacts[name]

@input_error
def all_contacts(_):
    if contacts:
        return "\n".join(f"{name.capitalize()}: {phone}" for name, phone in contacts.items())
    return "No contacts found."

@input_error
def process_command(user_input):
    command, *args = user_input.split(maxsplit=1)
    args = args[0] if args else ""

    commands = {
        "hello": hello,
        "add": add_contact,
        "change": change_contact,
        "phone": get_phone,
        "all": all_contacts,
    }
    
    if command in commands:
        return commands[command](args)
    return "Unknown command"