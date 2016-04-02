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
        Thsi function is used for finding the biggest
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
       
 
        for j in range(2, min( len(string)-i, i )):
            # print string[i-j+1: i+j+1]
            if string[i-j+1] != string[i+j]:
                break
            else:
                if len(bigPals) < len(string[i-j+1: i+j+1]):
                    bigPals = string[i-j+1: i+j+1]
 
    return bigPals


if __name__ == '__main__':
 
    inp = inputString()
    print inp
    print
    print findPalindrome2(inp)
 
    print 'done'


