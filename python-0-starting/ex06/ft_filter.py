def ft_filter(function: any, i: iter) -> iter:
    if function is None:
        return iter([item for item in i if item])
    return iter([item for item in i if function(item)])