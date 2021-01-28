def interface(): 
    print("Blood Test Analysis")
    print("\nOptions")
    print("1 - HDL")
    print("9 - Quit") 
    print("2 - LDL")
    
    choice = input("Enter an option:") 
    if choice == "9": 
        return 
    elif choice == "1": 
        HDL_driver()
    elif choice == "2": 
        LDL_driver()
            
            
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

def LDL_driver(): 
    # Get data 
    LDL_level = int(input("Enter LDL level:"))
    # Analyze the data
    if LDL_level < 130: 
        print("LDL level is normal") 
    elif 130 <= LDL_level < 159:
        print("LDL level is borderline high") 
    else: 
        print("LDL level is HIGH")    
    # Output the data 
    return 

interface()
