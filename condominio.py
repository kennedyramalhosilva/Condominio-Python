import sqlite3

con = sqlite3.connect('condominio.db')

def menu():

    print('''
    |----------------------------------|
    |BEM-VINDO AO SISTEMA DE CONDOMINIO|
    |----------------------------------|
    O que voce deseja?
    
    0) Sair;
    1) Registrar um novo dado;
    2) Atualizar um novo dado;
    3) Apagar um dado;
    4) Consultar um dado;
    
    ''')
    opcao = int(input('Entre com sua escolha:'))

    if opcao == 1:
        menu_registrar()

    elif opcao == 2:
        menu_atualizar()

    elif opcao == 3:
        menu_apagar()

    elif opcao == 4:
        menu_consultar()

    elif opcao == 0:
        print('''
        |-----------------|
        |Sistema encerrado|
        |-----------------|
        ''')

    else:
        print('''
        |----------------|
        |Escolha Invalida|
        |----------------|
                
        ''')
    return opcao


def menu_registrar():

    print('''
    |----------------------|
    |REGISTRAR UM NOVO DADO|
    |----------------------|
    
    O que voce deseja registrar?
    
    1) Registrar um condominio;
    2) Registrar um apartamento;
    3) Registrar um visitante;
    4) Registrar um morador;
    5) Registrar um veiculo;
    6) Registrar um funcionario;
    
    ''')
    opcao = int(input('Entre com sua escolha:'))

    if opcao == 1:
        registrar_condominio()

    elif opcao == 2:
        registrar_apartamento()

    elif opcao == 3:
        registrar_visitante()

    elif opcao == 4:
        registrar_morador()

    elif opcao == 5:
        registrar_veiculo()

    elif opcao == 6:
        registrar_funcionario()

    else:
        print('''
        |----------------|
        |Escolha Invalida|
        |----------------|
                    
        ''')

def menu_atualizar():
    
    print('''
        |----------------------|
        |ATUALIZAR UM NOVO DADO|
        |----------------------|

        O que voce deseja atualizar?

        1) Atualizar um condominio;
        2) Atualizar um apartamento;
        3) Atualizar um visitante;
        4) Atualizar um morador;
        5) Atualizar um veiculo;
        6) Atualizar um funcionario;
        
        ''')
    opcao = int(input('Entre com sua escolha:'))

    if opcao == 1:
        atualizar_condominio()

    elif opcao == 2:
        atualizar_apartamento()

    elif opcao == 3:
        atualizar_visitante()

    elif opcao == 4:
        atualizar_morador()

    elif opcao == 5:
        atualizar_veiculo()

    elif opcao == 6:
        atualizar_funcionario()

    else:
        print('''
        |----------------|
        |Escolha Invalida|
        |----------------|

        ''')

def menu_apagar():

    print('''
                |--------------|
                |APAGAR UM DADO|
                |--------------|

            O que voce deseja apagar?

            1) Apagar um condominio;
            2) Apagar um apartamento;
            3) Apagar um visitante;
            4) Apagar um morador;
            5) Apagar um veiculo;
            6) Apagar um funcionario;
            
            ''')
    opcao = int(input('Entre com sua escolha:'))

    if opcao == 1:
        id = int(input('Entre com id do condominio que deseja apagar:'))
        apagar_condominio(id)

    elif opcao == 2:
        id = int(input('Entre com id do apartamento que deseja apagar:'))
        apagar_apartamento(id)

    elif opcao == 3:
        id = int(input('Entre com id do visitante que deseja apagar:'))
        apagar_visitante(id)

    elif opcao == 4:
        id = int(input('Entre com id do morador que deseja apagar:'))
        apagar_morador(id)

    elif opcao == 5:
        id = int(input('Entre com id do veiculo que deseja apagar:'))
        apagar_veiculo(id)

    elif opcao == 6:
        id = int(input('Entre com id do funcionario que deseja apagar:'))
        apagar_funcionario(id)

    else:
        print('''
        |----------------|
        |Escolha Invalida|
        |----------------|

        ''')

