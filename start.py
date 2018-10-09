
import requests
import bs4
import collections
import webbrowser
import mysql.connector
from subprocess import call


##############      MySQL Connect       ##############

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="ZSTIOBOT"
)

def main():
      last = to_compare()
      page = get_page()
      print(page)
      print(last)
      if last != page:
            update(last , page)
            call(["python", "get_text.py"])

            


def to_compare():
      mycursor = mydb.cursor()
      sql_syntax = "SELECT * FROM lastzast"
      mycursor.execute(sql_syntax)
      temp = mycursor.fetchone()
      temp = str(temp)
      temp = temp.replace("('", "")
      temp = temp.replace("',)", "")
      return temp

def get_page():
      response = requests.get('https://www.zstiojar.edu.pl/plan-lekcji/zastepstwa')
      response = response.text
      soup = bs4.BeautifulSoup(response, 'html.parser')
      zast = soup.find(class_='list-title')
      zast = zast.get_text("|", strip=True)
      return str(zast)

def update(old , new):
      mycursor = mydb.cursor()
      sql = "UPDATE lastzast SET sub = %s WHERE sub = %s"
      val = (new , old)
      mycursor.execute(sql, val)
      mydb.commit()



if __name__ == '__main__':
    main()