import mysql.connector 
import guipython as db

criteria = list(db.selected_options)
#print(criteria)

degrees = ['Btech', 'Mtech']
courses = ['CSE', 'CSE AIML', 'CSE AIR', 'CSE CPS', 'EEE', 'ECM', 'Mech', 'Mechatronics']
years = ['1st Year', '2nd Year', '3rd Year', '4th Year']
accomodations = ['Hosteller', 'Day-Scholar']
hostel_blocks = ['A', 'D1', 'D2', 'B', 'C']
cgpas = ['CGPA Above 9.0', 'CGPA Below 9.0']

sql_query = "SELECT email FROM student_details WHERE "

conditions = []
current_column_conditions = []
current_column = None

for criterion in criteria:
    condition = None
    if criterion in degrees:
        condition = "degree='" + criterion + "'"
    elif criterion in years:
        condition = "year_of_study='" + criterion + "'"
    elif criterion in courses:
        condition = "course='" + criterion + "'"
    elif criterion in accomodations:
        condition = "accomodation_type='" + criterion + "'"
    elif criterion in hostel_blocks:
        condition = "hostel='" + criterion + "'"
    elif criterion in cgpas:
        if criterion == 'CGPA Above 9.0':
            condition = "cgpa > 9.0"
        else:
            condition = "cgpa <= 9.0"

    if condition:
        if current_column is None:
            current_column_conditions.append(condition)
            current_column = condition.split('=')[0]
        elif condition.split('=')[0] == current_column:
            current_column_conditions.append(condition)
        else:
            conditions.append("(" + " OR ".join(current_column_conditions) + ")")
            current_column_conditions = [condition]
            current_column = condition.split('=')[0]

# Add the last column's conditions
if current_column_conditions:
    conditions.append("(" + " OR ".join(current_column_conditions) + ")")

# Join all conditions using AND
sql_query += " AND ".join(conditions)

print("Generated SQL Query: ", sql_query, "\n")


#establishing the connection
conn = mysql.connector.connect(
   user='root', password='system', host='127.0.0.1', database='email_management')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving single row
sql = str(sql_query)

#Executing the query
cursor.execute(sql)

#Fetching 1st row from the table
result = cursor.fetchmany(size =2);
print(result)
list_of_emails = [email[0] for email in result]
print("List of emails: ",list_of_emails)

#Closing the connection
conn.close()