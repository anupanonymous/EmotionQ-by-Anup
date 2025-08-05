# Emotion Detection System with IoT & AI

**Author:** [Anup Chapagain](https://github.com/anupanonymous)  
**Email:** uanup.mpersonal.a@gmail.com  
**GitHub:** [anupanonymous](https://github.com/anupanonymous)  

---

## 🌟 Project Overview

This project is a **real-time emotion detection system** that combines:

- **Artificial Intelligence (DeepFace + OpenCV)**  
- **IoT Hardware (Raspberry Pi GPIO)**  
- **Interactive Feedback (RGB LEDs + Buzzer + Quotes)**

It captures human emotion via a camera, analyzes it using **DeepFace**, and responds by:  
1. **Lighting an RGB LED** in the color mapped to the detected emotion  
2. **Triggering a buzzer** upon motion detection  
3. **Displaying a context-based motivational quote**  

This system can be **adapted for multiple real-world applications**:
- 🎵 **Pubs** – Suggest a drink based on customer mood  
- 📚 **Libraries** – Recommend books based on emotional state  
- 🛍 **Retail** – Trigger emotion-based promotions  

---

## 🧠 Features

- Real-time **emotion detection** using DeepFace  
- **Motion detection** with PIR sensor  
- **RGB LED color mapping** per emotion  
- **Buzzer alert** for motion detection  
- **Motivational quote system** for user interaction  

**Emotion → LED Color Mapping**

| Emotion    | LED Color  |
|-----------|-----------|
| Happy     | Green      |
| Sad       | Blue       |
| Angry     | Red        |
| Neutral   | White      |
| Fear      | Yellow     |
| Surprise  | Purple     |
| Disgust   | Cyan       |

---

## 🖼 Project Demo

**Sample Outputs:**

<p align="center">
  <img src="sample_output/happy.png" width="220" />
  <img src="sample_output/sad.png" width="220" />
  <img src="sample_output/angry.png" width="220" />
</p>

---

## 🛠 Tech Stack

- **Python 3**
- **OpenCV** for camera & video feed
- **DeepFace** for emotion analysis
- **Raspberry Pi GPIO** for sensors and LEDs
- **Random & Time modules** for event logic

---

## 📂 Project Structure

