
#https://codverter.com/src/sqltoclass

class Videos:
	def __init__(self,
video_id,creator,age_restriction,genre,title, description, runtime,advertisement,comments_enabled,stream,availability,upload_date,meta_change,data_change):
		self.video_id=video_id
		self.creator=creator
		self.age_restriction=age_restriction
		self.genre=genre
		self.title=title
		self.description=description
		self.runtime=runtime
		self.advertisement=advertisement
		self.comments_enabled=comments_enabled
		self.stream=stream
		self.availability=availability
		self.upload_date=upload_date
		self.meta_change=meta_change
		self.data_change=data_change

	def serialize(self):
		return {
			"video_id":self.video_id,
			"creator":self.creator,
			"age_restriction":self.age_restriction,
			"genre":self.genre,
			"title":self.title,
			"description":self.description,
			"runtime":self.runtime,
			"advertisement":self.advertisement,
			"comments_enabled":self.comments_enabled,
			"stream":self.stream,
			"availability":self.availability,
			"upload_date":self.upload_date,
			"meta_change":self.meta_change,
			"data_change":self.data_change
		}