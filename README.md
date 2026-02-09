# Transcrição de Áudio com VLibras

Aplicação web para transcrição de áudio usando Whisper AI e tradução para Libras através do VLibras.

## 🚀 Funcionalidades

- **Gravação de áudio** diretamente pelo navegador
- **Transcrição automática** usando OpenAI Whisper
- **Tradução para Libras** integrada com VLibras
- Interface responsiva e moderna
- Suporte a GPU para processamento mais rápido

## 📋 Pré-requisitos

- Python 3.8+
- FFmpeg (necessário para o Whisper)
- Navegador moderno com suporte a MediaRecorder API

### Instalação do FFmpeg

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**
Baixe de [ffmpeg.org](https://ffmpeg.org/download.html)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/projeto-libras.git
cd projeto-libras
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 💻 Uso

1. Inicie o servidor Flask:
```bash
python app.py
```

2. Acesse no navegador:
```
http://localhost:5000
```

3. Clique em **"Gravar"** para iniciar a gravação de áudio
4. Clique em **"Parar"** quando terminar
5. O texto transcrito aparecerá automaticamente
6. Se habilitado, o VLibras traduzirá automaticamente para Libras

## 🛠️ Tecnologias Utilizadas

- **Flask** - Framework web Python
- **OpenAI Whisper** - Modelo de transcrição de áudio
- **VLibras** - Tradutor para Língua Brasileira de Sinais
- **PyTorch** - Backend para o Whisper
- **Flask-CORS** - Suporte a requisições cross-origin

## 📁 Estrutura do Projeto

```
projeto-libras/
├── app.py              # Aplicação Flask principal
├── stt.py              # Módulo de transcrição com Whisper
├── requirements.txt    # Dependências Python
├── templates/
│   └── index.html     # Interface web
└── uploads/           # Diretório temporário para áudios
```

## ⚙️ Configuração

### Modelo Whisper

Por padrão, o projeto usa o modelo `tiny` para transcrição rápida. Você pode alterar em `stt.py`:

```python
modelo = whisper.load_model("tiny", device=device)  # tiny, base, small, medium, large
```

**Modelos disponíveis:**
- `tiny` - Mais rápido, menos preciso (~75MB)
- `base` - Balance entre velocidade e precisão (~150MB)
- `small` - Boa precisão (~500MB)
- `medium` - Alta precisão (~1.5GB)
- `large` - Maior precisão (~3GB)

### GPU

O projeto detecta automaticamente se há GPU disponível (CUDA). Para forçar CPU:

```python
device = "cpu"
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abrir um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🙏 Agradecimentos

- [OpenAI Whisper](https://github.com/openai/whisper) - Modelo de transcrição
- [VLibras](https://www.gov.br/governodigital/pt-br/vlibras) - Tradutor para Libras
- Comunidade open source

## 📧 Contato

Para dúvidas ou sugestões, abra uma issue no GitHub.

---

Desenvolvido com ❤️ para acessibilidade