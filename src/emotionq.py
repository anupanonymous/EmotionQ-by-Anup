import RPi.GPIO as GPIO
import time
import cv2
from deepface import DeepFace
import random

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
PIR_PIN = 17
BUZZER_PIN = 27
RED_PIN = 22
GREEN_PIN = 23
BLUE_PIN = 24

# Configure GPIO pins
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# Initialize camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

if not cap.isOpened():
    print("Error: Could not open video device")
else:
    print("Camera initialized successfully")

# Define quotes based on emotions
quotes = {
    "happy": [
        "Happiness is the best medicine.",
        "Stay happy and positive!",
        "Keep smiling, it suits you."
    ],
    "sad": [
        "It's okay to feel sad sometimes.",
        "Stay strong, better days are ahead.",
        "It's just a bad day, not a bad life."
    ],
    "angry": [
        "Take a deep breath, it'll be okay.",
        "Stay calm and carry on.",
        "Anger doesn't solve anything."
    ],
    "neutral": [
        "Stay balanced and composed.",
        "Keep calm and stay neutral.",
        "Everything is under control."
    ],
    "fear": [
        "Fear is temporary, regret is forever.",
        "Face your fears with courage.",
        "You are stronger than you think."
    ],
    "surprise": [
        "Expect the unexpected.",
        "Life is full of surprises.",
        "Embrace the unexpected moments."
    ],
    "disgust": [
        "Find beauty in everything.",
        "Focus on the positives.",
        "Look for the good in every situation."
    ]
}

# Function to set RGB LED color
def set_rgb_color(r, g, b):
    GPIO.output(RED_PIN, r)
    GPIO.output(GREEN_PIN, g)
    GPIO.output(BLUE_PIN, b)

try:
    print("Starting PIR sensor...")
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion detected!")
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            set_rgb_color(1, 0, 0)  
            time.sleep(0.5)
            GPIO.output(BUZZER_PIN, GPIO.LOW)

            print("Camera feed opened. Position yourself and press 'Enter' to capture the image.")

            while True:
                ret, frame = cap.read()
                if ret:
                    cv2.imshow("Camera Feed", frame)
                    if cv2.waitKey(1) & 0xFF == 13:  
                        break
                else:
                    print("Failed to capture image")

            cv2.destroyAllWindows()

            print("Capturing image...")
            ret, frame = cap.read()
            if ret:
                print("Image captured successfully")
                cv2.imwrite("captured_frame.jpg", frame)

                result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                dominant_emotion = result[0]['dominant_emotion'] if isinstance(result, list) else result['dominant_emotion']

                if dominant_emotion:
                    print(f"Detected emotion: {dominant_emotion}")

                    # Set RGB color based on detected emotion
                    if dominant_emotion == 'happy':
                        set_rgb_color(0, 1, 0)  # Green
                    elif dominant_emotion == 'sad':
                        set_rgb_color(0, 0, 1)  # Blue
                    elif dominant_emotion == 'angry':
                        set_rgb_color(1, 0, 0)  # Red
                    elif dominant_emotion == 'neutral':
                        set_rgb_color(1, 1, 1)  # White
                    elif dominant_emotion == 'fear':
                        set_rgb_color(1, 1, 0)  # Yellow
                    elif dominant_emotion == 'surprise':
                        set_rgb_color(1, 0, 1)  # Purple
                    elif dominant_emotion == 'disgust':
                        set_rgb_color(0, 1, 1)  # Cyan

                    # Print a random quote based on detected emotion
                    if dominant_emotion in quotes:
                        print(random.choice(quotes[dominant_emotion]))
                else:
                    print("No dominant emotion detected")
                    set_rgb_color(1, 1, 1)  

            else:
                print("Failed to capture image")

            time.sleep(5)
        else:
            set_rgb_color(0, 0, 0)  
            time.sleep(0.1)
except KeyboardInterrupt:
    print("Program terminated")
finally:
    GPIO.cleanup()
    cap.release()
    cv2.destroyAllWindows()
