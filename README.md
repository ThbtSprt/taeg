# taeg
[![](https://img.shields.io/badge/pypi-v0.4-blue)](https://pypi.org/project/taeg/)

Module python de recherche du taux annuel effectif global à partir des données du contrat (dans l'hypothèse d'un déblocage des fonds en une seule fois).

**Textes de référence :**
- Articles R.314-1 et suivants du code de la consommation [lien](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032807602/#LEGISCTA000032807602)
- Annexe 1 de la DIRECTIVE 2008/48/CE DU PARLEMENT EUROPÉEN ET DU CONSEIL du 23 avril 2008 [lien (voir page 19 du pdf)](https://eur-lex.europa.eu/legal-content/FR/TXT/PDF/?uri=CELEX:32008L0048&from=FR)


**Installation :**
```python
pip install taeg
```

**Utilisation :**

La fonction principale de ce module est la fonction `calcul()`, qui prend les arguments suivants :

*arguments obligatoires :*
- montant_credit : une somme exprimée en chiffres
- nb_mens : le nombre de mensualités de remboursement
- montant_mens : le montant des mensualités (ou, si elles ne sont pas toutes identiques, celui des mensualités les plus nombreuses)

*arguments facultatifs :*
- frais : le montant des frais déduits de la somme prêtée (par défaut : `frais=''`
- num_mens_spec : le(s) numéro(s) d'ordre des mensualités d'un autre montant (à saisir au format `str` et à séparer par une virgule si plusieurs mensualités sont concernées)
- montant_mens_spec : le montant des mensualités dont le numéro d'ordre a été saisi dans `num_mens_spec`,
- deblocage : la date de déblocage des fonds si le décalage entre le financement et la première mensualité est supérieur ou inférieur à un mois,
- premiere_mens : la date de prélèvement de la première mensualité, dans l'hypothèse précitée


**Exemples:**

```python
>>> from taeg import calcul

>>> calcul(3000,24,130)
3.86077

>>> calcul(
        montant_credit = 3000,
        nb_mens = 24,
        montant_mens = 150,
        frais = 0,
        num_mens_spec = '1,2,24',
        montant_mens_spec = '100,100,200',
        deblocage = '01/01/2000',
        premiere_mens= '01/05/2000'
        )
13.71107
```
