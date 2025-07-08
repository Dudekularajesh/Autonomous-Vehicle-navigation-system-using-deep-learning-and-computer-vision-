Autonomous-Vehicle-navigation-system-using-deep-learning-and-computer-vision-

🚗 Real-Time Vehicle Detection and Speed Estimation using YOLOv8

This project uses computer vision and deep learning to detect and track vehicles in real-time from video footage. It calculates the speed of each detected vehicle and flags those exceeding a speed threshold.


**📸 Features**

1)Vehicle detection using YOLOv8 (yolov8s.pt)

2)Real-time speed calculation 

3)Detection of overspeeding vehicles

4)Logging overspeeding vehicle IDs to a file


**🛠 Technologies Used**

1)Python 3.x

2)OpenCV

4)Pandas

5)NumPy

6)Ultralytics 

7)YOLOv8

8)Custom tracking module (tracker.py)


**📂 File Structure**

├── main.py # Main script for detection and speed calculation

├── tracker.py # Object tracking logic

├── coco.txt # COCO class names

├── over_speeding_cars_ID.txt # Output file for overspeeding vehicle IDs

├── stock-footage-traffic-on-the-indian-roads.WEBM # Input video


**🚀 How to Run the Project**

1. Clone the Repository
   
     git clone  https://github.com/Dudekularajesh/Autonomous-Vehicle-navigation-system-using-deep-learning-and-computer-vision-

     cd Autonomous-Vehicle-navigation-system-using-deep-learning-and-computer-vision-

2. Install Dependencies

     pip install opencv-python, pandas, numpy, ultralytics 

3. Place Required Files Ensure coco.txt (COCO class names) is present.

4. Download and place the YOLOv8 weights file yolov8s.pt in the working directory.

5. Provide a traffic video named rajesh.mp4

6. Run the Application

     python main.py 

7.  Output The app will open a window showing real-time detection.

     It logs overspeeding vehicle IDs in over_speeding_cars_ID.txt.

     📈 Parameters Speed threshold: 40 km/h (hardcoded)

     Frame skip: processes every 3rd frame for performance

   

🧑‍💻 Author
                    
  Dudekula Rajesh Final Year Project – SVR Engineering College


  **📄 License This project is for educational and non-commercial use only.**
