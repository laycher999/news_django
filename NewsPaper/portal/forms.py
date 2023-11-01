from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class ProductForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'name',
            'text',
            'category',
        ]

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("text")
        if description is not None and len(description) < 20:
            raise ValidationError({
                "text": "Описание не может быть менее 20 символов."
            })

        name = cleaned_data.get("name")
        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data

        return cleaned_data