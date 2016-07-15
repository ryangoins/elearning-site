from django import forms


class SuggestionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    honeypot = forms.CharField(required=False,
                              widget=forms.HiddenInput,
                              label="Leave empty")
    #forms use a Charfield with widgets
    suggestion = forms.CharField(widget=forms.Textarea)


    def clean_honeypot(self):
        honeypot = self.cleaned_data['honeypot']
        if len(honeypot):
            raise forms.ValidationError(
                "Honeypot should be left empty. Bad bot!")
        return honeypot
