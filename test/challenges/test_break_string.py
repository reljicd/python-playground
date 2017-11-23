from src.challenges.break_string import break_string


def test_break_string():
    assert break_string('CatMat', ['Cat', 'Mat', 'Ca', 'tM', 'at', 'C', 'Dog', 'og', 'Do']) == 1
    assert break_string('CatMat', ['Mat', 'Ca', 'tM', 'at', 'Dog', 'og', 'Do']) == 2
    assert break_string('CatMat', ['CatM', 'Dog', 'og', 'Do', 'Mat', 'Ca', 't', 'tM', 'C']) == 2
