"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(
    express_queue: list[str],
    normal_queue: list[str],
    ticket_type: int,
    person_name: str
) -> list[str]:
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.

    Parameters:
        express_queue: The names in the Fast-track queue.
        normal_queue: The names in the normal queue.
        ticket_type: Type of ticket. 1 = express, 0 = normal.
        person_name: The name of person to add to a queue.

    Returns:
        The (updated) queue the name was added to.
    """
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    if ticket_type == 0:
        normal_queue.append(person_name)
        return normal_queue
    return None


def find_my_friend(queue: list[str], friend_name: str) -> int:
    """Search the queue for a name and return their queue position (index).

    Parameters:
        queue: The names in the queue.
        friend_name: The name of friend to find.

    Returns:
        The index at which the friends name was found.
    """
    index = 0
    for index_queue, friend in enumerate(queue):
        if friend_name == friend:
            index = index_queue
            return index
    return None


def add_me_with_my_friends(queue: list[str], index: int, person_name: str) -> list[str]:
    """Insert the late arrival's name at a specific index of the queue.

    Parameters:
        queue: The names in the queue.
        index: The index at which to add the new name.
        person_name: The name to add.

    Returns:
        The queue updated with new name.
    """
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue: list[str], person_name: str) -> list[str]:
    """Remove the mean person from the queue by the provided name.

    Parameters:
        queue: The names in the queue.
        person_name: The name of mean person.

    Returns:
        The queue updated with the mean persons name removed.
    """
    queue.remove(person_name)
    return queue


def how_many_namefellows(queue: list[str], person_name: str) -> int:
    """Count how many times the provided name appears in the queue.

    Parameters:
        queue: The names in the queue.
        person_name: The name you wish to count or track.

    Returns:
        The number of times the name appears in the queue.
    """
    counter = 0
    for name in queue:
        if name == person_name:
            counter += 1
    return counter


def remove_the_last_person(queue: list[str]) -> str:
    """Remove the person in the last index from the queue and return their name.

    Parameters:
        queue: The names in the queue.

    Returns:
        The name that has been removed from the end of the queue.
    """
    last_in_line = queue.pop()
    return last_in_line


def sorted_names(queue: list[str]) -> list[str]:
    """Sort the names in the queue in alphabetical order and return the result.

    Parameters:
        queue: The names in the queue.

    Returns:
        A copy of the queue in alphabetical order.
    """
    copy = queue.copy()
    copy.sort()
    return copy
