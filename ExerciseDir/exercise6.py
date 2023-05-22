# create a program that reads that file and prints out exercise6_txt_files/essay.txt text. The first letter of each word in the output should be uppercase.
file = open('exercise6_txt_files/essay.txt', 'r')
essay = file.read()
# file.read() = Returns the entire content of the file as a single string. vs 
# file.readlines = reads the entire content of the file and returns a list of strings where each elements of the list represetnes a single line from the file 
print(essay.title())

# Write a program that reads the essay.txt file and returns the number of characters contained in the file.
file = open('exercise6_txt_files/essay.txt', 'r')
essay = file.read()
print(len(essay))
# treated as a single string ^ 

# members.txt = create a program that, whenever executed, asks the user to enter a new member in the command line: "add a new member: 'solomon right'"Then, the member is added to members.txt.
# file_member = open('exercise6_txt_files/members.txt', 'r')
# members = file_member.readlines()
# file.close()

# new_member = input('add a new member: ').title().strip() + '\n'
# members.append(new_member)

# file_member = open('exercise6_txt_files/members.txt', 'w')
# file_member.writelines(members)
# file.close()

# Create a program that generates multiple text files by iterating over the filenames list. The text Hello should be written inside each generated text file.
filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(f'exercise6_txt_files/{filename}', 'w')
    file.writelines('hello')
    file.close

# Download the three text files a.txt, b.txt, and c.txt from the resources. Then, create a program that reads each text file and prints out the content of each in the command line. 
final_ex_files = ['a', 'b', 'c']

for i in final_ex_files:
    file = open(f'exercise6_txt_files/{i}.txt', 'r')
    iam = file.read()
    print(iam)

##### bug fixing #####
file = open("exercise6_txt_files/data.txt", 'w')
 
file.writelines("100.12\n")
file.writelines("111.23\n")
file.close()

# file.write()= Writes a single string to the file. If you want to write multiple lines, you need to add the newline character \n manually at the end of each line, except the last one.
# file.writelines() =  Writes a list of strings to the file, without adding any separator between the list items.