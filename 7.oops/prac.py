# class Emp:
#     __name = None
#     __age = None
#     __salary = None
    
#     def __init__(self, name , age , salary):
#         self.__name= name
#         self.__age = age
#         self.__salary = salary
        
#     def __show(self):
#         print('name',self.__name) 
#         print('age',self.__age)
#         print('salary',self.__salary)
    
#     def display(self):
#         self.__show()
# emp1 = Emp('vishwajeet',21,10000)
# emp1.display()

# class AccessModifier:
#     var1 = None
#     _var2 = None
#     __var3 = None
    
#     def __init__(self, var1, var2, var3):
#         self.var1 = var1
#         self._var2 = var2
#         self.__var3 = var3
    
#     def showpublicMembers(self):
#         print(self.var1)
        
#     def _showprotectedMembers(self):
#         print(self._var2)
        
#     def __showprivateMembers(self):
#         print(self.__var3)
        
#     def displayprivate(self):
#         self.__showprivateMembers()

# class demo(AccessModifier):
#     def __init__(self,var1,var2,var3):
#         AccessModifier.__init__(self,var1,var2,var3)
        
#     def displayProtected(self):
#         self._showprotectedMembers()

# d= demo(10,20,30)
# d.displayprivate()
# d.displayProtected()
# d.showpublicMembers()
# print(d._var2)


class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
        self.__bonus = 1000

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def get_bonus(self):
        return self.__bonus

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def __calculate_total_salary(self):
        total_salary = self._salary + self.__bonus
        return total_salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self._department = department

    def get_department(self):
        return self._department



emp = Employee("Vishwajeet", 5000)
print("Employee Name:", emp.get_name())
print("Employee Salary:", emp.get_salary())
emp.set_bonus(2000)
print("Employee Bonus:", emp.get_bonus())
total_salary = emp._Employee__calculate_total_salary()
print("Employee Total Salary:", total_salary)

print()

mgr = Manager("Anekar", 8000, "Sales")
print("Manager Name:", mgr.get_name())
print("Manager Salary:", mgr.get_salary())
print("Manager Department:", mgr.get_department())
mgr.set_bonus(3000)
print("Manager Bonus:", mgr.get_bonus())
total_salary = mgr._Employee__calculate_total_salary()
print("Manager Total Salary:", total_salary)

