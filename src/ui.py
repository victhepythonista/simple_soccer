# EXTRA UI SCREENS AND WIDGETS

from screen import Screen

from animation import PointAnimation

class GoalAnnouncement(Screen):
	"""

	screen FOR ANNOUNCING A GOAL 

	"""
	def __init__(self):
		Screen.__init__(self)

		self.goal_animation = PointAnimation("GOAL  !!!", (200,200))
		self.time_limit = 50
		self.timer = 0

	def display_widgets(self):
		self.window.fill((200,200,200))
		self.goal_animation.show(self.window)
		self.timer += 1
		if self.timer > self.time_limit:
			self.running = False



class Announcement(Screen):

	"""

	A SCREEN FOR GENERAL ANNOUNCEMENTS/POPUPS"""
	def __init__(self, message):
		Screen.__init__(self)

		self.goal_animation = PointAnimation(message, (200,200))
		self.time_limit = 50
		self.timer = 0

	def display_widgets(self):
		self.window.fill((200,200,200))
		self.goal_animation.show(self.window)
		self.timer += 1
		if self.timer > self.time_limit:
			self.running = False
