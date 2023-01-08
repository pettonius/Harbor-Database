import sqlite3
import sys
        
def New_Ship():
        ax=input('Νέο Ship_Id ')
        bx=input('Όνομα πολοίου ')
        cx=input('Μήκος πλοίου ')
        dx=input('Πλάτος πλοίου ')
        ex=input('Βάρος πλοίου ')
        if ex=="": ex="NULL"
        else: ex="'"+ex+"'"
        fx=input('Ημερομηνία κατασκευής ')
        if fx=="": fx="NULL"
        else: fx="'"+fx+"'"
        gx=input('Ιδιοκτήτης ')
        if gx=="": gx="NULL"
        else: gx="'"+gx+"'"
        code="INSERT INTO 'Ship' VALUES ('" +ax+"','"+bx+"',"+cx+","+dx+","+ex+","+fx+","+gx+")"
        c.execute(code)
        return(ax)
def New_Cargo():       
        print('Τα αγαθα μεταφέρονται ως:')
        print('1 Bulk')
        inp=input('2 Container ') 
        ax=input('Shipment_Id ')
        bx=input('Τύπος εμπορεύματος ')
        cx=input('Είναι εύθραυστο; ')
        dx=input('Είναι επικίνδυνο ')
        ex=input('Σημειώσεις για ειδική μεταχείρηση: ')
        if ex=="": ex="NULL"
        else: ex="'"+ex+"'"
        if dx=="": dx="FALSE"
        if cx=="": cx="FALSE"
        if inp=="1": 
            fx='bulk'
            gx=input('Όγκος ')
            code="INSERT INTO 'Cargo' VALUES ('" +ax+"','"+bx+"','"+fx+"',"+gx+",NULL,"+cx+","+dx+","+ex+")"
            c.execute(code)       
        if inp=="2": 
            fx='container'
            gx=input('Αριθμός Container ')
            code="INSERT INTO 'Cargo' VALUES ('" +ax+"','"+bx+"','"+fx+"',NULL,"+gx+","+cx+","+dx+","+ex+")"
            c.execute(code)  
        return(ax)
def New_Port():  
        ax=input('Port_Id ')
        bx=input('Χώρα ')
        cx=input('Πόλη ')
        code="INSERT INTO 'Port' VALUES ('" +ax+"','"+bx+"','"+cx+"')"
        c.execute(code) 
        return(ax)
def New_Station():
        ax=input('Station_Id ')
        bx=input('Ελάχιστο μήκος πλοίου ')
        cx=input('Μέγιστο μήκος πλοίου ')
        dx=input('Ελάχιστο πλάτος πλοίου ')
        ex=input('Μέγιστο πλάτος πλοίου ')
        code="INSERT INTO 'Station' VALUES ('" +ax+"',"+bx+","+cx+","+dx+","+ex+")"
        c.execute(code) 
        return(ax)
def New_Arrival(Ship_Id,Shipment_Id,Port_Id,Station_Id):
        ax=input('Expected DateTime ')
        bx=input('Actual DateTime ')
        code="INSERT INTO 'Arrival' VALUES ('" +Station_Id+"','"+Shipment_Id+"','"+Ship_Id+"','"+Port_Id+"','"+ax+"','"+bx+"')"
        c.execute(code)
def New_Departure(Ship_Id,Shipment_Id,Port_Id,Station_Id):
        ax=input('Expected DateTime ')
        bx=input('Actual DateTime ')
        code="INSERT INTO 'Departure' VALUES ('" +Station_Id+"','"+Shipment_Id+"','"+Ship_Id+"','"+Port_Id+"','"+ax+"','"+bx+"')"
        c.execute(code)


connection = sqlite3.connect("Database.db")
c=connection.cursor()
print('1: Εισαγωγή νέου δρομολογίου')
print('2: Διαγραφή στοιχείου')
print('3: Εμφάνηση όλων των δεδομένων για')
print('4: Απευθείας επεξεργασία της βάσης με κώδικα sqlite')
print('5: Συχνές αναζητήσεις')
x = input('Ποιά ενέργεια θα θέλατε να υλοποιήσετε;')


