import streamlit as st
import time
import numpy as np
import os
import tempfile
import random

# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)

st.write("## Hello Please Upload")
file = st.file_uploader('File uploader')

if st.button("Detect Now") and file:
	with st.spinner('Wait for it...'):
		#os.system("python3 darknet_video.py --input=test.mp4 --out_filename=outputrk.mp4 --weights=fire.weights --config_file fire.cfg --data=coco.data --dont_show")
		tfile = tempfile.NamedTemporaryFile(dir="tempvideos",delete=False)
		tfile.write(file.read())
		#st.write(tfile.name)
		outputdarknetFile = "tempvideo"+str(random.randint(1, 100))+".avi"
		outputFile = "tempvideo"+str(random.randint(1, 100))+".mp4"
		st.write("Upload Completed ! Hang Tight")
		os.system(f"python3 darknet_video.py --input={tfile.name} --ext_output --out_filename={outputdarknetFile} --weights=fire.weights --config_file fire.cfg --data=coco.data --dont_show")
		#print(dir(file))
		st.write("Video Processed... Converting Now to Web Format")
		os.system(f"ffmpeg -y -i {outputdarknetFile} -vcodec libx264 {outputFile}")
		st.video(outputFile)
		st.balloons()
		print(outputFile)
# Streamlit widgets automat
