from django.contrib import admin
from . import models as m

admin.site.register(m.Post)
admin.site.register(m.CPU)
admin.site.register(m.GPU)
admin.site.register(m.Motherboard)
admin.site.register(m.Ram_set)
admin.site.register(m.PSU)
admin.site.register(m.Storage)
admin.site.register(m.Case)
admin.site.register(m.CPU_Cooler)
admin.site.register(m.Sound_Card)
admin.site.register(m.Optical_Drive)
admin.site.register(m.Monitor)
admin.site.register(m.Operating_System)
admin.site.register(m.Configuration)
admin.site.register(m.Saved_build)
