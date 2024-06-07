def to_dict(obj):
    if hasattr(obj, '__dict__'):
        return {key: to_dict(value) for key, value in obj.__dict__.items()}
    else:
        return obj