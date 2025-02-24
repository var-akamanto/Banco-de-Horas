class Employee  :
     def __init__(
               self,
               matricula: int,
               nome : str,
               cargo : str,
               jornada : int,
               contato : str,
               email : str,
               situacao : str,
               observacoes : str
     ):
          self.matricula = matricula
          self.nome = nome
          self.cargo = cargo
          self.jornada = jornada
          self.contato = contato
          self.email = email
          self.situacao = situacao
          self.observacoes = []
          self.observacoes.append(observacoes)

          pass