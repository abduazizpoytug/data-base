import sqlite3
import time

connects = sqlite3.connect('mydatabase.db')



shopping = connects.cursor()

shopping.execute("""
CREATE TABLE IF NOT EXISTS shopping(
    name TEXT,
    last_name TEXT,
    age INTEGER    
)                
               
""")



shopping.execute("""
INSERT INTO shopping VALUES
('abduaziz', 'boymirzayev', 32),
('azizbek', 'nazarov', 82), 
('muhammad ali', 'boltaboyev', 38)             
 
               
""")

shopping.execute("SELECT * FROM shopping")

car = connects.cursor()

car.execute("""
CREATE TABLE IF NOT EXISTS car(
    name TEXT,
    number INTEGER    
)                
               
""")



car.execute("""
INSERT INTO car VALUES
('spark', 555),
('cobalt', 777), 
('gentra', 123)             
 
               
""")


car.execute("SELECT * FROM car")
# print(malumot.fetchall())


tikuv = connects.cursor()

tikuv.execute("""
CREATE TABLE IF NOT EXISTS tikuv(
    name TEXT,
    age INTEGER    
)                
               
""")



tikuv.execute("""
INSERT INTO tikuv VALUES
('holida', 14),
('gulshanoy', 32)
 
               
""")


tikuv.execute("SELECT * FROM tikuv")



# sorovnoma

game = connects.cursor()

game.execute("""
CREATE TABLE IF NOT EXISTS game(
    name TEXT,
    game TEXT    
)                
               
""")



game.execute("""
INSERT INTO game VALUES
('coll of duty', 'fortnite'),
('subvay surfers', 'pubg')
 
               
""")


game.execute("SELECT * FROM game")



sorov = input("boshlash uchun 1ni bosing: ")

while sorov == "1":
    search = input("qidiruv: ")
    if search == "shopping":
        print("iltimos kuting")
        time.sleep(1)
        print(shopping.fetchall())
    elif search == "car":
        print("iltimos kuting")
        time.sleep(1)
        print(car.fetchall())
    elif search == "tikuv":
        print("iltimos kuting")
        time.sleep(1)
        print(tikuv.fetchall())
    elif search == "game":
        time.sleep(1)
        print(game.fetchall())                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      