from tkinter import *
window=Tk()
window.geometry("1500x500")





label=Label(window, text=("Enter your already done course codes in CSV format"))
label.pack()

e=Entry(window,width=90)
e.pack()

def logicxx(coursesDone):

    print("coursesDone", coursesDone)

    #
    # coursesDone=['CSE110', 'CSE111', 'CSE220', 'CSE221', 'CSE230', 'CSE260','PHY111', 'PHY112', 'MAT110', 'MAT120', 'MAT215','BUS101',]

    s = {
        "CSE110": [0, 3],
        "CSE111": ["CSE110", 3],
        "CSE220": ['CSE111', 3],
        "CSE221": ['CSE220', 3],
        "CSE230": [0, 2],
        "CSE260": [0, 2],
        "CSE250": ["PHY112", 3],
        "CSE330": ["MAT120", 2],
        "CSE321": ["CSE221", 2],
        "CSE331": ["CSE221", 2],
        "CSE340": ["CSE260", 3],
        "CSE341": ["CSE260", 2],
        "CSE251": ["CSE250", 3],
        "CSE370": ["CSE321", 2],
        "CSE420": ["CSE331", 3],
        "PHY111": [0, 2],
        "PHY112": ["PHY111", 3],
        "MAT110": [0, 2],
        "MAT120": ["MAT110", 2],
        "MAT215": ["MAT120", 3],
        "MAT216": ["MAT120", 3],
        "BUS101": [0, 1],
        "BUS102": [0, 1],
        "ECO101": [0, 1],
        "BIO101": [0, 1],
        "POL101": [0, 1],
        "PSY101": [0, 1],
        "SOC101": [0, 1]

    }

    easy = []
    medium = []
    hard = []

    for i in s:
        if s[i][1] == 1:
            easy.append((i, s[i]))
        elif s[i][1] == 2:
            medium.append((i, s[i]))
        else:
            hard.append((i, s[i]))

    nextSemester = []

    print("DONE", coursesDone)

    count = 0
    for i in hard:
        if count == 2:
            break
        if i[0] not in coursesDone:
            nextSemester.append(i[0])
            count += 1

    for i in medium:
        if count == 3:
            break
        if i[0] not in coursesDone:
            nextSemester.append(i[0])
            count += 1

    for i in easy:
        if count == 4:
            break
        if i[0] not in coursesDone:
            nextSemester.append(i[0])
            count += 1

    print("dasdasdasdas",nextSemester)
    nextSemesterX=""
    for i in nextSemester:
        nextSemesterX+=i+" "

    label3 = Label(window, text=("Suggest courses for next semester  "+nextSemesterX))
    label3.pack()

    # print(easy)
    # print(medium)
    # print("HARD",hard)




def submitHandler():
    coursesDone = e.get()
    label2 = Label(window, text=("Courses you have done so far: "+coursesDone))
    logicxx(coursesDone)
    label2.pack()

submitBtn=Button(window, text="Submit courses", command=submitHandler)
submitBtn.pack()




window.mainloop()


