#!/usr/bin/env python
# coding: utf-8

# In[3]:


valorPassagem = 4.30

valorCorrida = input("Qual é o valor da corrida até o seu destino? ")

if float(valorCorrida) <= valorPassagem * 5:
    print("Pague a corrida")
    
if float(valorCorrida) > valorPassagem * 5:
    print("Pegue o ônibus")


# In[5]:


valorPassagem = 4.30

valorCorrida = input("Qual é o valor da corrida até o seu destino? ")

if float(valorCorrida) <= valorPassagem * 5:
    print("Pague a corrida")
    
else:
    print("Pegue o ônibus")


# In[23]:


valorPassagem = 4.30

valorCorrida = input('Qual é o valor da corrida até o seu destino? ')

if float(valorCorrida) <= valorPassagem * 5:
    print('Pague a corrida')
    
else:
    if float(valorCorrida) <= valorPassagem * 6:
        print('Aguarde um momento, o valor pode abaixar!')
    else:
        print('Pegue o ônibus')


# In[30]:


valorPassagem = 4.30

valorCorrida = input('Qual é o valor da corrida até o seu destino? ')

if float(valorCorrida) <= valorPassagem * 5:
    print('Pague a corrida')
    
elif float(valorCorrida) <= valorPassagem * 6:
        print('Aguarde um momento, o valor pode abaixar!')
        
else:
        print('Pegue o ônibus')


# In[ ]:




