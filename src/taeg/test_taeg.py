from taeg import calcul


def test_taeg():
    assert calcul(3000, 24, 130) == 3.8607706
    assert calcul(
            montant_credit = 3000,
            nb_mens = 24,
            montant_mens = 150,
            frais = 0,
            num_mens_spec = '1,2,24',
            montant_mens_spec = '100,100,200',
            deblocage = '01/01/2000',
            premiere_mens= '01/05/2000'
            ) == 13.7110692