###################################INSERT DATA###################################
if x=="1":
    z=input('Πρόκειται για νέο πλοίο; [Y/Ν]')
    if z=="Y":
        Ship_Id=New_Ship()
    if z=='N':
        Ship_Id=input('Δώστε το Ship_Id ')
    z=input('Πρόκειται για νέο αγαθό; [Y/Ν]')
    if z=="Y":
        Shipment_Id=New_Cargo()
    if z=="N":
        Shipment_Id=input('Δώστε το Shipment_Id ')
    m=input('Πρόκειται για νέα άφιξη[1] ή αναχώρηση[2]')
    z=input('Το πλοίο έρχεται/αναχωρεί από/προς γνωστό λιμάνι;[Y/Ν]')
    if z=="N":
        Port_Id=New_Port()
    if z=="Y":
        Port_Id=input('Δώστε το Port_Id ')
    if m=="1":
        z=input('Θα παραμέινει σε νέο σταθμό; [Y/Ν]')
        if z=="Y":
            try:
                Station_Id=New_Station()
            except:
                r=input('Λάθος εισαγωγή δεδομένων, θέλετε να προσπαθήσετε ξανα; [Y/Ν]')
                if r=="Y":
                    try:
                        Station_Id=New_Station()
                    except:
                        print('Λάθος εισαγωγή δεδομένων')
                        sys.exit()
        if z=='N':
            Station_Id=input('Δώστε το Station_Id ')     
        New_Arrival(Ship_Id,Shipment_Id,Port_Id,Station_Id)

        
    if m=="2":
        Station_Id=input('Δώστε το Station_Id ')     
        New_Departure(Ship_Id,Shipment_Id,Port_Id,Station_Id)

       
###################################DELETE DATA###################################
if x=="2":
    print('1: Διαγραφή δεδομένων πλοίου')
    print('2: Διαγραφή δεδομένων εμπορεύματος')
    print('3: Διαγραφή δεδομένων ξένου λιμανιού')
    print('4: Διαγραφή δεδομένων χώρου στάθμευσης')
    print('5: Διαγραφή δεδομένων αποθήκευσης')
    print('6: Διαγραφή δεδομένων άφιξης πλοίου')
    print('7: Διαγραφή δεδομένων αναχώρησης πλοίου')
    y=input('Ποιά ενέργεια θα θέλατε να υλοποιήσετε;')
    try:
        if y=="1":
                    inp=input('Δώστε το Ship_Id του πλοίου που θέλετε να διαγράψετε: ')
                    code="DELETE FROM Ship WHERE Ship_Id=="+inp
                    c.execute(code)
        if y=="2":
                    inp=input('Δώστε το Ship_Id του εμπορεύματος που θέλετε να διαγράψετε: ')
                    code="DELETE FROM Cargo WHERE Shipment_Id=="+inp
                    c.execute(code)
        if y=="3":
                    inp=input('Δώστε το Port_Id του λιμανιού που θέλετε να διαγράψετε: ')
                    code="DELETE FROM Port WHERE Port_Id=="+inp
                    c.execute(code)    
        if y=="4":
                    inp=input('Δώστε το Station_Id του χώρου στάθμευσης που θέλετε να διαγράψετε: ')
                    code="DELETE FROM Station WHERE Station_Id=="+inp
                    c.execute(code)                      
        if y=="5":
                    inp=input('Δώστε το StorageArea_Id του χώρου αποθήκευσης που θέλετε να διαγράψετε: ')
                    code="DELETE FROM StorageArea WHERE StorageArea_Id=="+inp
                    c.execute(code)
                    code="DELETE FROM Warehouse WHERE StorageArea_Id=="+inp
                    c.execute(code)
                    code="DELETE FROM ContainerYard WHERE StorageArea_Id=="+inp
                    c.execute(code)  
                    
        if y=="6":
                    inp=input('Δώστε το Ship_Id των δεδομένων άφιξης που θέλετε να διαγράψετε: ')
                    code="DELETE FROM Arrival WHERE Ship_Id=="+inp
                    c.execute(code)
        if y=="7":
                    inp=input('Δώστε το Ship_Id των δεδομένων αναχώρησης που θέλετε να διαγράψετε: ')
                    code="DELETE FROM Depatrure WHERE Ship_Id=="+inp
                    c.execute(code)                                          
        else:
                    sys.exit()
    except:
            sys.exit('Λάθος εισαγωγή δεδομένων')
       
       
