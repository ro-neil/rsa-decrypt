
'''An RSA Decrypter'''


import math
import time
import sys


def isWhole(value):
    """Determines if a given value is a whole number"""        
    try:
        if value > 0:    
            '''Compares the difference between a value an its integer representation'''
            difference = (value - int(value))
            return difference == 0
    except Exception:
        return False

class Prime:

    @staticmethod
    def isPrime(value):
        '''Determines whether a given input is a prime number'''

        if value == 0: return False

        counter = 2     # increments to determine a possible factor of {x}
        threshold = int(value/2)    # limits the iterations of the while loop
        while counter < threshold:
            if value % counter == 0: return False   # if {counter} is a factor of {value}
            else:
                counter += 1
                threshold = int(value/counter)  # reduce the threshold to avoid unnecessary computation
        return True
        
    @staticmethod
    def findFactors(value):
        '''Determines two(2) prime factors of a given input'''
        firstFactor = 0
        factors = list()    # for storing both prime factors
        counter = 2     # increments to determine a possible factor of {x}
        threshold = int(value/2)    # limits the iterations of the while loop
        while counter < threshold:
            if Prime.isPrime(counter) and value % counter == 0:   # if {counter} is prime and is also a factor of {value}
                firstFactor = counter   # the first found prime factor
                '''Append the first prime factor to the list of {factors}, then terminate the loop'''
                factors.append(firstFactor)
                break
            else:
                counter += 1
                threshold = int(value/counter)  # reduce the threshold to avoid unnecessary computation
        
        if firstFactor != 0:   # check to ensure that a first prime factor exists 
            secondFactor = int(value/firstFactor)    # second prime factor found by dividing the {value} by {firstFactor}
            if (secondFactor % 2) == 0:    # if the second factor is even then it is not prime
                return []
            factors.append(secondFactor)    # append second prime factor to the list of {factors}
        return factors

    @staticmethod
    def printFactors(value):
        factors = Prime.findFactors(value)
        print(value,'=',factors[0],'*',factors[1])   


class RSA:

    @staticmethod
    def phi_n(p,q):
        return (p-1)*(q-1)

    @staticmethod
    def find_d(phi_of_n,e):
        k = 0
        d = (k * phi_of_n + 1) / e
        d_lst = []    # a list for storing all possible values of 'd' given 'k'
        while d < phi_of_n:
            if isWhole(d): # if d is an integer, append to list of d's
                d_lst.append(int(d))
            k += 1
            d = (k * phi_of_n + 1) / e
        return d_lst

    @staticmethod
    def find_m(c,d,n):
        return (c**d) % n

    @staticmethod
    def decrypt(c,e,n):
        factors = Prime.findFactors(n)
        if factors: # if valid factors were found
            p = factors[0]
            q = factors[1]
            # msg = 'Given the tuple ({}, {}, {}).\n'.format(c,e,n)
            # msg += 'Where n = {}; '.format(n)
            # msg += 'by way of trial and error, the prime factors of '
            # msg += '{} and {} were deduced.\n'.format(p, q)
            phi_of_n = RSA.phi_n(p, q)
            # msg += '{}(n) = (p-1)(q-1) was then computed to be {}*{} = {}.\n'.format(chr(248),p,q,phi_of_n)
            d_list = RSA.find_d(phi_of_n,e)
            
            '''If no values for d could be determines'''
            if d_list == []:
                return "Invalid combination of values"
                
            # msg += 'Using e = {}, '.format(e)
            # msg += 'd = ( (k * {}(n) + 1) / e ) was then determined by '.format(chr(248))
            # msg += 'selecting "k", such that "d" is an integer < {}(n).\n'.format(chr(248))
            # msg += "An exhaustive search for k's was then conducted "
            # msg += 'where all possible values of "d" were subsequently recorded.\n'
            # msg += 'The set of values for "d" is as follows: '
            # msg_list = []   # stores a list of possible messages if multiple values of d are found
            # for d in d_list:
            #     if len(d_list) == 1: 
            #         msg += '{}'.format(d)   # specific formatting for a single value
            #     else:
            #         if d_list[-1] != d:
            #             msg += '{}, '.format(d)     # specific formatting for values in between
            #         else:
            #             msg += 'and {}.'.format(d)  # specific formatting the final value  
            #     msg_list.append(RSA.find_m(c,d,n))
            
            # msg += '\nUsing the formula, m = c^d mod n, where c = {}; the following message(s) were decrypted: '.format(c)
            
            # for m in msg_list:
            #     if len(msg_list) == 1: 
            #         msg += '{}\n'.format(m)   # specific formatting for a single value
            #     else:
            #         if msg_list[-1] != m:
            #             msg += '{}, '.format(m)     # specific formatting for values in between
            #         else:
            #             msg += 'and {}\n'.format(m)  # specific formatting the final value
            results = {
                'c': c,
                'e': e,
                'n': n,
                'p': p,
                'q': q,
                'phi-of-n': phi_of_n,
                'd': d_list[0],
                'm': RSA.find_m(c,d_list[0],n)
            }
            return results
        return '"n" is invalid'



if __name__ == "__main__":

    lst = []
    # lst.append(RSA.decrypt(1407,17,2173))
    # lst.append(RSA.decrypt(129,31,377))
    # lst.append(RSA.decrypt(196,61,1067))
    #lst.append(RSA.decrypt(1648,4,2117))

    for solution in lst:
        print(solution)

    print(Prime.findFactors(9783372036854777731))
        

