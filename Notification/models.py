# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


ADMIN_CHOICE = (
    ('Done', 'Done'),
    ('Re upload', 'Re upload'),
    ('Cancelled', 'Cancelled'),

)


class Files(models.Model):
    master_id = models.IntegerField()
    file_name = models.FileField(upload_to='media')
    date = models.DateTimeField(auto_now_add=True)
    remark = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=20, choices=ADMIN_CHOICE, verbose_name='Status', default='Processing')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.file_name)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        models.Model.save(self, force_insert, force_update, using, update_fields)


