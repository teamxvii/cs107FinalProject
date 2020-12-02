#!/usr/bin/env python3

from FADiff import FADiff as fd
import Elems as ef


# TODO: Debugging, etc. --
print(f'---- DEMOS / DEBUGGING / VERIFY CALCULATIONS ----\n')

print('Create input vars -->')
print(f'x = FADiff.new_scalar(2)')
x = fd.new_var(2, name='x')
print(f'y = FADiff.new_scalar(5)')
y = fd.new_var(5, name='y')
print(f'z = FADiff.new_scalar(3)')
z = fd.new_var(3, name='z')
print(f'x.val --> '                   
      f'{x.val}')              # Should be 2
print(f'x._der --> '           # '_der' is a dictionary containing the 
      f'{x._der}')             #   partial derivatives for a var
print(f'x.der --> '            # 'der' (no underscore) returns only the partial
      f'{x.der}')              #   derivatives wrt all parent inputs of a var
print(f'y.val --> '                  
      f'{y.val}')              # Should be 5
print(f'y.der --> '
      f'{y.der}')
print(f'z.val --> '                  
      f'{z.val}')              # Should be 3
print(f'z.der --> '
      f'{z.der}')

print(f'\ncheck = x * y + ef.sin(x)')
check = x * y + ef.sin(x)
print(f'check.val --> '
      f'{check.val}')                    # Should be 10.909...
print(f'check.der --> '
      f'{check.der}')
print(f'check.partial_der(x) --> '
      f'{check.partial_der(x)}')         # Should be 4.583...
print(f'check.partial_der(y) --> '  
      f'{check.partial_der(y)}')         # Should be 2

print(f'\ncheck = ef.sin(x + y)')
check = ef.sin(x + y)
print(f'check.val --> ' 
      f'{check.val}')                    # Should be 0.656...
print(f'check.der --> '
      f'{check.der}')
print(f'check.partial_der(x) --> '
      f'{check.partial_der(x)}')         # Should be 0.753...
print(f'check.partial_der(y) --> '
      f'{check.partial_der(y)}')         # Should be 0.753...

print(f'\ncheck = ef.sin(x * y)')
check = ef.sin(x * y)
print(f'check.val --> '
      f'{check.val}')                    # Should be -0.544..
print(f'check.der --> '
      f'{check.der}')
print(f'check.partial_der(x) --> '
      f'{check.partial_der(x)}')         # Should be -4.195...
print(f'check.partial_der(y) --> '
      f'{check.partial_der(y)}')         # Should be -1.678...

print(f'\ncheck = 8 * x')
check = 8 * x
print(f'check.val --> '
      f'{check.val}')                    # Should be 16
print(f'check.der --> '
      f'{check.der}')
print(f'check.partial_der(x) --> '
      f'{check.partial_der(x)}')         # Should be 8

print(f'\ncheck = 8 * y')
check = 8 * y
print(f'check.val --> '
      f'{check.val}')                    # Should be 40
print(f'check.der --> '
      f'{check.der}')
print(f'check.partial_der(y) --> '
      f'{check.partial_der(y)}')         # Should be 8

print(f'\ncheck = 8 + x')
check = 8 + x
print(f'check.val --> '
      f'{check.val}')                    # Should be 10
print(f'check.der --> '
      f'{check.der}')
print(f'check.partial_der(x) --> '
      f'{check.partial_der(x)}')         # Should be 1

print(f'\ncheck = 8 + y')
check = 8 + y
print(f'check.val --> '
      f'{check.val}')                    # Should be 13
print(f'check.der --> '
      f'{check.der}')
print(f'check.partial_der(y) --> '
      f'{check.partial_der(y)}')         # Should be 1

print(f'\ncheck = x * y + ef.sin(x) + z')  # Check that uses three input vars
check = x * y + ef.sin(x) + z
print(f'check.val --> '
      f'{check.val}')                    # Should be 13.909...
print(f'check.der --> '
      f'{check.der}')
print(f'check.partial_der(x) --> '
      f'{check.partial_der(x)}')         # Should be 4.583...
print(f'check.partial_der(y) --> '  
      f'{check.partial_der(y)}')         # Should be 2
print(f'check.partial_der(z) --> '  
      f'{check.partial_der(z)}')         # Should be 1

print(f'\nx1 = fd.new_var(2)\n'
      f'x2 = fd.new_var(3)\n'
      f'check = x1 * x2 + x1')
x1 = fd.new_var(2)
x2 = fd.new_var(3)
check = x1 * x2 + x1
print(f'check.val --> '
      f'{check.val}')                    # Should be 8
print(f'check.der --> '
      f'{check.der}')                    # Should be [4, 2]

# TODO: VECTOR DEBUGGING --

# i = x * y + ef.sin(x) + z
# j = x * y
#
# print('check = i + j')
# check = i + j
# print(f'check.val -->\n'
#       f'{check.val}')
# print(f'check.der -->\n'
#       f'{check.der}')
# print(f'check.partial_der(x) -->\n'
#       f'{check.partial_der(x)}')
# print(f'check.partial_der(y) -->\n'
#       f'{check.partial_der(y)}')
# print(f'check.partial_der(z) -->\n'
#       f'{check.partial_der(z)}')
