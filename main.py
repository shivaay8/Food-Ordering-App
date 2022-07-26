import admin2 as aa
from user import user
uhh=user(str,str,str,str,str)
inp=int(input("where you want to login select 1.Admin and 2.User and 3.Exit"))
if inp==1:
    Username=input("enter the username of admin:")
    Password=input("enter the password of admin:")
    if aa.admin_info[Username]==Password:
        print("you are successfully logged in")
        admin_crawler=True
        while admin_crawler:
            adm_choice=int(input("choose the options of admin portal 1.ADD NEW ITEM 2.EDIT ITEM 3.VIEW MENU 4.REMOVE ITEM 5.EXIT"))
            if adm_choice==1:
                aa.add_food_item()
            elif adm_choice==2:
                aa.edit_food_item()
            elif adm_choice==3:
                aa.show_menu_item()
            elif adm_choice==4:
                aa.removing_food_item()
            elif adm_choice==5:
                print(f"you are exit to the admin panel {Username}")
                admin_crawler=False
            else:
                print("this is the wrong selection please enter valid option") 
    else:
        print("these are the wrong credentials ! SORRY!!")
elif inp==2:
    print("welcome to the user panel")
    username=input("enter the email:")
    password=input("enter the password here:")
    if user.login(email_enter,password):
        print(f"you are logged in {email_enter}")
        user_crawler=True
        while user_crawler:
            usr_choice=int(input(f"{username},enter the option 1.place new order  2.order history  3.update profile  4.exit"))
            if usr_choice==1:
                uhh.place_new_order()
            elif usr_choice==2:
                print(f"here  is your order history,{email_enter}")
                print(uhh.order_history_see)
            elif usr_choice==3:
                print(f"profile is updated,{email_enter}")
                print(uhh.update_profile)
            elif usr_choice==4:
                user_crawler=False
                print("you are successfully logged out")
            else:
                print("you choose invalid option")
    elif inp==3:
        new_email=input("enter new email")
        if new_email in user.login_info.keys():
            print("email already registered")
        else:
            print("enter your detail here>>>")
            new_name=input("enter new name")
            new_phone_no=int(input("enter new phone no"))
            new_address=input("enter new address")
            new_password=input("enter new password")
            user=user(new_email,new_name,new_phone_no,new_address,new_password)
            print("you have registered successfully")
            print("now you cabn log in")
    elif inp==4:
        exit()
    else:
        prinnt("fo;;ow options")
            
