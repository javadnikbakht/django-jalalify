from typing import Union
from datetime import datetime
import jdatetime

from django_jalalify.timezone import TEHRAN_ZONE


class FieldDateTimeInJalaliGeneratorMixin:

    def _field_datetime_in_jalali(self, field_name) -> Union[None, str]:
        field_object = self._meta.get_field(field_name)
        field_value = field_object.value_from_object(self)
        if field_value is None:
            return None
        field_value_in_tehran_tz: datetime = field_value.astimezone(TEHRAN_ZONE)
        return field_value and jdatetime.datetime.fromgregorian(
            year=field_value_in_tehran_tz.year, month=field_value_in_tehran_tz.month,
            day=field_value_in_tehran_tz.day, hour=field_value_in_tehran_tz.hour,
            minute=field_value_in_tehran_tz.minute, second=field_value_in_tehran_tz.second,
        ).strftime(
            "%Y/%m/%d %H:%M:%S"
        )
