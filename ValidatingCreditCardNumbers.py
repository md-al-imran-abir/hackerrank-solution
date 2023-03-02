### This code provides correct answer in my machine
### But in HackerRank, I need to use single/double quoted string rather than tripple (""" """) quoted string.
### However, I am keeping this version, as it is more readable

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())

for i in range(1, N+1):
    crdt_card = input()
    
    # To check the last condition (i.e. no more than 3 repitition of a digit),
    # we will first remove all non digits character
    #(- can be between repititive digits, so this is to remove hyphens)
    wo_non_digit = re.sub(r"\D", "", crdt_card) #replace all non-digits character
    rep_pattern = r"(\d)\1{3,}" # checks if any digit has 4 or more repitions
    
    # The main pattern (16 digits, can be grouped into chunks of 4 digits seperated by hyphen)
    pattern = r"""
        ^[4-6]\d{3} #check if the 1st digit is 4,5, or, 6 and followed by three other digits
        -?\d{4}     # there can be - between every 4 digits. so check if 0 or 1 hyphen present followed by 4 digits
        -?\d{4}     # same as the last one
        -?\d{4}$    # same as the last one except it also checks if the string is ended (confirms there are only 16 digits)
    """

    if re.search(rep_pattern, wo_non_digit):
        # If there is any repition of 4 or more times of a digit, show invalid message, else check for other conditions
        print("Invalid")
    else:
        if re.match(pattern, crdt_card):
            # See if the main pattern matches or not.
            print("Valid")
        else:
            print("Invalid") 