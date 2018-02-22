# - Tool Inventory Manager

'''Project = personal python3 classes -
manage tool inventory for contractor on mult. sites
across mult site and employees - all empl. users check tools in or out
and out of main inventory, that tracks damaged or missing tools
- age of tools - maint and suggested replacement dates?
'''
class Tool:

    '''Full Tool Inventory e.g. Main Tool Box for company '''
    def __init__(self,name, ttype, id_num, location, status, age):
        self.name = name
        self.ttype = ttype
        self.id_num = id_num
        self.location = location
        self.status = status
        self.age = age

# def add tool,
# remove tool,
# assign too

class Employee:
    def __init__(self,name, email, emp_num, security, hire_date):
        self.name = name
        self.email = email
        self.emp_num = emp_num
        self.security = security
        self.hire_date = hire_date


class Site:
     def __init__(self, jobname, jobaddress, jobsize, jobstart, joblength, jobvalue):
         self.jobname = jobname
         self.jobaddress = jobaddress
         self.jobsize = jobsize
         self.jobstart = jobstart
         self.joblength = joblength
         self.jobvalue = jobvalue

         
import sqlite3 as lite
import sys
import copy
con = lite.connect('bigbox.db')

names = []
types = []
id_nums = []
locations = []
statuss = []
ages = []
    
conn = lite.connect('bigbox.db')
print ("Opened database successfully");
cursor = conn.execute("SELECT name, type, id_num, location, status, age from tool")
for row in cursor:

    name = row[0]
    ttype = row[1]
    id_num = row[2]
    location = row[3]
    status = row[4]
    age = row[5]
    
##    print ("name =  ", row[0])
##    print ("type = ", row[1])
##    print ("id num = ", row[2])
##    print('location =', row[3])
##    print('status =', row[4])
##    print('age =', row[5],"\n\n")
##   
   
    names.append(name)
    types.append(ttype)
    id_nums.append(id_num)
    locations.append(location)
    statuss.append(status)
    ages.append(age)


print (names,'\n\n\n')
print,('\n\n\n')
print (types)
print()
print(id_nums)
print()
print(locations,'\n\n\n')



for name in names:
    print(name, id_num)
    
    
print ("Operation done successfully");
conn.close()

##new_names = copy.copy(names)
##new_types = copy.copy(types)
##for i in range(5):
##    out = new_names
##    out2 = new_types
##    a = input('hit a key')
##    
##    print (out,out2);
    
    
print ("Operation done successfully");



