# ========================================================= OOP EMAIL PROGRAM =========================================================#

# Define email class
# Initiate constructor function using from_address and email_contents as parameters
# Set read and spam values as False when first opening inbox

# ========================================================= CLASS =========================================================#

class Email:

    def __init__(self, from_address, email_contents):
        self.from_address = from_address
        self.email_contents = email_contents
        self.has_been_read = False
        self.is_spam = False

# Define method to mark_as_read and mark_as_spam as True

    def mark_as_read(self):
        self.has_been_read = True
    
    def mark_as_spam(self):
        self.is_spam = True

# ========================================================= FUNCTIONS =========================================================#

# Set an empty inbox variable for all mails to be stored in

inbox = []
spambox= []
unreadbox = []

# Define a function that adds new mail to the inbox ==> in this case is used with the 'send' option as per task instruction
# Add the new message as a new Email object and append it to inbox[]
# This will reflect on inbox count 
# Set functions for counting spam and unread

def add_email(from_address, email_contents):
    add_message = Email(from_address, email_contents)
    inbox.append(add_message)

def get_count(inbox):
    return len(inbox)

def get_count_spam(spambox):
    return len(spambox)

def get_count_unread(unreadbox):
    return len(unreadbox)

# Set a function that pulls the email the user has selected from the index
# Use the enumerate function to index each mail
# Print using format

def get_email(index):
    get_message = inbox[index]
    for i, email in enumerate(inbox):
        print("-------------------------------------------")
        print(f'''\nFrom\n\n{get_message.from_address}\nContents\n\n{get_message.email_contents}''')
        print("-------------------------------------------")
        return inbox

# Set a function that pulls unread emails
# Use the enumerate function to index each mail
# If the mail has an attribute of not being read, append to unread inbox
# Print using format

def get_unread_emails():
    unread = []
    for i , email in enumerate(inbox):
        if not email.has_been_read:
            un_email = inbox[i]
            unread.append(un_email)
            unreadbox.append(unread)
            print(f"{i + 1}. From {un_email.from_address} Contents {un_email.email_contents}")
    return unread

# Set a function that pulls spam emails
# Use the enumerate function to index each mail
# If the mail has an attribute of being spam, append to spam inbox
# Print using format

def get_spam_emails():
    spam =[]
    for i, email in enumerate(inbox):
        if email.is_spam:
            get_spam = inbox[i]
            spam.append(get_spam)
            spambox.append(spam)
            print(f"{i + 1}. From {get_spam.from_address} Contents {get_spam.email_contents}")
    return spam

# Set a function that allows user to select indexed mail to spam
# Mark as spam

def add_spam(index):
    add_user_spam = inbox[index]
    add_user_spam.mark_as_spam()
    print("\nEmail added to spam\n")
    print("\nPlease select another option from the menu\n")

# Set a function that allows user to select indexed mail to mark as read
# Mark as read

def mark_read(index):
    read_message = inbox[index]
    read_message.mark_as_read()
    print("\nEmail marked as read")
    print("\nPlease select another option from the menu\n")

# Set a function that allows user to select indexed mail to delete
# Using try-except in case there is an error whilst deleting
# Delete using remove() function

def delete(index):
    try:
        inbox.remove(inbox[index])
        print("\nEmail deleted\n")
        print("\nPlease select another option from the menu\n")
    except:
        print("\nSorry email could not be deleted\n")
        print("\nPlease select another option from the menu\n")

# ========================================================= OOP EMAIL PROGRAM =========================================================#

# Print output menu and mailbox

print(input('''\n==============================WELCOME TO HYPERIONDEV MAILBOX==============================\n
                            Please push enter to continue'''))

user_choice = ""

# Using a loop for each menu selection as well as lower() to avoid errors

while user_choice != "quit":

    user_choice = input('''\nWhat would you like to do:
                            read
                            mark spam
                            send
                            delete
                            quit\n\n''').lower()

# If user_choice is read, prompt accordingly
# Get index from user to mark as read
# Minus 1 from selection because of indexing 

    if user_choice == "read":
        print(f"\nINBOX {get_count(inbox)}\n")
        get_unread_emails()
        num = int(input("\nPlease select the index you would like to mark as read:\n\n")) 
        get_email(num-1)
        mark_read(num-1)

# If user_choice is mark as spam, prompt accordingly
# Get index from user to mark as spam
# Minus 1 from selection because of indexing 
# Print spam emails

    elif user_choice == "mark spam":
        print(f"\nSPAM {get_count_spam(spambox)}\n")
        get_unread_emails()
        user_mark_spam = int(input("\nPlease select the index you would like to mark as spam:\n\n"))
        get_email(user_mark_spam-1)
        add_spam(user_mark_spam-1)
        get_spam_emails()

# If user_choice is send, prompt accordingly
# Get from_address and email_contents from user

    elif user_choice == "send":
        from_address = input("\nPlease enter your email address:\n\n")
        email_contents = input("\nPlease type out your email:\n\n")
        add_email(from_address, email_contents)

# If user_choice is delete, prompt accordingly
# Get index from user to mark as spam
# Minus 1 from selection because of indexing 

    elif user_choice == "delete":
        get_unread_emails()
        user_delete = int(input("\nPlease enter the index you would like to delete:\n"))
        delete(user_delete-1)

# If user_choice is quit, say goodbye

    elif user_choice == "quit":
        print("Goodbye")

# Else , in case of typos, prompt accordingly

    else:
        print("Oops - incorrect input")

# ========================================================= END OF EMAIL PROGRAM =========================================================#