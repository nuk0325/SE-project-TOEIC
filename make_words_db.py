import pandas as pd
import Database as db


df = pd.read_csv("���͸� ���ܾ��Ʈ.csv")
row_count = len(df)
column_count = df.shape[1]

for i in range(row_count) :
    for j in range(column_count) :
        db.cur.execute('''INSERT INTO words_db VALUES (?)''', 
                       df.at[i][j])

db.conn.commit()
db.conn.close()