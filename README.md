# imapgmail
Accessing your mail content through imaplib in python

This is a tutorial to access your email through a terminal using imaplib library in Python3.x.


For convenience's sake, we're using gmail.

First we import our required libraries: imaplib to access your mail account, email to process email objects which you will extract and finally getpass as a secure way to enter passwords on the terminal.

You can also import pandas if you want to store your data as a dataframe in case you want to use it for NLP, but that's optional, suit yourself.


We start by taking user inputs for email and password(use getpass.getpass() for this) and initialize our mail client(imap.gmail.com in this case).

We will then create an imaplib object, which will be used for all our functions regarding info extraction from your mail client.

You can then use this object to login to your email using the info we got earlier, and choose your mail label using the select function.

Then comes our search query. This is used as a criteria to extract mails from your selected label.

The search query returns info about the emails that satisfy your criteria, not the actual emails. This info is present in the [0] index of the object returned. It's a space separated string so you can use the split() method to get the individual mails.

Then you can use the fetch() function to fetch the actual mails from your mail client. The second parameter (RFC822) stands for the entire mail, but you can simply fetch parts of the mail you need as well.

The returned object's [0][1] string will be your data, which you can convert into a mail message object using the email.message_from_string() method. This message object now has the various parts of the mail, such as Subject, From, To, Body, etc. you can access these similar to how you access a dictionary.
