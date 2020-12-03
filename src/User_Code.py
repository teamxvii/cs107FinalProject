#!/usr/bin/env python3

from FADiff import FADiff as fd    # User needs to import
import Elems as ef                 # User needs to import
import numpy as np


# TODO: Debugging, etc. --
print(f'---- DEMOS / DEBUGGING / VERIFY CALCULATIONS ----\n')

print('Create input vars -->')
print(f'x = FADiff.new_scal(2)')
x = fd.new_scal(2, name='x')
print(f'y = FADiff.new_scal(5)')
y = fd.new_scal(5, name='y')
print(f'z = FADiff.new_scal(3)')
z = fd.new_scal(3, name='z')
print(f'x.val --> '                   
      f'{x.val}')              # Should be [2]
print(f'x._der --> '           # '_der' is a dictionary containing the 
      f'{x._der}')             #   partial derivatives for a var
print(f'x.der --> '            # 'der' (no underscore) returns only the partial
      f'{x.der}')              #   derivatives involved in the calculation
print(f'y.val --> '                  
      f'{y.val}')              # Should be [5]
print(f'y.der --> '
      f'{y.der}')              # Should be [1]
print(f'z.val --> '                  
      f'{z.val}')              # Should be [3]
print(f'z.der --> '
      f'{z.der}')              # Should be [1]

print(f'\ncheck = x * y + ef.sin(x)')
check = x * y + ef.sin(x)
print(f'check.val --> '
      f'{check.val}')                    # Should be [10.909...]
print(f'check.der --> '
      f'{check.der}')                 # Should be [4.583..., 2]
print(f'check._der.get(x) --> '
      f'{check._der.get(x)}')         # Should be 4.583...
print(f'check._der.get(y) --> '  
      f'{check._der.get(y)}')         # Should be 2

print(f'\ncheck = ef.sin(x + y)')
check = ef.sin(x + y)
print(f'check.val --> ' 
      f'{check.val}')                    # Should be [0.656...]
print(f'check.der --> '
      f'{check.der}')
print(f'check._der.get(x) --> '
      f'{check._der.get(x)}')         # Should be 0.753...
print(f'check._der.get(y) --> '
      f'{check._der.get(y)}')         # Should be 0.753...

print(f'\ncheck = ef.sin(x * y)')
check = ef.sin(x * y)
print(f'check.val --> '
      f'{check.val}')                    # Should be [-0.544..]
print(f'check.der --> '
      f'{check.der}')                    # Should be [-4.195..., -1.678...]
print(f'check._der.get(x) --> '
      f'{check._der.get(x)}')         # Should be -4.195...
print(f'check._der.get(y) --> '
      f'{check._der.get(y)}')         # Should be -1.678...

print(f'\ncheck = 8 * x')
check = 8 * x
print(f'check.val --> '
      f'{check.val}')                    # Should be 16
print(f'check.der --> '
      f'{check.der}')
print(f'check._der.get(x) --> '
      f'{check._der.get(x)}')         # Should be 8

print(f'\ncheck = 8 * y')
check = 8 * y
print(f'check.val --> '
      f'{check.val}')                    # Should be [40]
print(f'check.der --> '
      f'{check.der}')                    # Should be [8]
print(f'check._der.get(y) --> '
      f'{check._der.get(y)}')         # Should be 8

print(f'\ncheck = 8 + x')
check = 8 + x
print(f'check.val --> '
      f'{check.val}')                    # Should be [10]
print(f'check.der --> '
      f'{check.der}')                    # Should be [1]
print(f'check._der.get(x) --> '
      f'{check._der.get(x)}')         # Should be 1

print(f'\ncheck = 8 + y')
check = 8 + y
print(f'check.val --> '
      f'{check.val}')                    # Should be 13
print(f'check.der --> '
      f'{check.der}')
print(f'check._der.get(y) --> '
      f'{check._der.get(y)}')         # Should be 1

print(f'\ncheck = x * y + ef.sin(x) + z')  # Check that uses three input vars
check = x * y + ef.sin(x) + z
print(f'check.val --> '
      f'{check.val}')                    # Should be 13.909...
print(f'check.der --> '
      f'{check.der}')                 # Should be [4.583..., 2, 1]
print(f'check._der.get(x) --> '
      f'{check._der.get(x)}')         # Should be 4.583...
print(f'check._der.get(y) --> '  
      f'{check._der.get(y)}')         # Should be 2
print(f'check._der.get(z) --> '  
      f'{check._der.get(z)}')         # Should be 1

print(f'\nx1 = fd.new_var(2)\n'
      f'x2 = fd.new_var(3)\n'
      f'check = x1 * x2 + x1')
x1 = fd.new_scal(2)
x2 = fd.new_scal(3)
check = x1 * x2 + x1
print(f'check.val --> '
      f'{check.val}')                    # Should be [8]
print(f'check.der --> '
      f'{check.der}')                    # Should be [4, 2]

# TODO: VECTOR DEBUGGING --
print()

print(f'x1 = fd.new_vec([2, 3, 4])\n'
      f'x2 = fd.new_vec([3, 2, 1])\n'
      f'check = x1 - x2\n')
x1 = fd.new_vec([2, 3, 4])
x2 = fd.new_vec([3, 2, 1])
check = x1 - x2
print(f'x1._der.get(x1) -->\n'
      f'{x1._der.get(x1)}\n')
print(f'x2._der.get(x2) -->\n'
      f'{x2._der.get(x2)}\n')
print(f'check._der.get(x1) -->\n'
      f'{check._der.get(x1)}')
print(f'check._der.get(x2) -->\n'
      f'{(check._der.get(x2))}')


# print(np.array([1,2,3]) * np.array([1,2,4]))
# print(np.identity(2) - 0)
# print((np.eye(2) - np.eye(2)) * 2)
