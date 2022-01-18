def direction(facing, turn):
    l = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    return l[int(l.index(facing) + (turn / 45)) % 8]
