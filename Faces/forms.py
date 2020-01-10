from django import forms


class Upload(forms.Form):
    
    startdate = forms.DateField(widget=forms.TextInput(attrs={'id':'stdate'}),input_formats=('%Y-%m-%d', ))
    enddate  = forms.DateField(widget=forms.TextInput(attrs={'id':'endate'}),input_formats=('%Y-%m-%d', ))
    
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'id':'img'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'id':'name'}),max_length=100)
    
    
    '''
    def clean(self):
        
        if(self.startdate >= self.enddate):
            
            raise forms.ValidationError("Endate should be greater than start date")
            
    '''
    
            
            