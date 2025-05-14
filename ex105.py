def nota(*n, sit = False):
    """
    funcao para analisar nota e situacao do aluno
    :param n: para as notas do aluno
    :param sit: para saber a situacao do aluno
    :return: retorna um dicionario com varias funcoes
    """
    r = dict()
    r ['total'] = len(n)
    r ['maior'] = max(n)
    r ['menor']=min(n)
    r ['media']= sum(n)/len(n)
    if sit:
        if r['media'] >=7:
            r['situacao'] = 'Boa'
        elif r['media'] >=5:
            r['situacao'] = 'razoavel'
        else:
            r['situacao'] = 'ruim'
    return r
resp = nota(5, 2, 7,5 , sit=True )
print(resp)
help(nota)
