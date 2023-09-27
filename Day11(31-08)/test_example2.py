def greet(person):
    return "Hey {name}".format(**person)
    
def test_greet():
    Jon = {"name":"Jon"}
    greeting = greet(Jon)
    assert greeting == "Hey Jon"
    
