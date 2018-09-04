employee_personal=("Harsha Chaney","12345","03-06-1995","B+","BCA-MCA")
for i in range(0,5):
    if i==0:
        print("Employee Name : ",employee_personal[0])
    elif i==1:
        print("Employee Id : ",employee_personal[1])
    elif i==2:
        print("Employee DOB : ",employee_personal[2])
    elif i==3:
        print("Employee Blood Group : ",employee_personal[3])
    elif i==4:
        print("Employee Qualifications : ",employee_personal[4])
        
employee={"Employee_Contact":9804562137,"Employee_Email":"harsha@gmail.com","Employee_Age":25,"Employee_Department":"Computer Science and IT","Employee_Designation":"Software Development Engineer","Employee_Address":"Punjab","Employee_JoiningYear":"2017","Employee_ServiceYears":1,"Employee_TotalProjects":3,"Employee_CurrentProject":"Learning Management System"}
for i,j in employee.items():
    print(i," : ",j )

employee_professional=["e-learning solutions","Payment Gateway","Mobile Application Development"]
print("Projects done till now")
for i in range(0,3):
    print(employee_professional[i])
    
