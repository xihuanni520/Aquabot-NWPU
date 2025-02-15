# defect_detection.py
import cv2
import torch
from yolov7.models.experimental import attempt_load

class UnderwaterDefectDetector:
    def __init__(self, weights_path="weights/best.pt"):
        self.model = attempt_load(weights_path, map_location="cuda")
        self.names = self.model.names

    def detect(self, frame):
        # 预处理
        img = cv2.resize(frame, (640, 640))
        img = torch.from_numpy(img).permute(2, 0, 1).float().div(255.0).unsqueeze(0)
        # 推理
        with torch.no_grad():
            pred = self.model(img)[0]
        # 后处理
        defects = []
        for det in pred:
            if det[4] > 0.5:  # 置信度阈值
                x1, y1, x2, y2 = map(int, det[:4])
                label = self.names[int(det[5])]
                defects.append((label, (x1, y1, x2, y2)))
        return defects