def menu_consultar():

    print('''
                    |-----------------|
                    |CONSULTAR UM DADO|
                    |-----------------|

                O que voce deseja consultar?

                1) Consultar um condominio;
                2) Consultar um apartamento;
                3) Consultar um visitante;
                4) Consultar um morador;
                5) Consultar um veiculo;
                6) Consultar um funcionario;
                7) Consultar todas as tabelas;
                8) Consulta especifica;
                
                ''')
    opcao = int(input('Entre com sua escolha:'))

    if opcao == 1:
        consultar_condominio()

    elif opcao == 2:
        consultar_apartamento()

    elif opcao == 3:
        consultar_visitante()

    elif opcao == 4:
        consultar_morador()

    elif opcao == 5:
        consultar_veiculo()

    elif opcao == 6:
        consultar_funcionario()

    elif opcao == 7:
        consultar_todasTabelas()

    elif opcao == 8:
        consulta_especifica()

    else:
        print('''
        |----------------|
        |Escolha Invalida|
        |----------------|

        ''')

def criar_tabelas():

    c = con.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS condominio '
              '(idCondominio INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, '
              'cnpj TEXT, '
              'nome TEXT);')
    con.commit()

    c.execute('CREATE TABLE IF NOT EXISTS apartamento '
              '(idApartamento INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, '
              'bloco TEXT, '
              'numero INTEGER, '
              'idCondominio INTEGER,' 
              'FOREIGN KEY (idCondominio) REFERENCES condominio(idCondominio));')
    con.commit()

    c.execute('CREATE TABLE IF NOT EXISTS visitante '
              '(idVisitante INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, '
              'nome TEXT, '
              'rg TEXT, '
              'telefone TEXT,'
              'idApartamento INTEGER,'
              'FOREIGN KEY (idApartamento) REFERENCES apartamento(idApartamento)'
              ');')
    con.commit()

    c.execute('CREATE TABLE IF NOT EXISTS morador '
              '(idMorador INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, '
              'nome TEXT, '
              'rg TEXT, '
              'telefone TEXT,'
              'idApartamento INTEGER,'
              'FOREIGN KEY (idApartamento) REFERENCES apartamento(idApartamento)'
              ');')
    con.commit()


    c.execute('CREATE TABLE IF NOT EXISTS veiculo '
              '(idVeiculo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, '
              'placa TEXT, '
              'marca TEXT, '
              'modelo TEXT,'
              'cor TEXT,'
              'idMorador INTEGER,'
              'FOREIGN KEY (idMorador) REFERENCES morador(idMorador)'
              ');')
    con.commit()

    c.execute('CREATE TABLE IF NOT EXISTS funcionario '
              '(idFuncionario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, '
              'nome TEXT, '
              'rg TEXT, '
              'telefone TEXT,'
              'idCondominio INTEGER,'
              'FOREIGN KEY (idCondominio) REFERENCES condominio(idCondominio)'
              ');')
    con.commit()


def registrar_condominio():

    c = con.cursor()

    print()
    cnpj = input('Entre com o CNPJ:')
    nome = input('Entre com o nome do condominio:')
    condominio = [(cnpj,nome)]

    c.executemany('INSERT INTO condominio (cnpj, nome) VALUES (?,?)', condominio)
    con.commit()
    print('''
            |------------------------------|
            |Registro realizado com sucesso|
            |------------------------------|

            ''')

def registrar_apartamento():

    c = con.cursor()

    print()
    bloco = input('Insira o bloco do Apartamento:')
    num = int(input('Insira o numero do apartamento:'))
    idCondominio = int(input('Entre com o ID do condominio:'))

    c.execute('SELECT*FROM condominio;')
    result = c.fetchall()
    for i in range(len(result)):
        if idCondominio == result[i][0]:

            apartamento = [(bloco,num,idCondominio)]
            c.executemany('INSERT INTO apartamento (bloco,numero,idCondominio) VALUES (?,?,?)', apartamento)
            con.commit()
            print('''
                |------------------------------|
                |Registro realizado com sucesso|
                |------------------------------|
                
            ''')
            break

        elif i < len(result)-1:
            continue

        else:
            print('''
                |---------------------------|
                |************ERRO!**********|
                |idCondominio nao encontrado|
                |---------------------------|  
                ''')

