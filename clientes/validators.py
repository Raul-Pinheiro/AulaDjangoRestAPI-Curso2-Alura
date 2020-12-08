from validate_docbr import CPF



def cpf_valido(cpf_number):
   cpf=CPF()   
   valido=cpf.validate(cpf_number)
   return valido

def rg_valido(rg):
    return len(rg) ==9
   
def nome_valido(nome):
    return nome.isalpha()==True
 
#def celular_valido(celular):
    #return len(celular)<11:
  