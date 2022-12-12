def correct(s):
    mistake = {"0": "O", "5": "S", "1": "I"}
    for i in s:
        if i in mistake:
            s = s.replace(i, mistake[i])
    return s


if __name__ == '__main__':
    print(correct('PAR15'))
