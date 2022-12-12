class Teacher:
  def __init__(self, name, iq):
    in_school = True
    self.name = name
    self.iq = iq
#Class methods can be used to instantiate a new teacher
  @classmethod
  def adding_things(cls, num1, num2):
    return cls('Mike',num1 + num2)

teacher1 = Teacher('Harry', 240)

print(teacher1.adding_things(2,3))
# we use the @classmethodf to instantiate a new teacher
teacher2 = Teacher.adding_things(4,5)
print(teacher2.iq)

#static method is the same except we do not have access to cls 
@staticmethod
def subtracting_things(num1, num2):
    return num1 - num2

