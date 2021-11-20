import sqlite3
cnt = sqlite3.connect("primenum.db")  
print("Database opened successfully")  
  
cnt.execute("CREATE TABLE `Primenumgenerator` (	`Data` TEXT(5000) NOT NULL DEFAULT '',`Timestamp` BIGINT unsigned NOT NULL, `Range` VARCHAR(50) NOT NULL,`ElapseTime` BIGINT unsigned NOT NULL,	`Method` VARCHAR(10) NOT NULL,`Length` INT unsigned NOT NULL);")  
  
print("Table created successfully")  
  

cnt.close() 
