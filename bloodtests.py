def interface(): 
    print("Blood Test Analysis")
    while True: 
        print("\nOptions") 
        print("9 - Quit") 
        choice = input("Enter an option:") 
        if choice == "9": 
            return 
            
            
def HDL_driver(): 
    # Get data 
    HDL_level = int(input("Enter HDL level:"))
    # Analyze the data
    if HDL_level >= 60: 
        print("HDL level is normal") 
    elif HDL_level < 60: 
        if HDL_level > 40: 
            print("HDL level is borderline low") 
        else: 
            print("HDL level is low")    
    # Output the data 
    return 
    
#interface()
HDL_driver()