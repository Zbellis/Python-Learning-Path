# A faster way to copy and paste Email Addresses and send to outlook

import pyperclip

send_to_location = int(input("1 to send to USA or any key for Mexico: "))

if send_to_location == 1:
    usa = "ingrid.alvarado@hp.com; angelica.arriaga1@hp.com; suriel.deleon@hp.com; michael.mack@hp.com; george.doukas@hp.com;"
    pyperclip.copy(usa)
    pyperclip.paste()
else:
    mexico = "silvana.pulido@hp.com; michael.mack@hp.com"
    pyperclip.copy(mexico)
    pyperclip.paste()

