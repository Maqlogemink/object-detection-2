from roboflow import Roboflow
import supervision as sv
import cv2

rf = Roboflow(api_key="CQaP0vyM8H7nvsnDI8G2")
project = rf.workspace().project("people-detection-general")
model = project.version(7).model

result = model.predict("your_image.jpg", confidence=40, overlap=30).json()

labels = [item["class"] for item in result["predictions"]]

detections = sv.Detections.from_roboflow(result)

label_annotator = sv.LabelAnnotator()
bounding_box_annotator = sv.BoxAnnotator()

image = cv2.imread("your_image.jpg")

annotated_image = box_annotator.annotate(
    scene=image, detections=detections)
annotated_image = label_annotator.annotate(
    scene=annotated_image, detections=detections, labels=labels)

sv.plot_image(image=annotated_image, size=(16, 16))