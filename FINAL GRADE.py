print('Final Grade Remarks')
#Assume the highest score obtainable is 100
PreLims= float(input('Enter Pre-Lim Exam Score: '))
MidTerm= float(input('Enter Mid Term Exam Score: '))
Semis= float(input('Enter Semi Final Exam Score: '))
Finals= float(input('Enter Finals Exam Score: '))
Quiz= float(input('Enter Quiz Score: '))
Project= float(input('Enter Project Score: '))

prelim1= PreLims * 0.15
midt= MidTerm * 0.15
semi= Semis * 0.15
final= Finals * 0.15
quiz= Quiz * 0.25
proj= Project * 0.15

FinalGrade= prelim1 + midt + semi + final + quiz + proj

print('Final Grade: ', FinalGrade)

if FinalGrade >= 75:
    print('Congratulations! You Passed The Course')
else:
    print('Sorry, You Failed The Course')