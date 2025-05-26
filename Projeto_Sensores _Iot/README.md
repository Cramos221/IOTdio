# 🚀 Detecção de Objetos com YOLOv8 no Google Colab

Projeto simples para detectar objetos em imagens, vídeos ou webcam usando YOLOv8.  

## 🔧 Como Usar  

1. Acesse o Google Colab:  
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)  

2. Habilite a GPU:  
   `Runtime` > `Change runtime type` > Escolha **T4 GPU**.  

3. Instale as dependências:  
   ```python
   !pip install ultralytics opencv-python
   ```

4. Execute a detecção:  
   ```python
   from ultralytics import YOLO
   model = YOLO('yolov8n.pt')
   results = model('sua_imagem.jpg')  # Substitua pelo seu arquivo
   results[0].show()
   ```

## 📂 Estrutura do Projeto
```plaintext
/
├── yolov8_detection.ipynb          # Notebook do Colab
├── images/                         # Pasta para imagens de teste
├── runs/                           # Resultados das detecções
└── README.md                       # Este arquivo
```

## 📌 Exemplo
![Exemplo de Detecção](https://ultralytics.com/images/yolov8n-det.jpg)  

## **⚙️ Comandos Úteis**  
- **Detecção em vídeo**:  
  ```python
  results = model('video.mp4')
  ```
- **Treinamento customizado**:  
  ```python
  model.train(data='data.yaml', epochs=50)
  ```

## 📜 Licença 
MIT  

Feito  por CLEISSONrAMOS  

