from os import path

import requests
from django.core.files import base, images
from django.utils import timezone


def download_file(asset_url):
    response = requests.get(asset_url)
    data = response.json()['data']
    img_url = data[
        'adhocracy_mercator.sheets.mercator.IIntroImageMetadata']['detail']
    response = requests.get(img_url)
    filename = path.split(path.split(asset_url)[0])[1]
    return images.ImageFile(base.ContentFile(response.content), filename)


def parse_year(date_str):
    # remove colon in timezone offset
    parts = date_str.split(':')
    minutes_offset = parts.pop()
    date_str = ':'.join(parts) + minutes_offset

    date = timezone.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')
    return date.year


def floatstr_to_int(float_str):
    return int(float(float_str))


def map_and_append(dst_field, mapping, empty_value=[]):
    def handler(src_value, a4proposal):
        old = getattr(a4proposal, dst_field) or list(empty_value)
        new = mapping.get(src_value, src_value)

        if new not in old and new is not None:
            old.append(new)
            setattr(a4proposal, dst_field, old)
    return handler


def concat(dst_field, seperator=', '):
    def handler(src_value, a4proposal):
        old = getattr(a4proposal, dst_field) or ''
        new = seperator.join([old, src_value])

        if new not in old:
            setattr(a4proposal, dst_field, new)
    return handler
