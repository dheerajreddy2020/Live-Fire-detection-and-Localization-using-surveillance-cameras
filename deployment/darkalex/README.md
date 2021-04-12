# Yolo v4 Linux
./darknet detector demo coco.data fire.cfg fire.weights test.mp4 -dont_show -out_filename results.mp4

./darknet detect coco.data fire.cfg fire.weights fire.jpg -dont_show

python3 darknet_video.py --input=test.mp4 --out_filename="outputrk.avi" --weights=fire.weights --config_file fire.cfg --data=coco.data --dont_show
