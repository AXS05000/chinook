from django import forms
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from .models import (
    GlexGestaoDeParceria,
    GlexGente,
    GlexAdministrativo,
    GlexTecnologia,
    GlexMarketing,
    GlexAcademico,
    GlexGestaoEscolar,
    GlexOperacaoAcademica,
    GlexImplantacao,
    GlexComercial,
    GlexResultado,
    Dominio1,
    Dominio2,
    Dominio3,
    Dominio4,
)



class Dominio1Form(forms.ModelForm):
    class Meta:
        model = Dominio1
        exclude = ["escola"]  # O campo escola será preenchido automaticamente
        widgets = {
            "program_implementation": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "staffing_instructional_program": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "resource_allocation": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "implementation_supervision_instructional_program": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "professional_learning_opportunities": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "commitment_to_bilingual_education": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "strategic_planning": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        escola_id = kwargs.pop("escola_id", None)
        super().__init__(*args, **kwargs)
        if escola_id:
            self.fields["escola"].initial = escola_id
        
        # Remove a opção "-------" de todos os campos de RadioSelect
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]

        # Aplica classe 'form-control' aos campos TextField e remove obrigatoriedade
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({"class": "textarea-control", "rows": 4, 'placeholder': 'Leave a comment...'})
            field.required = False

        self.fields["program_implementation"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]

        self.fields["staffing_instructional_program"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]

        self.fields["resource_allocation"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]

        self.fields["implementation_supervision_instructional_program"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]

        self.fields["professional_learning_opportunities"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]

        self.fields["commitment_to_bilingual_education"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]

        self.fields["strategic_planning"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]


class Dominio2Form(forms.ModelForm):
    class Meta:
        model = Dominio2
        exclude = ["escola"]
        widgets = {
            "culture": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "safe_and_caring_school": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "equity_diversity_inclusion": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "stakeholder_communication": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "stakeholder_engagement": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "health_and_safety": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "collection_interpretation_data": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        escola_id = kwargs.pop("escola_id", None)
        super().__init__(*args, **kwargs)
        if escola_id:
            self.fields["escola"].initial = escola_id
        
        # Remove a opção "-------" de todos os campos de RadioSelect
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]

        # Aplica classe 'form-control' aos campos TextField e remove obrigatoriedade
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({"class": "textarea-control", "rows": 4, 'placeholder': 'Leave a comment...'})
            field.required = False

        self.fields["culture"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]

        self.fields["safe_and_caring_school"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]

        self.fields["equity_diversity_inclusion"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]

        self.fields["stakeholder_communication"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]

        self.fields["stakeholder_engagement"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]

        self.fields["health_and_safety"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]

        self.fields["collection_interpretation_data"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]


class Dominio3Form(forms.ModelForm):
    class Meta:
        model = Dominio3
        exclude = ["escola"]
        widgets = {
            "instructional_processes_practices": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "learning_plans": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "student_centered_learning": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "inclusionary_practices": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "teacher_collaboration": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "classroom_management": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "supervision_evaluation": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        escola_id = kwargs.pop("escola_id", None)
        super().__init__(*args, **kwargs)
        if escola_id:
            self.fields["escola"].initial = escola_id
        
        # Remove a opção "-------" de todos os campos de RadioSelect
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]

        # Aplica classe 'form-control' aos campos TextField e remove obrigatoriedade
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({"class": "textarea-control", "rows": 4, 'placeholder': 'Leave a comment...'})
            field.required = False

        self.fields["instructional_processes_practices"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]

        self.fields["learning_plans"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]

        self.fields["student_centered_learning"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]

        self.fields["inclusionary_practices"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]

        self.fields["teacher_collaboration"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]

        self.fields["classroom_management"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]

        self.fields["supervision_evaluation"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]


