from app import insecure_function

def test_insecure_function(capsys):
    insecure_function("secret")
    captured = capsys.readouterr()
    assert "secret" in captured.out
