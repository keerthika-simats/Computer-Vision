import cv2
import time

# Read the captured video
video = cv2.VideoCapture("video.mp4")

# Check whether the video is opened
if not video.isOpened():
    print("Error: Cannot open video!")
else:
    # Read video frames per second
    fps = video.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 30

    print("Press 'q' to exit.")

    while True:
        ret, frame = video.read()

        # Stop when the video ends
        if not ret:
            break

        # Display normal speed
        cv2.imshow("Normal Speed", frame)
        if cv2.waitKey(max(1, int(1000 / fps))) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

    # Reopen video for slow motion
    video = cv2.VideoCapture("video.mp4")

    while True:
        ret, frame = video.read()

        if not ret:
            break

        cv2.imshow("Slow Motion", frame)

        # Slow motion: wait longer between frames
        if cv2.waitKey(max(1, int(2000 / fps))) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

    # Reopen video for fast motion
    video = cv2.VideoCapture("video.mp4")

    while True:
        ret, frame = video.read()

        if not ret:
            break

        # Skip frames for fast motion
        video.set(cv2.CAP_PROP_POS_FRAMES,
                  video.get(cv2.CAP_PROP_POS_FRAMES) + 1)

        cv2.imshow("Fast Motion", frame)

        if cv2.waitKey(max(1, int(500 / fps))) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

    print("Video processing completed successfully!")