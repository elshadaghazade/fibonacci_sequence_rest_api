from django.db import models

class Logs(models.Model):
    start_idx = models.IntegerField()
    end_idx = models.IntegerField()
    request_time = models.TimeField(auto_now=True, auto_now_add=False)

    class Meta:
        # db_table = ''
        # managed = True
        verbose_name = 'Logs'
        verbose_name_plural = 'Logs'