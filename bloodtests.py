def interface(): 
    print("Blood Test Analysis")
    print("\nOptions")
    print("1 - HDL")
    print("9 - Quit") 
    
    choice = input("Enter an option:") 
    if choice == "9": 
        return 
    elif choice == "1": 
        HDL_driver()
            
            
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
    
interface()
