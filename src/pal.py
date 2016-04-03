import sys
import argparse 

helpString = '''
usage: pal.py [-h] [-v] string [string ...]

positional arguments:
  string         The string to search a palindrome in

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  provide detailed program output
'''

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

        Edit: 
        In this version of the input, we are going to add 
        optinal arguments parsing using argparse. We shall
        have the following arguments:

            -h and --help: with argparse, we get it for free
            -v and --verbose: will show detailed program execution

        Verbosity level:

            0 = quiet output
                given an empty string, it will return an error 
                   this is the default behavior of the `argparse`
                   library and is not a default behavior of the program
                given a string with no palindromes in it, it will 
                return the first character of the string

            1 = print semantics such as the input string and that
                the string has no palindrome etc. It will also
                identify the location of the palindrome within the 
                string.

            2 = This is going to give detailed program execution output.  


    '''
 
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', 
        help    = 'provide detailed program output',
        action  = 'count',
        default = 0)
    parser.add_argument('string', 
        help = 'The string to search a palindrome in',
        nargs='+')

    args = parser.parse_args()
    string = ''.join(args.string)
    string = filter(str.isalpha, string.lower())

    return { 
        'string': string,
        'verbose': args.verbose
    }

def findPalindrome2(string, verbose=0):
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

    if verbose > 1:
        print '\t\tSearching for the longest even palindrome'

 
    bigPals = ''
    for i in range(len(string)-1):
        if string[i] != string[i+1]: continue

        if verbose > 1:
            print '\t\t\tInitial match found: ', string[i:i+1+1]

 
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

            if verbose > 1:
                print '\t\t\t\tNew match:', string[i-j+1: i+j+1]

    if bigPals == '': return None

    return bigPals

def findPalindrome3(string, verbose=0):
    '''
        This function finds the biggest palindrome
        in a string by starting with groupings of 3
    '''

    if len(string) < 3: return None

    if verbose > 1:
        print '\t\tSearching for the longest odd palindrome'

    bigPals = ''
    for i in range(1, len(string)-2):
        if string[i-1] != string[i+1]: continue

        if verbose > 1:
            print '\t\t\tInitial match found: ', string[i-1:i+1+1]


        # We are in palindrome territory ...
        if len(string[i-1:i+1+1]) > len(bigPals): bigPals = string[i-1:i+1+1]
        # print string[i-1:i+1+1]
        for j in range(2, len(string)):
            if i-j < 0: break
            if i+j >= len(string): break
            if string[i-j] != string[i+j]: break
            if len(string[i-j:i+j+1]) > len(bigPals): bigPals = string[i-j:i+j+1]

            if verbose > 1:
                print '\t\t\t\tNew match:', string[i-j:i+j+1]

    if bigPals == '': return None
    return bigPals

def findPalindrome(string, verbose=0):

    s  = None 
    s2 = findPalindrome2(string, verbose)
    s3 = findPalindrome3(string, verbose)

    if verbose > 1:
        if s2 is not None:
            print '\tLongest even palindrome: ', s2
        else:
            print '\tEven palindromes not present'

    if verbose > 1:
        if s3 is not None:
            print '\tLongest odd palindrome: ', s3
        else:
            print '\tOdd palindromes not present'


    s = s2 if s2 is not None else None
    s = s3 if s3 is not None and \
            ( (s is None)    or  \
              (s is not None and len(s3)>len(s))) \
            else s

    if verbose > 1:
        if s is not None:
            print '\tLongest palindrome selected: ', s
        else:
            print '\tPalindrome not present'

    return s

if __name__ == '__main__':
 
    inpDict = inputString()
    inp     = inpDict['string']
    verbose = inpDict['verbose']

    if verbose > 0:
        print 'Input String: [%s]'%inp 

    if verbose > 1:
        print 'Finding the palindrome within the string ...'
    pal = findPalindrome(inp, verbose)

    if pal is None:
        if verbose > 0:
            print 'A real palindrome isn`t present. Please consider [%s] to be a palindrome ...'%inp[0]
        else:
            print inp[0]
    else:
        if verbose > 0:
            print 'Palindrome found: [%s]'%pal
            print 'Palindrome within the string:', ('['+pal+']').join( inp.split(pal) )
        else:
            print inp[0]

 
