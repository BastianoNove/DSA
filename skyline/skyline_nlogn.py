
def skyline1D(data):
    data_sorted = sorted(((point, sum(point)) for point in data), key=lambda x: x[1])
    data = [item[0] for item in data_sorted]
    skyline = data[:1]
    for i in range(1, len(data)):
        x, y = data[i]
        skypoint = [(x,y)]
        for x_p, y_p in skyline:
            if x_p <= x and y_p <= y:
                skypoint = []
                break
        skyline.extend(skypoint)
    return skyline

def test():
    points = [(2,6), (4, 7), (5, 5), (7, 5), (9, 9), (10, 4), (4, 4), (3, 2), (6, 2), (9, 1)]
    print(skyline1D(points))

if __name__ == '__main__':
    test()