###################################SEARCH DATA###################################
if x=="3":   
    print('Επιλέξτε τον πίνακα που σας ενδιαφέρει: ')
    print('1: Ship')
    print('2: Cargo')
    print('3: Station')
    print('4: Port')
    print('5: StorageArea')
    print('6: Warehouse')
    print('7: ContainerYard')
    print('8: Arrival')
    print('9: Depatrure')
    y=input()
    if y=="1":
                    rec=c.execute('SELECT * FROM ship').fetchall()
                    for row in rec:
                        print("Id: ", row[0])
                        print("Type: ", row[1])
                        print("Width: ", row[2])
                        print("Weight: ", row[3])
                        print("ConstructionDate: ", row[4])
                        print("Owner: ", row[5])
                        print("\n")

    if y=="2":
                    rec=c.execute('SELECT * FROM Cargo').fetchall()
                    for row in rec:
                        print("Id: ", row[0])
                        print("Type: ", row[1])
                        print("ShipmentMethod: ", row[2])
                        if row[2]=="bulk":
                            print("Volume: ", row[3])
                        if row[2]=="container":
                            print("Container Number: ", row[4])
                        print("Is Fragile: ", row[5])
                        print("Is Dangerous: ", row[6])
                        print("Special_Care: ", row[7])
                        print("\n")
    if y=="3":
                   rec=c.execute('SELECT * FROM Station').fetchall()
                   for row in rec:
                        print("Id: ", row[0])
                        print("Minimum Length: ", row[1])
                        print("Maximum Length: ", row[2])
                        print("Minimum Width: ", row[3])
                        print("Maximum Width: ", row[4])
                        print("\n") 
    if y=="4":
                   rec=c.execute('SELECT * FROM Port').fetchall()
                   for row in rec:
                        print("Id: ", row[0])
                        print("Country: ", row[1])
                        print("City: ", row[2])
                        print("\n")     
    if y=="5":
                   rec=c.execute('SELECT * FROM StorageArea').fetchall()
                   for row in rec:
                        print("Id: ", row[0])
                        print("Merchandise Type: ", row[1])
                        print("Location: ", row[2])
                        print("\n")                        
    if y=="6":
                   rec=c.execute('SELECT * FROM Warehouse').fetchall()
                   for row in rec:
                        print("Id: ", row[0])
                        print("Total Volume Cpacity: ", row[1])
                        print("Free Volume Cpacity: ", row[2])
                        print("\n")
    if y=="7":
                   rec=c.execute('SELECT * FROM ContainerYard').fetchall()
                   for row in rec:
                        print("Id: ", row[0])
                        print("Total Container Space: ", row[1])
                        print("Free Container Space: ", row[2])
                        print("\n")
    if y=="8":
                   rec=c.execute('SELECT * FROM Arrival').fetchall()
                   for row in rec:
                        print("Station_Id: ", row[0])
                        print("Shipment_Id: ", row[1])
                        print("Ship_Id: ", row[2])
                        print("Port_Id: ", row[3])
                        print("Expected Date&Time: ", row[4])
                        print("Actual Date&Time: ", row[5])
                        print("\n") 
    if y=="9":
                   rec=c.execute('SELECT * FROM Depatrure').fetchall()
                   for row in rec:
                        print("Station_Id: ", row[0])
                        print("Shipment_Id: ", row[1])
                        print("Ship_Id: ", row[2])
                        print("Port_Id: ", row[3])
                        print("Expected Date&Time: ", row[4])
                        print("Actual Date&Time: ", row[5])
                        print("\n")                         
    else:
                    sys.exit()
    
    
###################################CUSTOM SQL###################################   
if x=="4":
    code= input('Πληκτρολογίστε τον κώδικα σας:')
    c.execute(code)
    
