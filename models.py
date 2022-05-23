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
#                       currencysign varchar(100),
#                       currency varchar(200),
#                       PRIMARY KEY(companyid))
#                 """)

# mycursor.execute(
#     "create table currency(symbol c,formal_name varchar(200),currency_code varchar(200),decimal_places int,amount_in_millions varchar(100),suffix_symbol varchar(100),space varchar(100),word_repsn varchar(100),decimal_words varchar(200))")

# mycursor.execute(
#     "create table voucher(name varchar(200),type varchar(200),abbreviation varchar(200),voucher_activate varchar(100),voucher_method varchar(200),Use_effective_dates varchar(100),allow_zero_valued varchar(100),voucher_type_optional varchar(100),voucher_narration varchar(100),ledger_narration varchar(200),voucher_saving varchar(200))")

# mycursor.execute(
#     "create table stockGroup(stock_id int AUTO_INCREMENT,name varchar(200),stock_under varchar(200),stock_quantities varchar(200),stock_details varchar(200), PRIMARY KEY(stock_id))")

# mycursor.execute(
#     "create table stock_Catagory(stock_id int AUTO_INCREMENT,name varchar(200),PRIMARY KEY(stock_id))")

# mycursor.execute(
#     "create table stock_item(stock_itemid int AUTO_INCREMENT,stock_id int,name varchar(200),units varchar(200),gst_applicable varchar(200),gst_details varchar(200),supply_type varchar(200), PRIMARY KEY(stock_itemid),FOREIGN KEY(stock_id) REFERENCES stockGroup(stock_id) ON DELETE CASCADE)")

# mycursor.execute(
#     "create table unit(unit_id int AUTO_INCREMENT,type varchar(200),symbol varchar(100),formal_name varchar(200),quantity_code varchar(200),no_of_decimal_places int,PRIMARY KEY(unit_id))")

# mycursor.execute(
#     "create table godown(gd_id int AUTO_INCREMENT,name varchar(200),under varchar(200),PRIMARY KEY(gd_id))")
        
# mycursor.execute('drop table unit')
