#-*-coding:UTF-8 -*-
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='yuan',
    password='test1234',
    database='testdb'
)
cursor = conn.cursor()

def new_data(name,stuid,num,in_year):
    sql = "INSERT INTO 球員( 名字, 學號, 背號, 入隊學年 )VALUES(%s, %s, %s, %s)"
    try:
        cursor.execute(sql,(name,stuid,num,in_year))
    # 執行SQL语句
    # 提交到資料庫系統執行
        conn.commit()
   # 發生異常錯誤時回復
        conn.rollback()
    
def fix_data(new_name,new_stuid,new_num,new_in_year,odd_name,odd_stuid,odd_num,odd_in_year):
    sql = "UPDATE 球員 SET 名字 = %s, 學號= %s ,背號 = %s,入隊學年= %s WHERE 球員.名字 = %s and 球員.學號 = %s and 球員.背號 = %s and 球員.入隊學年=%s "
    try:
        cursor.execute(sql,(new_name,new_stuid,new_num,new_in_year,odd_name,odd_stuid,odd_num,odd_in_year))
    # 執行SQL语句
    # 提交到資料庫系統執行
        conn.commit()

    except:
   # 發生異常錯誤時回復
        conn.rollback()

def new_game(date,game,oppschool,oppdep):
    sql = "INSERT INTO 比賽( 日期, 盃賽名稱, 對手學校, 對手系名 )VALUES(%s, %s, %s, %s)"
    try:
        cursor.execute(sql,(date,game,oppschool,oppdep))
    # 執行SQL语句
    # 提交到資料庫系統執行
        conn.commit()
   # 發生異常錯誤時回復
        conn.rollback()



