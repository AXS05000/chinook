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

        self.order_fields([
            "registros_documentacao",
            "registros_documentacao_file",
            "registros_documentacao_comment",
            "polices_seguro",
            "polices_seguro_file",
            "polices_seguro_comment",
            "registros_legais",
            "registros_legais_file",
            "registros_legais_comment",
            "contrato_franquia",
            "contrato_franquia_file",
            "contrato_franquia_comment",
            "senso_franquia",
            "senso_franquia_file",
            "senso_franquia_comment",
            "reclamacoes_defesa_consumidor",
            "reclamacoes_defesa_consumidor_file",
            "reclamacoes_defesa_consumidor_comment",
            "envio_cases_sucesso",
            "envio_cases_sucesso_file",
            "envio_cases_sucesso_comment",
            "cadastro_crm",
            "cadastro_crm_file",
            "cadastro_crm_comment",
            "avcb_atualizado",
            "avcb_atualizado_file",
            "avcb_atualizado_comment",
            "alvara_sanitaria",
            "alvara_sanitaria_file",
            "alvara_sanitaria_comment",
            "encontros_lideres",
            "encontros_lideres_file",
            "encontros_lideres_comment",
        ])


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
        self.order_fields([
            "funcionarios_presentes",
            "funcionarios_presentes_file",
            "funcionarios_presentes_comment",
            "registros_licencas",
            "registros_licencas_file",
            "registros_licencas_comment",
            "uso_uniformes",
            "uso_uniformes_file",
            "uso_uniformes_comment",
            "desenvolvimento_profissional",
            "desenvolvimento_profissional_file",
            "desenvolvimento_profissional_comment",
            "controle_absenteismo",
            "controle_absenteismo_file",
            "controle_absenteismo_comment",
            "plano_carreira",
            "plano_carreira_file",
            "plano_carreira_comment",
            "entrevista_desligamento",
            "entrevista_desligamento_file",
            "entrevista_desligamento_comment",
            "comunicacao_interna",
            "comunicacao_interna_file",
            "comunicacao_interna_comment",
            "legislacao_trabalhista",
            "legislacao_trabalhista_file",
            "legislacao_trabalhista_comment",
            "descricao_cargos",
            "descricao_cargos_file",
            "descricao_cargos_comment",
            "onboarding_colaboradores",
            "onboarding_colaboradores_file",
            "onboarding_colaboradores_comment",
            "acesso_academy",
            "acesso_academy_file",
            "acesso_academy_comment",
            "identificacao_colaboradores",
            "identificacao_colaboradores_file",
            "identificacao_colaboradores_comment",
            "pesquisa_clima",
            "pesquisa_clima_file",
            "pesquisa_clima_comment",
            "recrutamento_selecao",
            "recrutamento_selecao_file",
            "recrutamento_selecao_comment",
            "avaliacao_desempenho",
            "avaliacao_desempenho_file",
            "avaliacao_desempenho_comment",
        ])



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
        self.order_fields([
            "profissionais_qualificados",
            "profissionais_qualificados_file",
            "profissionais_qualificados_comment",
            "sistema_administracao",
            "sistema_administracao_file",
            "sistema_administracao_comment",
            "pagamentos_em_dia",
            "pagamentos_em_dia_file",
            "pagamentos_em_dia_comment",
            "gerencia_queixas",
            "gerencia_queixas_file",
            "gerencia_queixas_comment",
            "desempenho_kpi",
            "desempenho_kpi_file",
            "desempenho_kpi_comment",
            "politica_negocios",
            "politica_negocios_file",
            "politica_negocios_comment",
            "controle_inadimplencia",
            "controle_inadimplencia_file",
            "controle_inadimplencia_comment",
            "balanco_dre",
            "balanco_dre_file",
            "balanco_dre_comment",
            "planejamento_orcamento",
            "planejamento_orcamento_file",
            "planejamento_orcamento_comment",
            "compartilhamento_orcamento",
            "compartilhamento_orcamento_file",
            "compartilhamento_orcamento_comment",
        ])


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
        self.order_fields([
            "uso_intranet",
            "uso_intranet_file",
            "uso_intranet_comment",
            "cadastro_lex",
            "cadastro_lex_file",
            "cadastro_lex_comment",
            "crm_b2c",
            "crm_b2c_file",
            "crm_b2c_comment",
            "gestao_leads",
            "gestao_leads_file",
            "gestao_leads_comment",
            "tarefas_leads",
            "tarefas_leads_file",
            "tarefas_leads_comment",
            "visitas_familias",
            "visitas_familias_file",
            "visitas_familias_comment",
            "oportunidades_matriculas",
            "oportunidades_matriculas_file",
            "oportunidades_matriculas_comment",
            "pedidos_matriculas",
            "pedidos_matriculas_file",
            "pedidos_matriculas_comment",
            "eventos_leads",
            "eventos_leads_file",
            "eventos_leads_comment",
            "toddle_habilitado",
            "toddle_habilitado_file",
            "toddle_habilitado_comment",
            "uso_sponte",
            "uso_sponte_file",
            "uso_sponte_comment",
        ])


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
        self.order_fields([
            "campanhas_marketing",
            "campanhas_marketing_file",
            "campanhas_marketing_comment",
            "planejamento_eventos",
            "planejamento_eventos_file",
            "planejamento_eventos_comment",
            "comite_gestao_crise",
            "comite_gestao_crise_file",
            "comite_gestao_crise_comment",
            "newsletter_semanal",
            "newsletter_semanal_file",
            "newsletter_semanal_comment",
            "ambientacao_datas_especiais",
            "ambientacao_datas_especiais_file",
            "ambientacao_datas_especiais_comment",
            "google_meu_negocio",
            "google_meu_negocio_file",
            "google_meu_negocio_comment",
            "uso_site_oficial",
            "uso_site_oficial_file",
            "uso_site_oficial_comment",
            "redes_sociais",
            "redes_sociais_file",
            "redes_sociais_comment",
            "participacao_congressos",
            "participacao_congressos_file",
            "participacao_congressos_comment",
            "uso_testemunhos",
            "uso_testemunhos_file",
            "uso_testemunhos_comment",
            "registros_crm",
            "registros_crm_file",
            "registros_crm_comment",
        ])



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
        self.order_fields([
            "uso_curriculo_atual",
            "uso_curriculo_atual_file",
            "uso_curriculo_atual_comment",
            "resultado_qa",
            "resultado_qa_file",
            "resultado_qa_comment",
            "participacao_treinamento",
            "participacao_treinamento_file",
            "participacao_treinamento_comment",
            "guia_teacher_toddle",
            "guia_teacher_toddle_file",
            "guia_teacher_toddle_comment",
            "recursos_alunos_professores",
            "recursos_alunos_professores_file",
            "recursos_alunos_professores_comment",
        ])


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
        self.order_fields([
            "plano_emergencia",
            "plano_emergencia_file",
            "plano_emergencia_comment",
            "info_medicas_atualizadas",
            "info_medicas_atualizadas_file",
            "info_medicas_atualizadas_comment",
            "contato_atualizado",
            "contato_atualizado_file",
            "contato_atualizado_comment",
            "seguranca_contra_incendio",
            "seguranca_contra_incendio_file",
            "seguranca_contra_incendio_comment",
            "saidas_emergencia",
            "saidas_emergencia_file",
            "saidas_emergencia_comment",
            "kits_primeiros_socorros",
            "kits_primeiros_socorros_file",
            "kits_primeiros_socorros_comment",
            "funcionarios_treinados_primeiros_socorros",
            "funcionarios_treinados_primeiros_socorros_file",
            "funcionarios_treinados_primeiros_socorros_comment",
            "simulacoes_emergencia",
            "simulacoes_emergencia_file",
            "simulacoes_emergencia_comment",
            "recursos_maple_bear",
            "recursos_maple_bear_file",
            "recursos_maple_bear_comment",
            "garantia_qualidade",
            "garantia_qualidade_file",
            "garantia_qualidade_comment",
            "treinamento_academico",
            "treinamento_academico_file",
            "treinamento_academico_comment",
            "reunioes_lideranca",
            "reunioes_lideranca_file",
            "reunioes_lideranca_comment",
            "processo_padronizado_atendimento",
            "processo_padronizado_atendimento_file",
            "processo_padronizado_atendimento_comment",
            "controle_frequencia_alunos",
            "controle_frequencia_alunos_file",
            "controle_frequencia_alunos_comment",
            "controle_media_alunos",
            "controle_media_alunos_file",
            "controle_media_alunos_comment",
            "atividades_extracurriculares",
            "atividades_extracurriculares_file",
            "atividades_extracurriculares_comment",
            "analise_pontos_fortes",
            "analise_pontos_fortes_file",
            "analise_pontos_fortes_comment",
            "planos_acao_defasagens",
            "planos_acao_defasagens_file",
            "planos_acao_defasagens_comment",
            "experiencia_professores",
            "experiencia_professores_file",
            "experiencia_professores_comment",
            "professores_por_turma",
            "professores_por_turma_file",
            "professores_por_turma_comment",
            "observacao_aulas",
            "observacao_aulas_file",
            "observacao_aulas_comment",
            "lideranca_graduada",
            "lideranca_graduada_file",
            "lideranca_graduada_comment",
            "coordenacao_por_segmento",
            "coordenacao_por_segmento_file",
            "coordenacao_por_segmento_comment",
            "cumprimento_legislacao",
            "cumprimento_legislacao_file",
            "cumprimento_legislacao_comment",
            "guia_familia",
            "guia_familia_file",
            "guia_familia_comment",
            "comunicacao_interna",
            "comunicacao_interna_file",
            "comunicacao_interna_comment",
            "toddle_comunicacao",
            "toddle_comunicacao_file",
            "toddle_comunicacao_comment",
            "nps_acima_70",
            "nps_acima_70_file",
            "nps_acima_70_comment",
            "orientador_pedagogico",
            "orientador_pedagogico_file",
            "orientador_pedagogico_comment",
            "certificado_lei_lucas",
            "certificado_lei_lucas_file",
            "certificado_lei_lucas_comment",
        ])



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
        self.order_fields([
            "treinamentos_pedagogicos",
            "treinamentos_pedagogicos_file",
            "treinamentos_pedagogicos_comment",
            "professores_nivel_superior",
            "professores_nivel_superior_file",
            "professores_nivel_superior_comment",
            "professores_certificacao_internacional",
            "professores_certificacao_internacional_file",
            "professores_certificacao_internacional_comment",
            "preparo_aulas_previo",
            "preparo_aulas_previo_file",
            "preparo_aulas_previo_comment",
            "metodologia_maple_bear",
            "metodologia_maple_bear_file",
            "metodologia_maple_bear_comment",
        ])


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
        self.order_fields([
            "interior_logotipo_maple_bear",
            "interior_logotipo_maple_bear_file",
            "interior_logotipo_maple_bear_comment",
            "exterior_logotipo_maple_bear",
            "exterior_logotipo_maple_bear_file",
            "exterior_logotipo_maple_bear_comment",
            "logotipo_estado_conservacao",
            "logotipo_estado_conservacao_file",
            "logotipo_estado_conservacao_comment",
            "sistema_monitoramento_seguranca",
            "sistema_monitoramento_seguranca_file",
            "sistema_monitoramento_seguranca_comment",
            "controle_acesso_predio",
            "controle_acesso_predio_file",
            "controle_acesso_predio_comment",
            "sistema_alarme_emergencia",
            "sistema_alarme_emergencia_file",
            "sistema_alarme_emergencia_comment",
            "area_recreacao_conformidade",
            "area_recreacao_conformidade_file",
            "area_recreacao_conformidade_comment",
            "equipamento_recreacao_conservacao",
            "equipamento_recreacao_conservacao_file",
            "equipamento_recreacao_conservacao_comment",
            "instalacoes_limpeza_organizacao",
            "instalacoes_limpeza_organizacao_file",
            "instalacoes_limpeza_organizacao_comment",
            "seguranca_estrutural",
            "seguranca_estrutural_file",
            "seguranca_estrutural_comment",
            "sinalizacao_predio",
            "sinalizacao_predio_file",
            "sinalizacao_predio_comment",
            "proporcao_adultos_alunos",
            "proporcao_adultos_alunos_file",
            "proporcao_adultos_alunos_comment",
            "mobilia_salas_conservacao",
            "mobilia_salas_conservacao_file",
            "mobilia_salas_conservacao_comment",
            "organizacao_corredores",
            "organizacao_corredores_file",
            "organizacao_corredores_comment",
            "acessibilidade_pne",
            "acessibilidade_pne_file",
            "acessibilidade_pne_comment",
            "politica_embarque_desembarque",
            "politica_embarque_desembarque_file",
            "politica_embarque_desembarque_comment",
            "banheiros_conservacao",
            "banheiros_conservacao_file",
            "banheiros_conservacao_comment",
            "conservacao_geral_instalacoes",
            "conservacao_geral_instalacoes_file",
            "conservacao_geral_instalacoes_comment",
            "danos_esteticos_instalacoes",
            "danos_esteticos_instalacoes_file",
            "danos_esteticos_instalacoes_comment",
            "danos_estruturais_eventuais",
            "danos_estruturais_eventuais_file",
            "danos_estruturais_eventuais_comment",
            "danos_estruturais_risco",
            "danos_estruturais_risco_file",
            "danos_estruturais_risco_comment",
            "pia_salas_infantil",
            "pia_salas_infantil_file",
            "pia_salas_infantil_comment",
            "banheiro_trocador_bear_care",
            "banheiro_trocador_bear_care_file",
            "banheiro_trocador_bear_care_comment",
            "banheiro_chuveiro_infantil",
            "banheiro_chuveiro_infantil_file",
            "banheiro_chuveiro_infantil_comment",
            "playground_externo",
            "playground_externo_file",
            "playground_externo_comment",
            "rampas_corrimaos",
            "rampas_corrimaos_file",
            "rampas_corrimaos_comment",
            "sala_comercial_padroes",
            "sala_comercial_padroes_file",
            "sala_comercial_padroes_comment",
            "refeitório_conservacao",
            "refeitório_conservacao_file",
            "refeitório_conservacao_comment",
            "cozinha_vigilancia_sanitaria",
            "cozinha_vigilancia_sanitaria_file",
            "cozinha_vigilancia_sanitaria_comment",
            "playground_interno",
            "playground_interno_file",
            "playground_interno_comment",
            "espaco_esportes",
            "espaco_esportes_file",
            "espaco_esportes_comment",
            "quadra_poliesportiva",
            "quadra_poliesportiva_file",
            "quadra_poliesportiva_comment",
            "biblioteca_conservacao",
            "biblioteca_conservacao_file",
            "biblioteca_conservacao_comment",
            "banheiros_pne_legislacao",
            "banheiros_pne_legislacao_file",
            "banheiros_pne_legislacao_comment",
            "laboratorio_ciencias",
            "laboratorio_ciencias_file",
            "laboratorio_ciencias_comment",
            "mobiliario_fornecedores_homologados",
            "mobiliario_fornecedores_homologados_file",
            "mobiliario_fornecedores_homologados_comment",
            "mobiliario_salas_admin_professores",
            "mobiliario_salas_admin_professores_file",
            "mobiliario_salas_admin_professores_comment",
            "sala_coordenacao",
            "sala_coordenacao_file",
            "sala_coordenacao_comment",
            "sala_professores",
            "sala_professores_file",
            "sala_professores_comment",
            "vagas_estacionamento",
            "vagas_estacionamento_file",
            "vagas_estacionamento_comment",
            "iluminacao_ventilacao",
            "iluminacao_ventilacao_file",
            "iluminacao_ventilacao_comment",
            "paredes_balcao_logos",
            "paredes_balcao_logos_file",
            "paredes_balcao_logos_comment",
            "salas_55m2",
            "salas_55m2_file",
            "salas_55m2_comment",
            "copa_colaboradores",
            "copa_colaboradores_file",
            "copa_colaboradores_comment",
        ])



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
        self.order_fields([
            "processo_matricula_robusto",
            "processo_matricula_robusto_file",
            "processo_matricula_robusto_comment",
            "plano_marketing_matricula",
            "plano_marketing_matricula_file",
            "plano_marketing_matricula_comment",
            "materiais_marketing_padroes",
            "materiais_marketing_padroes_file",
            "materiais_marketing_padroes_comment",
            "equipe_lideranca_comercial",
            "equipe_lideranca_comercial_file",
            "equipe_lideranca_comercial_comment",
            "reunioes_lideranca_comercial",
            "reunioes_lideranca_comercial_file",
            "reunioes_lideranca_comercial_comment",
            "recepcao_visitantes",
            "recepcao_visitantes_file",
            "recepcao_visitantes_comment",
            "metas_matriculas_rematriculas",
            "metas_matriculas_rematriculas_file",
            "metas_matriculas_rematriculas_comment",
            "metas_nps",
            "metas_nps_file",
            "metas_nps_comment",
            "mentoria_vendas",
            "mentoria_vendas_file",
            "mentoria_vendas_comment",
            "trilha_treinamento_vendas",
            "trilha_treinamento_vendas_file",
            "trilha_treinamento_vendas_comment",
            "funil_vendas_crm",
            "funil_vendas_crm_file",
            "funil_vendas_crm_comment",
            "cliente_oculto",
            "cliente_oculto_file",
            "cliente_oculto_comment",
            "participacao_campanhas_acoes",
            "participacao_campanhas_acoes_file",
            "participacao_campanhas_acoes_comment",
            "pesquisas_mercado",
            "pesquisas_mercado_file",
            "pesquisas_mercado_comment",
            "conversao_leads_marketing",
            "conversao_leads_marketing_file",
            "conversao_leads_marketing_comment",
            "capacitacao_exposicao_metodologia",
            "capacitacao_exposicao_metodologia_file",
            "capacitacao_exposicao_metodologia_comment",
            "politica_comissionamento",
            "politica_comissionamento_file",
            "politica_comissionamento_comment",
            "calendario_trade_marketing",
            "calendario_trade_marketing_file",
            "calendario_trade_marketing_comment",
            "equipe_marketing",
            "equipe_marketing_file",
            "equipe_marketing_comment",
            "entrega_kits_rematricula",
            "entrega_kits_rematricula_file",
            "entrega_kits_rematricula_comment",
            "entrega_kits_visita",
            "entrega_kits_visita_file",
            "entrega_kits_visita_comment",
            "leads_atraso_crm",
            "leads_atraso_crm_file",
            "leads_atraso_crm_comment",
        ])


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
        self.order_fields([
            "taxa_retenção_rotatividade",
            "taxa_retenção_rotatividade_file",
            "taxa_retenção_rotatividade_comment",
            "meta_rematricula_carta",
            "meta_rematricula_carta_file",
            "meta_rematricula_carta_comment",
            "meta_matricula_carta",
            "meta_matricula_carta_file",
            "meta_matricula_carta_comment",
            "compras_slm_conjuntas",
            "compras_slm_conjuntas_file",
            "compras_slm_conjuntas_comment",
            "resultado_financeiro_bp",
            "resultado_financeiro_bp_file",
            "resultado_financeiro_bp_comment",
        ])







