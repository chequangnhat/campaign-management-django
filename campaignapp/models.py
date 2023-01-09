from django.db import models

# Create your models here.


class User(models.Model):
	id = models.AutoField(primary_key=True)
	email = models.EmailField(max_length=255)
	password = models.CharField(max_length=255)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	phone_number = models.CharField(max_length=11)
	deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
			return self.id + " - " + self.email


class Campaign(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	status = models.BooleanField(default=True)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	budget = models.IntegerField()
	bid_amount = models.IntegerField()
	title = models.TextField()
	description = models.TextField()
	banner = models.TextField()
	final_url = models.TextField()
	used_amount = models.DecimalField(max_digits=5, decimal_places=2)
	usage_rate = models.DecimalField(max_digits=5, decimal_places=2)
	deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.id + " - " + self.user_id + " - " + self.name


class RefreshToken(models.Model):
	id = models.AutoField(primary_key=True)
	expire_day = models.DateField()
	token = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.id + " - " + self.user_id + " - " + self.expire_day


















# ### create user object to add to database:
# user1 = User(email = "nhat@gmail.com", password = "nhatnhat", first_name = "Quang", last_name = "Nhat", phone_number = "0934676767")

# ### create campaign object to add to database:
# camp = Campaign(name = "campaign 1", start_time = "2023-01-05", end_time = "2023-01-07", budget = 10000, bid_amount = 10, title = "campaign title", description = "desc", banner="banner", final_url="url", used_amount = 0, usage_rate = 0, user_id = 1)