def registrar_visitante():

    c = con.cursor()

    print()
    nome = input('Insira o nome do visitante: ')
    rg = input('Insira o rg do visitante: ')
    telefone = input('Insira o telefone do visitante: ')
    idApartamento = int(input('Insira o id do apartamento: '))

    c.execute('SELECT*FROM apartamento;')
    result = c.fetchall()
    for i in range(len(result)):
        if idApartamento == result[i][0]:

            visitante = [(nome, rg, telefone, idApartamento)]
            c.executemany('INSERT INTO visitante (nome, rg, telefone, idApartamento) VALUES (?, ?, ?, ?)', visitante)
            con.commit()
            print('''
                |------------------------------|
                |Registro realizado com sucesso|
                |------------------------------|

                ''')
            break

        elif i < len(result) - 1:
            continue

        else:
            print('''
                |----------------------------|
                |************ERRO!***********|
                |idApartamento nao encontrado|
                |----------------------------|

                    ''')

def registrar_morador():

    c = con.cursor()

    print()
    nome = input('Insira o nome do morador: ')
    rg = input('Insira o rg do morador: ')
    telefone = input('Insira o telefone do morador: ')
    idApartamento = int(input('Insira o id do apartamento: '))

    c.execute('SELECT*FROM apartamento;')
    result = c.fetchall()
    for i in range(len(result)):
        if idApartamento == result[i][0]:

            morador = [(nome, rg, telefone, idApartamento)]
            c.executemany('INSERT INTO morador (nome, rg, telefone, idApartamento) VALUES (?, ?, ?, ?)', morador)
            con.commit()
            print('''
                |------------------------------|
                |Registro realizado com sucesso|
                |------------------------------|

                    ''')
            break

        elif i < len(result) - 1:
            continue

        else:
            print('''
                |----------------------------|
                |************ERRO!***********|
                |idApartamento nao encontrado|
                |----------------------------|

                        ''')

def registrar_veiculo():

    c = con.cursor()

    print()
    placa = input('Insira uma placa: ')
    marca = input('Insira uma marca: ')
    modelo = input('Insira um modelo: ')
    cor = input('Insira uma cor: ')
    idMorador = int(input('Insira um id de morador: '))

    c.execute('SELECT*FROM morador;')
    result = c.fetchall()
    for i in range(len(result)):
        if idMorador == result[i][0]:

            veiculo = [(placa, marca, modelo, cor, idMorador)]
            c.executemany('INSERT INTO veiculo (placa, marca, modelo, cor, idMorador) VALUES (?, ?, ?, ?, ?)', veiculo)
            con.commit()
            print('''
                |------------------------------|
                |Registro realizado com sucesso|
                |------------------------------|

                        ''')
            break

        elif i < len(result) - 1:
            continue

        else:
            print('''
                |------------------------|
                |**********ERRO!*********|
                |idMorador nao encontrado|
                |------------------------|

                            ''')

def registrar_funcionario():

    c = con.cursor()

    print()
    nome = input('Insira o nome do Funcionário: ')
    rg = input('Insira um rg: ')
    telefone = input('Insira um telefone: ')
    idCondominio = int(input('Insira um id de condomínio: '))

    c.execute('SELECT*FROM condominio;')
    result = c.fetchall()
    for i in range(len(result)):
        if idCondominio == result[i][0]:

            funcionario = [(nome, rg, telefone, idCondominio)]
            c.executemany('INSERT INTO funcionario (nome, rg, telefone, idCondominio) VALUES (?, ?, ?, ?)', funcionario)
            con.commit()
            print('''
                    |------------------------------|
                    |Registro realizado com sucesso|
                    |------------------------------|

                ''')
            break

        elif i < len(result) - 1:
            continue

        else:
            print('''
                    |---------------------------|
                    |************ERRO!**********|
                    |idCondominio nao encontrado|
                    |---------------------------|

                    ''')

