def add_me_to_the_queue(
    express_queue: list[str],
    normal_queue: list[str],
    ticket_type: int,
    person_name: str,
) -> list[str]:
    """

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue:  list - names in the normal queue.
    :param ticket_type:  int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """
    return (
        normal_queue + [person_name]
        if ticket_type == 0
        else express_queue + [person_name]
    )


def find_my_friend(queue: list[str], friend_name: str) -> int:
    """

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """
    return queue.index(friend_name)


def add_me_with_my_friends(
    queue: list[str], index: int, person_name: str
) -> list[str]:
    """

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """
    return queue[:index] + [person_name] + queue[index:]


def remove_the_mean_person(queue: list[str], person_name: str) -> list[str]:
    """

    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return:  list - queue update with the mean persons name removed.
    """
    return [name for name in queue if name != person_name]


def how_many_namefellows(queue: list[str], person_name: str) -> int:
    """

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return:  int - the number of times the name appears in the queue.
    """
    return queue.count(person_name)


def remove_the_last_person(queue: list[str]) -> str:
    """

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """
    return queue[-1]


def sorted_names(queue: list[str]) -> list[str]:
    """

    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """
    return sorted(queue)
