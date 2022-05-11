import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Tkinterdb",
    port=4306
)
mycursor=mydb.cursor()
# mycursor.execute("""
#                  create table company(
#                      companyid int AUTO_INCREMENT, 
#                      name varchar(255),
#                      mailing_name varchar(255),
#                      address varchar(255),
#                       email varchar(255),
#  		             state varchar(255),
#  		             country varchar(255),
#  		             pincode int,
#                       telephone varchar(200),
#                       mobile varchar(200),
#                       fax varchar(200),
#                       website varchar(200),
#                       financial_year DATE,
#                       year_begin DATE,
#                       currency varchar(200),
#                      currencysign int,
# 		             currsignplace varchar(255),
#                      decimalseperator varchar(155),
#                      excurrency varchar(255),
#                      PRIMARY KEY(companyid))
#                 """)