def atualizar_condominio():

    c = con.cursor()

    print()
    idCondominio = int(input('Entre com o id do condominio que deseja atualizar:'))

    c.execute('SELECT*FROM condominio;')
    result = c.fetchall()
    for i in range(len(result)):
        if idCondominio == result[i][0]:

            print('''
                O que deseja atualizar?
                1) CNPJ;
                2) Nome Condominio;
                ''')
            opcao = int(input('Entre com sua escolha:'))

            if opcao == 1:
                print()
                cnpj = input('Entre com o novo CNPJ:')
                c.execute('UPDATE condominio SET cnpj = ? WHERE idCondominio = ?', (cnpj, idCondominio))
                con.commit()

            elif opcao == 2:
                print()
                nomeNovo = input('Entre com o novo nome:')
                c.execute('UPDATE condominio SET nome = ? WHERE idCondominio = ?', (nomeNovo, idCondominio))
                con.commit()

            print('''
                    |-------------------------------|
                    |Registro atualizado com sucesso|
                    |-------------------------------|

                ''')
            break
            
        elif i < len(result)-1:
            continue

        else:
            print('''
                    |---------------------------|
                    |************ERRO!**********|
                    |idCondominio nao encontrado|
                    |---------------------------|

                    ''')

def atualizar_apartamento():

    c = con.cursor()

    print()
    id = int(input('Entre com o id do Apartamento que deseja atualizar:'))

    c.execute('SELECT*FROM apartamento;')
    result = c.fetchall()
    for i in range(len(result)):
        if id == result[i][0]:

            print('''
            O que deseja atualizar?
            1) Bloco do Apartamento;
            2) Numero do Apartamento;
            ''')
            opcao = int(input('Entre com sua escolha:'))

            if opcao == 1:
                print()
                blocoNovo = input('Entre com o novo Bloco do Apartamento:')
                c.execute('UPDATE apartamento SET bloco = ? WHERE idApartamento = ?', (blocoNovo,id))
                con.commit()

            elif opcao == 2:
                print()
                numApar = int(input('Entre com o novo Numero do Apartamento:'))
                c.execute('UPDATE apartamento SET numero = ? WHERE idApartamento = ?', (numApar,id))
                con.commit()

            elif opcao == 3:
                print()
                idCon = int(input('Entre com o novo idCondominio:'))
                c.execute('UPDATE apartamento SET idCondominio = ? WHERE idApartamento = ?', (idCon,id))
                con.commit()

            print('''
                    |-------------------------------|
                    |Registro atualizado com sucesso|
                    |-------------------------------|

                    ''')
            break

        elif i < len(result) - 1:
            continue

        else:
            print('''
                    |----------------------------|
                    |************ERRO!***********|
                    |idApartamento nao encontrado|
                    |----------------------------|

                                ''')

def atualizar_visitante():

    c = con.cursor()

    print()
    id = int(input('Entre com o id do Visitante que deseja atualizar:'))
    c.execute('SELECT*FROM visitante;')
    result = c.fetchall()
    for i in range(len(result)):
        if id == result[i][0]:

            print('''
                O que deseja atualizar?
                1) Nome do Visitante;
                2) RG do Visitante;
                3) Telefone do Visitante;
                ''')
            opcao = int(input('Entre com sua escolha:'))

            if opcao == 1:
                print()
                nomeVisi = input('Entre com o novo nome do Visitante:')
                c.execute('UPDATE visitante SET nome = ? WHERE idVisitante = ?', (nomeVisi,id))
                con.commit()

            elif opcao == 2:
                print()
                rgVisi = input('Entre com o novo RG do Visitante:')
                c.execute('UPDATE visitante SET rg = ? WHERE idVisitante = ?', (rgVisi,id))
                con.commit()

            elif opcao == 3:
                print()
                telVisi = input('Entre com o novo telefone do Visitante:')
                c.execute('UPDATE visitante SET telefone = ? WHERE idVisitante = ?', (telVisi,id))
                con.commit()

            elif opcao == 4:
                print()
                idApar = int(input('Entre com o novo numero de idApartamento:'))
                c.execute('UPDATE visitante SET idApartamento = ? WHERE idVisitante = ?', (idApar,id))
                con.commit()

            print('''
                    |-------------------------------|
                    |Registro atualizado com sucesso|
                    |-------------------------------|

                    ''')
            break

        elif i < len(result) - 1:
            continue

        else:
            print('''
                    |--------------------------|
                    |************ERRO!*********|
                    |idVisitante nao encontrado|
                    |--------------------------|

                ''')

