# Webcam-Tester
A Python script for testing the FPS and resolution of external webcams

## How to run

Clone the repository:
```
git clone https://github.com/MataiMoorfield/Webcam-Tester.git
```
Enter the directory:
```
cd Webcam-Tester
```
Install the reqirements:
```
pip install -r requirements.txt
```
Double check the webcam location in the Python code. External webcams defult to 0 (```cv2.VideoCapture(0)```).

Run the Python script:
```
python main.py
```
> [!NOTE]
> Allow the IDE to use the camera
