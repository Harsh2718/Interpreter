import sys


def input_txt():
    lines = [] # initalise to empty list
    lines1=[]
    with open('input_file.txt') as  f:
        lines = f.readlines() # read all lines into a list of strings
    for i in range(len(lines)):
        lines1.append(lines[i].strip())   #Using strip() function to remove \n from the input list
    return lines




def interpreter():
    L=input_txt()  #Initialising l to input text file with each represented as a sublist of list L
    lenL=[]
    DATA=[]                #defining a lot of empty lists for further use in the code
    l=[]
    l3=[]
    garbage=[]
    i1=[]
    i2=[]
    op=['+','−','∗','/','>','<','>=','<=','==','!=','and','or','not',"%"]   #list containing operators

    for statement in L: # each statement is on a separate line
        token_list = statement.split() # split a statement into a list of tokens
        l.append(token_list)


    for i in range(len(l)):    #USING A for loop to interpret each line in the list
        p=l[i]                 #Taking the ith line of the input text file into p

        l1=p[2:]               #Separating the RHS using slicing

        s=""


        for k in range(len(l1)):   #HERE I HAVE RUN A LOOP FOR CHECKING ELEMENTS OF RHS
                                   #IF ANY ERROR IS IDENTIFIED IN THE INPUT
                                   #THE CODE IS TERMINATED WITHOUT ANY FURTHER EXECUTION
            if(len(l1)==2) :

                if(l1[1] in op):

                    sys.exit("INVALID SYNTAX")

                if(l1[0] != "-" and l1[0]!= "not" and l1[0] in op):

                    sys.exit("INVALID SYNTAX")

            if(len(l1)==3):

                if(l1[0] in op or l1[2] in op):

                    sys.exit("INVALID SYNTAX")
            if(len(l1)==1):

                if(l1[0] in op):

                    sys.exit("INVALID SYNTAX")

            if(l1[k].isnumeric() or l1[k]=="True" or l1[k]=="False"):

                #APPENDING INT AND BOOL VALUES TO DATA IF IT's NOT PRESENT ALREADY IN DATA
                if(l1[k] not in DATA):

                    DATA.append((l1[k]))
        m=0       #VARIABLE USED TO STORE THE VALUE OBTAINED ON EVALUATION RHS

        flag=0    #COUNTER VARIABLE TO CHECK IF THERE ARE ANY ALPHABET STRINGS ON RHS

        for b in l1:

            if(b.isalpha()):

                flag=flag+1  #INCREMENTING FLAG BY 1 IF ANY ALPHABET IS FOUND


        if(flag==0):    #IF THERE ARE NO ALPHABETS

            for a in l1:
                              #CONVERTING RHS AS A STRING OF EXPRESSION
                s=s+a+" "

            if (type( eval(s))==float):

                m=str( int(eval(s)))

            else:                      #USING eval() FUNCTION TO OBTAIN THE VALUE OF THE EXPRESSION

                m=str( eval(s))

            if(m not in DATA):

               DATA.append(m)         #APPENDING THE CALCULATED VALUE TO DATA

            f=False
            for g in DATA:            #NOW I HAVE USED A SEARCH LOOP FOR TESTING
                                      #IF THE VARIABLE HAS ALREADY BEEN ASSIGNED ANY VALUE

                if(type(g)==tuple):
                    if (g[0]==p[0]):
                        m1=DATA.index(g)
                        y=(p[0],DATA.index(m))
                        f=True
                else:
                    y=(p[0],DATA.index(m))
            if(f==True):            #IF FOUND
                                    #OVERWRITING THE VALUE OF THE VARIABLE AND REFERING IT TO NEW INDEX
                DATA[m1]=y
            else:
                DATA.append(y)     #ELSE APPENDING THE VARIABLE AND REFERENCE TO THE DATA LIST

        else:

            l5=[]
            for a in l1:     #RUNNING A SEARCH LOOP FOR RHS SIDE OF EXPRESSION

                l5.append(a)

                if(a.isalpha() and not((a=="False")or(a=="True")or(a in op))):   #CHECKING IF ELEMENT IS ALPHABET OR NOT

                    if(any(a in i for i in DATA if isinstance(i,tuple))):       #CHECKING IF THE ELEMENT IS ALREADY PRESENT IN A TUPLE IN DATA LIST
                                                                                #FOR THAT PURPOSE I HAVE USED any KEYWORD

                        for tup in range(len(DATA)):

                            if(type(DATA[tup])==tuple and a in DATA[tup]):

                                i1.append(a)                     #IF ITS PRESENT IN DATA APPENDING IT TO LIST i1 AND APPENDING ITS INDEX INTO i2

                                i2.append(tup)
                    if( a in l5 and a not in i1):                               #IF AN ELEMENT IS PRESENT IN RHS BUT NOT IN LIST i1 THEN RETURNING AN ERROR

                        sys.exit("Variable" + " " + a + " " + "is not defined")

                    else:

                        vo=max(i2)     #IF VARIABLE PRESENT IN DATA THEN  STORING ITS INDEX IN vo

                        x=DATA[vo]     #STORING THE TUPLE IN A VARIABLE AND THEN OBTAINING THE INDEX TO WHICH IT WAS REFERRING TO


                        z=x[1]

                        y=str(DATA[z]) #OBTAINING THE VALUE OF THE VARIABLE a FROM THE REFERENCE WE OBTAINED


                        l1= list(map(lambda x: x.replace(a,y), l1))   #I HAVE USED LAMBDA FUNCTION TO REPLACE THE VARIABLE WITH ITS VALUE IN LIST l1
                                                                      #IT WILL BE EASIER TO CALCULATE THE EXPRESSION IN THIS WAY


            m=0

            for a in l1:    #CONVERTING RHS AS A STRING OF EXPRESSION
                s=s+a+" "

            if (type( eval(s))==float):

                m= str(int(eval(s)))

            else:                    #USING eval() FUNCTION TO OBTAIN THE VALUE OF THE EXPRESSION

                m= str(eval(s))

            if(m not in DATA):

                DATA.append(m)      #APPENDING THE CALCULATED VALUE TO DATA IF ITS ALREADY NOT PRESENT

            f=False

            for g in DATA:        #NOW I HAVE USED A SEARCH LOOP FOR TESTING
                                  #IF THE VARIABLE HAS ALREADY BEEN ASSIGNED ANY VALUE

                if(type(g)==tuple):

                    if (g[0]==p[0]):

                        m1=DATA.index(g)

                        y=(p[0],DATA.index(m))

                        f=True
                else:
                    y=(p[0],DATA.index(m))

            if(f==True):        #IF FOUND
                                #OVERWRITING THE VALUE OF THE VARIABLE AND REFERING IT TO NEW INDEX

                DATA[m1]=y

            else:

                DATA.append(y)  #ELSE APPENDING THE VARIABLE AND REFERENCE TO THE DATA LIST

    for o in DATA:
        if(type(o)==tuple):

            x1=DATA.index(o)
            lenL.append(x1)     #STORING INDICES OF TUPLES AND THE REFERENCE INDEX IN THE TUPLE IN lenL
            l3.append(x1)       #STORING INDICES OF TUPLES IN l3
            l2=DATA[x1]
            lenL.append(l2[1])

    for c in DATA:           #CHECKING FOR ELEMENTS IN DATA THAT ARENT TUPLES AND
                             #WHICH ARE NOT REFERENCED BY ANY VALUE AND APPENDING TO GARBAGE

        if(DATA.index(c) not in lenL):
            garbage.append(c)

    out1=[]

    out2=[]
    for j in l3:    #LIST l3 CONTAINS INDICES OF TUPLES IN DATA

        out1.append(DATA[j][0])    #APPENDING VARIABLES INTO out1
        out2.append(DATA[j][1])    #APPENDING REFERENCE INDEX INTO out2

    DATALIST=convert(DATA)        #CONVERTING THE DATA LIST IN WHICH ELEMENTS ARE IN THEIR RESPECTIVE DATA TYPES



    print("DATA LIST =", DATALIST)

    for i in range(len(out1)): #USING A FOR LOOP TO PRINT THE NAME AND VALUE OF THE VARIABLE


        print("The Value Of The Variable" + " " + out1[i] +" " + "=",DATALIST[out2[i]])

#PRINTING THE GARBAGE LIST

    print("Garbage List =",convert(garbage))




#HELPER FUNCTION convert() WHICH IS USED TO CONVERT THE DATA TYPE OF EACH ELEMENT FROM STRING TO THEIR RESPECTIVE DATA TYPE
def convert(L):

    for c in L:     #EMPLOYING A SEARCH RANGE FOR CHECKING THE LIST L AND THEN OVERWRITING THE PARTICULAR VALUES IN THE LIST
                    #INTO THEIR CORRESPONDING DATA TYPES


        if(not type(c)==tuple):
            if(c[0]=='-'):

                m=L.index(c)
                L[m]=-int(c[1])
            if(c.isnumeric()):
                m=L.index(c)
                L[m]=int(c)
            if(c=="True"):
                m=L.index(c)
                L[m]=True
            if(c=="False"):
                m=L.index(c)
                L[m]=False

#OUTPUT IS THE OVERWRITTEN FORM OF INPUT LIST L WHICH HAS THE REPRESENTATION OF ANY ELEMENT IN ITS CORRECT DATA TYPE AND NOT AS STRINGS
    return L
interpreter()




