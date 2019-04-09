from django.apps import AppConfig


def MultiSelectField__from_db_value(self, value, expression,
                                    connection, *args):
    if value is None:
        return value
    return self.to_python(value)


class Config(AppConfig):
    name = 'apps.contrib'
    label = 'advocate_europe_contrib'

    def ready(self):
        from multiselectfield.db.fields import (
            MultiSelectField
        )

        MultiSelectField.from_db_value = (
            MultiSelectField__from_db_value
        )
