class Employee:
    def __init__(self, name, age, language):
        self._name = name
        self._age = age
        self._language = [language]

    def print_language(self):
        print("{} is {} years old and can speak".format(self._name,self._age), *self._language)
        
    def add_language(self,new_lang):
        self._language.append(new_lang)

class Manager(Employee):
    pass

employee_1 = Employee("Aylin", "29", "Turkish")
employee_1.add_language("English")
employee_1.add_language("Chinese")

employee_2 = Employee("Alex", "35", "Spanish")

manager_1 = Manager("Ali", "29", "Turkish")

manager_2 = Manager("John", "40", "English")

person = {"Aylin": {"Employee": employee_1}, "Nazlı": {"Employee": employee_2}, "Ali": {"Manager": manager_1}, "Necati": {"Manager": manager_2}}

person["Aylin"]["Employee"].print_language()
