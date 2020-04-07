import mysql.connector


def getMySQLTableAndCols(user: [str], password: [str], host: [str], database, port="3306"):
    """
    :return: ["table_name",[cols]]
    """
    cnx = mysql.connector.connect(user=user, password=password, host=host, port=port, database=database)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("show tables")
    table_name_list = [tuple[0] for tuple in cursor.fetchall()]
    res = []
    for table_name in table_name_list:
        cursor.execute(
            "select DISTINCT COLUMN_NAME,COLUMN_TYPE,CHARACTER_MAXIMUM_LENGTH,COLUMN_DEFAULT,COLUMN_KEY,COLUMN_COMMENT from INFORMATION_SCHEMA.Columns where `table_name`='%s'" % table_name)
        res.append([table_name, cursor.fetchall()])
    cnx.close()
    return res


if __name__ == '__main__':
    print("xxx")
