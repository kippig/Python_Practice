def isValid(s):
    counter = dict()
    for i in range(len(s)):
        if counter.get(s[i]) is None:
            counter[s[i]] = 1
        else:
            counter[s[i]] += 1

    values = list(counter.values())
    print(values)
    if len(set(values)) == 1:
        return 'YES'
    elif len(set(values)) == 2:
        a = (values[0], 1)
        b = (None, 0)
        for i in range(1, len(values)):
            print(i, a, b)
            if (values[i] == 1 or abs(values[i] - a[0]) == 1) and b[0] is None:
                b = (values[i], 1)
            elif abs(values[i] - a[0]) > 1:
                return 'NO'
            elif values[i] == a[0] and b[1] < 2:
                a = (a[0], a[1] + 1)
            elif values[i] == b[0] and a[1] < 2:
                b = (b[0], b[1] + 1)
            else:
                print('fail!')
                return 'NO'
        return 'YES'
    return 'NO'


s = 'ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'
print(isValid(s))