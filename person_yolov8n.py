from ultralytics import YOLO
from PIL import Image

im1=Image.open("insan.jpg")

#model yükle
model=YOLO("yolov8n.pt")

# resim ile etiket
#sonuc=model.predict(source=im1,save=True)

# web cam ile etiket
# sonuc=model.predict(source="0")

#vidyo ile etiket yapma
sonuc=model.predict(source="yürüme.mp4.mp4",save=True)