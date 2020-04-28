from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title} -- {self.date_posted}'


class CPU(models.Model):
    Brand = models.CharField(max_length = 50)
    Name = models.CharField(max_length = 50)
    Generation = models.CharField(max_length = 50, default = "field not yet filled")
    Socket = models.CharField(max_length = 10)
    Nr_of_Cores = models.IntegerField()
    Nr_of_Threads = models.IntegerField()
    Frequency = models.FloatField()
    Boost_Frequency = models.FloatField()
    TDP = models.IntegerField()
    Overclockable = models.BooleanField()
    Integrated_GPU = models.CharField(max_length = 50)
    Release_Date = models.DateField()
    Price = models.FloatField()
    Image = models.ImageField(default='default.jpg', upload_to='Part_Pics/CPUs')
    Description = models.TextField(default="not yet available")
    Recommendations = models.TextField(default="not yet available")

    def __str__(self):
        return f'{self.Brand} {self.Name}'

class GPU(models.Model):
    Brand = models.CharField(max_length = 50)
    Name = models.CharField(max_length = 50)
    Nr_of_Cores = models.IntegerField()
    Frequency = models.FloatField()
    VRAM = models.IntegerField()
    Ports = models.CharField(max_length = 50)
    Power = models.IntegerField()
    Recommended_System_Power = models.IntegerField()
    Length = models.IntegerField(default = 0)
    Release_Date = models.DateField()
    Price = models.FloatField()
    Image = models.ImageField(default='default.jpg', upload_to='Part_Pics/GPUs')
    Description = models.TextField(default="not yet available")
    Recommendations = models.TextField(default="not yet available")

    def __str__(self):
        return f'{self.Brand} {self.Name}'

class Motherboard(models.Model):
    Brand = models.CharField(max_length = 50)
    Name = models.CharField(max_length = 50)
    Form_Factor = models.CharField(max_length = 50)
    CPU_Brand = models.CharField(max_length = 50)
    Chipset = models.CharField(max_length = 10)
    CPU_socket = models.CharField(max_length = 10)
    Supported_CPU_generations = models.CharField(max_length = 300, default = "field not yet filled")
    Supported_ram_types = models.CharField(max_length=100, default = "field not yet filled")
    Nr_of_PCIe_slots = models.IntegerField()
    Nr_of_Ram_slots = models.IntegerField()
    Nr_of_Sata_ports = models.IntegerField()
    Nr_of_mdot2_slots = models.IntegerField()
    Price = models.FloatField()
    Image = models.ImageField(default='default.jpg', upload_to='Part_Pics/Motherboards')
    Description = models.TextField(default="not yet available")
    Recommendations = models.TextField(default="not yet available")

    def __str__(self):
        return f'{self.Brand} {self.Name}'

class Ram_set(models.Model):
    Brand = models.CharField(max_length = 50)
    Name = models.CharField(max_length = 50)
    Memory_Type = models.CharField(max_length = 50)
    Memory_amount = models.IntegerField()
    Nr_of_Sticks = models.IntegerField()
    Memory_speed = models.IntegerField()
    Price = models.FloatField()
    Image = models.ImageField(default='default.jpg', upload_to='Part_Pics/Ram_sets')
    Description = models.TextField(default="not yet available")
    Recommendations = models.TextField(default="not yet available")

    def __str__(self):
        return f'{self.Brand} {self.Name}'

class PSU(models.Model):
    Brand = models.CharField(max_length = 50)
    Name = models.CharField(max_length = 50)
    Efficiency_Rating = models.CharField(max_length = 50)
    Connectors = models.CharField(max_length = 500)
    Total_Wattage = models.IntegerField()
    Dimmensions = models.CharField(max_length = 100)
    Fan_size = models.IntegerField()
    Form_Factor = models.CharField(max_length = 10)
    Price = models.FloatField()
    Image = models.ImageField(default='default.jpg', upload_to='Part_Pics/PSUs')
    Description = models.TextField(default="not yet available")
    Recommendations = models.TextField(default="not yet available")

    def __str__(self):
        return f'{self.Brand} {self.Name}'

