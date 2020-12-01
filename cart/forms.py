from django import forms
from .models import OrderItem, ColorVariation, Product, SizeVariation


class AddToCartForm(forms.ModelForm):
    color = forms.ModelChoiceField(queryset=ColorVariation.objects.none())
    size = forms.ModelChoiceField(queryset=SizeVariation.objects.none())

    class Meta:
        model = OrderItem
        fields = ['quantity', 'color', 'size']

        def __init__(self, *args, **kwargs):
            product_id = kwargs.pop('product_id')
            product = Product.objects.get(id=product_id)
            super().__init__(*args, **kwargs)

            self.fields['color'].queryset = product.available_colors.all()
            self.fields['size'].queryset = product.available_size.all()