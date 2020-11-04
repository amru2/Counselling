
 # RAJALAKSHMI ENGINEERING COLLEGE
def avail():
    dept=input("choose any one:mct,mech,eee,aero,it,cse,ece,bio tech")
    if(dept=="mct" or dept=="mech" or dept=="eee" or dept=="ece" or dept=="it" or dept=="cse" or dept=="aero" or dept=="bio tech"):
         print("WELCOME TO RAJALAKSHMI ENGINEERING COLLEGE")
# RAJALAKSHMI INSTITUTE OF TECHNOLOGY
def availl():
    dept=input("choose any one:mech,eee,it,cse,ece,bio tech")
    if(dept=="mech" or dept=="eee" or dept=="ece" or dept=="it" or dept=="cse" or dept=="bio tech"):
         print("WELCOME TO RAJALAKSHMI INSTITUTE OF TECHNOLOGY")
# SRI VENKATESHWARA COLLEGE OF ENGINEERING
def availll():
    dept=input("choose any one:mech,eee,aero,it,cse,ece,bio tech")
    if(dept=="mech" or dept=="eee" or dept=="ece" or dept=="it" or dept=="cse" or dept=="aero" or dept=="bio tech"):
         print("WELCOME TO SRI VENKATESHWARA COLLEGE OF ENGINEERING")
# PANIMALAR ENGINEERING COLLEGE
def availlll():
    dept=input("choose any one:mech,eee,aero,it,cse,ece,bio tech")
    if(dept=="mech" or dept=="eee" or dept=="ece" or dept=="it" or dept=="cse" or dept=="aero" or dept=="bio tech"):
         print("WELCOME TO PANIMALAR ENGINEERING COLLEGE")
# PANIMALAR INSTITUTE OF TECHNOLOGY
def availllll():
    dept=input("choose any one:mech,eee,it,cse,ece,bio tech")
    if(dept=="mech" or dept=="eee" or dept=="ece" or dept=="it" or dept=="cse" or dept=="bio tech"):
         print("WELCOME TO PANIMALAR INSTITUTE OF TECHNOLOGY ")
#Cutoff
def cutoff(x,y,z):
        co=(x/4)+(y/4)+(z/2)
        return co

#INPUT

p=float(input("enter the physics mark"))
c=float(input("enter the chemistry mark"))
m=float(input("enter the maths mark"))
l=cutoff(p,c,m)
if(l<=158):
      print("try any other college")
      print("YOU ARE NOT ELIGIBLE TO BE PLACED IN THESE FIVE(SVC REC RIT PEC PIT) COLLEGES")
      print(" THANKS FOR COMING")

#Check for REC    
def rec(l,cat):
        if(cat=="fc"):
            if(l>198):
                 avail()
            else:
                print("try any other college")
                clg=input("choose any one: rit pec pit")
                if(clg=="rit"):
                       rit(l,cat)
                if(clg=="pec"):
                       pec(l,cat)
                if(clg=="pit"):
                       pit(l,cat)
       
        if(cat=="bc" or cat=="mbc"):
              if(l>190):
                   avail()
              else:
                 print("try any other college")
                 clg=input("choose any one: rit pec pit")
                 if(clg=="rit"):
                        rit(l,cat)
                 if(clg=="pec"):
                     pec(l,cat)
                 if(clg=="pit"):
                     pit(l,cat)
       
        if(cat=="sc" or cat=="st"):
                if (l>177):
                      avail()
                else:
                    print("try any other college")
                    clg=input("choose any one: rit pec pit")
                    if(clg=="rit"):
                        rit(l,cat)
                    if(clg=="pec"):
                        pec(l,cat)
                    if(clg=="pit"):
                        pit(l,cat)
       
        
            

#Check for RIT
def rit(l,cat):
        if (cat=="fc"):
            if(l>195):
                 availl()
            else:
                  print("try any other college")
                  clg=input("choose any one: pec pit")
                  if(clg=="pec"):
                          pec(l,cat)
                  if(clg=="pit"):
                           pit(l,cat)
                
        if(cat=="bc" or cat=="mbc"):
              if(l>185):
                   availl()
              else:
                print("try any other college")
                clg=input("choose any one: pec pit")
                if(clg=="pec"):
                      pec(l,cat)
                if(clg=="pit"):
                      pit(l,cat)
        if(cat=="sc" or cat=="st"):
                if (l>172):
                      availl()
                else:
                   print("try any other college")
                   clg=input("choose any one: pec pit")
                   if(clg=="pec"):
                      pec(l,cat)
                   if(clg=="pit"):
                        pit(l,cat)
             
             


