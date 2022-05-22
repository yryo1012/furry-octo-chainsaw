import pyodbc as pdb
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

def login_con():
    instance = "DESKTOP-115PO0H"
    #user = "test"
    #password = "P@ssw0rd!"
    trustedConnection = "yes"
    db = "TESTDB"
    
    #connection = "DRIVER={SQL Server};SERVER=" + instance + ";PORT=61000;uid=" + user + ";pwd=" + password + ";DATABASE=" + db
    #connection = "DRIVER={SQL Server};SERVER=" + instance + ";Trusted_Connection=" + trustedConnection + ";DATABASE=" + db + ";PORT=61000"
    connection = "DRIVER={SQL Server};SERVER=" + instance + ";Trusted_Connection=" + trustedConnection + ";DATABASE=" + db
    return pdb.connect(connection)

con = login_con()
sql = '''
    select * from Meetings
    '''
df = pd.read_sql(sql, con)

print(df)
