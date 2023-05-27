import requests
#help(requests)
'''
import requests
r = requests.get('')
print(r.status_code)
'''
'''
students= list()
for method in dir(students):
    print(method)
    
help(list())
'''

'''
print(hasattr(list(), "reverse"))
print(getattr(list(), "remove"))
print(callable(list().remove))
print(callable(requests.status_codes))
print(issubclass(Exception, BaseException))
print(issubclass(Exception, str))
'''
class Human:
    pass
class Student(Human):
    pass
student = Student()
#print(issubclass(Student, Human))
#print(issubclass(Student, object))
import inspect as ins
print(ins.ismodule(requests))
print(ins.ismodule(Student))
print(ins.isclass(requests))
print(ins.isclass(Student))
print(ins.isfunction(requests.get))
print(ins.isfunction(requests.post))
print(ins.isfunction(requests.put))
print(ins.isfunction(requests.patch))
print(ins.getmodule(list))