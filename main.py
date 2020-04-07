import sys

from conn.mysqlconn import getMySQLTableAndCols
from table2doc.Table2Doc import Table2Doc

if __name__ == '__main__':
    cols_name = [
        '字段名',
        '类型',
        '最大长度',
        '默认值',
        '键类型',
        '备注'
    ]
    cmd = {'-h': None, '-P': None, '-u': None, '-p': None, '-db': None}
    for i in range(0, len(sys.argv[1:]), 2):
        cmd[sys.argv[i + 1]] = sys.argv[i + 2]
    print(cmd)

    if cmd['-db'] is None:
        print("database name is None！")
        sys.exit(-1)

    host = 'localhost' if cmd['-h'] is None else cmd['-h']
    port = '3306' if cmd['-P'] is None else cmd['-P']
    user = 'root' if cmd['-u'] is None else cmd['-u']
    password = 'root' if cmd['-p'] is None else cmd['-p']
    db_name = cmd['-db']

    table_and_records = getMySQLTableAndCols(user=user, password=password, host=host, database=db_name, port=port)

    d = Table2Doc()
    for table_name, records in table_and_records:
        print(table_name)
        for i in records:
            print(i)
        print(records)
        d.create_table(table_name, cols_name)
        d.insert(records)
    d.save(file_name=db_name)