class Dominio4Form(forms.ModelForm):
    class Meta:
        model = Dominio4
        exclude = ["escola"]
        widgets = {
            "learning_goals_success_criteria": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "assessment_strategies_tools": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "fair_assessment_practices": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "assessment_triangulation_data": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "reporting_student_achievement": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        escola_id = kwargs.pop("escola_id", None)
        super().__init__(*args, **kwargs)
        if escola_id:
            self.fields["escola"].initial = escola_id
        
        # Remove a opção "-------" de todos os campos de RadioSelect
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]

        # Aplica classe 'form-control' aos campos TextField e remove obrigatoriedade
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({"class": "textarea-control", "rows": 4, 'placeholder': 'Leave a comment...'})
            field.required = False

        self.fields["learning_goals_success_criteria"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]

        self.fields["assessment_strategies_tools"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]

        self.fields["fair_assessment_practices"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]

        self.fields["assessment_triangulation_data"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]

        self.fields["reporting_student_achievement"].choices = [
            (1, mark_safe('<span>Below Expectations <i class="material-icons" style="font-size: 16px" title="Evidence of implementation integrity is not yet established:&#10;&#10; - Few teachers are using appropriate methodology, curriculum and programs.&#10; - Few classrooms are sufficiently resourced with math and science manipulatives as well as grade appropriate books and textbooks from the most current book lists.&#10; - The school has designated spaces for instruction in a few classrooms.&#10;&#10;Instructional time for both English and Local programming is not monitored and documented yet. The school is aware that this is an area for critical growth.">info</i></span>')),
            (2, mark_safe('<span>Approaching Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets some of the following expectations:&#10;&#10; - Teachers are implementing appropriate methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented.">info</i></span>')),
            (3, mark_safe('<span>Meeting Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that meets all of the following expectations:&#10;&#10; - Teachers are implementing appropriate and updated methodology, curriculum and programs.&#10; - Classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists.&#10; - Classrooms have designated spaces for instruction and learning.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
            (4, mark_safe('<span>Exceeding Expectations <i class="material-icons" style="font-size: 16px" title="There is evidence of program implementation that exceeds all expectations:&#10;&#10; - All teachers are implementing appropriate methodology, curriculum and programs with fidelity and cultivate energy, creativity, curiosity, imagination, and innovation.&#10; - All teachers provide curriculum-based rich tasks to advance learning, creativity and innovation.&#10; - All classrooms are resourced with required math and science manipulatives as well as required grade appropriate books and textbooks from the most current book lists - these are available in print to students.&#10; - All classrooms offer flexibility for large and small group collaboration, quiet places for reflection, active areas for investigation, inquiry, communication and documentation and rich Maple Bear resources that are transparently accessible.&#10;&#10;Instructional time for both English and Local programming is monitored and documented according to Maple Bear proposed scheduling.">info</i></span>')),
        ]





################### GLEX ##########################

class GlexGestaoDeParceriaForm(forms.ModelForm):
    class Meta:
        model = GlexGestaoDeParceria
        exclude = ["escola"]  # O campo escola será preenchido automaticamente
        widgets = {
            "registros_documentacao": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "polices_seguro": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "registros_legais": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "contrato_franquia": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "senso_franquia": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "reclamacoes_defesa_consumidor": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "envio_cases_sucesso": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "cadastro_crm": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "avcb_atualizado": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "alvara_sanitaria": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
            "encontros_lideres": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        escola_id = kwargs.pop("escola_id", None)
        super().__init__(*args, **kwargs)
        if escola_id:
            self.fields["escola"].initial = escola_id

        # Remove a opção "-------" de todos os campos de RadioSelect
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]

        # Aplica classe 'textarea-control' aos campos de comentário e remove obrigatoriedade
        for field_name, field in self.fields.items():
            if "comment" in field_name and isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    "class": "textarea-control", 
                    "rows": 4, 
                    "placeholder": "Leave a comment..."
                })
            field.required = False


class GlexGenteForm(forms.ModelForm):
    class Meta:
        model = GlexGente
        exclude = ["escola"]  # O campo escola será preenchido automaticamente
        widgets = {
            "funcionarios_presentes": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "registros_licencas": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "uso_uniformes": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "desenvolvimento_profissional": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "controle_absenteismo": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "plano_carreira": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "entrevista_desligamento": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "comunicacao_interna": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "legislacao_trabalhista": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "descricao_cargos": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "onboarding_colaboradores": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "acesso_academy": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "identificacao_colaboradores": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "pesquisa_clima": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "recrutamento_selecao": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "avaliacao_desempenho": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
        }

    def __init__(self, *args, **kwargs):
        escola_id = kwargs.pop("escola_id", None)
        super().__init__(*args, **kwargs)
        if escola_id:
            self.fields["escola"].initial = escola_id

        # Remove a opção "-------" de todos os campos de RadioSelect
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]

        # Aplica classe 'textarea-control' aos campos de comentário e remove obrigatoriedade
        for field_name, field in self.fields.items():
            if "comment" in field_name and isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    "class": "textarea-control", 
                    "rows": 4, 
                    "placeholder": "Leave a comment..."
                })
            field.required = False


