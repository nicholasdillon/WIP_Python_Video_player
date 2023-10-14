import cv2
import numpy as np

def play_video(file_path):
    """Play the video at the given file path."""

    video = cv2.VideoCapture(file_path)
    if not video.isOpened():
        print("Error opening video file")
        return

    fps = video.get(cv2.CAP_PROP_FPS)

    cv2.namedWindow("Video Player", cv2.WINDOW_NORMAL)
    cv2.moveWindow("Video Player", 100, 100)
    window_width, window_height = 400, 300
    cv2.resizeWindow("Video Player", window_width, window_height)

    def handle_key_input(key):
        """Handle key inputs and return whether to continue playing or not."""
        if key == ord('q'):
            return False
        elif key == ord('m'):
            nonlocal volume
            volume = 1.0 if volume == 0 else 0
        return True

    volume = 1.0
    delay = int(1000 / fps)

    while True:
        ret, frame = video.read()
        if not ret:
            break

        # Here, we don't actually modify the video volume, we just simulate the effect by adjusting pixel brightness
        frame = (frame * volume).astype(np.uint8)
        frame = cv2.resize(frame, (window_width, window_height))

        cv2.imshow("Video Player", frame)

        key = cv2.waitKey(delay) & 0xFF  # wait for a key event
        if not handle_key_input(key):
            break

    video.release()
    cv2.destroyAllWindows()

# Usage example
video_file = r"your_path_here"  # Enter the path to the video file
play_video(video_file)
