import os
import pymysql


def get_sql_files(path):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if file.endswith(".sql"):
                files.append(os.path.join(r, file))

    for f in files:
        print(f)

    return files


def generate_sql(sql_file_list):
    sql_list = []
    for file in sql_file_list:
        with open(file, "r") as f:
            sql_list.append(f.read())
    return sql_list


def execute_sql(sql_list):
    db = pymysql.connect("host", "username", "password", "database", 3306, ssl={'ssl_verify_cert': False})
    cursor = db.cursor()
    for sql in sql_list:
        cursor.execute(sql)


if __name__ == "__main__":
    path = './'
    sql_file_list = get_sql_files(path)
    print(sql_file_list)
    sql_list = generate_sql(sql_file_list)
    print(sql_list)
    execute_sql(sql_list)
