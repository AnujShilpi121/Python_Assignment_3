import random
import mysql.connector as con
connection = con.connect(host='localhost',user='root',password='Anuj@123s',database='python_questions')
cursor = connection.cursor()

registration_email = []
registration_password = []

cursor.execute("SELECT * FROM LOGIN_DETAILS")
reg_email_and_pass = cursor.fetchall()
for item in reg_email_and_pass:
    reg_email,reg_pass = item
    registration_email.append(reg_email)
    registration_password.append(reg_pass)


def Registration():
    while(True):
        email = input("Please enter your email:\n").casefold().strip()
        if email.endswith("gmail.com") and ("@" in email):
            if (" " or '\t' ) not in email:
                pass
            else:
                print("Please enter the email which should not contain white space between character")
                continue
        else:
            print("Please enter the email which should contain ('@') and should ends with ('gmail.com')")
            continue

        temp = 0
        if email in registration_email:
            print("Please enter valid email. This email has already registered")
            while(True):
                num = input("Enter '1' for try again and '2' for Home Page: \n")
                if num.isalpha():
                    print("Please enter a valid input")
                    continue
                elif num == '1':
                    break
                elif num == '2':
                    temp = int(num)
                    break
                else:
                    print("Please enter a valid input")
                    continue
            if temp == 2:
                break

            continue

        else:
            password = input("Please enter password:\n")
            while(True):
                password_len = len(password)
                if password_len < 6:
                    print("Please enter a strong password,length of your password should be greater than or equal to 6")
                    password = input()
                    continue
                else:
                    break

            registration_email.append(email)
            registration_password.append(password)

            r_email_pass = "INSERT INTO LOGIN_DETAILS(email,password) VALUES(%s,%s)"
            val = (email,password)

            cursor.execute(r_email_pass,val)
            connection.commit()

            print("You have registered successfully.")
            break




def Login(email):
    while(True):
        password = input("Please enter password for the registered email:\n").strip()
        i = registration_email.index(email)
        if registration_password[i] != password:
            print("Wrong Password\n")


            while(True):
                ask = input("Please enter '1' for try again and 'h' to retrurn Home Page for change password:\n").lower()
                if ask.isalpha() and ask != 'h':
                    print("Please enter the valid input:\n")
                    continue
                elif ask == '1':
                    break

                elif ask == 'h':
                    break

                else:
                    print("Please enter the valid input:\n")
                    continue

            if ask == 'h':
                return 0
            if ask == 'h':
                break


            continue
        else:
            break




def Generate_Question():

    cursor.execute("SELECT * FROM QUESTIONS")
    all_ques_list = cursor.fetchall()

    Questions = []

    for i,question in enumerate(all_ques_list):
        q_id,q_text,opt1,opt2,opt3,correct_opt = question
        Questions.append((q_text,[opt1,opt2,opt3],correct_opt))


    quiz = random.sample(Questions,5)

    for i,(ques,options,correct_option) in enumerate(quiz,start=1):
        print(f"Question {i}: {ques}")
        for j,opts in enumerate(options,start=1):
            print(f"{'\t'} {j}: {opts}")
        print("\n")





    given_answer = []
    right_answer_given = 0
    for k in range(len(quiz)):
        k += 1
        while(True):
            answ = input(f"Select the option for Answer {k}:\t")
            if answ.isalpha() or int(answ) < 0 or int(answ) > 3:
                print("Please select the option no as [1,2 or 3].")
                continue
            else:
                answ = int(answ)
                given_answer.append(answ)
                break

    print("\n")

    for l,ques in enumerate(quiz):
        q = ques[2]
        p = given_answer[l]

        if q == p:
            right_answer_given += 1
        else:
            print(f"The right Answer for Question {l + 1} is : {quiz[l][1][q-1]} ")


    print(f"\nYou have given {right_answer_given} right answer out of 5")
    given_answer.clear()
    right_answer_given = 0



