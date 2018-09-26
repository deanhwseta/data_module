from django.contrib import admin
from .models import Designation, Provider, Employer, Person, Learnership, Qualification, Unit_Standard, Alternate_Id_Type_Id, Internship_Placement, Non_NQF_Intervention, Non_NQF_Placements
from django import forms

##########################
### PERSON OVERRIDES   ###
##########################

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def clean(self):

        super().clean()

        person_alternate_id = self.cleaned_data.get('person_alternate_id')
        #alternate_id_type_id = self.cleaned_data.get('alternate_id_type_id')
        #alternate_id_type_id = self.cleaned_data['alternate_id_type_id']
        alternate_id_type_id = u'%s' % self.cleaned_data.get('alternate_id_type_id')

        #if person_alternate_id != "" and alternate_id_type_id == "533":
        #      raise forms.ValidationError("Person Alternate ID is not blank, therefore Alternate ID Type ID cannot be 533")
        #if person_alternate_id == "" and alternate_id_type_id != "533":
        #       raise forms.ValidationError("Person Alternate ID is blank, therefore Alternate ID Type ID must be 533")

        #if person_alternate_id != "":
        #    raise forms.ValidationError("Person Alternate ID is not blank")
        #if person_alternate_id == "":
        #    raise forms.ValidationError("Person Alternate ID is blank")
        #if alternate_id_type_id == "None":
        #    raise forms.ValidationError("is 533")
        #if alternate_id_type_id != "None":
        #    raise forms.ValidationError("is not 533")

        if person_alternate_id == "" and alternate_id_type_id != "None":
            raise forms.ValidationError("Blank but not 533")
        if person_alternate_id != "" and alternate_id_type_id == "None":
            raise forms.ValidationError("Not Blank but 533")




        #if 1==1:
        #    raise forms.ValidationError("Person Alternate ID is blank, therefore Alternate ID Type ID must be 533")

        return self.cleaned_data

class PersonAdmin(admin.ModelAdmin):
    form = PersonForm

admin.site.register(Person, PersonAdmin)

# Register your models here.

admin.site.register(Employer)
admin.site.register(Learnership)
admin.site.register(Qualification)
admin.site.register(Unit_Standard)
admin.site.register(Internship_Placement)
admin.site.register(Designation)
admin.site.register(Non_NQF_Intervention)
admin.site.register(Non_NQF_Placements)
admin.site.register(Provider)
