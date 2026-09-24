name = input("Enter student name: ");
roll_number = input("Enter student roll number: ");

print("Enter student marks in: ");
python = int(input("Python: "));
Dbms = int(input("DBMS: "));
maths = int(input("Maths: "));
cyber_security = int(input("Cyber security: "));
software_engineering = int(input("Software engineering: "));

total = python+Dbms+maths+cyber_security+software_engineering;
percentage = total/500*100;
if total>=400 and python>=27 and Dbms>=27 and maths>=27 and cyber_security>=27 and software_engineering>=27:
    grade='A';
elif total>=350 and python>=27 and Dbms>=27 and maths>=27 and cyber_security>=27 and software_engineering>=27:
    grade='B';
elif total>=300 and python>=27 and Dbms>=27 and maths>=27 and cyber_security>=27 and software_engineering>=27:
    grade='C';
elif total>=200 and python>=27 and Dbms>=27 and maths>=27 and cyber_security>=27 and software_engineering>=27:
    grade='D';
else:
    grade='F';

if python>=27 and Dbms>=27 and maths>=27 and cyber_security>=27 and software_engineering>=27:
    result = 'Pass';
else:
    result = 'Fail';

print("-------------Result-------------");
print("Name : ", name);
print("Roll Number: ",roll_number);
print("Total: ",total);
print("Percentage: ",percentage);
print("Grade: ",grade);
print("Result: ", result);