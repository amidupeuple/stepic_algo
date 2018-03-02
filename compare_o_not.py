from sympy import *

def l_rule(t, g, n):
    '''
        this function compare two fucntions and 
        return human readable result to the console
    '''
    res = str(limit(t/g, n, oo))
    if res == '0':
        return str(t) + ' имеет меньший порядок роста, чем ' + str(g)
    elif res == 'oo':
        return str(t) + ' имеет больший порядок роста, чем ' + str(g)
    else:
        return str(t) + ' имеет тот же порядок роста, что и ' + str(g)

        
def compare_functions(f1, f2):        
    res = str(limit(f1/f2, n, oo))
    if res == '0':
        return -1
    elif res == 'oo':
        return 1
    else:
        return 0
        
        
def rate_functions(funcs):
    '''
        sort functions by speed of growth in ascending order.
        input - array of functions
        outpu - sorted array of functions
    '''
    flag = True
    while flag:
        flag = False
        for i in range(len(funcs)-1):
            if compare_functions(funcs[i], funcs[i+1]) == 1:
                tmp = funcs[i]
                funcs[i] = funcs[i+1]
                funcs[i+1] = tmp
            if i > 0:
                if compare_functions(funcs[i-1], funcs[i]) == 1:
                    flag = True
    return funcs

n = Symbol('n')

'''funcs = {
    n**2 : 3 ** log(n)
}'''
funcs = [n**(n**0.5), 2**2**n]
#funcs = [n**0.5, (log(n))**0.5, log(log(n)), log(n), (log(n))**2]
print(funcs)
print(rate_functions(funcs))

#http://www.wolframalpha.com/input/?i=x!+%3D+2%5Ex
'''for func1, func2 in funcs.items():
    print(l_rule(func1, func2, n))'''