from django.db import models

# Create your models here.
class Login(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length= 50)
    name = models.CharField(max_length = 50)
    phone = models.IntegerField()
    roles = models.CharField(max_length= 300)


    class Meta:
        db_table = "login"
        
class RunTime(models.Model):
    hours =  models.IntegerField()
    minutes = models.IntegerField()
    
    class Meta:
        db_table = "runtime"
        
        
class Movies(models.Model):
    
    movie_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length = 50)
    rating_classification = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    release_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    run_time =  models.ForeignKey(RunTime, on_delete=models.CASCADE)
    avg_rating = models.IntegerField()


    class Meta:
        db_table = "movies"
      
      
class People(models.Model):
    person_id = models.BigAutoField(primary_key= True)
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    born = models.CharField(max_length = 50)
    died = models.CharField(max_length = 10)
    description = models.CharField(max_length = 200)
    roles = models.ForeignKey(Movies, on_delete=models.CASCADE)

    class Meta:
        db_table = "people"
      

      
      