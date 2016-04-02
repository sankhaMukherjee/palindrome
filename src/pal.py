import sys

def inputString():
    '''
        This function takes the arguments provided to the program
        and returns the rest of the string. 
 
        It automatically removes spaces, all non-alphabetic
        characters, and converts the entire string to lower
        case. The assumption is that the palindrome is formed
        within a long string even when there are other special 
        characters present. We just neglect the special characters.

        We may need to change this functionallity later ...

    '''
 
    string = ''.join(sys.argv[1:]).lower()
    string = filter( str.isalpha, string )
    return string

def findPalindrome2(string):
    '''
        This function is used for finding the biggest
        palindrome within a string. It does a grouping
        by 2 ...
    '''
 
    if len(string) == 1: return None
    if len(string) == 2:
        if string[0]==string[1]:
            return string
        else:
            return None
 
    bigPals = ''
    for i in range(len(string)-1):
        if string[i] != string[i+1]: continue
 
        # ok, lets start adding the palindromes ...
        if len(bigPals) < len(string[i:i+2]):
            bigPals = string[i:i+2]
       

        # print  i, len(string)-i, i+1
 
        for j in range(1, len(string)):

            if i-j+1 < 0 : break
            if i+j >= len(string): break

            if string[i-j+1] != string[i+j]:
                break
            else:
                if len(bigPals) < len(string[i-j+1: i+j+1]):
                    bigPals = string[i-j+1: i+j+1]

    if bigPals == '': return None

    return bigPals

def findPalindrome3(string):
    '''
        This function finds the biggest palindrome
        in a string by starting with groupings of 3
    '''

    if len(string) < 3: return None

    bigPals = ''
    for i in range(1, len(string)-2):
        if string[i-1] != string[i+1]: continue

        # We are in palindrome territory ...
        if len(string[i-1:i+1+1]) > bigPals: bigPals = string[i-1:i+1+1]
        # print string[i-1:i+1+1]
        for j in range(2, len(string)):
            if i-j < 0: break
            if i+j >= len(string): break
            if string[i-j] != string[i+j]: break
            if len(string[i-j:i+j+1]) > len(bigPals): bigPals = string[i-j:i+j+1]
            # print string[i-j], string[i+j], string[i-j:i+j+1]

    if bigPals == '': return None
    return bigPals


if __name__ == '__main__':
 
    inp = inputString()
    print zip(inp, range(len(inp)))
    
    print 'Finding for 2'
    print findPalindrome2(inp)

    print 'Finding for 3'
    print findPalindrome3(inp)

 
    print 'done'


