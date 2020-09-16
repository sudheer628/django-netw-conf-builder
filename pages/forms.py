from django import forms

class ContactForm(forms.Form):
    asn = forms.CharField(max_length=30,help_text='Local ASN')
    peer = forms.GenericIPAddressField()
    peerasn = forms.CharField(max_length=30,help_text='Peer ASN')
    netw = forms.GenericIPAddressField()
#    source = forms.CharField(       # A hidden input for internal use
#        max_length=50,              # tell from which page the user sent the message
#        widget=forms.HiddenInput()
#    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        asn = cleaned_data.get('asn')
        peer = cleaned_data.get('peer')
        peerasn = cleaned_data.get('peerasn')
        netw = cleaned_data.get('netw')
        if not asn and not peer and not peerasn and not netw:
            raise forms.ValidationError('You have to write something!')
