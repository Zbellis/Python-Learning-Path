
def extract_email(email, message):


        
    error_message1 = "Your printer already has ink and you need to find the package"
    error_message2 = "I ordered more toner for you"

    
   

    split_email = email.split('@')
    
    full_name = split_email[0].split('.')
    
    first_name = full_name[0].capitalize()
    last_name = full_name[1].capitalize()



    if message == 1:        
        final_message = error_message1
    else:
        final_message = error_message2

    print("Hello {} {}, {}".format(first_name,last_name,final_message))


extract_email('zachary.ellis@ipaper.com', 1)



    
    





    




    
    
