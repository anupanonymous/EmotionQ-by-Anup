# Emotion Detection System with IoT and AI

A **real-time emotion detection system** that combines **computer vision, deep learning, and IoT**.  
It captures human emotions via a camera, triggers RGB LEDs and a buzzer on a Raspberry Pi, and displays **contextual motivational quotes** based on the detected emotion.

## 🎯 Features
- **Emotion detection** using [DeepFace](https://github.com/serengil/deepface) and OpenCV
- **Real-time motion detection** using a PIR sensor
- **IoT Integration**:
  - RGB LED changes color based on detected emotion
  - Buzzer alerts on motion detection
- **Context-based quotes** displayed per emotion
- Modular and **multi-purpose** concept:
  - **Pubs:** Suggest drinks based on customer mood  
  - **Libraries:** Recommend books based on mood  
  - **Retail:** Trigger emotion-based promotions  

---

## 🖼️ Project Demo

Sample emotion detection screenshots:

<p align="center">
  <img src="sample_output/happy.png" width="250" />
  <img src="sample_output/sad.png" width="250" />
</p>

---

## 🛠️ Tech Stack

- **Python 3**  
- **OpenCV** – Real-time camera feed  
- **DeepFace** – Emotion recognition  
- **Raspberry Pi GPIO** – Controlling PIR sensor, RGB LEDs, and buzzer  
- **Random & Time modules** – Event handling & response timing  

---

## 📂 Project Structure

