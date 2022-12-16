import os

def main():
    print("****THIS IS A TEXT FILE CREATOR APP****")
    
    startMenu = ("\n==> 1 Create text file\n" +
        "==> 2 Write text file\n" +
          "==> 3 Open the text file")

    print(startMenu)

    txtInput = input("\nChoose an option:")

   
    if txtInput == '1':
        txtName = input("\nEnter the text file name or type q to back to menu:")
        if(txtName == "q"):
           main() 
        else:
            while (txtName == ""):
                print("Please don't leave a blank name")
                txtName = input("Enter the text file name: incluse the .txt")
        
            if(txtName != ""):
                while(os.path.isfile(txtName + '.txt')):
                    print("\nFile name already exist")
                    txtName = input("Enter the text file name:")
                
            txtFile = open( txtName + ".txt", "w")
            print("\nThe text file has been created!")
            txtFile.close()
            input("\nPress enter to go back to menu..")
            main()

   
    elif txtInput == '2':
        txtName = input("\nEnter the text file name or type q to back to menu:")
        if(txtName == "q"):
           main() 
        else:
            while not os.path.isfile(txtName):
                print("\nFile not exist")
                txtName = input("\nEnter the text file name or type q to back to menu:")

                if(txtName == "q"):
                   main()

            print("\n" +txtName + " Has been opened!")
            txtMsg = input("Please write something to your text file:")

            while (txtMsg == ""):
                txtMsg = input("Please write something to your text file:")

            txtFile = open(txtName, "w")
            txtFile.writelines(txtMsg)
            txtFile.close()
            print("\nSuccesfully write a text!")
            input("Press enter to go back to menu...")
            main()
        
 
    elif txtInput == '3':
        txtName = input("\nEnter the text file name or type q to back to menu:")

        if(txtName == "q"):
           main() 
        else:
            while not os.path.isfile(txtName):
                print("\nFile not exist")
                txtName = input("\nEnter the text file name or type q to back to menu:")

                if(txtName == "q"):
                   main()
                   
            print("Opening the file..\n")
            os.startfile(txtName)
            input("Press enter to go back to menu...")
            main()      

    else:
        print("\nPlease enter only the number in the menu\n")
        input("Press enter to continue...")
        main()

main()

