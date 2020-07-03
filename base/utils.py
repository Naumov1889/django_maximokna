import functools



def memoize(method):
    # Memoize remembers return value of a function call,
    # under the key made from it's arguments.
    # For each arguments combination it's called at most one time.
    # This function is for making context processors lazy!
    @functools.wraps(method)
    def memoizer(*args, **kwargs):
        method._cache = getattr(method, '_cache', {})
        key = args
        if key not in method._cache:
            method._cache[key] = method(*args, **kwargs)
        return method._cache[key]

    return memoizer


def get_page_range(index, max_index):
    # Only 3 pages in pagination
    # wherever page you are on
    if index <= 1:
        start_index = 0
    elif index == max_index - 1:
        start_index = index - 2
    else:
        start_index = index - 1

    if index <= max_index - 1 and index < 1:
        end_index = index + 3
    elif index <= max_index - 2:
        end_index = index + 2
    else:
        end_index = max_index

    # start_index = index - 2 if index >= 3 else 0
    # end_index = index + 3 if index <= max_index - 2 else max_index

    return start_index, end_index


