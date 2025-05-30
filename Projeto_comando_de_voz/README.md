# Sistema de Automação Residencial por Voz

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Um sistema de controle de lâmpadas por comandos de voz em português, desenvolvido em Python.

## Funcionalidades

- Controle individual de até 3 lâmpadas por voz
- Comandos para ligar/desligar todas as lâmpadas
- Verificação do status das lâmpadas
- Reconhecimento de voz em português brasileiro
- Resposta por voz com sintetizador configurado

## Comandos Suportados

- `ligar lâmpada [1-3]`
- `desligar lâmpada [1-3]`
- `ligar todas as lâmpadas`
- `desligar todas as lâmpadas`
- `status das lâmpadas`
- `sair` ou `encerrar` - para terminar o programa

## Pré-requisitos

- Python 3.6 ou superior
- Microfone funcional
- Conexão com a internet (para reconhecimento de voz)

## Bibliotecas Necessárias

```bash
pip install SpeechRecognition pyttsx3