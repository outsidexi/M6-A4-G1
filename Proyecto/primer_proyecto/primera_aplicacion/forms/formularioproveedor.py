from django import forms

class FormularioSupplierForm(forms.Form):
    direccion = forms.CharField(max_length=50, label="Direccion", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su direccion'}))
    area = forms.CharField(label="Area", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su area'}))
    producto = forms.CharField(max_length=50, label="Producto", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su producto'}))
    
