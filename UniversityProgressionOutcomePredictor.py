## I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
## Any code taken from other sources is referenced within my code solution.
##        Student ID: 20231777
##        Date: 29/11/2023

## The program should allow students to predict their progression outcome.according to part 1 A, we should use for student and staff members

while True:   # while loop- 1
    try:
        option_1 = input("Enter 's' for student and enter 't' for staff member: ").lower()    # enter s or t or S or T, it does not affect
        while option_1 != 's' and option_1 != 't':
            option_1 = input("Enter 's' for student and enter 't' for staff member: ").lower()
        break
    except (KeyboardInterrupt,EOFError):  # enter Ctrl+c(Ctrl-c, Ctrl+Alt+c, Ctrl+Alt-c) and Ctrl+d(Ctrl-d, Ctrl+Alt+d, Ctrl+Alt-d)
        print("ERROR, enter again(KeyboardInterrupt or EOFError)")
    except:
        print("ERROR, enter again ")
        
from graphics import *              # import graphics python file
progress_count = 0
trailing_count = 0
exclude_count = 0
module_retriever_count = 0

# creat a text file
file = open('progression data.txt','w')
file.close()
def progression_data_text_file():
    # the received data appending (is written and storedo ne by one) in the "progress data" file
    with open('progression data.txt','a') as file_1:
        file_1.write(data+'\n')
        
# the received data is stored here     
credits_data = []
def progression_data_list():
    # getting new data and append to "credits_data" variable
    credits_data.append(data)

while True:             # while loop- 2
    while True:         # while loop- 3
        try:
            passed = int(input('Enter your total PASS credits: '))
            if passed in range(0,121,20):
                defer = int(input('Enter your total DEFER credits: '))
                if defer in range(0,121,20):
                    total_1 = passed + defer
                    if total_1 <= 120:
                        fail = int(input('Enter your total FAIL credits: '))
                        if fail in range(0,121,20):
                            total_2 = passed + defer + fail
                            if total_2 == 120:
                                break       # break the while loop- 3
                            else:
                                print('Total incorrect')
                        else:
                            print('Out of range')
                    else:
                        print('Total incorrect')
                else:
                    print('Out of range')
            else:    
                print('Out of range')
        except ValueError:
            print('Integer required')
        except (KeyboardInterrupt,EOFError):  # don't enter Ctrl+c(Ctrl-c, Ctrl+Alt+c, Ctrl+Alt-c) and Ctrl+d(Ctrl-d, Ctrl+Alt+d, Ctrl+Alt-d)
            print("ERROR, enter again(KeyboardInterrupt or EOFError)")
        except:
            print("ERROR, enter again ")
        continue      # continue the while loop- 3

    def creadts():
        # when we assigned a value to a global variable in other functions, it is declared as global in each function.
        global progress_count,trailing_count,module_retriever_count,exclude_count
        if passed == 120:
            outcome = 'Progress'
            progress_count += 1
        elif passed == 100:
            outcome = 'Progress (module trailer)'
            trailing_count += 1
        elif fail >= 80:
            outcome = 'Exclude'
            exclude_count += 1
        else:
            outcome = 'Module retriever'
            module_retriever_count += 1
        return outcome              # returns a value to function's caller ( return to "outcome = creadts()" )
    outcome = creadts()
    print(outcome)
    if option_1 == 's':
        break      # break the while loop- 2
    
    data = (f'{outcome}- {passed},{defer},{fail}')
    progression_data_list()
    progression_data_text_file()
    
    # the program loops to allow a staff member to predict progression outcomes for multiple students. according to part 1 C
    print('Would you like to enter another set of data?')
    while True:         # while loop- 4
        try:
            option_2 = input("Enter 'y' for yes or 'q' to quit and view results ").lower()  # enter y or q or Y or Q, it does not affect
            while option_2 != 'y' and option_2 != 'q':          # while loop- 5
                option_2 = input("Enter 'y' for yes or 'q' to quit and view results ").lower()
            break      # break the while loop- 4
        except:   # (KeyboardInterrupt,EOFError, and other error)
            print("ERROR, enter again ")
    if option_2 == 'y':
        continue     # continue the while loop- 2
    else:
        break        # break the while loop- 2
    
