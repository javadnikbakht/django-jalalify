from datetime import datetime
from typing import Tuple

import jdatetime
import pytz

from django_jalalify.functions import convert_date_to_int, convert_time_to_int
from django_jalalify.timezone import TEHRAN_ZONE, TEHRAN_LMT_ZONE, tehran_timezone


def tehran_now() -> datetime: return datetime.now(pytz.timezone('Asia/Tehran'))


def get_now_tehran_jalali_datetime():
    return jdatetime.datetime.fromgregorian(datetime=datetime.now().astimezone(tehran_timezone))


def get_now_tehran_jalali_date_strftime(string_format="%Y/%m/%d") -> str:
    return get_now_tehran_jalali_datetime().date().strftime(string_format)


def get_now_tehran_jalali_time_strftime(string_format="%H:%M:%S") -> str:
    return get_now_tehran_jalali_datetime().time().strftime(string_format)


def get_now_tehran_jalali_date_intftime() -> int:
    """
    convert today Jalali date as a integer date
    e.g: datetime(2023-03-29) => 1402/01/09 => 14020109
    """
    today_jalali_date_strftime = get_now_tehran_jalali_date_strftime(string_format="%Y-%m-%d")
    return convert_date_to_int(today_jalali_date_strftime)


def get_now_tehran_jalali_time_intftime() -> int:
    today_jalali_time_strftime = get_now_tehran_jalali_time_strftime(string_format="%H:%M:%S")
    return convert_time_to_int(today_jalali_time_strftime)


def get_tehran_timestamp_with_three_digits_of_microsecond_accuracy(timestamp) -> str:
    return timestamp.astimezone(TEHRAN_ZONE).strftime("%Y/%m/%d %H:%M:%S:%f")[:-3]


def get_jalali_tehran_datetime_from_date_string(time) -> datetime:
    return jdatetime.datetime.strptime(time, "%Y/%m/%d %H:%M:%S").replace(tzinfo=tehran_timezone).todatetime()


def int_jalali_date_to_jalali_datetime(date) -> datetime:
    """
    convert 14010105 to datetime.datetime(2022, 3, 25, 0, 0, tzinfo=+03:30 dst:60).
    """
    day = date % 100
    date //= 100
    month = date % 100
    year = date // 100
    return jdatetime.datetime(year=year, month=month, day=day, tzinfo=tehran_timezone)


def str_of_int_to_jalali_datetime(date, time) -> datetime:
    """
    convert "14020202", "101010" to datetime.datetime(2022, 3, 25, 0, 0, tzinfo=+03:30 dst:60).
    """
    return jdatetime.datetime(
        year=int(date[:4]), month=int(date[4:6]), day=int(date[6:8]),
        hour=int(time[:2]), minute=int(time[2:4]), second=int(time[4:6]),
        tzinfo=tehran_timezone
    )


def jalali_datetime_to_int(jalali_datetime) -> Tuple:

    date = f"{jalali_datetime.year:02d}{jalali_datetime.month:02d}{jalali_datetime.day:02d}"
    time = f"{jalali_datetime.hour:02d}{jalali_datetime.minute:02d}{jalali_datetime.second:02d}"
    return date, time


def convert_datetime_to_custom_jalali_date(date_time: datetime) -> int:
    """
    Convert input date to Jalali integer date
    e.g: datetime(2023-03-29) => 1402/01/09 => 14020109
    """
    dt_in_tehran_tz = date_time.astimezone(TEHRAN_LMT_ZONE)
    date_in_jalali = jdatetime.datetime(
        year=dt_in_tehran_tz, month=dt_in_tehran_tz, day=dt_in_tehran_tz.day).strftime("%Y%m%d")
    return convert_date_to_int(date_in_jalali)
