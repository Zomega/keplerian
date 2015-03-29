# This file allows for easy procedural creation of constructors.
# For now, this is effectively accomplished through forward chaining. In the future, it might be prudent to make decorators to crystallize this data on program load for speed / to avoid the computational pitfalls of chaining.

# The rules MUST have properly named arguments. Existing quantities will be passed in with kwargs.
  
def compute( desired, rules, givens ):
    # For now, brute force forward chain.
    # Later on, we can do fancy path stuff.
    results = givens # TODO: Copy?
    
    untouched = False # Make sure we go around at least once.
    while not untouched:
        # Check if we can terminate
        if desired.issubset( results.keys() ):
            return results
        
        untouched = True
        for quantity in rules:
            if quantity in results:
                continue
            for pre, f in rules[quantity]:
                if pre.issubset( results.keys() ):
                    results[quantity] = f(**results) # TODO: Allow Specifc Excptions here -- i.e. computational path failed.
                    untouched = False
                    break
    raise NoSolutionError() # TODO


###
# A simple nonsense example.
#
#  a = b + c
#  c = sqrt( b )
#  d = a b c
#
###
if __name__ == '__main__':
    from math import sqrt

    def f_bc_a( b, c ):
        return b + c
        
    def f_b_c( b ):
        return sqrt( b )
        
    def f_abc_d( a, b, c ):
        return a*b*c
        
    rules = {
        'a' : [ ({'b', 'c'}, f_bc_a) ],
        'b' : [ ],
        'c' : [ ({'b'}, f_b_c) ],
        'd' : [ ({'a','b','c'}, f_abc_d) ] }
        
    desired = {'a', 'c'}
    givens = {'b' : 5.0}

    result = compute( desired, rules, givens )
    print result
    for x in desired:
        print x, " = ", result[ x ]
