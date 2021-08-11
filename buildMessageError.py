build_error_message1 = input("Copy order number and date: ")
serial_number = input("Enter serial number: ")


full_error_message = ("""Hello Name\n
I have placed an order for you in the HP website, DCC\n
{}.\n
There is no tracking shipment yet, however your toner-cartridge(s) will arrive in 1-2 business days\n
When it arrives, please place the toner-cartridges in the device with Serial Number: {}.\n
Thanks in advance,""".format(build_error_message1, serial_number))

print(full_error_message)
