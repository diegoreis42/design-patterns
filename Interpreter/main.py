class Context:
    """
    O contexto que mantém informações sobre o sistema de automação residencial.
    """
    def __init__(self):
        self.devices = {
            "luz": "desligada",
            "termostato": "desligado",
            "porta": "destrancada",
        }
    
    def execute_action(self, device, action, value=None):
        if device not in self.devices:
            return f"Dispositivo '{device}' não encontrado."
        
        if action == "ligar":
            self.devices[device] = "ligado"
            return f"{device.capitalize()} ligada."
        elif action == "ajustar":
            self.devices[device] = f"ajustado para {value} graus"
            return f"{device.capitalize()} ajustado para {value} graus."
        elif action == "trancar":
            self.devices[device] = "trancada"
            return f"{device.capitalize()} trancada."
        else:
            return f"Ação '{action}' não suportada."

class Expression:
    """
    Interface abstrata para todas as expressões.
    """
    def interpret(self, context):
        pass

class TerminalExpression(Expression):
    """
    Expressão terminal que interpreta palavras-chave específicas.
    """
    def __init__(self, word):
        self.word = word

    def interpret(self, context):
        return self.word

class CommandExpression(Expression):
    """
    Expressão não terminal que interpreta um comando completo.
    """
    def __init__(self, action, device, value=None):
        self.action = action
        self.device = device
        self.value = value

    def interpret(self, context):
        return context.execute_action(self.device.interpret(context), 
                                      self.action.interpret(context), 
                                      self.value.interpret(context) if self.value else None)

class ValueExpression(Expression):
    """
    Expressão terminal para interpretar valores numéricos.
    """
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value

# Simulação de entrada de comandos
if __name__ == "__main__":
    context = Context()

    # Comandos: "Ligar luz", "Ajustar termostato para 22 graus", "Trancar a porta"
    commands = [
        CommandExpression(TerminalExpression("ligar"), TerminalExpression("luz")),
        CommandExpression(TerminalExpression("ajustar"), TerminalExpression("termostato"), ValueExpression(22)),
        CommandExpression(TerminalExpression("trancar"), TerminalExpression("porta"))
    ]

    # Interpretando e executando os comandos
    for command in commands:
        print(command.interpret(context))

    # Exibindo o estado atual dos dispositivos
    print("\nEstado atual dos dispositivos:")
    for device, state in context.devices.items():
        print(f"{device.capitalize()}: {state}")
