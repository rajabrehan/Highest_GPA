# Name: Rajab Rehan
# Date: October 23, 2022
# File: a1.py
# Description: After my chemistry midterm, I really wanted to find out what the maximum mark was THAT I could  get in the class.
# I couldn't however find an online resource to do this. This is why I decided to code a program that intakes the # of assessments,
# how much each is worth, and how much was or wants to be acquired, and uses this information to calculate the maximum & minimum
# (pass and zero) possible final grades. This will in-turn lead to more reasonable expectations for the course's final GPA.

#Defines a function in the program.
def gpa_calculator():
        #Outputs an introduction and options to the user.
        print("Welcome to \"Maximum & Minimum Grade Calculator\", for all of your post-Exam stress needs!")
        print("\n-----------------------------------\nHere are your Options!\nMaximum Grade\nMinimum Grade with Zeroes\nMinimum Grade with all Passes\n-----------------------------------")
        #Decision variable equals 2 so that the while loop will keep looping until the user enters a correct input.
        decision = 2
        #While loop which keeps looping when the user's input isn't 0 or 1
        while not (decision == 0 or decision == 1):
            # Outputs questions to the user using the input function and stores the inputs into the variable "decision".
            decision = int(input("\nDo you want to choose Everything or Pick which to calculate? Input 0 for Everything or 1 to Pick: "))
        #If conditional where when the decision variable is 0, it is converted into the boolean data type, False.
        if decision == 0:
            decision = False
        #If conditional where when the decision variable is 1, it is converted into the boolean data type, True.
        elif decision == 1:
            decision = True

        #If conditional where when the user's decision is True, the code outputs appropriately
        if decision == True:
            #Outputs options to user again but this time including numbers for each option.
            print("\n-----------------------------------\nMaximum Grade - 1 \nMinimum Grade with Zeroes - 2 \nMinimum Grade with all Passes - 3\n-----------------------------------")
            # Decision variable equals 0 so that the while loop will keep looping until the user enters a correct input.
            choice = 0
            # While loop which loops when the user's input isn't 1, 2 or, 3.
            while not(choice == 1 or choice == 2 or choice == 3):
                #Asks the user for their choice.
                choice = int(input("What is your Choice?: "))

        test_num = int(input("\nHow many assessments have you done? (You must know how much they were worth!!) : "))

        #Creates list for the percentage worth of each assessment.
        perc_num = []
        #Creates list for the mark achieves on each assessment.
        mark_num = []
        #Assigns a value to the loop variable, which is used in the output.
        loop_num = 1
        #Assigns the values of 0 to the mark acquired to use for later.
        mark_acquire = 0
        #Assigns the values of 0 to the total percentage to use for later.
        total_perc = 0

        #While loop for number of assessments inputted by the user.
        while test_num > 0:
            # Appends user's inputs to its respective lists, as well as formatting the variable into the input function to be printed.
            perc_num.append(float(input('\nHow much (in percentage) is assessment {} worth of your total grade: '.format(loop_num))))
            mark_num.append(float(input("How much (in percentage) did you or do you want to get on this assessment? : ")))
            # Adds 1 to the loop variable to be used for the output, and subtracts 1 from the "# of tests variable" to use for the while loop.
            test_num = test_num - 1
            loop_num = loop_num + 1
        #For loop in range of how many asessments there are.
        for inputs in range(len(perc_num)):
            #Divides the percentage value of an assessment by 100 and multiplies it by how much was acquired on said assesesment, then adding it to the "mark_acquire" variable to store for later.
            mark_acquire += ((perc_num[inputs]/100)*(mark_num[inputs]))
            #Adds all the percentages for the assessments the user wants to consider.
            total_perc += perc_num[inputs]

        #Calculates the maximum possible mark by adding the "mark acquired" variable with the total percentage of all the asessments, which is subtracted from 100, to get a proper percentage mark out of 100. This value is rounded to the 2nd decimal with the round function.
        mark_max= round(mark_acquire + (100-total_perc),2)
        # Calculates the minimum possible mark by using the "mark acquired" variable without the total percentage remaining, to get a proper percentage mark out of 100. This value is rounded to the 2nd decimal with the round function.
        mark_min =  round(mark_acquire, 2)
        #Calculates the  possible mark if you pass everything else by adding the "mark acquired" variable with the total percentage of all the asessments, which is subtracted from 100 and multiplied by 0.5, to get a proper percentage mark out of 100. This value is rounded to the 2nd decimal with the round function.
        mark_pass = round(mark_acquire + ((100-total_perc)*0.5),2)

        #If conditional which when the percentages inputted do not equal to a value less than or equal to 100, displays an error message to the user.
        if total_perc > 100:
            print("\nYour inputs are invalid, Try Again")
        #Else conditional containing the remaining outputs for when the percentage inputs are valid.
        else:
            #If conditional for when the "choosing" decision is True
            if decision == True:
                #If conditional for when the user picks option 1
                if choice == 1:
                    #Converts "mark_max" float value into a string and outputs it with an appropriate output sentence.
                    print("\nIf you ace the rest of the assessments, the maximum mark you can get in this class is " + str(mark_max) + "%!")
                #Elseif conditional for when the user picks option 2
                elif choice == 2:
                    #Converts "mark_min" float value into a string and outputs it with an appropriate output sentence.
                    print("\nIf you skip the rest of the assessments, the minimum mark you can get in this class is " + str(mark_min)+ "%!")
                # Elseif conditional for when the user picks option 3
                elif choice == 3:
                    #Converts "mark_mpass" float value into a string and outputs it with an appropriate output sentence.
                    print("\nIf you only pass (50%) the rest of the assessments, the maximum mark you can get in this class is " + str(mark_pass) + "%!")

            #If conditional for when the "choosing" decision is False
            if decision == False:
                #Outputs all the possible calculations in 3 different string lines while converting the float variables into strings.
                print("\nIf you ace the rest of the assessments, the maximum mark you can get in this class is " + str(mark_max) + "%!")
                print("If you skip the rest of the assessments, the minimum mark you can get in this class is " + str(mark_min) + "%!")
                print("If you only pass (50%) the rest of the assessments, the maximum mark you can get in this class is " + str(mark_pass) + "%!")

#Calls everything in the main method.
if __name__ == "__main__":
    #Calls the function defined on line 10
    gpa_calculator()
