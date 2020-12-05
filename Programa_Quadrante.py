
x = int (input('Digite a coordenada x: ')) 

y = int (input('Digite a coordenada y: '))

if x > 0 and y > 0: 

 print ('As coordenadas',x,y, 'pertencem ao 1º Quadrante') 

elif x > 0 and y < 0: 

 print ('As coordenadas',x,y, 'pertencem ao 4º Quadrante') 

elif x < 0 and y > 0: 

 print ('As coordenadas',x,y, 'pertencem ao 2º Quadrante') 

elif x < 0 and y < 0: 

 print ('As coordenadas',x,y, 'pertencem ao 3º Quadrante') 

elif x == 0: 

 print (x,y, 'A coordenada x está no ponto central') 

elif y == 0: 

 print (x,y, 'A coordenada y está no ponto central') 
