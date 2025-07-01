#1.
class Employee: #superclass
    def __init__(self, name, employee_id, department, salary): #initialize and accept arguments for Employee info
        self.__name = name
        self.__employee_id = employee_id
        self.__department = department
        self.__salary = salary

    #the set method is a mutator for the employee attributes
    def set_name(self, name):
        self.__name = name
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id
    def set_department(self, department):
        self.__department = department
    def set_salary(self, salary):
        self.__salary = salary

    #the get method is an accessors for employee attributes
    def get_name(self):
        return self.__name
    def get_employee_id(self):
        return self.__employee_id
    def get_department(self):
        return self.__department
    def get_salary(self):
        return self.__salary
    def display_info(self): #display employee details
        print(f"ID: {self.get_employee_id()} | Name: {self.get_name()} | Department: {self.get_department()} | Salary: ${self.get_salary():.2f}")  

#2.
#supclass
class Manager(Employee):
    def __init__(self, name, employee_id, department, salary, bonus):
        #Overide new salary
        new_salary = salary + bonus
        Employee.__init__(self, name, employee_id, department, new_salary) #refer to the parent class & passed required arguments
        #super().__init___(self, name, employee_id, department, salary)
        self.__bonus = bonus #initalize
    def set_bonus(self, bonus): #mutator for the bonus attribute
        self.__bonus = bonus
    def get_bonus(self): #accessor
        return self.__bonus
    def display_info(self):
        print(f"ID: {self.get_employee_id()} | Name: {self.get_name()} | Department: {self.get_department()} | Salary: ${self.get_salary():.2f} | Bonus: ${self.get_bonus():.2f}")

class HourlyEmployee(Employee):
    def __init__(self, name, employee_id, department, salary, hourly_rate):

        #Overide the passing salary when initializing ths salary
        TOTAL_WORKING_HOURS = 1000
        new_salary = hourly_rate * TOTAL_WORKING_HOURS
        Employee.__init__(self, name, employee_id, department,new_salary) #refer to the parent class & passed required arguments
        self.__hourly_rate = hourly_rate #initialize
    def set_hourly_rate(self, hourly_rate): #mutator for the hourly rate attribute
        self.__hourly_rate = hourly_rate

    def calculate_weekly_pay(self): #calculate weekly pay and set constant for working hours
        HOURS_WORKED = 40
        return self.__hourly_rate * HOURS_WORKED

    def get_hourly_rate(self): #accessor
        return self.__hourly_rate

    def __str__(self): #automatically print when call
        return f"ID: {self.get_employee_id()} | Name: {self.get_name()} | Department: {self.get_department()} | Hourly rate: ${self.get_hourly_rate()}/hr"
    
class Intern(Employee):
    def __init__(self, name, employee_id, department, salary, unpaid):
        Employee.__init__(self, name, employee_id, department, salary) #refer to the parent class & passed required arguments
        self.__unpaid = unpaid #initialize
    def set_unpaid(self, unpaid): #mutator for the unpaid attribute (boolean)
        self.__unpaid = unpaid
    def get_unpaid(self): #accessor
        return self.__unpaid
    def display_info(self): #display intern info while overiding the original 
        print(f"ID: {self.get_employee_id()} | Name: {self.get_name()} | Department: {self.get_department()} | {self.get_unpaid()}")

#3. Department
class Department:
    def __init__(self, dept_name, budget, employees):  #initialize and accept arguments for department class
        self.__dept_name = dept_name
        self.__budget = budget
        self.__employees = [] #initialize an empty list to store employee objects

    def get_employees(self): #get the values
        return self.__employees

    def get_dept_name(self):
        return self.__dept_name
    def get_budget(self):
        return self.__budget
    def add_employee(self, employees):
        self.__employees.append(employees)
        return self.__employees
    def calculate_total_salary(self):
        total_salary = 0
        for i in self.__employees: #items in the list employee
            total_salary = total_salary + i.get_salary() #calculate sum salary 
        return total_salary
    def display_department_info(self): #display info 
        print(f"{self.get_dept_name()}: Budget ${float(self.get_budget()):.2f} | Total Salaries: ${self.calculate_total_salary():.2f}")

#4. Payroll System
class Payroll:        
    def __init__(self): #initlizing empty list
        self.__employees = []

    def set_employees(self, i_employees):
        if isinstance(i_employees,list): #check an instance and add into an empty list
            self.__employees = i_employees
            
    def get_employees(self):
        return self.__employees
    
    def process_payroll(self):
        YEAR_WEEKS = 52
        for i in self.__employees: #get names and salary, then calculate weekly pay
          v_name = i.get_name()
          v_weeklypay = i.get_salary()/YEAR_WEEKS
          print(f"{v_name}: Weekly Pay: ${v_weeklypay:.2f}")
            
def main():
    #create instances of the employee class with sample data
    employee1 = Employee('Alice Johnson', 1001, 'Engineering', 85000)
    employee2 = Manager('Bob Smith', 1002, 'HR', 65000, 5000)
    employee3 = HourlyEmployee('Charlie Green', 1003, 'Engineering',0, 25)
    #print(f": ${employee3.get_salary()}")
    employee4 = Intern('David White', 1004, 'HR',0,'Unpaid Intern')

        
    #Display the information of employees
    print('Employee Directory:')
    print('--------------------')
    #Employee1
    employee1.display_info()    
    #Employee2
    employee2.display_info()
    #Employee3
    print(employee3)
    #Employee4
    employee4.display_info()
    
    #Create instances of department class with sample data of 2 departments
    enginneering = Department('Enginneering', 200000,[])
    hr = Department('HR', 150000,[])
    #call the add_employee method, and assign each employee into their department for calculation
    enginneering.add_employee(employee1)
    hr.add_employee(employee2)
    enginneering.add_employee(employee3)
    hr.add_employee(employee4)
    
    print('\nDepartment Budgets:')
    print('--------------------')
    #display info for department
    enginneering.display_department_info()
    hr.display_department_info()

    print('\nPayroll Processing:')
    print('--------------------')
    #display info for payroll
    payroll = Payroll() #create instance for Payroll class
    #get engineering employees payroll info
    payroll.set_employees(enginneering.get_employees())
    payroll.get_employees()
    payroll.process_payroll()
    #get hr employees payroll info
    payroll.set_employees(hr.get_employees())
    payroll.get_employees()
    payroll.process_payroll()


    
main()
    






    
