import sqlite3
import pickle
model = pickle.load(open("model_chuc_nang.pkl", 'rb'))
database = sqlite3.connect('process.db')
a = [];
text = 'tìm kiếm bạn bè'
a.append(text);
y_pred = model.predict(a)
b = y_pred[0];
c = database.cursor();
c.execute(f"SELECT * FROM process WHERE id like {b}")
for i in c.fetchall():
	print(i);

# print(add)
# database.commit()
database.close()
