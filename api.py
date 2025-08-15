import os
from flask import Flask, jsonify, request, send_file
from kittentts import KittenTTS
import soundfile as sf

m = KittenTTS("KittenML/kitten-tts-nano-0.1")



# Save the audio


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<html><body>ktts</body></html>"

@app.route("/health")
def health():
    return jsonify({"status":"ok"}), {"Content-Type": "text/csv"}

@app.route("/tts")
def tts():
  text = request.args.get('text')

  filepath = f"./vol/audio_{hash(text)}.wav"

  if not os.path.exists(filepath):
    # available_voices : [  'expr-voice-2-m', 'expr-voice-2-f', 'expr-voice-3-m', 'expr-voice-3-f',  'expr-voice-4-m', 'expr-voice-4-f', 'expr-voice-5-m', 'expr-voice-5-f' ]
    audio = m.generate(text, voice='expr-voice-2-f')
    sf.write(filepath, audio, 24000)

  return send_file(
    filepath,
    mimetype='audio/wav'
  )