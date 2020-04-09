'''
Progrmam will check if entered brackets are symetric. Using Stack.
'''

def stack_test():
    char_dict = {0:"[",1:'{',2:'(',3:']',4:'}',5:")"}
    invalue = ""
    check = False
    condition = 0
    position_dictionary = {'[':']','{':'}','(':')'}
    
    
    while len(invalue) < 2 or check == False or len(invalue)%2 !=0 :
        value_list = []
        invalue = input("Enter value to check (minimum two chars):")
        for char in invalue:
            if char in char_dict.values():
                check = True
                value_list.append(char)
            else:
                check = False
                print(f'Dictionary don\'t support char: {char}')
        if len(invalue) != len(value_list):
            check = False
            print("You can enter:",*char_dict.values())
            print("The number of characters entered must be even")

    
    if check == True:
        for char in value_list:
            
            if position_dictionary[char] == value_list.pop():
                condition += 1
    
    if check == True and condition == len(invalue)/2 :
        print("Entered value is symetric in the middle")
    else:
         print("Entered value is not symetric in the middle")
        
                