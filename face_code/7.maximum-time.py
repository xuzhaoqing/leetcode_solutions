# Maximum Time
# https#://leetcode.com/discuss/interview-question/396769/Google-or-OA-2019-or-Maximum-Time


def giveMeMaxTime(time):
    result = [''] * len(time)
    if time[0] != '?':
        result[0] = time[0]
    else:
        result[0] = '1' if time[1] != '?' and time[1] >= '4' else '2'
    result[1] = time[1] if time[1] != '?' else ('9' if result[0] <= '1' else '3')
    result[2] = ':'
    result[3] = time[3] if time[3] != '?' else '5'
    result[4] = time[4] if time[4] != '?' else '9'
    print(''.join(result))


giveMeMaxTime("23:5?") ##;// 23:59
giveMeMaxTime("2?:22") # #;// 23:22
giveMeMaxTime("0?:??") #;// 09:59
giveMeMaxTime("1?:??") #;// 19:59
giveMeMaxTime("?4:??") #;// 14:59
giveMeMaxTime("?3:??") #;// 23:59
giveMeMaxTime("??:??") #;// 23:59
giveMeMaxTime("?4:5?") #;# //14:59
giveMeMaxTime("?4:??") #;# //14:59
giveMeMaxTime("?3:??") #;# //23:59
giveMeMaxTime("23:5?") #;# //23:59
giveMeMaxTime("2?:22") #;# //23:22
giveMeMaxTime("0?:??") #;# //09:59
giveMeMaxTime("1?:??") #;# //19:59
giveMeMaxTime("?4:0?") #;# //14:09
giveMeMaxTime("?9:4?") #;# //19:49



    