def atualizar_morador():

    c = con.cursor()

    print()
    id = int(input('Entre com o id do morador que deseja atualizar:'))

    c.execute('SELECT*FROM morador;')
    result = c.fetchall()
    for i in range(len(result)):
        if id == result[i][0]:

            print('''
                O que deseja atualizar?
                1) Nome do morador;
                2) RG do morador;
                3) Telefone do morador;
            ''')
            opcao = int(input('Entre com sua escolha:'))

            if opcao == 1:
                print()
                nomeMor = input('Entre com o novo nome do morador:')
                c.execute('UPDATE morador SET nome = ? WHERE idMorador = ?', (nomeMor,id))
                con.commit()

            elif opcao == 2:
                print()
                rgMor = input('Entre com o novo RG do morador:')
                c.execute('UPDATE morador SET rg = ? WHERE idMorador = ?', (rgMor,id))
                con.commit()

            elif opcao == 3:
                print()
                telMor = input('Entre com o novo numero de telefone do morador:')
                c.execute('UPDATE morador SET telefone = ? WHERE idMorador = ?', (telMor,id))
                con.commit()

            elif opcao == 4:
                print()
                idApar = int(input('Entre com o novo numero de idApartamento:'))
                c.execute('UPDATE morador SET idApartamento = ? WHERE idMorador = ?', (idApar,id))
                con.commit()

            print('''
                    |-------------------------------|
                    |Registro atualizado com sucesso|
                    |-------------------------------|

                    ''')
            break

        elif i < len(result) - 1:
            continue

        else:
            print('''
                    |------------------------|
                    |**********ERRO!*********|
                    |idMorador nao encontrado|
                    |------------------------|

                    ''')

def atualizar_veiculo():

    c = con.cursor()

    print()
    id = int(input('Entre com o id do veiculo que deseja atualizar:'))

    c.execute('SELECT*FROM veiculo;')
    result = c.fetchall()
    for i in range(len(result)):
        if id == result[i][0]:

            print('''
                O que deseja atualizar?
                1) Placa do veiculo;
                2) Marca do veiculo;
                3) Modelo do veiculo;
                4) Cor do veiculo;
                ''')
            opcao = int(input('Entre com sua escolha:'))

            if opcao == 1:
                print()
                placaVei = input('Entre com a nova placa do veiculo:')
                c.execute('UPDATE veiculo SET placa = ? WHERE idVeiculo = ?', (placaVei,id))
                con.commit()

            elif opcao == 2:
                print()
                marcaVei = input('Entre com a nova marca do veiculo:')
                c.execute('UPDATE veiculo SET marca = ? WHERE idVeiculo = ?', (marcaVei,id))
                con.commit()

            elif opcao == 3:
                print()
                modeloVei = input('Entre com o novo modelo do veiculo:')
                c.execute('UPDATE veiculo SET modelo = ? WHERE idVeiculo = ?', (modeloVei, id))
                con.commit()

            elif opcao == 4:
                print()
                corVei = input('Entre com a nova cor do veiculo:')
                c.execute('UPDATE veiculo SET cor = ? WHERE idVeiculo = ?', (corVei, id))
                con.commit()

            elif opcao == 5:
                print()
                idMor = input('Entre com o novo numero de idMorador:')
                c.execute('UPDATE veiculo SET idMorador = ? WHERE idVeiculo = ?', (idMor, id))
                con.commit()

            print('''
                    |-------------------------------|
                    |Registro atualizado com sucesso|
                    |-------------------------------|

                    ''')
            break

        elif i < len(result) - 1:
            continue

        else:
            print('''
                    |------------------------|
                    |**********ERRO!*********|
                    |idVeiculo nao encontrado|
                    |------------------------|

                        ''')

