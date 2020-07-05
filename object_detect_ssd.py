import tensorflow as tf

from utils import backbone
from api import object_counting_api

input_video = "./input_images_and_videos/object_test.mp4"

detection_graph, category_index = backbone.set_model('ssd_mobilenet_v1_coco_2018_01_28', 'mscoco_label_map.pbtxt')

is_color_recognition_enabled = 0 
roi = 185 
deviation = 2 

object_counting_api.cumulative_object_counting_y_axis(input_video, detection_graph, category_index, is_color_recognition_enabled, roi, deviation) 

#object_counting_api.object_counting_webcam(detection_graph, category_index, is_color_recognition_enabled)

