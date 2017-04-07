# Crossin 2017/04/07


def pingpong(n, label = 1):
    pingpong_list = [1]
    try:
        for i in range(1, n+1):
            label *= (i % 7 == 0 or '7' in str(i))*-2+1
            pingpong_list.append(pingpong_list[-1] + label)
        print( pingpong_list[-2])
    except:
        print('input error')
    return 0


if __name__ == '__main__':
    pingpong(7)
    pingpong(8)
    pingpong(21)
    pingpong(100)
    pingpong(-1)
    pingpong(1.0)
