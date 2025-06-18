Speed-Detection---Computer-Vision
🚗 Real-Time Vehicle Detection and Speed Estimation using YOLOv8
This project uses computer vision and deep learning to detect and track vehicles in real-time from video footage. It calculates the speed of each detected vehicle and flags those exceeding a speed threshold.

📸 Features
Vehicle detection using YOLOv8 (yolov8s.pt)
Real-time speed calculation using two virtual lines
Detection of overspeeding vehicles
Logging overspeeding vehicle IDs to a file
Direction-based vehicle counting (up and down)
🛠 Technologies Used
Python 3.x
OpenCV
Pandas, NumPy
Ultralytics YOLOv8
Custom tracking module (tracker.py)
📂 File Structure
. ├── main.py # Main script for detection and speed calculation

├── tracker.py # Object tracking logic

├── coco.txt # COCO class names

├── over_speeding_cars_ID.txt # Output file for overspeeding vehicle IDs

├── stock-footage-traffic-on-the-indian-roads.WEBM # Input video

🚀 How to Run the Project
1. Clone the Repository
git clone https://github.com/Dudekularajesh/vehicle-speed-tracking-yolo.git

cd vehicle-speed-tracking-yolo

Install Dependencies
pip install opencv-python pandas numpy ultralytics 3. Place Required Files Ensure coco.txt (COCO class names) is present.

Download and place the YOLOv8 weights file yolov8s.pt in the working directory.

Provide a traffic video named stock-footage-traffic-on-the-indian-roads.WEBM.

Run the Application
python main.py 5. Output The app will open a window showing real-time detection.

It logs overspeeding vehicle IDs in over_speeding_cars_ID.txt.

📈 Parameters Speed threshold: 40 km/h (hardcoded)

Frame skip: processes every 3rd frame for performance

Distance between virtual lines: 10 meters (simulated)

📌 Notes Make sure your video shows traffic with vehicles moving across two horizontal lines.

You can adjust cy1 and cy2 in main.py to change the line positions.

🧑‍💻 Author Dudekula Rajesh Final Year Project – SVR Engineering College

📄 License This project is for educational and non-commercial use only.