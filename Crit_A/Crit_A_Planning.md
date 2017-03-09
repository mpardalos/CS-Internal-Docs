---
geometry: margin=1in
---


# Criterion A - Planning 

## Defining the problem

The **client**, Dr. Venia Papaspyrou, is the director of the IBDP at my school. At the
beginning of each year she is responsible for creating the timetable which will be used for
the rest of the academic year. 

**Currently**, at the beginning of each academic year, she asks each prospective IB1 student
for their preferred subjects and then manually creates the timetable. This takes a lot of
time, given the number of students and subjects. It is also error-prone, as it is possible
that, for example, some students might end up with overlapping subjects, meaning that
further adjustments will have to be made. 

## Rationale and proposed solution

After discussing with the client about her requirements, I decided that the best solution
would be an application, where she would input the required data (student subject
preferences, maximum class sizes, other limitations concerning the students or teachers,
etc.), and the application would create an appropriate timetable given those limitations. 

This would greatly reduce the time required for creating the timetable, since it would take
at most a few minutes, rather than the days that are required for creating the timetable
manually. It would also lead to far fewer errors since the possibility of human error would
be eliminated. 

Dr. Papaspyrou already uses Microsoft Excel for storing the data regarding the timetable,
meaning that she is already familiar with the program. Therefore, it would help with the
learnability of the application if she could continue to use the same format for inputting
the data as well as for receiving the output. For this reason, I decided to have the
application receive its data from a Microsoft Excel spreadsheet, meaning that the user will
input which students chose which subjects in a spreadsheet with a specified form, open the
application, choose the file they have created and then the application will output a second
Microsoft Excel spreadsheet containing the final timetable.

The application will be created in python, mainly because of my familiarity with the
language as well as its simplicity.

# Success criteria
1. The timetables produced allow students to attend all subjects they have chosen (i.e. no
   student has two subjects on the same period)
2. The input as well as the output of the program is in Microsoft Excel form
3. The interface is simple and easy to use
4. The layout of the spreadsheet used for input is intuitive and a skeleton is provided with
   the program
5. The output is produced within a reasonable amount of time
6. The input data is validated and, if there is an error, the user is told which cell it is in

