#!/usr/bin/python3
"""Solves the lock bxs puzzle """


def my_next(opn_bx):
    """Looks for the next opened box
    Args:
        opn_bx (dict): Dictionary which contains bxs already opened
    Returns:
        list: List with the keys contained in the opened box
    """
    for index, box in opn_bx.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(bxs):
    """Check if all bxs can be opened
    Args:
        bxs (list): List which contain all the bxs with the keys
    Returns:
        bool: True if all bxs can be opened, otherwise, False
    """
    if len(bxs) <= 1 or bxs == [[]]:
        return True

    an_au = {}
    while True:
        if len(an_au) == 0:
            an_au[0] = {
                'status': 'opened',
                'keys': bxs[0],
            }
        keys = my_next(an_au)
        if keys:
            for key in keys:
                try:
                    if an_au.get(key) and an_au.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    an_au[key] = {
                        'status': 'opened',
                        'keys': bxs[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in an_au.values()]:
            continue
        elif len(an_au) == len(bxs):
            break
        else:
            return False

    return len(an_au) == len(bxs)


def main():
    """Entry point"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
