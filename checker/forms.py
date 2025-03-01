from django import forms


class PingForm(forms.Form):
    url_or_ip = forms.CharField(
        label="Enter an IP address or a Domain name ",
        max_length=225,
    )
