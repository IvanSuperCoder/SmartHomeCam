from imutils.video import FileVideoStream
from imutils.video import FPS
import numpy as np
import imutils
import time

import argparse
import cv2

# init command-line arguments parser
ap = argparse.ArgumentParser()
# declare an argument for the stream URL
ap.add_argument('--url', required=True, metavar='', help='RTSP IP Camera URL')

# extract the stream URL from command-line arguments
stream_url = vars(ap.parse_args())['url']





# start the file video stream thread and allow the buffer to
# start to fill
print("[INFO] starting video file thread...")
fvs = FileVideoStream(stream_url).start()
time.sleep(1.0)

# start the FPS timer
fps = FPS().start()

# loop over frames from the video file stream
while fvs.more():
	# grab the frame from the threaded video file stream, resize
	# it, and convert it to grayscale (while still retaining 3
	# channels)
	frame = fvs.read()
	# frame = imutils.resize(frame, width=450)
	# frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# frame = np.dstack([frame, frame, frame])
	# display the size of the queue on the frame
	cv2.putText(frame, "Queue Size: {}".format(fvs.Q.qsize()),
		(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)	
	# show the frame and update the FPS counter
	cv2.imshow("Frame", frame)
	cv2.waitKey(1)
	fps.update()
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break
	
    # stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
# do a bit of cleanup
cv2.destroyAllWindows()
fvs.stop()