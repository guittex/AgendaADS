import funcoes

def test_adicionar_sucesso ():
    assert funcoes.adicionar('pablo','12345678') == True

def test_adicionar_falha ():
    assert funcoes.adicionar('pablo', '1234') == False