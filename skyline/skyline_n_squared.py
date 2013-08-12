
def skyline1D(data):
    skyline_points = []
    for x, y in data:
        sky_point = [(x,y)] #assume point belongs to skyline
        for x_p, y_p in data:
            if x== x_p and y == y_p:
                continue
            if x_p <= x and y_p <= y:
                sky_point = []
                break
        skyline_points.extend(sky_point)
    return skyline_points
  


def test():
   points = [(2,6), (4, 7), (5, 5), (7, 5), (9, 9), (10, 4), (4, 4), (3, 2), (6, 2), (9, 1)]
   print('skyline: ', skyline1D(points))

if __name__ == '__main__':
    test()
