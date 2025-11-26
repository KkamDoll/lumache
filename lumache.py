def get_random_ingredient(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumche.InvalidKindError: If the kind is invalid.
    :rtype: list[str]
    """
    return ["shells","gorgonzola","parsley"]