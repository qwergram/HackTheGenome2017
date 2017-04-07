from django import forms

"""
input data looks like:
    <QueryDict: {
        'name': ['Norton'], 
        'message': ['Hello there'], 
        'subject': ['Website is cool'], 
        'csrfmiddlewaretoken': ['arlDIYO3KRlBRd1jHcJghYMSwpqBN4I6SD4wDi54G0OjrL5ZOY5N1az053tLR5gb'], 
        'file_button': ['on'], 
        'q2': ['a4'], 
        'q4': ['a11'], 
        'file': ['80599'], 
        'email': ['npengra317@gmail.com'], 
        'q3': ['a9'], 
        'q5': ['a14'], 
        'q1': ['a2']
    }>
"""

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    message = forms.CharField()
    subject = forms.CharField()


class GenomeForm(forms.Form):
    file_button = forms.CharField()
    file = forms.CharField()


class BasicQuestionaire(object):
    
    def __init__(self, requestPost):
        self.post = requestPost
        self.questions = {}
        self._is_valid = False
        self._retrieveQuestions()
        
    def _retrieveQuestions(self):
        for key, value in self.post.items():
            if key.startswith('q') and key not in questions:
                questions[key] = value
            else:
                self.questions = {}
                break
        else:
            self._is_valid = True
    
    def is_valid(self):
        return self._is_valid


class GeneticCodeIncludedForm(forms.Form):
    forms.