'''
ex_file.py
[결과확인] deohagi(3,4)
          deohagi(3,4.9)
          deohagi(3,'4')
'''

'''import ex_module
print(ex_module.deohagi(3,4))
print(ex_module.deohagi(3,4.9))
print(ex_module.deohagi(3,'4'))'''

from c_module_class.abc.xyz import ex_module as ex
print(ex.deohagi(3,4))
print(ex.deohagi(3,4.9))
print(ex.deohagi(3,'4'))

'''from c_module_class.abc.xyz.ex_module import deohagi
print(deohagi(3,4))
print(deohagi(3,4.9))
print(deohagi(3,'4'))'''


