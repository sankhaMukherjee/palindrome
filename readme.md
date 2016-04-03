# Longest Palindrome in a string

This is going to be a command line tool, much like other command line tools available on the Unix command line. The `src` folder contains the source files for the program. 

 - `.\src\pal.py`  --> This is the program that returns the longest palindrome within a string
 - `.\src\testPal.py` --> This is a nosetest. This fuction tests whether the palindrome function really returns the values that it should. 

## Running the program:

On your terminal, run the program as follows

`python pal.py [-vvv] [-h] A string that may contain the palindrome`

`-h` returns a help message on usage

`-v` turns on the verbose mode. You have several levels of verbose. You can turn on verbose level 2 by using the following option: `-vv`. Omit `-v` for quiet mode.

*Verbosity level*:

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

    3 ... = 2

## Caveats

 1. Some terminals interpret the input differently. For example, a `*` or a `;` on the `bash` terminal will be automatically converted into a list of files and command separators respectively.
 2. `argparse` is used for parsing arguments. This interprets such things as `(` diferently. 