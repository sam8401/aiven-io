import psycopg2


def get_connection(conn_string):
	try:
		conn = psycopg2.connect(conn_string)
		return conn
	except:
		print('Unable to connect to %s' % conn_string)

def table_exists(conn, table_name):
	exists_query = "select * from information_schema.tables where table_name='%s'" % table_name

	cur = conn.cursor()
	cur.execute(exists_query)
	table_exists = bool(cur.rowcount)
	cur.close()

	return table_exists


def create_table(conn, table_name):
	if table_exists(conn, table_name) == False:

		create_query = "CREATE TABLE %s \
		(time_stamp VARCHAR (20) NOT NULL,\
		response_time VARCHAR (10),\
		error_code VARCHAR (10),\
		content_found VARCHAR (5) NOT NULL);" % table_name


		cur = conn.cursor()
		cur.execute(create_query)

		conn.commit()
		cur.close()
	else:
		print('Table already exists!')


def insert_row(conn, table_name, dict):
	insert_query = "INSERT INTO %s values ('%s', '%s', '%s', '%s');"\
	% (table_name, dict.get('time_stamp'),\
		dict.get('response_time'),\
		dict.get('error_code'),\
		dict.get('content_found'))

	cur = conn.cursor()
	cur.execute(insert_query)
	conn.commit()


def drop_table(conn, table_name):

	cur = conn.cursor()
	drop_query = "DROP TABLE %s;" % table_name

	cur.execute(drop_query)
	conn.commit()
	cur.close()



