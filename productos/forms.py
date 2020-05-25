from django import forms
from phonenumber_field.formfields import PhoneNumberField


class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': ('Nombre Completo'), 'id': ('from-name'), 'class': ('form-control')}))
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'placeholder': ('Email'), 'id': ('from-email'), 'class': ("form-control")}))
    telefono = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': ('Telefono'), 'id': ('from-phone'), 'class': ('form-control')}),
                                label=("Telefono"), required=False)
    horario = forms.ChoiceField(
        choices=[('Mañana', 'Mañana'), ('Tarde', 'Tarde'), ('Noche', 'Noche')], required=False, widget=forms.Select(attrs={'class': ('form-control'), 'id': ('from-calltime')}))
    comentarios = forms.CharField(
        max_length=256, widget=forms.Textarea(attrs={'class': ('form-control'), 'id': ('from-comments'), 'rows': ('5'), 'placeholder': ('Enter Comments')}), required=False)

    def __str__(self):
        return self.email
