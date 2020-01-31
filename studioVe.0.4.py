# Criado o PMV com estoque
# 0.1 - def cabec
# 0.2 - def gravaMatrix
# 0.3 - var cod_fim para fazer str + int pois trabalhamos com str na carga
# 0.4 - def carrega

from time import sleep


def cabec(nome, op):
    """
    M O N T A    C A B E Ç A L H O
    :param nome: nome do menu
    :param op: dicionário com as opções do menu
    :return: null
    """
    print('\033[30m', end='')
    print('#' * 80)
    print('#', ' ' * 28, 'S T U D I O    V E', ' ' * 28, '#')
    print('#' * 80)
    tmn = len(nome) + 4
    print('~' * tmn)
    print(f'~ {nome} ~')
    print('~' * tmn)
    for kop, vop in op.items():
        print(f'({kop}){vop}')
    tmo = 12 - len(op)
    print('\n' * tmo)
    print('#' * 80)


def grava_matrix(m, a):
    """
    GRAVA UMA MATRIX EM ARQUIVO SEPARADO COM (|)
    :param m: matrix com as listas
    :param a: local/nome do arquivo
    :return: null
    """
    arq = open(f'{a}', 'w')
    for m_ct in m:
        for l_ct in m_ct:
            arq.writelines(f'{l_ct}|')
        arq.writelines(f'\n')
    arq.close()
    print('Gravado com sucesso !')
    sleep(1)


def carrega_matrix(a):
    """
    Carrega um arquivo dele na matrix de retorno
    :param a: local e nome do arquivo ex: ./nome.csv
    :return: matrix sem as quebras de linha \n
    """

    mret = list()
    arq = open(f'{a}', encoding='utf-8')
    for l_ct in arq.readlines():
        if l_ct != '':
            mret.append(l_ct.split('|'))
    arq.close()
    for l_ret in mret:
        l_ret.pop()
    return mret


'''
https://www.devmedia.com.br/como-trabalhar-com-listas-em-python/37460
C A R R E G A M E N T O
'''
m_mat = carrega_matrix('./materiais.csv')
m_con = m_ben = m_inv = list()
l_con = l_ben = l_inv = list()

'''
M E N U
'''
op1 = {'1': 'ESTOQUE DE MATERIAL',
       '2': 'CONSUMO POR PROCEDIMENTO',
       '3': 'RATEIO BENS DURÁVEIS',
       '4': 'INVESTIMENTO ESTUDOS E MARKETING',
       '0': 'S A I R'}
while True:
    cabec('MENU', op1)
    menu = input()
    if menu in '0':
        break
    elif menu in op1.keys():
        '''
        S U B - M E N U
        '''
        op2 = {'1': 'CONSULTA',
               '2': 'CADASTRO',
               '0': 'V O L T A R'}
        while True:
            cabec(op1[menu], op2)
            # print(m_mat) # --LOG
            m1 = input()
            if m1 in '0':
                break
            elif m1 in op2.keys():
                while True:
                    if m1 in '1' and menu in '1':
                        '''
                        E S T O Q U E   M A T E R I A L - C O N S U L T A e EXCLUSAO
                        '''
                        for ctm in m_mat:
                            print(f'|{ctm[0]:<{6}}|{ctm[1]:<{40}}|{ctm[2]:<{6}}1|R${ctm[3]:<{6}}|')
                        print('\n' * (18 - len(m_mat)))
                        exc_mat = input('(X)EXCLUIR / (0)V O L T A R <Enter>').upper()
                        if 'X' in exc_mat:
                            mat_id = (input('Numero CODIGO:'))
                            for kl, vl in enumerate(m_mat):
                                if mat_id == vl[0]:
                                    conf_mat = input(f'Confirma a exclusão do {vl[1]} ? (S/N)')
                                    sleep(1)
                                    if conf_mat in 'Ss':
                                        m_mat.pop(kl)
                                        print('Excluido com sucesso !')
                                        sleep(1)
                                        grava_matrix(m_mat, './materiais.csv')
                            print(m_mat)
                        else:
                            break
                    if m1 in '2' and menu in '1':
                        '''
                        E S T O Q U E   M A T E R I A L - I N C L U S A O
                        '''
                        l_mat = list()
                        print('#'*80, '\n'*16)
                        print('\033[35m', end='')
                        cod_fim = int(m_mat[-1][0])
                        l_mat.append(str(cod_fim + 1))
                        l_mat.append(input('NOME......:').upper())
                        l_mat.append(input('QT.(só num):'))
                        l_mat.append(input('VALOR TOTAL:'))
                        m_mat.append(l_mat[:])
                        l_mat.clear()
                        grava_matrix(m_mat, './materiais.csv')
                        break