if __name__ == "__main__" :
    while(True):
        print('''    ----Enter the following input-----
              1 for registration
              2 for login'
              3 to know who has already registered
            'e' for exit
            'd' for delete account
            'c' for change password
        ------------------------------------------''')

        num = input("\n").lower()
        if num.isalpha() and (num not in ['e','d','c']):
            print("Please enter the valid input")
            continue

        elif num.isdigit() and num == '1':
            Registration()
            continue

        elif  num.isdigit() and num == '2':
            while (True):
                email = input("Please enter your registered email:\n").casefold()
                if email in registration_email:
                    # Login(email)
                    break
                else:
                    print("Account not found")
                    while(True):
                        num2 = input("Press '2' for try again to login , Press '1' for registration:\n")
                        if num2.isalpha():
                            print("Please enter a valid input")
                            continue
                        elif num2 == '1':
                            Registration()
                            break

                        elif num2 == '2':
                            break

                        else:
                            print("Please enter a valid input")
                            continue

                    continue
            if Login(email) != 0:
                print("\n")
                Generate_Question()
            else:
                continue

            while(True):
                gen = input("Do you want to generate 5 question again . Press 'y' for Yes and 'n' for No exit: \n").lower()
                while(True):
                    if gen.isnumeric() or gen.isdigit():
                        print("Please enter a valid input:")
                        gen = input()
                        continue
                    elif gen == 'y':
                        Generate_Question()
                        break
                    elif gen == 'n':
                        exit_code = input("Press '1 for Home Page' , 'e for exit':\n")
                        while(True):
                            if exit_code.isalpha() and exit_code != 'e':
                                print("Please enter the valid input:")
                                exit_code = input()
                                continue
                            elif exit_code == 'e':
                                exit()
                            elif exit_code == '1':
                                break
                            else:
                                print("Please enter the valid input:")
                                exit_code = input()
                                continue

                        break
                    else:
                        print("Please enter a valid input:")
                        gen = input()
                        continue
                if gen == 'n':
                    break
                continue
            continue

        elif num.isdigit and num == '3':
            print(f"These are the registered emails: {registration_email}")
            continue
        elif num == 'e':
            exit()
        elif num == 'd':
            while (True):
                r_email = input("Please enter your registered email for deletion of your account:\n")
                if r_email.endswith("gmail.com") and ("@" in r_email):
                    if (" " or '\t') not in r_email:
                        break
                    else:
                        print("Please enter the valid email account")
                        continue
                else:
                    print("Please enter the valid email account")
                    continue

            if r_email in registration_email:
                r_pass_ind = registration_email.index(r_email)
                registration_email.remove(r_email)
                registration_password.remove(registration_password[r_pass_ind])
                delete_account = "DELETE FROM LOGIN_DETAILS WHERE email = %s"
                r_email = [r_email]
                cursor.execute(delete_account,r_email)
                connection.commit()
                print("\nAccount has been deleted successfully.\n")
                continue
            else:
                print("Account not registered yet.\n")
                continue

        elif num == 'c':
            l = 0
            while (True):
                log_email = input("Enter your registered email:\n")
                if log_email in registration_email:
                    log_email_ind = registration_email.index(log_email)
                    z = 0
                    while (True):
                        set_pass = input("Please set your password:\n")
                        if len(set_pass) < 6:
                            print("Please enter the password which should have minimum 6 character:\n")
                            z += 1
                            if z > 2:
                                print("Too many tries.May be you can delete your account and register again")
                                break
                            continue
                        else:
                            registration_password.remove(registration_password[log_email_ind])
                            registration_password.insert(log_email_ind,set_pass)
                            cursor.execute("UPDATE LOGIN_DETAILS SET password = %s WHERE email = %s",
                                           (set_pass, log_email))
                            connection.commit()
                            print("Password changed successfully:\n")
                            break
                    break

                else:
                    print("Account not found:\n")
                    l += 1
                    if l > 2:
                        print("You have reached the limit:\n")
                        break
                    continue

            continue


        else:
            print("Please enter a valid input")
            continue

