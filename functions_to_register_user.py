"""
You are a junior developer working in a small start-up. Your managers have asked you to develop a new account registration system for a mobile app. 
The system must validate user input on the sign-up form before creating an account.

The previous junior developer wrote some helper functions that validate the name, email, and password. 
Use these functions to register users, store their data, and implement some error handling! These have been imported into the workspace for you.
They will be a great help to you when registering the user, 
but first you have to understand what the function does!
Inspect the docstrings of each of the helper functions: validate_name, validate_email and validate_password.
"""

# Re-run this cell and examine the docstring of each function
from python_functions import validate_name, validate_email, validate_password, top_level_domains

print("validate_name\n")
print(validate_name.__doc__)
print("--------------------\n")

print("validate_email\n")
print(validate_email.__doc__) 
print("--------------------\n")

print("validate_password\n")
print(validate_password.__doc__)

# The top level domains variable is used in validate_email to approve only certain email domains
print(top_level_domains)

# Start coding here
# Use as many cells as you need

def validate_user(name, email, password):
    """ Validate the user name, email and password.
    Args:
        name (string) : Name that we're attempting to validate.
        email (string) : Email address that we're attempting to validate.
        password (string) : Password that we're attempting to validate.

    Returns:
        bool : Returns True if all validation checks pass.
    Raises:
        ValueError : If any validation check fails.
    """
    if validate_name(name) == False:
        raise ValueError("Please make sure your name is greater than 2 characters!")

    if validate_email(email) == False:
       raise ValueError("Your email address is in the incorrect format, please enter a valid email.")

    if validate_password(password) == False:
       raise ValueError("Your password is too weak, ensure that your password is greater than 8 characters, and it should contains a capital letter and a number.")

    return True




def register_user (name, email, password):
    """ Attempt to register the user if they pass validation.
    
    Args:
        name (string): Name of the user.
        email (string): Email address of the user.
        password (string): Password of the user.
        
    Returns:
        dict or bool: Returns a dictionary with the user details if validation is succesful, or False if the validation fails
        
    """ 
    try:
        validate_user(name, email, password)
    except:
        return False

    user = {
        "name" : name,
        "email" : email,
        "password" : password
    }

    return user
    

register_user("Mar", "mar@gmail.com", "Password123")
