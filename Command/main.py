# 1. Command - Interface
class Command:
    def execute(self):
        pass


# 2. ConcreteCommand - Comandos Concretos
class PedidoPratoPrincipalCommand(Command):
    def __init__(self, cozinha_principal, prato):
        self.cozinha_principal = cozinha_principal
        self.prato = prato

    def execute(self):
        self.cozinha_principal.preparar_prato(self.prato)


class PedidoSobremesaCommand(Command):
    def __init__(self, cozinha_secundaria, sobremesa):
        self.cozinha_secundaria = cozinha_secundaria
        self.sobremesa = sobremesa

    def execute(self):
        self.cozinha_secundaria.preparar_sobremesa(self.sobremesa)


# 3. Receiver - Destinatários (Cozinhas)
class CozinhaPrincipal:
    def preparar_prato(self, prato):
        print(f"Cozinha Principal: Preparando o prato principal {prato}.")


class CozinhaSecundaria:
    def preparar_sobremesa(self, sobremesa):
        print(f"Cozinha Secundária: Preparando a sobremesa {sobremesa}.")


# 4. Invoker - Remetente (Garçom)
class Garcom:
    def __init__(self):
        self.comando = None

    def set_comando(self, comando):
        self.comando = comando

    def fazer_pedido(self):
        if self.comando:
            self.comando.execute()


# 5. Client - Cliente (configura os comandos)
if __name__ == "__main__":
    # Criando as cozinhas (destinatários)
    cozinha_principal = CozinhaPrincipal()
    cozinha_secundaria = CozinhaSecundaria()

    # Criando os comandos com as referências para as cozinhas
    pedido_prato = PedidoPratoPrincipalCommand(cozinha_principal, "Pizza")
    pedido_sobremesa = PedidoSobremesaCommand(cozinha_secundaria, "Torta de Limão")

    # Criando o garçom (invocador)
    garcom = Garcom()

    # Garçom faz o pedido do prato principal
    garcom.set_comando(pedido_prato)
    garcom.fazer_pedido()

    # Garçom faz o pedido da sobremesa
    garcom.set_comando(pedido_sobremesa)
    garcom.fazer_pedido()
