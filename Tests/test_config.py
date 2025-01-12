import configparser
import os

BASE_PATH = os.path.dirname(__file__)
PASSED_CONFIG = os.path.join(BASE_PATH, 'test_configuration/config_should_passed.cfg')
FAILED_CONFIG = os.path.join(BASE_PATH, 'test_configuration/config_should_failed.cfg')

def test_config_passed():
    config = configparser.ConfigParser()
    config.read(PASSED_CONFIG)
    type_value = config.get('Settings', 'TYPE', fallback=None)
    video_url_value = config.get('Settings', 'VIDEO_URL', fallback=None)
    amount_value = config.get('Settings', 'AMOUNT', fallback=None)
    webhook_value = config.get('Settings', 'WEBHOOK', fallback=None)
    each_views_value = config.get('Settings', 'EACH_VIEWS', fallback=None)

    results = {
        'TYPE': validate_type(type_value),
        'VIDEO_URL': validate_video_url(video_url_value),
        'AMOUNT': validate_amount(amount_value),
        'WEBHOOK': validate_webhook(webhook_value),
        'EACH_VIEWS': validate_each_views(each_views_value)
    }

    failed_validations = [field for field, passed in results.items() if not passed]
    assert not failed_validations, f"The following fields failed validation: {', '.join(failed_validations)}"

def test_config_failed():
    config = configparser.ConfigParser()
    config.read(FAILED_CONFIG)
    type_value = config.get('Settings', 'TYPE', fallback=None)
    video_url_value = config.get('Settings', 'VIDEO_URL', fallback=None)
    amount_value = config.get('Settings', 'AMOUNT', fallback=None)
    webhook_value = config.get('Settings', 'WEBHOOK', fallback=None)
    each_views_value = config.get('Settings', 'EACH_VIEWS', fallback=None)

    results = {
        'TYPE': validate_type(type_value),
        'VIDEO_URL': validate_video_url(video_url_value),
        'AMOUNT': validate_amount(amount_value),
        'WEBHOOK': validate_webhook(webhook_value),
        'EACH_VIEWS': validate_each_views(each_views_value)
    }

    passed_validations = [field for field, passed in results.items() if passed]
    assert not passed_validations, f"The following fields passed validation but should not: {', '.join(passed_validations)}"

def validate_type(value):
    expected_types = ['views', 'shares', 'favorites', 'hearts']
    return value in expected_types

def validate_video_url(value):
    if not value:
        return False
    if not isinstance(value, str):
        return False
    if not value.startswith('https://www.tiktok.com/'):
        return False
    if '/video/' not in value:
        return False
    if '/photo/' in value:
        return False
    return True

def validate_amount(value):
    try:
        amount = int(value)
        return amount > 0
    except (ValueError, TypeError):
        return False

def validate_webhook(value):
    return bool(value)

def validate_each_views(value):
    try:
        each_views = int(value)
        return True
    except (ValueError, TypeError):
        return False
