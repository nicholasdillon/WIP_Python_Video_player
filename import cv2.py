import cv2
import numpy as np

def play_video(file_path):
    # Open the video file
    video = cv2.VideoCapture(file_path)

    # Check if the video file was opened successfully
    if not video.isOpened():
        print("Error opening video file")
        return

    # Get the video's frame rate
    fps = video.get(cv2.CAP_PROP_FPS)

    # Create a window to display the video
    cv2.namedWindow("Video Player", cv2.WINDOW_NORMAL)

    # Set the window position
    cv2.moveWindow("Video Player", 100, 100)

    # Set the window size
    window_width, window_height = 400, 300
    cv2.resizeWindow("Video Player", window_width, window_height)

    # Initialize volume (start with maximum volume)
    volume = 1.0

    while True:
        # Read the current frame from the video
        ret, frame = video.read()

        if not ret:
            # End of the video
            break

        # Convert frame color space to BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Convert frame to float32 for volume scaling
        frame = frame.astype(np.float32)

        # Set the volume (scale the frame by the volume)
        frame = cv2.multiply(frame, volume)

        # Convert frame back to uint8 for display
        frame = cv2.convertScaleAbs(frame)

        # Resize frame to fit the window size
        frame = cv2.resize(frame, (window_width, window_height))

        # Display the frame in the window
        cv2.imshow("Video Player", frame)

        # Wait for the specified amount of time (in milliseconds) based on the frame rate
        delay = int(1000 / fps)
        if cv2.waitKey(delay) == ord('q'):
            # Press 'q' to quit the video player
            break
        elif cv2.waitKey(1) == ord('m'):
            # Press 'm' to mute/unmute the video
            if volume == 0:
                # Unmute the video (restore the volume)
                volume = 1.0
            else:
                # Mute the video (set volume to 0)
                volume = 0

    # Release the video object and close the window
    video.release()
    cv2.destroyAllWindows()

# Usage example
video_file = r ## Enter the path to the video file here ##
play_video(video_file)
