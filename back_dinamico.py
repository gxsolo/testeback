import sqlite3

connection = sqlite3.connect('banco.db')
c = connection.cursor()
op = 1

def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS  tb_customer_account (
    id_customer number(4) not null
    constraint id_customer_pk PRIMARY KEY,
    cpf_cnpj varchar2(10) not null,
    nm_customer varchar2(30) not null,
    is_active varchar2(1) not null,
    vl_total number(30) not null
    )''')

def dataentry(id, cpf, nome, ativo, valor):
    c.execute(f'''INSERT INTO tb_customer_account VALUES({id},'{cpf}','{nome}','{ativo}',{valor})''')
    connection.commit()

def read_data():
    media = 0
    m = 0
    sql  = 'SELECT * FROM tb_customer_account WHERE vl_total > 560 AND (id_customer BETWEEN 1500 AND 2700) ORDER BY vl_total desc'
    for row in c.execute(sql):
        media = row[4] + media
        print("id_customer: ", row[0], "\tcpf_cnpj: ", row[1], "\tnm_customer: ", row[2], "\tis_active: ", row[3], "\tvl_total: ", row[4])
        m += 1
    print("Média: R$ %.2f" %(media/m))

create_table()

while(op != 2):
	op = int(input("Para adicionar um novo cliente tecle 1 \nPara sair tecle 2\n"))
	if (op == 1):
		id	= input("Digite o Id: ")
		nome = input("Digite o nome: ")
		cpf = input("Digite o cpf: ")
		valor = input("Digite o valor total da conta: ")
		ativo = input("Digite Y para caso a conta esteja ativa e N para caso esteja inativa\n")
		dataentry(id, cpf, nome, ativo, valor)

read_data()
