import sqlite3

connection = sqlite3.connect('banco.db')
c = connection.cursor()


def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS  tb_customer_account (
    id_customer number(4) not null
    constraint id_customer_pk PRIMARY KEY,
    cpf_cnpj varchar2(10) not null,
    nm_customer varchar2(30) not null,
    is_active varchar2(1) not null,
    vl_total number(30) not null
    )''')

def dataentry():
    c.execute('''INSERT INTO tb_customer_account VALUES(1523,'01234567893','Carlos','Y',580)''')
    c.execute('''INSERT INTO tb_customer_account VALUES(2900,'11234568790','Maria','Y',900)''')
    c.execute('''INSERT INTO tb_customer_account VALUES(1695,'21234576894','Carla','N',720)''')
    c.execute('''INSERT INTO tb_customer_account VALUES(1305,'31234657898','Roberto','Y',750)''')
    c.execute('''INSERT INTO tb_customer_account VALUES(2700,'01235467899','Roberta','Y',600)''')
    c.execute('''INSERT INTO tb_customer_account VALUES(1500,'51243567897','Mario','Y',400)''')
    connection.commit()



def read_data():
    sql  = 'SELECT * FROM tb_customer_account WHERE vl_total > 560 AND (id_customer BETWEEN 1500 AND 2700) ORDER BY vl_total desc'
    media = 0
    m = 0
    for row in c.execute(sql):
        media = row[4] + media
        print("id_customer: ", row[0], "\tcpf_cnpj: ", row[1], "\tnm_customer: ", row[2], "\tis_active: ", row[3], "\tvl_total: ", row[4])
        m += 1
    print("Média: R$ %.2f" %(media/m))

create_table()

dataentry()

read_data()
