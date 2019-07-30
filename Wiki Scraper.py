import requests
print('Which number PPV UFC Event would you like to pull Results Information for?')
ufcInput = input()
website_url = requests.get('https://en.wikipedia.org/wiki/UFC_' + ufcInput)
html = website_url.content

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

resultsTable = soup.find('table', class_ = 'toccolours')


weightClass = []
fighterWinner = []
defeat = []
fighterLoser = []
victoryType = []
victoryRound = []
victoryTime = []
notes =[]

for row in resultsTable.findAll('tr'):
    cells=row.findAll('td')
    if len(cells) == 8:
        weightClass.append(cells[0].find(text=True))
        fighterWinner.append(cells[1].find(text=True))
        defeat.append(cells[2].find(text=True))
        fighterLoser.append(cells[3].find(text=True))
        victoryType.append(cells[4].find(text=True))
        victoryRound.append(cells[5].find(text=True))
        victoryTime.append(cells[6].find(text=True))
        notes.append(cells[7].find(text=True))


import pandas as pd
df=pd.DataFrame(weightClass, columns=['Weight Class'])
df['Winner'] = fighterWinner
df['def'] = defeat
df['Loser'] = fighterLoser
df['Won By'] = victoryType
df['Round'] = victoryRound
df['Time'] = victoryTime
df['Notes'] = notes
df = df.replace('\n','', regex=True)
print (df)

import sqlite3
from sqlite3 import Error

"""-- fightcard table
CREATE TABLE IF NOT EXISTS fightcard table (
 weightClass text,  
 fighterWinner text PRIMARY KEY,
 defeat text,
 fighterLoser text,
 victoryType text,
 victoryRound text,
 victoryTime text,
 notes text,

);"""

def create_connection(db_file):
    # create a database connection to the SQLite database
    #    specified by db_file
    #:param db_file: database file
    #:return: Connection object or None
    
    try:
        conn = sqlite3.connect('PythonDatabase.db')
        return conn
    except Error as e:
        print(e)
 
    return None

def create_table(conn, create_table_sql):
    # create a table from the create_table_sql statement
    #:param conn: Connection object
    #:param create_table_sql: a CREATE TABLE statement
    #:return:
    
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = "/Users/andrewlittlejohn/projects/AutomatedEdit/Python Database.db"

    sql_create_fightcard_table =  """CREATE TABLE IF NOT EXISTS fightcard (
                                        weightClass text NOT NULL,  
                                        fighterWinner text,
                                        defeat text NOT NULL,
                                        fighterLoser text NOT NULL,
                                        victoryType text NOT NULL,
                                        victoryRound text NOT NULL,
                                        victoryTime text NOT NULL,
                                        notes text NOT NULL
                                    ); """
 
 
    # create a database connection
    conn = create_connection('PythonDatabase.db')
    if conn is not None:
        # create UFC table
        create_table(conn, sql_create_fightcard_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()

#Seeding data to table
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///pythondatabase.db', echo=False)
df.to_sql('fightcard', con=engine, if_exists='append')