def atualizar_funcionario():

    c = con.cursor()

    print()
    id = int(input('Entre com o id do Funcionario que deseja atualizar:'))

    c.execute('SELECT*FROM funcionario;')
    result = c.fetchall()
    for i in range(len(result)):
        if id == result[i][0]:

            print('''
                    O que deseja atualizar?
                    1) Nome do funcionario;
                    2) RG do funcionario;
                    3) Telefone do funcionario;
            ''')
            opcao = int(input('Entre com sua escolha:'))

            if opcao == 1:
                print()
                nomeFun = input('Entre com o novo nome do Funcionario:')
                c.execute('UPDATE funcionario SET nome = ? WHERE idFuncionario = ?', (nomeFun,id))
                con.commit()

            elif opcao == 2:
                print()
                rgFun = input('Entre com o novo numero de RG do Funcionario:')
                c.execute('UPDATE funcionario SET rg = ? WHERE idFuncionario = ?', (rgFun, id))
                con.commit()

            elif opcao == 3:
                print()
                telFun = input('Entre com o novo numero de telefone do Funcionario:')
                c.execute('UPDATE funcionario SET telefone = ? WHERE idFuncionario = ?', (telFun, id))
                con.commit()

            elif opcao == 4:
                print()
                idCon = input('Entre com o novo numero idCondominio:')
                c.execute('UPDATE funcionario SET idCondominio = ? WHERE idFuncionario = ?', (idCon, id))
                con.commit()

            print('''
                    |-------------------------------|
                    |Registro atualizado com sucesso|
                    |-------------------------------|

                    ''')
            break

        elif i < len(result) - 1:
            continue

        else:
            print('''
                    |----------------------------|
                    |**********ERRO!*************|
                    |idFuncionario nao encontrado|
                    |----------------------------|

                ''')

def apagar_condominio(id):

    c = con.cursor()
    print()
    c.execute('SELECT*FROM apartamento WHERE idCondominio = ?;',(id,))
    result = c.fetchall()
    for i in range(len(result)):
        apagar_apartamento(result[i][0])
    con.commit()

    c.execute('SELECT*FROM funcionario WHERE idCondominio = ?;', (id,))
    result = c.fetchall()
    for i in range(len(result)):
        apagar_funcionario(result[i][0])
    con.commit()

    c.execute('DELETE FROM condominio WHERE idCondominio = ?', (id,))
    con.commit()

    print('''
            |--------------------------|
            |Dados apagados com sucesso|
            |--------------------------|

                    ''')

def apagar_apartamento(id):

    c = con.cursor()

    c.execute('SELECT*FROM visitante WHERE idApartamento = ?;', (id,))
    result = c.fetchall()
    for i in range(len(result)):
        apagar_visitante(result[i][0])
    con.commit()

    c.execute('SELECT*FROM morador WHERE idApartamento = ?;', (id,))
    result = c.fetchall()
    for i in range(len(result)):
        apagar_morador(result[i][0])
    con.commit()

    c.execute('DELETE FROM apartamento WHERE idApartamento = ?', (id,))
    con.commit()

    print('''
            |--------------------------|
            |Dados apagados com sucesso|
            |--------------------------|

                        ''')

def apagar_visitante(id):

    c = con.cursor()

    c.execute('DELETE FROM visitante WHERE idVisitante = ?', (id,))
    con.commit()

    print('''
            |--------------------------|
            |Dados apagados com sucesso|
            |--------------------------|

                        ''')

def apagar_morador(id):

    c = con.cursor()

    c.execute('SELECT*FROM veiculo WHERE idMorador = ?;', (id,))
    result = c.fetchall()
    for i in range(len(result)):
        apagar_veiculo(result[i][0])
    con.commit()

    c.execute('DELETE FROM morador WHERE idMorador = ?', (id,))
    con.commit()

    print('''
            |--------------------------|
            |Dados apagados com sucesso|
            |--------------------------|

                        ''')

def apagar_veiculo(id):

    c = con.cursor()

    c.execute('DELETE FROM veiculo WHERE idVeiculo = ?', (id,))
    con.commit()

    print('''
            |--------------------------|
            |Dados apagados com sucesso|
            |--------------------------|

                        ''')

def apagar_funcionario(id):

    c = con.cursor()

    c.execute('DELETE FROM funcionario WHERE idFuncionario = ?', (id,))
    con.commit()

    print('''
            |--------------------------|
            |Dados apagados com sucesso|
            |--------------------------|

                        ''')

def consultar_condominio():

    c = con.cursor()

    print()
    print('CONDOMINIOS:')
    print(f'{"ID:":<10}{"CNPJ:":<25}{"NOME:":<45}')
    c.execute('SELECT*FROM condominio;')
    result = c.fetchall()
    for i in range(len(result)):
        print(f'{result[i][0]:<10}{result[i][1]:<25}{result[i][2]:<45}')

