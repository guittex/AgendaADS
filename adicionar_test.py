import funcoes

def test_adicionar_sucesso ():
    assert funcoes.adicionar('pablo','12345678') == False

def test_adicionar_falha ():
    assert funcoes.adicionar('pablo', '1234') == True