class Person:
    def __init__(self, cx, cy, start_cx, pid):
        self.pid = pid
        self.cx = cx
        self.cy = cy
        self.start_cx = start_cx
        self.frames_updated = 0

    def get_updated_frames(self):
        return self.frames_updated
    def update_frames(self, x):
        self.frames_updated=x
    
    def update_cord(self, cx, cy):
        self.cx = cx
        self.cy = cy

    def getId(self):
        return self.pid
    def getCX(self):
        return self.cx
    def getCY(self):
        return self.cy
    def setCxCy(self, cx, cy):
        self.cx = cx
        self.cy = cy
    def get_start_cx(self):
        return self.start_cx
        
