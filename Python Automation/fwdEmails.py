# This file is modified from the orignal code used at International Paper for confidentiality of the company's B2B partner's email addresses.

# A faster way to copy and paste Email Addresses and send to outlook

import pyperclip

send_to_location = int(input("1 to send to group 1 or any key for group 2: "))

if send_to_location == 1:
    group1 = "user1; user2...10;"
    pyperclip.copy(group1)
    pyperclip.paste()
else:
    group2 = "player1; player2...10"
    pyperclip.copy(group2)
    pyperclip.paste()

