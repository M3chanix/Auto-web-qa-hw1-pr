from hw1.Figure import Figure

def test_instance():
    figure = None
    try: 
        figure = Figure()
    except TypeError:
        pass
    assert figure == None

