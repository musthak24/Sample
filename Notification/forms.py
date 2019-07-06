from django import forms
from models import *


class FilesForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = (
            'master_id',
            'file_name',
            'remark',
        )