class GlexAdministrativoForm(forms.ModelForm):
    class Meta:
        model = GlexAdministrativo
        exclude = ["escola"]  # O campo escola será preenchido automaticamente
        widgets = {
            "profissionais_qualificados": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "sistema_administracao": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "pagamentos_em_dia": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "gerencia_queixas": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "desempenho_kpi": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "politica_negocios": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "controle_inadimplencia": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "balanco_dre": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "planejamento_orcamento": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "compartilhamento_orcamento": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
        }

    def __init__(self, *args, **kwargs):
        escola_id = kwargs.pop("escola_id", None)
        super().__init__(*args, **kwargs)
        if escola_id:
            self.fields["escola"].initial = escola_id

        # Remove a opção "-------" de todos os campos de RadioSelect
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]

        # Aplica classe 'textarea-control' aos campos de comentário e remove obrigatoriedade
        for field_name, field in self.fields.items():
            if "comment" in field_name and isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    "class": "textarea-control", 
                    "rows": 4, 
                    "placeholder": "Leave a comment..."
                })
            field.required = False


class GlexTecnologiaForm(forms.ModelForm):
    class Meta:
        model = GlexTecnologia
        exclude = ["escola"]  # O campo escola será preenchido automaticamente
        widgets = {
            "uso_intranet": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "cadastro_lex": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "crm_b2c": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "gestao_leads": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "tarefas_leads": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "visitas_familias": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "oportunidades_matriculas": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "pedidos_matriculas": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "eventos_leads": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "toddle_habilitado": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "uso_sponte": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
        }

    def __init__(self, *args, **kwargs):
        escola_id = kwargs.pop("escola_id", None)
        super().__init__(*args, **kwargs)
        if escola_id:
            self.fields["escola"].initial = escola_id

        # Remove a opção "-------" de todos os campos de RadioSelect
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]

        # Aplica classe 'textarea-control' aos campos de comentário e remove obrigatoriedade
        for field_name, field in self.fields.items():
            if "comment" in field_name and isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    "class": "textarea-control", 
                    "rows": 4, 
                    "placeholder": "Leave a comment..."
                })
            field.required = False


class GlexMarketingForm(forms.ModelForm):
    class Meta:
        model = GlexMarketing
        exclude = ["escola"]  # O campo escola será preenchido automaticamente
        widgets = {
            "campanhas_marketing": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "planejamento_eventos": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "comite_gestao_crise": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "newsletter_semanal": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "ambientacao_datas_especiais": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "google_meu_negocio": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "uso_site_oficial": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "redes_sociais": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "participacao_congressos": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "uso_testemunhos": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "registros_crm": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
        }

    def __init__(self, *args, **kwargs):
        escola_id = kwargs.pop("escola_id", None)
        super().__init__(*args, **kwargs)
        if escola_id:
            self.fields["escola"].initial = escola_id

        # Remove a opção "-------" de todos os campos de RadioSelect
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]

        # Aplica classe 'textarea-control' aos campos de comentário e remove obrigatoriedade
        for field_name, field in self.fields.items():
            if "comment" in field_name and isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    "class": "textarea-control", 
                    "rows": 4, 
                    "placeholder": "Leave a comment..."
                })
            field.required = False


