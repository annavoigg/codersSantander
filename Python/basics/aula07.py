#!/usr/bin/env python
# coding: utf-8

# In[3]:


contador = 0

while contador < 10:
    contador = contador + 1
    if contador == 1:
        print(contador, " item limpo")
    
    else:
        print(contador, " itens limpos")
        
print("Fim da repetição do bloco while")


# In[8]:


contador = 0

while True:
    if contador < 10:
        contador = contador + 1
        if contador == 1:
            print(contador, " item limpo")
        else:
            print(contador, " itens limpos")
    else:
        break
        
print("Fim da repetição do bloco while")


# In[9]:


texto = input("Digite a sua senha: ")

while texto != "letscode":
    texto = input("Senha inválida. Tente novamente")
    
print("Acesso permitido")


# In[10]:


contador = 0

while contador < 10:
    contador = contador + 1
    if contador == 1:
        continue
    print(contador, " itens limpos")
        
print("Fim da repetição do bloco while")


# In[ ]:




