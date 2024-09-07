l=[]
while True:
    c = int(input("""
                 1->Push Elements
                 2->pop Elements
                 3->font elements
                 4->last elements
                 5->display elements
                 6->Exit
                 
                  """))
    if c==1:
        n=input("Enter the value:- ")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Queue is empty")
        else:
            del l[0]
            print(l)
    elif c==3:
        if len(l)==0:
            print("Queue is empty")
        else:
            print("font element is ",l[0])
    elif c==4:
        if len(l)==0:
            print("Queue is empty")
        else:
            print("last element is ",l[-1])
    elif c==5:
        print("Display Queue",l)
    elif c==6:
        break;
    else:
        print("Invalid operator ")