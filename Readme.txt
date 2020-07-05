Preparing the environment:
-Install Anaconda and open the conda command prompt
-prepare the environment by installing the below packages.
	conda create -n myenv python=3.6
	pip install tensorflow==1.13.1
	pip install openv-contrib-python
	pip install matplotlib
	pip install pillow
	pip install scipy
	pip install easydict
	conda activate myenv

- Place the video files you want to test using this model under the folder input_images_and_videos
- Go to the folder containing the .py files(object_detect_frcn.py, object_detect_ssd.py, video_demo.py) and execute the program using below command.
	python object_detect_frcn.py ( For Faster RCNN model)
	python object_detect_ssd.py ( For SSD model)
	python video_demo.py ( For YOLO)