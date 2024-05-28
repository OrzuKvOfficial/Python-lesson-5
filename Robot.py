import turtle
import speech_recognition as sr

# Tanlangan qadam miqdori
step_size = 20

# Turtle obyektini yaratish
t = turtle.Turtle()

# Qol ishorasiga qarab harakatlanuvchi robot funksiyasi
def move_forward():
    t.forward(step_size)

def move_backward():
    t.backward(step_size)

def turn_left():
    t.left(90)

def turn_right():
    t.right(90)

# Ovozni qabul qilish va boshqarish funksiyalari
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Iltimos, gapiring...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        speech = r.recognize_google(audio, language="uz-UZ")
        print("Sizning so'zingiz:", speech)
        execute_command(speech)
    except sr.UnknownValueError:
        print("Men gaplarni eshitib bo'lmadim")
    except sr.RequestError:
        print("Google Xizmatlariga ulanib bo'lmadi")

def execute_command(command):
    if "yur" in command:
        move_forward()
    elif "orqaga" in command:
        move_backward()
    elif "chap" in command:
        turn_left()
    elif "o'ng" in command:
        turn_right()

# Asosiy dastur
def main():
    # Tugma funksiyalari bilan qol ishorasiga qarab harakatlanuvchi robotni boshlash
    while True:
        recognize_speech()

# Dasturni boshlash
if __name__ == "__main__":
    main()


# Liste oluşturma
words = ["apple", "banana", "cherry", "date"]

# Uzunluğa göre sıralama
words.sort(key=len)

# Sonuçları yazdırma
print("Uzunluğa göre sıralanmış liste:", words)