class GlexAcademicoForm(forms.ModelForm):
    class Meta:
        model = GlexAcademico
        exclude = ["escola"]  # O campo escola será preenchido automaticamente
        widgets = {
            "uso_curriculo_atual": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "resultado_qa": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "participacao_treinamento": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "guia_teacher_toddle": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "recursos_alunos_professores": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
        }

    def __init__(self, *args, **kwargs):
        escola_id = kwargs.pop("escola_id", None)
        super().__init__(*args, **kwargs)
        if escola_id:
            self.fields["escola"].initial = escola_id

        # Remove a opção "-------" de todos os campos de RadioSelect
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]

        # Aplica classe 'textarea-control' aos campos de comentário e remove obrigatoriedade
        for field_name, field in self.fields.items():
            if "comment" in field_name and isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    "class": "textarea-control", 
                    "rows": 4, 
                    "placeholder": "Leave a comment..."
                })
            field.required = False


class GlexGestaoEscolarForm(forms.ModelForm):
    class Meta:
        model = GlexGestaoEscolar
        exclude = ["escola"]  # O campo escola será preenchido automaticamente
        widgets = {
            "plano_emergencia": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "info_medicas_atualizadas": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "contato_atualizado": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "seguranca_contra_incendio": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "saidas_emergencia": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "kits_primeiros_socorros": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "funcionarios_treinados_primeiros_socorros": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "simulacoes_emergencia": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "recursos_maple_bear": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "garantia_qualidade": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "treinamento_academico": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "reunioes_lideranca": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "processo_padronizado_atendimento": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "controle_frequencia_alunos": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "controle_media_alunos": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "atividades_extracurriculares": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "analise_pontos_fortes": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "planos_acao_defasagens": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "experiencia_professores": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "professores_por_turma": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "observacao_aulas": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "lideranca_graduada": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "coordenacao_por_segmento": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "cumprimento_legislacao": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "guia_familia": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "comunicacao_interna": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "toddle_comunicacao": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "nps_acima_70": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "orientador_pedagogico": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "certificado_lei_lucas": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
        }

    def __init__(self, *args, **kwargs):
        escola_id = kwargs.pop("escola_id", None)
        super().__init__(*args, **kwargs)
        if escola_id:
            self.fields["escola"].initial = escola_id

        # Remove a opção "-------" de todos os campos de RadioSelect
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]

        # Aplica classe 'textarea-control' aos campos de comentário e remove obrigatoriedade
        for field_name, field in self.fields.items():
            if "comment" in field_name and isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    "class": "textarea-control", 
                    "rows": 4, 
                    "placeholder": "Leave a comment..."
                })
            field.required = False


class GlexOperacaoAcademicaForm(forms.ModelForm):
    class Meta:
        model = GlexOperacaoAcademica
        exclude = ["escola"]  # O campo escola será preenchido automaticamente
        widgets = {
            "treinamentos_pedagogicos": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "professores_nivel_superior": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "professores_certificacao_internacional": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "preparo_aulas_previo": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "metodologia_maple_bear": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
        }

    def __init__(self, *args, **kwargs):
        escola_id = kwargs.pop("escola_id", None)
        super().__init__(*args, **kwargs)
        if escola_id:
            self.fields["escola"].initial = escola_id

        # Remove a opção "-------" de todos os campos de RadioSelect
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]

        # Aplica classe 'textarea-control' aos campos de comentário e remove obrigatoriedade
        for field_name, field in self.fields.items():
            if "comment" in field_name and isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    "class": "textarea-control", 
                    "rows": 4, 
                    "placeholder": "Leave a comment..."
                })
            field.required = False