if option_1 == 't':
    
    ### Histogram - when we change histogram window size (height and width), other sizes are autogenerate
    
    win = GraphWin('Histogram',550,550)
    win.setBackground(color_rgb(238, 242, 238))
    # for histogram making to easy
    total = [ progress_count , trailing_count , module_retriever_count , exclude_count ]
    number_of_students = sum(total)
    max_creadit = max(total)
    size = ((win.getHeight()- win.getHeight()/(550/200)) / max_creadit)        # win.getHeight()-200 / max_creadit --> 350/max_creadit
    gap = win.getWidth()/(550/20)                                   # 20
    bar_width = win.getWidth()/(550/80)                             # 80
    start_width = win.getWidth()/(550/100)                          # 100
    start_height = win.getHeight()- (win.getHeight()/(550/100))     # win.getHeight()-100 -->450
    bar_name_height = win.getHeight()/(550/30)                      # 30
    bar_number = win.getHeight()/(550/20)                           # 20
       
    # Titles -----------------------------------------------------------------------------------------------------------------------------
    title = Text(Point(win.getWidth()/(550/180), win.getHeight()/(550/40)), 'Histogram Rusults')
    title.setStyle('bold'), title.setSize(18), title.setFill(color_rgb(80,80,80)), title.draw(win)
    
    sub_title = Text(Point(win.getWidth()/(550/180), win.getHeight()-win.getHeight()/(550/30)), f'{number_of_students} outcomes in total.')
    sub_title.setStyle('bold'), sub_title.setFill('gray'), sub_title.setSize(15), sub_title.draw(win)

    # Line -------------------------------------------------------------------------------------------------------------------------------
    line = Line(Point(win.getWidth()/(550/50), start_height), Point(win.getWidth()-(win.getWidth()/(550/20)), start_height))
    line.setFill('gray'), line.draw(win)

    # Progress_bar -----------------------------------------------------------------------------------------------------------------------
    progress_bar = Rectangle(Point(start_width, start_height) , Point(start_width+bar_width,start_height-(size*progress_count)))
    progress_bar.setFill('light green'), progress_bar.setOutline('gray'), progress_bar.draw(win)

    progress_bar_name = Text(Point(start_width + (bar_width/2), start_height + bar_name_height),'Progress')
    progress_bar_name.setStyle("bold"), progress_bar_name.setFill('gray'), progress_bar_name.draw(win)

    progress_bar_number = Text(Point(start_width + (bar_width/2), start_height - (size*progress_count) - bar_number), progress_count)
    progress_bar_number.setStyle("bold"), progress_bar_number.setFill('gray'), progress_bar_number.draw(win)

    # Trailer_bar ------------------------------------------------------------------------------------------------------------------------
    trailer_bar = Rectangle(Point(start_width + bar_width + gap,start_height ) , Point(start_width + 2*(bar_width) + gap, start_height - (size*trailing_count)))
    trailer_bar.setFill(color_rgb(142, 188, 137)), trailer_bar.setOutline('gray'), trailer_bar.draw(win)

    trailer_bar_name = Text(Point(start_width + bar_width+gap + (bar_width/2),start_height + bar_name_height),'Trailer')
    trailer_bar_name.setStyle("bold"), trailer_bar_name.setFill('gray'), trailer_bar_name.draw(win)

    trailer_bar_number = Text(Point(start_width + bar_width + gap + (bar_width/2), start_height-(size*trailing_count) - bar_number),trailing_count)
    trailer_bar_number.setStyle("bold"), trailer_bar_number.setFill('gray'), trailer_bar_number.draw(win)

    # Retriever_bar ----------------------------------------------------------------------------------------------------------------------
    retriever_bar = Rectangle(Point(start_width+2*bar_width+ 2*gap, start_height),Point(start_width+3*bar_width+ 2*gap,start_height-(size*module_retriever_count)))
    retriever_bar.setFill(color_rgb(158, 182, 114)), retriever_bar.setOutline('gray'), retriever_bar.draw(win)

    retriever_bar_name = Text(Point(start_width + 2*bar_width + 2*gap + (bar_width/2), start_height + bar_name_height),'Retriever')
    retriever_bar_name.setStyle("bold"), retriever_bar_name.setFill('gray'), retriever_bar_name.draw(win)

    retriever_bar_number = Text(Point(start_width+ 2*bar_width+ 2*gap +(bar_width/2),start_height-(size*module_retriever_count)-bar_number),module_retriever_count)
    retriever_bar_number.setStyle("bold"), retriever_bar_number.setFill('gray'), retriever_bar_number.draw(win)

    # Excluded_bar -----------------------------------------------------------------------------------------------------------------------
    excluded_bar = Rectangle(Point(start_width + 3*bar_width + 3*gap,start_height), Point(start_width + 4*bar_width + 3*gap,start_height-(size*exclude_count)))
    excluded_bar.setFill('pink'), excluded_bar.setOutline('gray'), excluded_bar.draw(win)
    
    excluded_bar_name = Text(Point(start_width + 3*bar_width + 3*gap + (bar_width/2), start_height + bar_name_height),'Excluded')
    excluded_bar_name.setStyle("bold"), excluded_bar_name.setFill('gray'), excluded_bar_name.draw(win)
    
    excluded_bar_number = Text(Point(start_width + 3*bar_width + 3*gap + (bar_width/2), start_height - (size*exclude_count) - bar_number), exclude_count)
    excluded_bar_number.setStyle("bold"), excluded_bar_number.setFill('gray'), excluded_bar_number.draw(win)

    # when click on window, will close our histogram
    try:
        win.getMouse()
        win.close()
    # clicking on close icon or entering Ctrl+C gives error, so we need to do error handling
    except:
        None
        
    print('\nPart 2:')
    for element in credits_data:
            print(element)

    print('\nPart 3:')
    with open('progression data.txt','r') as file_2:
        read = file_2.read()
        print(read)

## END THE PROGRAM
#_____________________________________________________________________________________________________________________________________________
