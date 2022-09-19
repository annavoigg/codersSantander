#!/usr/bin/env python
# coding: utf-8

# In[1]:


idade = input("Informe sua idade: ")
print(idade, type(idade))


# In[2]:


idade = int(idade)
print(idade, type(idade))


# In[3]:


print(float('123.25'))
print(str(123.25))
print(bool(''))
print(bool('abc'))
print(bool(0))
print(bool(-2))


# In[4]:


salarioMensal = input("Digite o valor do seu salário mensal: ")
salarioMensal = float(salarioMensal)

gastoMensal = input("Digite o valor do seu gasto mensal: ")
gastoMensal = float(gastoMensal)

salarioTotal = salarioMensal * 12
gastoTotal = gastoMensal * 12

montanteEconomizado = salarioTotal - gastoTotal
print("O montante que você pode economizar ao fim do ano é de: ", montanteEconomizado)


# In[ ]:




