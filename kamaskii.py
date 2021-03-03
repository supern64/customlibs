# Kamaskii Alpha
import numpy as np
import json

class SceneDisplay:
	def __init__(self, screen, camera):
		self._screen = screen
		self.width = screen.width
		self.height = screen.height
		self.camera = camera
		self._screen.clear()
	def set_camera(self, camera):
		self._screen.clear_buffer(1, 0, 0)
		if type(camera) != Camera:
			raise InvalidType("camera must be of type Camera")
		self.camera = camera
	def render_frame(self):
		frame = self.camera.get_final_frame()
		self._screen.clear_buffer(1, 0, 0)
		for y in range(0, len(frame)):
			for x in range(0, len(frame[y])):
				if frame[y][x] != "" and frame[y][x] != " ":
					self._screen.print_at(frame[y][x], x, y)
		self._screen.refresh()

class Camera:
	def __init__(self, w, h, x, y, scene):
		self.width = w
		self.height = h
		self.x = x
		self.y = y
		self.scene = scene
		self.overlays = np.zeros((h, w), "<U1")
		self.overlays.fill(" ")
	def get_raw_frame(self):
		return self.scene.get_section(self.x, self.y, self.width, self.height)
	def get_final_frame(self):
		frame = self.scene.get_section(self.x, self.y, self.width, self.height)
		for y in range(len(self.overlays)):
			for x in range(len(self.overlays[y])):
				if self.overlays[y][x] != "" and self.overlays[y][x] != " ":
					frame[y][x] = self.overlays[y][x]
		return frame
	def print_overlay_char(self, c, x, y):
		self.overlays[y,x] = c
	def print_overlay(self, str, x, y):
		for i in range(len(str)):
			self.print_overlay_char(str[i], x+i, y)

class Scene:
	def __init__(self, w, h):
		self.width = w
		self.height = h
		self._buffer = np.zeros((h, w), "<U1")
		self._buffer.fill(" ")
	def get_section(self, x, y, w, h):
		if x < 0 or y < 0 or x+w > self.width or y+h > self.height:
			raise BeyondBufferRange("trying to read beyond what exists")
		return json.loads(json.dumps([x_a[x:x+w] for x_a in self._buffer[y:y+h]], cls=NumPyEncoder)) # deepclone :amogus:
	def print_char(self, c, x, y):
		self._buffer[y,x] = c
	def print_to(self, string, x, y):
		for i in range(len(string)):
			self.print_char(string[i], x+i, y)

class InvalidType(Exception):
	pass
class BeyondBufferRange(Exception):
	pass

class NumPyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)