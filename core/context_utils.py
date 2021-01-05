def cache(func):
    def is_cached(context):
        return func.__name__ in context.caching

    def wrap_func(context):
        print(is_cached(context))
        if is_cached(context):
            return context.get_from_cache(func.__name__)
        result = func(context)
        context.set_cache(func.__name__, result)
        return result

    return wrap_func
