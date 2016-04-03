import unittest
import random
import pal as tP

# The list is obtained from 
# http://www.palindromelist.net

def generateRandomString():
    return ''.join([  chr(65+int(random.uniform(1, 25)))  for i in range(int( random.uniform(5, 10) ))])

def padString(string):
    s1 = generateRandomString()
    s2 = generateRandomString()
    
    # break the generation of incidental palindromes
    if s1[-1] == s2[0]:
        s2 =  chr(ord(s1[-1])+1) + chr(ord(s1[-1])-1) + s2

    return  s1 + string + s2

def get10Strings(string):
    return [  padString(string) for i in range(10) ]

def generatePalTuples():
    palindromeList = '''A but tuba.
    A car, a man, a maraca.
    A dog, a plan, a canal: pagoda.
    A dog! A panic in a pagoda!
    A lad named E. Mandala
    A man, a plan, a canal: Panama.
    A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!
    A new order began, a more Roman age bred Rowena.
    A nut for a jar of tuna.
    A Santa at Nasa.
    A Santa dog lived as a devil God at NASA.
    A slut nixes sex in Tulsa.
    A tin mug for a jar of gum, Nita.
    A Toyota! Race fast, safe car! A Toyota!
    A Toyota's a Toyota.
    Able was I ere I saw Elba.
    Acrobats stab orca.
    Aerate pet area.
    Ah, Satan sees Natasha!
    Air an aria.
    Al lets Della call Ed Stella.
    Amen icy cinema.
    Amore, Roma.
    Amy, must I jujitsu my ma?
    Animal loots foliated detail of stool lamina.
    Anne, I vote more cars race Rome to Vienna.
    Are Mac 'n' Oliver ever evil on camera?
    Are we not drawn onward to new era?
    Are we not drawn onward, we few, drawn onward to new era?
    Are we not pure? "No sir!" Panama's moody Noriega brags. "It is garbage!" Irony dooms a man; a prisoner up to new era.
    Art, name no tub time. Emit but one mantra.
    As I pee, sir, I see Pisa!'''

    palindromeList = palindromeList.split('\n')
    greatList   = []
    palindromes = []

    for p in palindromeList:
        greatList.append(p)
        greatList += get10Strings(p)

        p1 = filter( str.isalpha, p.lower() )
        palindromes += [p1]*11

    greatList = [filter(str.isalpha, g.lower()) for g in greatList]

    return zip(palindromes, greatList)

class TestPal(unittest.TestCase):

    def testPalindrome(self):
        '''
            This function feeds a bunch of different strings 
            to the palindrome function to check if the function
            returns the right value of the palindrome or not 
        '''

        pss = generatePalTuples()
        for ps in pss:
            # print '-----------------'
            # print  tP.findPalindrome(ps[1])
            # print '-----------------'
            # print ps[0], ps[1]
            # print 
            self.assertEqual( tP.findPalindrome(ps[1]), ps[0] )

        return

if __name__ == '__main__':
    unittest.main()




