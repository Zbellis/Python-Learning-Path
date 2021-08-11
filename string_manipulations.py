

def create_errorMessage():
    build_error_message1 = input("Copy order number and date: ")
    serial_number = input("Enter serial number: ")

    full_error_message = ("""I have placed an order for you in the HP website, DCC\n
    {}.
    There is no tracking shipment yet, however your toner-cartridge(s) will arrive in 1-2 business days\n
    When it arrives, please place the toner-cartridges in the device with Serial Number: {}.\n
    Thanks in advance,""".format(build_error_message1, serial_number))

    return full_error_message


def extract_email(email):


        
    error_message1 = "Your printer already has ink and you need to find the package"
    error_message2 = "I ordered more toner for you"

    
   

    split_email = email.split('@')
    
    full_name = split_email[0].split('.')
    
    first_name = full_name[0].capitalize()
    last_name = full_name[1].capitalize()

    message = create_errorMessage()
    errorMessageType = input("Enter the type of error message: ")
    
    if  errorMessageType == "1":        
        final_message = error_message1
    else:
        final_message = error_message2

    print("Hello {} {}, {}. {}".format(first_name,last_name,final_message,message))
    

extract_email('zachary.ellis@ipaper.com')
    










    




    
    