################################### FAQ ###################################  
if x=="5":
    print('1: Δειξτε τα ονοματα και τον κώδικό των πλοιων που φτανουν στο λιμανι μίας Πόλης.')
    print('2: Δειξτε τα ονοματα των πλοιων που δεν πραγματοποίησαν ταξιδι έναν χρόνο')
    print('3: Δειξτε ποια πλοία (Όνομα πλοίου) μπορούν να σταθμεύσουν σε έναν σταθμό')
    print('4: Δειξτε πόσα πλοία μετέφεραν ένα εμπόρευμα σε μία χώρα;')
    print('5: Δειξτε σε ποιες αποθήκες (id και περιοχη) μπορούμε να αποθηκεύσουμε συγκεκριμμένο βάρος ενός προϊόντος')
    print('6: Δειξτε ποιους σταθμους θα προτιμούσατε για ένα συγκεκριμμένο πλοίο; ')
    print('7: Δειξτε σε ποσες και ποιες αποθήκες για ένα αγαθό δεν έχει γίνει αποθήκευση μετά απο μία χρονιά')
    print('8: Δειξτε Πόσος χρόνος (σε ώρες) μεσολάβησε από την αναχώρηση (depart) ενός πλοίου από το λιμάνι που βρισκόταν και της αποχώρησης του εμπορέυματός του από την αποθήκη στην οποία βρισκόταν')
    print('9: Δείξτε τα ονόματα, τους ιδιοκτήτες και το βάρος των πλοίων που δεν έχουν μεταφέρει δέματα με αλφαβητική σειρά ιδιοκτητών')
    y=input('Ποιά ενέργεια θα θέλατε να υλοποιήσετε;')
    try:
        if y=="1":
                    inp=input('Ποιά Πόλη ')
                    code="""SELECT s.Ship_Id,s.ShipName
                            FROM Ship as s,Port as p,Arrival as a
                            WHERE p.Port_Id = a.Port_Id AND a.Ship_Id = s.Ship_Id AND p.City = '"""+inp+"';"
                    print(c.execute(code).fetchall())
        if y=="2":
                    inp=input('Ποιόν χρόνο; ')
                    code="""SELECT s.ShipName
                        FROM Ship as s
                        EXCEPT
                        SELECT s.ShipName
                        FROM Ship as s, Arrival as a, Departure as d
                        WHERE (s.Ship_Id = a.Ship_Id AND strftime('%Y',a.ActualDateTime) = """+inp+") OR (s.Ship_Id = d.Ship_Id AND strftime('%Y',d.ActualDateTime) = "+inp+");"
                    print(c.execute(code).fetchall()) 
        if y=="3":
                    inp=input('Ποιόν σταθμό; ')
                    code="""SELECT DISTINCT s.ShipName
                        FROM Ship as s, Station as st
                        WHERE s.Length <=st.MaximumLength AND s.Width <= st.MaximumWidth AND st.Station_Id = '"""+inp+"';"
                    print(c.execute(code).fetchall())                   
        if y=="4":
                    inp=input('Τι εμπόρευμα; ')
                    inp1=input('Ποιά χώρα; ')
                    code="""SELECT count(*)
                        FROM Arrival as a,Cargo as c,Port as p
                        WHERE p.Port_Id = a.Port_Id AND c.Shipment_Id = a.Shipment_Id AND c.Type ='"""+inp+"' AND p.Country = '"+inp1+"';"
                    print(c.execute(code).fetchall()) 
                    
        if y=="5":
                    inp=input('Πόσους τόνους; ')
                    inp1=input('Ποιό προϊόν; ')
                    code="""SELECT DISTINCT sa.StorageArea_Id,sa.Location
                        FROM StorageArea as sa,Warehouse as w
                        WHERE sa.StorageArea_Id = w.StorageArea_Id AND sa.MerchandiseType = '"""+inp1+"' AND w.FreeCpacity>"+inp+";"
                    print(c.execute(code).fetchall())
        if y=="6":
                    inp=input('Ποιό πλοίο; ')
                    code="""SELECT Station_Id
                        FROM Station,Ship
                        WHERE MinimumLength < Length AND MaximumLength > Length AND MinimumWidth<Width AND MaximumWidth>Width AND ShipName = '"""+inp+"';"
                    print(c.execute(code).fetchall())  
        if y=="7":
                    inp=input('Τι εμπόρευμα; ')
                    inp1=input('Ποιά χρονιά; ')
                    code="""SELECT count(*),sa.StorageArea_Id
                        FROM StorageArea as sa, Is_Stored as i
                        WHERE sa.StorageArea_Id = i.SA_Id AND strftime('%Y',i.StartDate)>"""+inp1+" AND MerchandiseType = '"+inp+"';"
                    print(c.execute(code).fetchall())
        if y=="8":
                    inp=input('Ποιό πλοίο; ')
                    code="""SELECT ROUND((julianday(EndDate)-julianday(d.ActualDateTime))*60)
                        FROM Departure as d,Is_Stored as i,Ship as s,Cargo as c
                        WHERE ShipName = '"""+inp+"' AND s.Ship_Id = d.Ship_Id AND c.Shipment_Id = d.Shipment_Id AND c.Shipment_Id = i.Shipment_Id;"
                    print(c.execute(code).fetchall())  
        if y=="9":
                    code="""SELECT s.ShipName,s.Owner,s.Weight
                        FROM Ship as s
                        EXCEPT
                        SELECT s.ShipName,s.Owner,s.Weight
                        FROM Ship as s, Arrival as a, Cargo as c
                        WHERE s.Ship_Id = a.Ship_Id AND c.Shipment_Id = a.Shipment_Id AND c.Type = 'package'
                        ORDER BY Owner ASC;"""
                    print(c.execute(code).fetchall())  
        else:sys.exit()
    except: sys.exit()
connection.commit()
connection.close()


