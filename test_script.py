from website_checker import check
from pg_client import *
from literals import *


result = check(WEBSITE, WEBSITE_TITLE)

conn_string = "dbname=%s user=%s password='%s' host=%s port=%s" % (POSTGRES_DB, POSTGRES_USER, POSTGRES_PWD, POSTGRES_HOST, POSTGRES_PORT)


c = get_connection(conn_string)

create_table(c, METRICS_TABLE)

insert_row(c, METRICS_TABLE, result)


# verify that insert worked
cur = c.cursor()
cur.execute("SELECT * FROM %s;" % METRICS_TABLE)
for r in cur.fetchall():
	print(r)