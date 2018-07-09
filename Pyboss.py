#-*- coding: UTF-8 -*-
#importing the dependencies   
import os
import csv
import datetime


#placeholders for the reformatted content
em_id = []
em_first_name = []
em_last_name = []
em_dob = []
em_ssn = []
em_state = []


#Dictionary of states with their abbreviations

Abbreviated_State_Name_Dict ={
    'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA',
'Colorado': 'CO','Connecticut': 'CT','Delaware': 'DE','Florida': 'FL','Georgia': 'GA',
'Hawaii': 'HI','Idaho': 'ID','Illinois': 'IL','Indiana': 'IN','Iowa': 'IA',
'Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA','Maine': 'ME','Maryland': 'MD',
'Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS',
'Missouri': 'MO','Montana': 'MT','Nebraska': 'NE','Nevada': 'NV','New Hampshire': 'NH',
'New Jersey': 'NJ','New Mexico': 'NM','New York': 'NY','North Carolina': 'NC',
'North Dakota': 'ND','Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA',
'Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN',
'Texas': 'TX','Utah': 'UT','Vermont': 'VT','Virginia': 'VA','Washington': 'WA',
'West Virginia': 'WV','Wisconsin': 'WI','Wyoming': 'WY'}


#Reading the csv one line at a time
csv_path = os.path.join('/Users/tegaileleji/Desktop/UCBSAN201805DATA1/02-Homework/03-Python/Instructions/solutions/PyBoss/raw_data/employee_data1.csv')

with open(csv_path,"r") as csvfile:
    reading_the_csv = csv.DictReader(csvfile) #delimiter=","
    
    next(reading_the_csv)
    
 
#print(csvfile)
#Reading through the rows, collecting the reduirements and storing it in a list
    for row in reading_the_csv:
        
    #em_id += em_id.append(row[1])
#grab employee IDs and store in a list
        em_id = em_id.append(row[0])
        
        print(em_id)
    
#Collect the names, split them and store them in the list temporarily 
        name_split = row[1] #you can also use another option #name_split = row["Name"].split(" ")
        em_first_name = em_first_name.append[name_split[0]]
        em_last_name = em_last_name.append[name_split[1]]
    
    
#Grab the date of birth and reformat it 
    
        date_formatted_1 =  datetime.datetime.strptime(row[2], "%Y-%m-%d")
        date_formatted_1 = date_formatted_1.strptime("%m-%d-%Y")
        em_dob.append(date_formatted_1)
    
#Grab the SSN and reformat it 
        ssn = row[3]
        ssn_spliting = ssn.split("-")
        em_ssn.append(f"***-**-{ssn_spliting[2]}")
    
#Grab the state from the dictionary
        states = Abbreviated_State_Name_Dict(row[4])
        em_state.append(states)
    
    
#zip the lists together 
employees = zip(em_id,em_first_name,em_last_name,em_dob,em_ssn,em_state)
    
 # save as csv
save_filepath = filename.strip(".csv") + "_reformatted.csv"
employee_list = list(employees)   
    
    
    
with open(save_filepath,"w", newline="") as csvfile:
    csvwriter =csv.writer(csvfile, delimiter = ",")

    csvwriter.writerow(["Emp ID","First Name","Last Name","DOB","SSN", "State"])
    for row in writing_the_csv:
        csvwriter.writerow(row)  
        
        
        
        
        
        
        
        
        