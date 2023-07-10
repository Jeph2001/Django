from django.db import models



# Create your models here.
class SignUp(models.Model):
    username = models.CharField(max_length=100, default='your user name')
    email_address = models.EmailField(max_length=100, default='your email')
    password = models.CharField(max_length=50, default='use strong password')
    confirm_password = models.CharField(max_length=50, default='use same password')


class KeepReset(models.Model):
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)


# class Login(models.Model):
#     username = models.ForeignKey(SignUp, on_delete=models.CASCADE, related_name='logging')
#     password = models.ForeignKey(SignUp, on_delete=models.CASCADE, related_name='logins')

# class Login(models.Model):
#     username = models.CharField(max_length=100, default='your username')
#     for username in signup:
#         if signup.username != username:
#             ValueError('unkown User')
#         else:
#             pass
#     for password in signup:
#         password = models.CharField(max_length=50, default='your password')
#         if signup.username != password:
#             ValueError('incorrect password')




    
    
        







