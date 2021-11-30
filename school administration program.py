#student Information Program
import csv
def write_csv(info_list):
  with open("student_info.csv",'a',newline='')as csv_file:
    writer =csv.writer(csv_file)
    if csv_file.tell()==0:
      writer.writerow(["Name","Age","Contact Number","Email-id"])
    writer.writerow(info_list)
#main function
if __name__ == '__main__':
  condition=True
  student_num=1
  while(condition):
   student_info=input("enter student information for student {} in the following format "
                      "(Name Age Contact_number Email id :\n".format(student_num))
   #print("entered information",student_info)
   student_info_list = student_info.split(' ')
  # print("Entered split up information is:"+str(student_info_list))
   print("\nThe Entered Information is :\nName:{}\nAge:{}\nContact_number:{}\nEmail-id:{}"
         .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
   choice_check = input("Is the above information correct? (yes/no:")
   if choice_check=="yes":
     write_csv(student_info_list)
   elif choice_check == "no":
        print("\n please re-enter the values!")
        input("enter student information for student {} in the following format "
                      "(Name Age Contact_number Email id :\n".format(student_num))

   condition_check=input("enter (yes/no) if you want to enter another  information  \n")
   if condition_check=="yes" :
    condition= True
    student_num=student_num+1
   elif condition_check=="no":
    condition=False