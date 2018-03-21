import funcoes

def test_adicionar_sucesso ():
    assert funcoes.adicionar('pablo','123456') == True

def test_adicionar_falha ():
    assert funcoes.adicionar('pablo', '1234') == False