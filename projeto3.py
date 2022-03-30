'''
Projeto - Medidor de Velocidade

Levando em consideração a velocidade máxima de 80km em uma determinada rua. Crie um programa que recebe do usuário um valor que representa a velocidade e com base nessa velocidade diga se ele tomou uma multa leve, grave ou gravíssima. Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "não houve multa" , caso esteja até 10km acima, deve exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velocidade máxima, exiba : "levou multa gravíssima".

Anaalise criticamente o problema e descubra :
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada nescessários
- Velocidade
2. O que devo fazer com estes dados?
Levando em consideração que se a pessoa estiver abaaixo da velocidade máxima seu programa deve exibir "não houve multa" , caso esteja até 10km acima, deve exibir: "levou a multa leve", caso esteja entre 11 a 20km acima da velocidade máxima, exiba: "levou multa gravíssima"
3. Quais são as restrições deste problema?
4. Qual é o resultado esperado?
- O resultado esperado é exibir a mensagem que corresponde ao nivel da múlta que a pessoa levou exibir: "levou multa grave", caso esteja entre 11 a 20km acima da velocidade máxima, exibir: "levou multa grave", e caso esteja acima de 20km da velocidade máxima, exiba: "levou multa gravíssima")
5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
input velocidade
velocidade_máxima = 80
if velocidade <= velocidade_maxima
 print "não levou multa"
if velocidade > velocidade_maxima e velocidade <= velocidade_maxima + 10:
 print'levou multa leve'
if velocidade > velocidade_maxima + 11 e velocidade <= velocidade_maxima + 20:
 print "levou multa grave"
if velocidade > velocidade_maxima +20:
 print "levou multra gravíssima"'''

velocidade = int(input('Digite sua velocidade'))
velocidade_maxima = 89
if velocidade <= velocidade_maxima:
   print('não levou multa')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
   print ('levou multa leve')
elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
   print('levou multa grave')
elif velocidade > velocidade_maxima + 20: 
  print ('levou multa gravissima')