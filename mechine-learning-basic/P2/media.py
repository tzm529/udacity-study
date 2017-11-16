# -*- coding:utf-8 -*-  
import webbrowser

class Movie(object):
	"""
	存储电影相关信息
	"""
	def __init__(self, title, storyline, poster_image_url, trailer_url):
		"""
		 Input: title => 影片名称
		 		storyline => 故事简介
		 		poster_image_url => 图片地址
		 		trailer_url => 预告片地址
		"""
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image_url
		self.trailer_url = trailer_url


	def show_trailer(self):
		"""
		调用浏览器打开预告片链接
		"""
		webbrowser.open(self.trailer_url)

