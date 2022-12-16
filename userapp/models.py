from django.db import models 
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image
import os


# Create your models here.
class UserModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    aadhar_no = models.CharField(max_length=12)
    profile = models.ImageField(upload_to='images/',null=True)
    gender = models.CharField(max_length=50)
    password = models.CharField(max_length=8,null=True)
    
    
    
    def _str_(self) :
        return self.name

    class Meta:
        db_table = 'user_details'
        
        
# create applynewpass model here.
 
class NewPass(models.Model):
    pass_id = models.AutoField(primary_key=True)
    pass_user = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='user_pass_details',null=True)
    alldetails = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='alldetails',null=True)
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField(null=True)
    aadhar = models.CharField(max_length=12,null=True)
    payment_mode = models.CharField(max_length=50,null=True)
    bus_travel_type = models.CharField(max_length=50,null=True)
    mobile = models.CharField(max_length=50,null=True)
    father = models.CharField(max_length=50,null=True)
    date_of_birth = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=50,null=True)
    pass_photo = models.ImageField(upload_to='images/',null=True)
    passduration = models.CharField(max_length=50,null=True)
    city = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=50, default='pending')
    qr_code = models.ImageField(blank=True,upload_to='images/',null=True)
    validity = models.CharField(max_length=50,null=True)
    

    def save(self, *args, **kwargs):
                    if self.qr_code:
                              try:
                                  path = "media/"+str(self.qr_code)
                                  file = path
                                  os.remove(file)
                                  print('success') 
                              except:
                                  pass
                    qr_image = qrcode.make(f" ID:{self.pass_id}\n Name:{self.name}\n Phone:{self.mobile}\n DOB:{self.date_of_birth} \n Gender:{self.gender} \n status:{self.status}\n Address:{self.city} \n Valid:{self.validity}")
                    qr_offset = Image.new('RGB',(850,850),'white')
                    qr_offset.paste(qr_image)
                    files_name = f'{self.name}_qr.png'
                    stream = BytesIO()
                    qr_offset.save(stream, 'PNG')
                    self.qr_code.save(files_name, File(stream), save=False)
                    qr_offset.close()
                    super().save(*args, **kwargs)
    
        
    def _str_(self) :
        return self.name
    
    class meta:
        db_table = 'user_applynewpass'



class UserFeedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    feedback2 = models.ForeignKey(NewPass,on_delete=models.CASCADE)
    overall = models.IntegerField(help_text = 'data' , null=True)
    travelling = models.IntegerField(help_text='travelling' ,null=True)
    suggestion = models.CharField(help_text='suggestion' , max_length=400, null=True)
    sentiment = models.CharField(help_text='sentiment', null=True, max_length=80)
    
    
    class Meta:
        db_table = "UserFeedback_details"


# class SentimentAnalysis(models.Model):
#     sentiment_id = models.AutoField(primary_key=True)
#     senti = models.ForeignKey(NewPass,on_delete=models.CASCADE,null=True)
#     overall = models.IntegerField(help_text = 'data' ,null=True)
#     travelling = models.IntegerField(help_text= 'travelling' ,null=True)
#     suggestion = models.CharField(help_text='suggetion', max_length=400, null=True)
#     sentiment = models.CharField(help_text='sentiment', null=True, max_length=80)
    
#     class Meta:
#         db_table = "UserSentimentAnalysis"
        
    
        

        