from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(label='Nome')
	email = forms.EmailField(label='E-mail')
	massage = forms.CharField(label='Mensagem',widget=forms.Textarea())

	def clean_name(self):
		name = self.cleaned_data['name']
		if name == 'fulano':
			raise forms.ValidationError('Este não pode ser seu nome')
		return name