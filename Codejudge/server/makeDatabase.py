import sqlite3
conn = sqlite3.connect('user.db')
conn.execute('''CREATE TABLE USER
	(NAME         TEXT     NOT NULL,
	EMAIL         TEXT     NOT NULL PRIMARY KEY,
	PASSWORD      TEXT     NOT NULL,
	ROLL          TEXT     NOT NULL,
	P1            TEXT     NOT NULL,
	P1_TIME       TEXT     NOT NULL,
	P2            TEXT     NOT NULL,
	P2_TIME       TEXT     NOT NULL,
	P3            TEXT     NOT NULL,
	P3_TIME       TEXT     NOT NULL,
	P4            TEXT     NOT NULL,
	P4_TIME       TEXT     NOT NULL,
	P5            TEXT     NOT NULL,
	P5_TIME       TEXT     NOT NULL,
	P6            TEXT     NOT NULL,
	P6_TIME       TEXT     NOT NULL,
	P7            TEXT     NOT NULL,
	P7_TIME       TEXT     NOT NULL,
	TLE           TEXT     NOT NULL,
	SIZE          TEXT     NOT NULL);''')
conn.close()