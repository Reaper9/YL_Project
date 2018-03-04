def get_class( classToGet ):
    parts = classToGet.split('.')
    module = ".".join(parts[:-1])
    result = __import__( module )
    for comp in parts[1:]:
        result = getattr(result, comp)
    return result