from django.db import models
from django.contrib.auth.models import AbstractUser

gender_choice = [
    ("M","Male"),
    ("F","Female"),
    ("O","Other"),
    ("N","Don't want to mention"),
]

state_choice = [
    ("AN", "Andaman and Nicobar Islands"),
    ("AP", "Andhra Pradesh"),
    ("AR", "Arunachal Pradesh"),
    ("AS", "Assam"),
    ("BR", "Bihar"),
    ("CH", "Chandigarh"),
    ("CG", "Chhattisgarh"),
    ("DN", "Dadra and Nagar Haveli and Daman and Diu"),
    ("DL", "Delhi"),
    ("GA", "Goa"),
    ("GJ", "Gujarat"),
    ("HR", "Haryana"),
    ("HP", "Himachal Pradesh"),
    ("JK", "Jammu and Kashmir"),
    ("JH", "Jharkhand"),
    ("KA", "Karnataka"),
    ("KL", "Kerala"),
    ("LA", "Ladakh"),
    ("LD", "Lakshadweep"),
    ("MP", "Madhya Pradesh"),
    ("MH", "Maharashtra"),
    ("MN", "Manipur"),
    ("ML", "Meghalaya"),
    ("MZ", "Mizoram"),
    ("NL", "Nagaland"),
    ("OD", "Odisha"),
    ("PY", "Puducherry"),
    ("PB", "Punjab"),
    ("RJ", "Rajasthan"),
    ("SK", "Sikkim"),
    ("TN", "Tamil Nadu"),
    ("TG", "Telangana"),
    ("TR", "Tripura"),
    ("UP", "Uttar Pradesh"),
    ("UK", "Uttarakhand"),
    ("WB", "West Bengal")
]


class User(AbstractUser):
    location=models.CharField(max_length=50,choices=state_choice,null=False,blank=False)
    gender=models.CharField(max_length=10,choices=gender_choice,default="Male")
    dob=models.DateField(null=True)
    created_on=models.DateField(auto_now_add=True)  
    active=models.BooleanField(default=True)  
    def Namee(self):
        return f"{self.first_name} {self.last_name} "

    def _str_(self):
        return f"{self.role} : {self.username}  - {self.department}"