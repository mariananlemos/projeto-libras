# Audio Transcription with VLibras

Web application for audio transcription using Whisper AI and translation into Libras through VLibras.

## Features

- **Audio recording** directly through the browser  
- **Automatic transcription** using OpenAI Whisper  
- **Translation to Libras** integrated with VLibras  
- Responsive and modern interface  
- GPU support for faster processing  

## Technologies Used

- **Flask** - Python web framework  
- **OpenAI Whisper** - Audio transcription model  
- **VLibras** - Brazilian Sign Language translator  
- **PyTorch** - Backend for Whisper  
- **Flask-CORS** - Support for cross-origin requests  

## Project Structure

```
projeto-libras/
├── app.py              # Main Flask application
├── stt.py              # Transcription module with Whisper
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Web interface
└── uploads/           # Temporary directory for audio files
```

---

Developed with ❤️ for accessibility
