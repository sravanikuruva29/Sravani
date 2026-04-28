import numpy as np

class Sort:
    def __init__(self):
        self.id = 0

    def update(self, detections):
        tracks = []

        for det in detections:
            x1,y1,x2,y2,conf = det
            self.id += 1
            tracks.append([x1,y1,x2,y2,self.id])

        return np.array(tracks)