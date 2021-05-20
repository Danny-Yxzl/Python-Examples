from win32com.client import Dispatch
speaker = Dispatch("SAPI.SpVoice")

speaker.Speak("你好，世界！")
speaker.Speak("Hello World!")
