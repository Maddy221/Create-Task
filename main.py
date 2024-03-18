#import tkinter 
import tkinter

#create window
window = tkinter.Tk()
window.title("Quizz Game")
window.geometry("600x700")

#A list to keep track of all the scores
each_score=[]



#make function to keep track of the points
def point_counter():
    count = 0
    if question_select1.get() == "spanish":
        count= count + 1
    if question_select2.get() == "smith":
        count= count + 1
    if question_select3.get() == "apollo":
        count= count + 1
    if question_select4.get() == "yellow":
        count= count + 1
    if question_select5.get() == "saturn":
        count= count + 1
    count_label.config( text="Your score is: "+ str(count))
    each_score.append(count)
    print(each_score)
    
        

#Make a function to see the total of all the previous scores
def total_score_count():
    global each_score
    score=0
    for i in each_score:
        score= score + i
    total_label.config(text="The Total of all your Scores is: "+ str(score))



#welcome label
welcome_label = tkinter.Label(window, text="Welcome!")
welcome_label.pack()

#instructions
intro = tkinter.Label(window,text="Welcome to my quizz game please select your anwser and if you get it correct your score will go up! ")
intro.pack()

#create the questions 
question_select1 = tkinter.StringVar(value=" ")
question_1 = tkinter.Label(window, text = "Which language has the more native speakers: English or Spanish?")
q1_anwser1 = tkinter.Radiobutton(window, text = "English", value = "english", variable = question_select1 )
q1_anwser2 = tkinter.Radiobutton(window, text = "Spanish", value = "spanish", variable = question_select1)
question_1.pack()
q1_anwser1.pack()
q1_anwser2.pack()

question_select2 = tkinter.StringVar(value=" ")
question_2 = tkinter.Label(window, text = "What is the most common surname in the United States?")
q2_anwser1 = tkinter.Radiobutton(window, text = "Johnson", value = "johnson", variable = question_select2 )
q2_anwser2 = tkinter.Radiobutton(window, text = "Smith", value = "smith", variable = question_select2)
q2_anwser3 = tkinter.Radiobutton(window, text = "Jones", value = "jones", variable = question_select2)
q2_anwser4 = tkinter.Radiobutton(window, text = "Brown", value = "brown", variable = question_select2)
question_2.pack()
q2_anwser1.pack()
q2_anwser2.pack()
q2_anwser3.pack()
q2_anwser4.pack()

question_select3 = tkinter.StringVar(value=" ")
question_3 = tkinter.Label(window, text = "Who was the Ancient Greek God of the Sun?")
q3_anwser1 = tkinter.Radiobutton(window, text = "Hermes", value = "hermes", variable = question_select3 )
q3_anwser2 = tkinter.Radiobutton(window, text = "Artimis", value = "artimis", variable = question_select3)
q3_anwser3 = tkinter.Radiobutton(window, text = "Apollo", value = "apollo", variable = question_select3)
q3_anwser4 = tkinter.Radiobutton(window, text = "Ares", value = "ares", variable = question_select3)
question_3.pack()
q3_anwser1.pack()
q3_anwser2.pack()
q3_anwser3.pack()
q3_anwser4.pack()

question_select4 = tkinter.StringVar(value=" ")
question_4 = tkinter.Label(window, text = "Aureolin is a shade of what color? ")
q4_anwser1 = tkinter.Radiobutton(window, text = "Green", value = "green", variable = question_select4 )
q4_anwser2 = tkinter.Radiobutton(window, text = "Yellow", value = "yellow", variable = question_select4)
q4_anwser3 = tkinter.Radiobutton(window, text = "Red", value = "red", variable = question_select4)
q4_anwser4 = tkinter.Radiobutton(window, text = "Blue", value = "blue", variable = question_select4)
question_4.pack()
q4_anwser1.pack()
q4_anwser2.pack()
q4_anwser3.pack()
q4_anwser4.pack()

question_select5 = tkinter.StringVar(value=" ")
question_5 = tkinter.Label(window, text = "Which planet has the most moons? ")
q5_anwser1 = tkinter.Radiobutton(window, text = "Saturn", value = "saturn", variable = question_select5 )
q5_anwser2 = tkinter.Radiobutton(window, text = "Mars", value = "mars", variable = question_select5)
q5_anwser3 = tkinter.Radiobutton(window, text = "Jupiter", value = "jupiter", variable = question_select5)
q5_anwser4 = tkinter.Radiobutton(window, text = "Earth", value = "earth", variable = question_select5)
submit_q5 = tkinter.Button(window, text = "Submit", command=point_counter)
question_5.pack()
q5_anwser1.pack()
q5_anwser2.pack()
q5_anwser3.pack()
q5_anwser4.pack()
submit_q5.pack(pady=20)

#print the score
count_label=tkinter.Label(window, text="Your score is: ")
count_label.pack()

#total scoe button
total= tkinter.Button(window, text="Total Combined score", command=total_score_count)
total.pack()

#prints the total scores
total_label= tkinter.Label(window)
total_label.pack()

tkinter.mainloop()
