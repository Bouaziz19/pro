det="""{"t_population": "1", "depots": [["d1,d2"]], "bathint": [["9580", "520"], ["0", "1"]], "nb": "8", "cont_dem": true,
 "delai_fin": "2000", "volumebatch": "10100", "Localdep": [["6200", "10100"], ["6200", "10100"]],
 "fin": [["6200,10100"]], "n_c_a": "50", "p_c_c": "0.2", "temps_sum": "15", "crit_dar": "1", "ndepo": "2",
 "Demdepo": [["1200", "400", "80", "0"], ["3000", "800", "150", "150"]],
 "cont_entr": [["n", "28", "30", "n"], ["28", "n", "n", "0"], ["30", "n", "n", "n"], ["30", "n", "n", "n"]],
 "debu": [["6200,10100"]], "nprod": "4", "co_inj": [["1,5000"]], "co_pom_inj": [["150,300"]], "pas": "1",
 "produits": [["p1,p2,p3,p4"]]}"""
det.replace('true','True')
print det.replace('true','True')