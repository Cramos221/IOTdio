import speech_recognition as sr
import pyttsx3
import re
import subprocess

# Configuração das lâmpadas (simulação)
lampadas = {
    1: False,
    2: False,
    3: False
}

def configurar_voz():
    """Configura o sintetizador de voz com a melhor voz disponível"""
    engine = pyttsx3.init()
    
    # Verificar e configurar a melhor voz em português
    try:
        # Tentar usar MBROLA (voz mais natural)
        engine.setProperty('voice', 'mbrola/pt1')
    except:
        try:
            # Tentar usar RHVoice (se instalado)
            engine.setProperty('voice', 'RHVoice/brazil')
        except:
            try:
                # Usar eSpeak como fallback
                engine.setProperty('voice', 'pt-br')
            except:
                # Usar voz padrão do sistema
                pass
    
    # Ajustes de qualidade de voz
    engine.setProperty('rate', 160)     # Velocidade (140-180 é ideal)
    engine.setProperty('volume', 0.9)   # Volume (0.0 a 1.0)
    engine.setProperty('pitch', 50)     # Tom (0-100)
    
    return engine

def falar(texto):
    """Faz o assistente falar o texto fornecido"""
    print(f"Assistente: {texto}")
    
    # Tentar usar MBROLA diretamente (produz melhor qualidade)
    try:
        subprocess.run(['espeak-ng', '-v', 'pt-br', '-s', '160', texto])
        return
    except:
        pass
    
    # Fallback para pyttsx3
    engine.say(texto)
    engine.runAndWait()

# Inicializa o reconhecedor de voz e o sintetizador
recognizer = sr.Recognizer()
engine = configurar_voz()

def ouvir_microfone():
    """Captura áudio do microfone e converte para texto"""
    with sr.Microphone() as source:
        print("\nAguardando comando...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            texto = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {texto}")
            return texto.lower()
        except sr.WaitTimeoutError:
            falar("Não detectei nenhum comando. Tente novamente.")
            return None
        except sr.UnknownValueError:
            falar("Não consegui entender o comando. Pode repetir?")
            return None
        except sr.RequestError as e:
            falar(f"Erro no serviço de reconhecimento: {e}")
            return None

def processar_comando(comando):
    """Processa o comando de voz e executa a ação correspondente"""
    if not comando:
        return

    # Padroniza variações de pronúncia
    comando = re.sub(r'l[âa]mpada[s]?', 'lampada', comando)
    
    # Controle individual das lâmpadas
    for num in [1, 2, 3]:
        if f"lampada {num}" in comando:
            if "liga" in comando:
                lampadas[num] = True
                falar(f"Lâmpada {num} ligada")
            elif "desliga" in comando:
                lampadas[num] = False
                falar(f"Lâmpada {num} desligada")
            return

    # Controle geral
    if "toda" in comando:
        estado = "liga" in comando
        for num in lampadas:
            lampadas[num] = estado
        falar(f"Todas as lâmpadas {'ligadas' if estado else 'desligadas'}")
    
    elif "status" in comando:
        status = ", ".join([f"Lâmpada {num}: {'ligada' if estado else 'desligada'}" 
                          for num, estado in lampadas.items()])
        falar(f"Status atual: {status}")
    
    elif "sair" in comando or "encerra" in comando:
        falar("Encerrando sistema de automação residencial")
        return True
    
    else:
        falar("Comando não reconhecido. Diga algo como 'ligar lâmpada 1' ou 'desligar todas'")

def main():
    falar("Sistema de automação residencial iniciado")
    falar("Como posso ajudar?")
    
    while True:
        comando = ouvir_microfone()
        if comando and processar_comando(comando):
            break

if __name__ == "__main__":
    main()