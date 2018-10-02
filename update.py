#UPDATING APP 
#USE IT EVERY OCTOBER
#TO UPDETE YOUR DATABASE

import requests
import bs4
import collections
import webbrowser
import mysql.connector

##############      MySQL Connect       ##############

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="ZSTIOBOT"
)
mycursor = mydb.cursor()

###########33


def main():
    url = 'https://www.zstiojar.edu.pl/plan/plan_lekcji/lista.html'
    raw_text = get_raw_text(url)
    data_to_update = get_all(raw_text)
    insert_data(data_to_update)

    

def insert_data(list):
    d=1
    for x in list:
        adress = 'plany/o%s.html' %(d) 
        d=d+1
        sql_syntax = "INSERT INTO oddzialy (oddzial , adres) VALUES (%s , %s)"
        var = (x.text , adress)
        mycursor.execute(sql_syntax,var)
        mydb.commit()

        print(adress)
    


def get_raw_text(url):
    response = requests.get(url)
    return response.text

def get_all(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    soup=soup.find('select')
    options = soup.find_all('option')[1:]
    for x in options:
        x = x.text
    
    return options
        

#TODO Jeszcze nauczyciele i sale XDD

if __name__ == '__main__':
    main()