def consultar_apartamento():

    c = con.cursor()

    print()
    print('APARTAMENTOS:')
    print(f'{"ID:":<10}{"BLOCO:":<10}{"NUMERO:":<10}{"ID (CONDOMINIO):":<10}')
    c.execute('SELECT*FROM apartamento;')
    result = c.fetchall()
    for i in range(len(result)):
        print(f'{result[i][0]:<10}{result[i][1]:<10}{result[i][2]:<10}{result[i][3]:<10}')

def consultar_visitante():

    c = con.cursor()

    print()
    print('VISITANTES:')
    print(f'{"ID:":<10}{"NOME:":<35}{"RG:":<20}{"TELEFONE:":<20}{"ID (APARTAMENTO):":<10}')
    c.execute('SELECT*FROM visitante;')
    result = c.fetchall()
    for i in range(len(result)):
        print(f'{result[i][0]:<10}{result[i][1]:<35}{result[i][2]:<20}{result[i][3]:<20}{result[i][4]:<10}')

def consultar_morador():

    c = con.cursor()

    print()
    print('MORADORES:')
    print(f'{"ID:":<10}{"NOME:":<35}{"RG:":<20}{"TELEFONE:":<20}{"ID (APARTAMENTO):":<10}')
    c.execute('SELECT*FROM morador;')
    result = c.fetchall()
    for i in range(len(result)):
        print(f'{result[i][0]:<10}{result[i][1]:<35}{result[i][2]:<20}{result[i][3]:<20}{result[i][4]:<10}')

def consultar_veiculo():

    c = con.cursor()

    print()
    print('VEICULOS:')
    print(f'{"ID:":<10}{"PLACA:":<15}{"MARCA:":<20}{"MODELO:":<20}{"COR:":<15}{"ID (MORADOR):":<10}')
    c.execute('SELECT*FROM veiculo;')
    result = c.fetchall()
    for i in range(len(result)):
        print(f'{result[i][0]:<10}{result[i][1]:<15}{result[i][2]:<20}{result[i][3]:<20}{result[i][4]:<15}{result[i][5]:<10}')

def consultar_funcionario():

    c = con.cursor()

    print()
    print('FUNCIONARIOS:')
    print(f'{"ID:":<10}{"NOME:":<35}{"RG:":<20}{"TELEFONE:":<20}{"ID (CONDOMINIO):":<10}')
    c.execute('SELECT*FROM funcionario;')
    result = c.fetchall()
    for i in range(len(result)):
        print(f'{result[i][0]:<10}{result[i][1]:<35}{result[i][2]:<20}{result[i][3]:<20}{result[i][4]:<10}')

def consultar_todasTabelas():

    consultar_condominio()
    consultar_apartamento()
    consultar_visitante()
    consultar_morador()
    consultar_veiculo()
    consultar_funcionario()

def consulta_especifica():

    print('''
                        |-------------------|
                        |CONSULTA ESPECIFICA|
                        |-------------------|

                    O que voce deseja consultar?

                    1) Consultar um condominio por nome;
                    2) Consultar todos apartamentos de um determinado condominio;
                    3) Consultar todos visitantes de um determinado apartamento;
                    4) Consultar os dados de um morador por nome;
                    5) Consultar um veiculo por placa e seu respectivo dono;
                    6) Consultar dados de um funcionarios atraves de seu RG;

                    ''')
    opcao = int(input('Entre com sua escolha:'))

    if opcao == 1:
        consultar_ConPorNome()

    elif opcao == 2:
        consultar_todosAparCon()

    elif opcao == 3:
        consultar_todosVisiAp()

    elif opcao == 4:
        consultar_morPorNome()

    elif opcao == 5:
        consultar_VeicPlaca()

    elif opcao == 6:
        consultar_FuncPorRg()

    else:
        print('''
                |----------------|
                |Escolha Invalida|
                |----------------|

                ''')

def consultar_ConPorNome():

    c = con.cursor()

    print()
    nomeCon = input('Entre com o nome do condominio:')
    print()
    print('CONDOMINIO:')
    print(f'{"ID:":<10}{"CNPJ:":<25}{"NOME:":<45}')
    c.execute("SELECT*FROM condominio WHERE nome LIKE ?;", (str('%'+nomeCon+'%'),))
    result = c.fetchall()
    for i in range(len(result)):
        print(f'{result[i][0]:<10}{result[i][1]:<25}{result[i][2]:<45}')

