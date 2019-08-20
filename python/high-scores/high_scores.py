def latest(scores):
    """ Return the latest score from a list
    """
    return scores[-1]


def personal_best(scores):
    """ Return the highest score from a list
    """
    return max(scores)


def personal_top_three(scores):
    """ Return the top (up-to) 3 scores (descending) from a list
    """
    return sorted(scores, reverse=True)[0:3]