class Storage(models.Model):
    Brand = models.CharField(max_length = 50)
    Name = models.CharField(max_length = 50)
    Type = models.CharField(max_length = 10)
    Connection = models.CharField(max_length = 10)
    Capacity = models.IntegerField()
    Sequential_Read = models.FloatField()
    Sequential_Write = models.FloatField()
    Form_Factor = models.CharField(max_length = 10)
    Price = models.FloatField()
    Image = models.ImageField(default='default.jpg', upload_to='Part_Pics/Storage')
    Description = models.TextField(default="not yet available")
    Recommendations = models.TextField(default="not yet available")

    def __str__(self):
        return f'{self.Brand} {self.Name}'

class Case(models.Model):
    Brand = models.CharField(max_length = 50)
    Name = models.CharField(max_length = 50)
    Color = models.CharField(max_length = 50)
    Supported_Motherboard_Form_Factors = models.CharField(max_length = 100)
    Fans = models.CharField(max_length = 100)
    Dimmensions = models.CharField(max_length = 50)
    Max_GPU_lenght = models.IntegerField()
    Max_CPU_Cooler_height = models.IntegerField()
    Price = models.FloatField()
    Image = models.ImageField(default='default.jpg', upload_to='Part_Pics/Cases')
    Description = models.TextField(default="not yet available")
    Recommendations = models.TextField(default="not yet available")

    def __str__(self):
        return f'{self.Brand} {self.Name}'

class CPU_Cooler(models.Model):
    Brand = models.CharField(max_length = 50)
    Name = models.CharField(max_length = 50)
    Type = models.CharField(max_length = 50)
    Compatible_CPU_sockets = models.CharField(max_length = 500)
    Noise_Level = models.CharField(max_length = 50)
    Material = models.CharField(max_length = 500)
    Dimmensions = models.CharField(max_length = 50)
    Price = models.FloatField()
    Image = models.ImageField(default='default.jpg', upload_to='Part_Pics/CPU_Coolers')
    Description = models.TextField(default="not yet available")
    Recommendations = models.TextField(default="not yet available")

    def __str__(self):
        return f'{self.Brand} {self.Name}'

class Configuration(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    CPU = models.ForeignKey(CPU, on_delete=models.SET_NULL, null=True)
    GPU = models.ForeignKey(GPU, on_delete=models.SET_NULL, null=True)
    Motherboard = models.ForeignKey(Motherboard, on_delete=models.SET_NULL, null=True)
    Ram_set = models.ForeignKey(Ram_set, on_delete=models.SET_NULL, null=True)
    PSU = models.ForeignKey(PSU, on_delete=models.SET_NULL, null=True)
    Storage = models.ForeignKey(Storage, on_delete=models.SET_NULL, null=True)
    Case = models.ForeignKey(Case, on_delete=models.SET_NULL, null=True)
    CPU_Cooler = models.ForeignKey(CPU_Cooler, on_delete=models.SET_NULL, null=True)
    Date_Saved = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Saved build of user {self.UserID} - {self.Date_Saved}'

class Saved_build(models.Model):
    Belongs_to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    Configuration = models.ForeignKey(Configuration, on_delete=models.CASCADE)

class Orders(models.Model):
    Recipient_First_Name = models.CharField(max_length = 50)
    Recipient_Last_Name = models.CharField(max_length = 50)
    Billing_address = models.CharField(max_length = 50)
    Delivery_address = models.CharField(max_length = 50)
    Order_Creation_Date = models.DateTimeField(default=timezone.now)
    Payment_Method = models.CharField(max_length = 50)
    Configuration = models.ForeignKey(Configuration, on_delete=models.SET_NULL, null=True)