def consultar_todosAparCon():

    c = con.cursor()

    print()
    cnpjCon = input('Entre com o CNPJ do condominio:')
    print()
    print('APARTAMENTOS:')
    print(f'{"ID:":<10}{"BLOCO:":<10}{"NUMERO:":<10}{"ID (CONDOMINIO):":<10}')
    c.execute('''SELECT apartamento.idApartamento, apartamento.bloco, apartamento.numero, condominio.idCondominio 
                FROM apartamento INNER JOIN condominio 
                ON apartamento.idCondominio = condominio.idCondominio WHERE condominio.cnpj = ? 
                ORDER BY 1;''',(cnpjCon,))
    result = c.fetchall()
    for i in range(len(result)):
        print(f'{result[i][0]:<10}{result[i][1]:<10}{result[i][2]:<10}{result[i][3]:<10}')

def consultar_todosVisiAp():

    c = con.cursor()

    print()
    idApar = int(input('Entre com o id do apartamento:'))
    print()
    print('VISITANTES:')
    print(f'{"NOME:":<35}{"RG:":<20}{"TELEFONE:":<20}')
    c.execute('''SELECT visitante.nome, visitante.rg, visitante.telefone 
                FROM visitante INNER JOIN apartamento 
                ON visitante.idApartamento = apartamento.idApartamento WHERE apartamento.idApartamento = ?
                ORDER BY 1;''', (idApar,))
    result = c.fetchall()
    for i in range(len(result)):
        print(f'{result[i][0]:<35}{result[i][1]:<20}{result[i][2]:<20}')

def consultar_morPorNome():

    c = con.cursor()

    print()
    nomeMor = input('Entre com o nome do morador:')
    print()
    print('MORADOR:')
    print(f'{"NOME:":<35}{"RG:":<20}{"TELEFONE:":<20}{"BLOCO (APARTAMENTO):":<25}{"NUMERO (APARTAMENTO):":<30}')
    c.execute('''SELECT morador.nome, morador.rg, morador.telefone, apartamento.bloco, apartamento.numero
     FROM morador INNER JOIN apartamento
     ON morador.idApartamento = apartamento.idApartamento WHERE nome LIKE ?;''',(str('%'+nomeMor+'%'),))
    result = c.fetchall()
    for i in range(len(result)):
        print(f'{result[i][0]:<35}{result[i][1]:<20}{result[i][2]:<20}{result[i][3]:<25}{result[i][4]:<30}')

def consultar_VeicPlaca():

    c = con.cursor()

    print()
    placa = input('Entre com a placa do veiculo:')
    print()
    print('VEICULO:')
    print(f'{"NOME DONO":<35}{"PLACA:":<15}{"MARCA:":<20}{"MODELO:":<20}{"COR:":<15}')
    c.execute('''SELECT morador.nome, veiculo.placa, veiculo.marca, veiculo.modelo, veiculo.cor
                FROM morador INNER JOIN veiculo 
                ON morador.idMorador = veiculo.idMorador WHERE veiculo.placa = ?;''', (placa,))
    result = c.fetchall()
    for i in range(len(result)):
        print(f'{result[i][0]:<35}{result[i][1]:<15}{result[i][2]:<20}{result[i][3]:<20}{result[i][4]:<15}')

def consultar_FuncPorRg():

    c = con.cursor()

    print()
    funcRg = input('Entre com o RG do funcionario:')
    print()
    print('FUNCIONARIO:')
    print(f'{"NOME:":<35}{"RG:":<20}{"TELEFONE:":<20}{"NOME CONDOMINIO:":<30}')
    c.execute('''SELECT funcionario.nome, funcionario.rg, funcionario.telefone, condominio.nome
                FROM funcionario INNER JOIN condominio
                ON funcionario.idCondominio = condominio.idCondominio WHERE funcionario.rg = ?;''', (funcRg,))
    result = c.fetchall()
    for i in range(len(result)):
        print(f'{result[i][0]:<35}{result[i][1]:<20}{result[i][2]:<20}{result[i][3]:<30}')

criar_tabelas()
opcao = menu()

while opcao != 0:
    opcao = menu()
con.close()