# Target: Interface esperada pelo aplicativo
class AudioDevice:
    def play(self):
        raise NotImplementedError("Método 'play' precisa ser implementado")
    
    def stop(self):
        raise NotImplementedError("Método 'stop' precisa ser implementado")

# Adaptee: O rádio com uma interface incompatível
class OldRadio:
    def start_radio(self):
        print("Rádio: Ligado e tocando música.")
    
    def stop_radio(self):
        print("Rádio: Desligado.")

# Adapter: Traduz a interface do rádio para o padrão esperado
class RadioAdapter(AudioDevice):
    def __init__(self, radio):
        self.radio = radio

    def play(self):
        self.radio.start_radio()
    
    def stop(self):
        self.radio.stop_radio()

# Client: Sistema que usa a interface esperada
class AudioApp:
    def __init__(self, device):
        self.device = device

    def start_audio(self):
        self.device.play()

    def stop_audio(self):
        self.device.stop()

# Uso do sistema
# Instanciamos o rádio antigo
radio = OldRadio()

# Criamos um adaptador para o rádio
radio_adapter = RadioAdapter(radio)

# Passamos o adaptador para o aplicativo
app = AudioApp(radio_adapter)

# Controlamos o rádio pelo aplicativo
app.start_audio()  # Rádio: Ligado e tocando música.
app.stop_audio()   # Rádio: Desligado.
