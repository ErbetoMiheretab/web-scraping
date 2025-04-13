import pandas as pd

states = ["cali","texas","Florida", "NY"]
population = [1234,4567,8910,111213]

dict_states = {'States':states, 'Population': population}

df_states = pd.DataFrame.from_dict(dict_states)


print(df_states)
#df_states.to_csv('states.csv', index-Fasle)

"""
ITts recommended to find elts in this order
ID CLASS NAME  TAG NAME,CSS SELECTOR XPATH
"""