#Check for SVC
def svc(l,cat):
        if (cat=="fc"):
            if(l>199): 
                 availll()
            else:
                print("try any other college")
                clg=input("choose any one: rec rit pec pit")
                if(clg=="rec"):
                  rec(l,cat)
                if(clg=="rit"):
                    rit(l,cat)
                if(clg=="pec"):
                  pec(l,cat)
                if(clg=="pit"):
                  pit(l,cat)
        if(cat=="bc" or cat=="mbc"):
              if(l>192):
                   availll()
              else:
                
                 print("try any other college")
                 clg=input("choose any one: rec rit pec pit")
                 if(clg=="rec"):
                  rec(l,cat)
                 if(clg=="rit"):
                    rit(l,cat)
                 if(clg=="pec"):
                    pec(l,cat)
                 if(clg=="pit"):
                     pit(l,cat)
        if(cat=="sc" or cat=="st"):
                if (l>180):
                      availll()
                else:
                   print("try any other college")
                   clg=input("choose any one: rec rit pec pit")
                   if(clg=="rec"):
                        rec(l,cat)
                   if(clg=="rit"):
                      rit(l,cat)
                   if(clg=="pec"):
                        pec(l,cat)
                   if(clg=="pit"):
                        pit(l,cat)
        
               

#Check for PEC
def pec(l,cat):
        if (cat=="fc"):
            if(l>190):
                 availlll()
            else:
                 print("try any other college")
                 clg=input("only pit is available,if you want pit : enter yes and if you don't want : enter no")
                 if(clg=="yes"):
                    pit(l,cat)
                 if(clg=="no"):
                     print("YOU ARE NOT ELIGIBLE TO BE PLACED IN THESE FIVE(SVC REC RIT PEC PIT) COLLEGES")
                     print(" THANKS FOR COMING")
        
        if(cat=="bc" or cat=="mbc"):
              if(l>178):
                   availlll()
              else:
                 print("try any other college")
                 clg=input("only pit is available,if you want pit : enter yes and if you don't want : enter no")
                 if(clg=="yes"):
                    pit(l,cat)
                 if(clg=="no"):
                     print("YOU ARE NOT ELIGIBLE TO BE PLACED IN THESE FIVE(SVC REC RIT PEC PIT) COLLEGES")
                     print(" THANKS FOR COMING")
        
        if(cat=="sc" or cat=="st"):
                if (l>162):
                      availlll()
                else:
                    print("try any other college")
                    clg=input("only pit is available,if you want pit : enter yes and if you don't want : enter no")
                    if(clg=="yes"):
                         pit(l,cat)
                    if(clg=="no"):
                       print("YOU ARE NOT ELIGIBLE TO BE PLACED IN THESE FIVE(SVC REC RIT PEC PIT) COLLEGES")
                       print(" THANKS FOR COMING")
        
            
#Check for PIT
def pit(l,cat):
        if (cat=="fc"):
            if(l>185):
                 availllll()
            else:
                print("try any other college")
                print("YOU ARE NOT ELIGIBLE TO BE PLACED IN THESE FIVE(SVC REC RIT PEC PIT) COLLEGES")
                print(" THANKS FOR COMING")
        
        if(cat=="bc" or cat=="mbc"):
              if(l>172):
                   availllll()
              else:
                print("try any other college")
                print("YOU ARE NOT ELIGIBLE TO BE PLACED IN THESE FIVE(SVC REC RIT PEC PIT) COLLEGES")
                print(" THANKS FOR COMING")
        
        if(cat=="sc" or cat=="st"):
                if (l>158):
                      availllll()
                else:
                   print("try any other college")
                   print("YOU ARE NOT ELIGIBLE TO BE PLACED IN THESE FIVE(SVC REC RIT PEC PIT) COLLEGES")
                   print(" THANKS FOR COMING")
        
             
#Eligible        
if(l>158):
    cat=input("enter category")
    clg=input("choose any one: rec rit svc pec pit")
    if(clg=="rec"):
          rec(l,cat)
    if(clg=="rit"):
          rit(l,cat)
    if(clg=="svc"):
           svc(l,cat)
    if(clg=="pec"):
          pec(l,cat)
    if(clg=="pit"):
           pit(l,cat)
