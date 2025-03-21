import cv2
import os

def extract_frames(video_path, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Open video file
    cap = cv2.VideoCapture(video_path)
    
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break  # Stop if video ends
        
        frame_filename = os.path.join(output_folder, f'frame_{frame_count:04d}.jpg')
        cv2.imwrite(frame_filename, frame)  # Save frame
        
        frame_count += 1
    
    cap.release()
    print(f'Extracted {frame_count} frames to {output_folder}')

# Example usage
video_path = '/home/ariane/Pictures/IMG_2045_2.MOV'  
output_folder = '/home/ariane/Pictures/frames'  # Change this to your desired output folder
extract_frames(video_path, output_folder)
