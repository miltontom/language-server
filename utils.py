def to_dict(obj):
    if not hasattr(obj, '__dict__'):
        return obj
    return {key: to_dict(value) for key, value in obj.__dict__.items()}