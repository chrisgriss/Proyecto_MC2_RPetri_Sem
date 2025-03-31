from graphviz import Digraph
dot = Digraph(comment='Red De Semaforos', format = 'png')
#Tipo de luces en la vía principal
dot.node('L_VP', 'Luz verde principal', shape = 'ellipse', style= 'filled', color = 'darkgreen')
dot.node('L_AP', 'Luz amarilla principal', shape = 'ellipse',  style= 'filled', color = 'yellow')
dot.node('L_RP', 'Luz roja principal', shape = 'ellipse', style= 'filled', color = 'red')
#Tipo de luces en la vía secundaria
dot.node('L_VS', 'Luz verde secundaria', shape = 'ellipse', style= 'filled', color = 'darkgreen')
dot.node('L_AS', 'Luz amarilla secundaria', shape = 'ellipse', style= 'filled', color = 'yellow')
dot.node('L_RS', 'Luz roja secundaria', shape = 'ellipse', style= 'filled', color = 'red')

#Transiciones
dot.node('TRVP','Trans. rojo a verde principal', shape = 'box', style= 'filled', color = 'purple')
dot.node('TVAP','Trans. verde a amarillo principal', shape = 'box', style= 'filled', color = 'purple')
dot.node('TARP','Trans. amarillo a rojo principal', shape = 'box', style= 'filled', color = 'purple')
dot.node('TRVS','Trans. rojo a verde secundaria', shape = 'box', style= 'filled', color = 'purple')
dot.node('TVAS','Trans. verde a amarillo secundaria', shape = 'box', style= 'filled', color = 'purple')
dot.node('TARS','Trans. amarillo a rojo secundaria', shape = 'box', style= 'filled', color = 'purple')

#Arcos
dot.edge('L_RP', 'TRVP','Luz Roja a T1')
dot.edge('TRVP', 'L_VP', 'T1 a Luz verde')
dot.edge('TRVP','TARS', 'T1 a T5')
dot.edge('TARS','L_RS','T5 a Luz Roja')
dot.edge('L_RS','TRVS','Luz roja a T6')
dot.edge('TRVS','L_VS', 'T6 a Luz verde')
dot.edge('TRVS','TARP','T6 a T4')
dot.edge('L_VS','TVAS','Luz verde a T7')
dot.edge('TVAS','L_AS','T7 a Luz amarilla')
dot.edge('L_AS','TARS', 'luz amarilla a T5')
dot.edge('L_VP', 'TVAP', 'Luz verde a T2')
dot.edge('TVAP', 'L_AP','De T3 a amarilla')
dot.edge('L_AP','TARP','Luz Amarilla a Roja T4')
dot.edge('TARP','L_RP','T4 a Luz Roja')



dot.render('semaforo_red_Pet')