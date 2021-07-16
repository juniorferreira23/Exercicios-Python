from time import sleep
from emoji import emojize
print('-=-' * 14)
print('Contagem regressiva para queima de fogos!')
print('-=-' * 14)
for c in  range(10, -1 , -1):
    print(c)
    sleep(0.5)
print('Queima de fogos!')
print(emojize(':fireworks::fireworks::fireworks::fireworks::fireworks:'))
