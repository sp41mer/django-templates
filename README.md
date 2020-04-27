# Django views & forms — side-by-side reference

Teaching repo with two parallel implementations of the same small app, so
you can compare approaches line by line instead of reading abstract advice.

## Function-based vs class-based views

`school/views/fb_views.py` and `school/views/cb_views.py` implement the
**same screens over the same models** — list, detail, create — once as
plain functions, once as generic CBVs. Read them side by side to see
exactly what `ListView`/`DetailView`/`CreateView` buy you and what they
hide.

## The forms ladder

`school/forms.py` builds up in four steps:

1. `SchoolSimpleForm` — bare `forms.Form` with manual fields
2. `SchoolForeignKeyForm` — `ModelChoiceField` for related objects
3. `SchoolWidgetForm` — custom widgets + a custom validator
4. `ModelForm` — the same thing generated from the model

## Run

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Custom template tags

`school/templatetags/school_extras.py` shows the three kinds you actually
use: a filter (`age_group`), a `simple_tag` computing a value in place,
and an `inclusion_tag` rendering `templates/school_card.html` with its own
context — the template-side analogue of extracting a helper function.