class GlexImplantacaoForm(forms.ModelForm):
    class Meta:
        model = GlexImplantacao
        exclude = ["escola"]  # O campo escola será preenchido automaticamente
        widgets = {
            "interior_logotipo_maple_bear": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "exterior_logotipo_maple_bear": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "logotipo_estado_conservacao": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "sistema_monitoramento_seguranca": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "controle_acesso_predio": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "sistema_alarme_emergencia": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "area_recreacao_conformidade": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "equipamento_recreacao_conservacao": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "instalacoes_limpeza_organizacao": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "seguranca_estrutural": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "sinalizacao_predio": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "proporcao_adultos_alunos": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "mobilia_salas_conservacao": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "organizacao_corredores": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "acessibilidade_pne": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "politica_embarque_desembarque": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "banheiros_conservacao": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "conservacao_geral_instalacoes": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "danos_esteticos_instalacoes": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "danos_estruturais_eventuais": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "danos_estruturais_risco": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "pia_salas_infantil": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "banheiro_trocador_bear_care": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "banheiro_chuveiro_infantil": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "playground_externo": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "rampas_corrimaos": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "sala_comercial_padroes": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "refeitório_conservacao": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "cozinha_vigilancia_sanitaria": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "playground_interno": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "espaco_esportes": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "quadra_poliesportiva": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "biblioteca_conservacao": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "banheiros_pne_legislacao": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "laboratorio_ciencias": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "mobiliario_fornecedores_homologados": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "mobiliario_salas_admin_professores": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "sala_coordenacao": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "sala_professores": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "vagas_estacionamento": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "iluminacao_ventilacao": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "paredes_balcao_logos": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "salas_55m2": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
            "copa_colaboradores": forms.RadioSelect(
                attrs={"class": "horizontal-radio form-check-label form-check-input form-check radio-options"}
            ),
        }

    def __init__(self, *args, **kwargs):
        escola_id = kwargs.pop("escola_id", None)
        super().__init__(*args, **kwargs)
        if escola_id:
            self.fields["escola"].initial = escola_id

        # Remove a opção "-------" de todos os campos de RadioSelect
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]

        # Aplica classe 'textarea-control' aos campos de comentário e remove obrigatoriedade
        for field_name, field in self.fields.items():
            if "comment" in field_name and isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    "class": "textarea-control", 
                    "rows": 4, 
                    "placeholder": "Leave a comment..."
                })
            field.required = False


class GlexComercialForm(forms.ModelForm):
    class Meta:
        model = GlexComercial
        exclude = ["escola"]  # O campo escola será preenchido automaticamente
        widgets = {
            field_name: forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            )
            for field_name in [
                "processo_matricula_robusto",
                "plano_marketing_matricula",
                "materiais_marketing_padroes",
                "equipe_lideranca_comercial",
                "reunioes_lideranca_comercial",
                "recepcao_visitantes",
                "metas_matriculas_rematriculas",
                "metas_nps",
                "mentoria_vendas",
                "trilha_treinamento_vendas",
                "funil_vendas_crm",
                "cliente_oculto",
                "participacao_campanhas_acoes",
                "pesquisas_mercado",
                "conversao_leads_marketing",
                "capacitacao_exposicao_metodologia",
                "politica_comissionamento",
                "calendario_trade_marketing",
                "equipe_marketing",
                "entrega_kits_rematricula",
                "entrega_kits_visita",
                "leads_atraso_crm",
            ]
        }

    def __init__(self, *args, **kwargs):
        escola_id = kwargs.pop("escola_id", None)
        super().__init__(*args, **kwargs)
        if escola_id:
            self.fields["escola"].initial = escola_id

        # Remove a opção "-------" de todos os campos de RadioSelect
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]

        # Aplica classe 'textarea-control' aos campos de comentário e remove obrigatoriedade
        for field_name, field in self.fields.items():
            if "comment" in field_name and isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    "class": "textarea-control",
                    "rows": 4,
                    "placeholder": "Leave a comment...",
                })
            field.required = False


class GlexResultadoForm(forms.ModelForm):
    class Meta:
        model = GlexResultado
        exclude = ["escola"]  # O campo escola será preenchido automaticamente
        widgets = {
            field_name: forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check radio-options"
                }
            )
            for field_name in [
                "taxa_retenção_rotatividade",
                "meta_rematricula_carta",
                "meta_matricula_carta",
                "compras_slm_conjuntas",
                "resultado_financeiro_bp",
            ]
        }

    def __init__(self, *args, **kwargs):
        escola_id = kwargs.pop("escola_id", None)
        super().__init__(*args, **kwargs)
        if escola_id:
            self.fields["escola"].initial = escola_id

        # Remove a opção "-------" de todos os campos de RadioSelect
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]

        # Aplica classe 'textarea-control' aos campos de comentário e remove obrigatoriedade
        for field_name, field in self.fields.items():
            if "comment" in field_name and isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    "class": "textarea-control",
                    "rows": 4,
                    "placeholder": "Deixe seu comentário aqui...",
                })
            field.required = False







