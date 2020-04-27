from django import template

register = template.Library()


# Usage in a template:
#   {% load school_extras %}
#   {{ student.age|age_group }}
@register.filter
def age_group(age):
    if age is None:
        return "unknown"
    if age < 11:
        return "junior"
    if age < 15:
        return "middle"
    return "senior"


# Simple tag: computes a value right in the template.
#   {% students_per_class school.student_set.count school.number %}
@register.simple_tag
def students_per_class(total_students, number_of_classes):
    if not number_of_classes:
        return 0
    return round(total_students / number_of_classes, 1)


# Inclusion tag: renders a sub-template with its own small context —
# the template-side analogue of extracting a helper function.
#   {% school_card school %}
@register.inclusion_tag('school_card.html')
def school_card(school):
    return {
        "school": school,
        "students": school.student_set.count(),
    }
