# Crossin 2017/04/07


def pingpong(n, k=7, label=1):
    pingpong_list = [1]
    try:
        for i in range(1, n+1):
            label *= (i % k == 0 or str(k) in str(i))*-2+1
            pingpong_list.append(pingpong_list[-1] + label)
        print(pingpong_list[-2])
    except:
        print('input error')
    return 0


if __name__ == '__main__':
    pingpong(7, 7)
    pingpong(8, 8)
    pingpong(55, 6)
    pingpong(100, 9)
