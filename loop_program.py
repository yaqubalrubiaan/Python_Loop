try:
    print("Hello Welcome To My Program in the python,, By: MrOsta  :) \n ----------------- \n Twitter: @MrOsta_ \n")
    name = input("Please Type Your Value:")
    howch = int(input("Please Type the number of loop ( only numbers ): "))
    auth = input("Your sure? | yes or no: ")
    
    def looping_f():
        for i in range(howch):
            print(name)
        print("\n \n ---- \n \n Thanks For Try. This is",howch,"Loop. \n \n By: @MrOsta")
    if auth == "yes" or auth == "Yes":
        looping_f()
    elif auth == "no":
                print("Sorry! We Can't Continue ..")
    else:
        i = 1 
        for i in range(3):
            hh = input("Please Try Again, Your sure? ( yes or no ): ")
            if hh == "yes" or hh == "Yes":
                looping_f()
                
            elif hh == "no":
                print("Sorry! We Can't Continue ..")
                
    #----------------- By MrOsta -----------------------------
except:
    print("\n#######\n Something Wrong Please Try Again! ):\n####### \n Contact Me in twitter: @MrOsta_")
