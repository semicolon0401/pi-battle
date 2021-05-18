'''본 작품은 긱블의 '파이 배틀'이라는 게임을 리메이크한 것을 알려드립니다'''

#importing line
import threading, pyautogui
from keyboard import is_pressed as click

def pi():
    return(''.join(['3.',
    '14159 26535 89793 23846 26433 83279 50288 41971 69399 37510',
    '58209 74944 59230 78164 06286 20899 86280 34825 34211 70679',
    '82148 08651 32823 06647 09384 46095 50582 23172 53594 08128',
    '48111 74502 84102 70193 85211 05559 64462 29489 54930 38196',
    '44288 10975 66593 34461 28475 64823 37867 83165 27120 19091',
    '45648 56692 34603 48610 45432 66482 13393 60726 02491 41273',
    '72458 70066 06315 58817 48815 20920 96282 92540 91715 36436',
    '78925 90360 01133 05305 48820 46652 13841 46951 94151 16094',
    '33057 27036 57595 91953 09218 61173 81932 61179 31051 18548',
    '07446 23799 62749 56735 18857 52724 89122 79381 83011 94912',
    '98336 73362 44065 66430 86021 39494 63952 24737 19070 21798',
    '60943 70277 05392 17176 29317 67523 84674 81846 76694 05132',
    '00056 81271 45263 56082 77857 71342 75778 96091 73637 17872',
    '14684 40901 22495 34301 46549 58537 10507 92279 68925 89235',
    '42019 95611 21290 21960 86403 44181 59813 62977 47713 09960',
    '51870 72113 49999 99837 29780 49951 05973 17328 16096 31859',
    '50244 59455 34690 83026 42522 30825 33446 85035 26193 11881',
    '71010 00313 78387 52886 58753 32083 81420 61717 76691 47303',
    '59825 34904 28755 46873 11595 62863 88235 37875 93751 95778',
    '18577 80532 17122 68066 13001 92787 66111 95909 21642 01989',
    '38095 25720 10654 85863 27886 59361 53381 82796 82303 01952',
    '03530 18529 68995 77362 25994 13891 24972 17752 83479 13151',
    '55748 57242 45415 06959 50829 53311 68617 27855 88907 50983',
    '81754 63746 49393 19255 06040 09277 01671 13900 98488 24012',
    '85836 16035 63707 66010 47101 81942 95559 61989 46767 83744',
    '94482 55379 77472 68471 04047 53464 62080 46684 25906 94912',
    '93313 67702 89891 52104 75216 20569 66024 05803 81501 93511',
    '25338 24300 35587 64024 74964 73263 91419 92726 04269 92279',
    '67823 54781 63600 93417 21641 21992 45863 15030 28618 29745',
    '55706 74983 85054 94588 58692 69956 90927 21079 75093 02955',
    '32116 53449 87202 75596 02364 80665 49911 98818 34797 75356',
    '63698 07426 54252 78625 51818 41757 46728 90977 77279 38000',
    '81647 06001 61452 49192 17321 72147 72350 14144 19735 68548',
    '16136 11573 52552 13347 57418 49468 43852 33239 07394 14333',
    '45477 62416 86251 89835 69485 56209 92192 22184 27255 02542',
    '56887 67179 04946 01653 46680 49886 27232 79178 60857 84383',
    '82796 79766 81454 10095 38837 86360 95068 00642 25125 20511',
    '73929 84896 08412 84886 26945 60424 19652 85022 21066 11863',
    '06744 27862 20391 94945 04712 37137 86960 95636 43719 17287',
    '46776 46575 73962 41389 08658 32645 99581 33904 78027 59009',
    '94657 64078 95126 94683 98352 59570 98258 22620 52248 94077',
    '26719 47826 84826 01476 99090 26401 36394 43745 53050 68203',
    '49625 24517 49399 65143 14298 09190 65925 09372 21696 46151',
    '57098 58387 41059 78859 59772 97549 89301 61753 92846 81382',
    '68683 86894 27741 55991 85592 52459 53959 43104 99725 24680',
    '84598 72736 44695 84865 38367 36222 62609 91246 08051 24388',
    '43904 51244 13654 97627 80797 71569 14359 97700 12961 60894',
    '41694 86855 58484 06353 42207 22258 28488 64815 84560 28506',
    '01684 27394 52267 46767 88952 52138 52254 99546 66727 82398',
    '64565 96116 35488 62305 77456 49803 55936 34568 17432 41125',
    '15076 06947 94510 96596 09402 52288 79710 89314 56691 36867',
    '22874 89405 60101 50330 86179 28680 92087 47609 17824 93858',
    '90097 14909 67598 52613 65549 78189 31297 84821 68299 89487',
    '22658 80485 75640 14270 47755 51323 79641 45152 37462 34364',
    '54285 84447 95265 86782 10511 41354 73573 95231 13427 16610',
    '21359 69536 23144 29524 84937 18711 01457 65403 59027 99344',
    '03742 00731 05785 39062 19838 74478 08478 48968 33214 45713',
    '86875 19435 06430 21845 31910 48481 00537 06146 80674 91927',
    '81911 97939 95206 14196 63428 75444 06437 45123 71819 21799',
    '98391 01591 95618 14675 14269 12397 48940 90718 64942 31961',
    '56794 52080 95146 55022 52316 03881 93014 20937 62137 85595',
    '66389 37787 08303 90697 92077 34672 21825 62599 66150 14215',
    '03068 03844 77345 49202 60541 46659 25201 49744 28507 32518',
    '66600 21324 34088 19071 04863 31734 64965 14539 05796 26856',
    '10055 08106 65879 69981 63574 73638 40525 71459 10289 70641',
    '40110 97120 62804 39039 75951 56771 57700 42033 78699 36007',
    '23055 87631 76359 42187 31251 47120 53292 81918 26186 12586',
    '73215 79198 41484 88291 64470 60957 52706 95722 09175 67116',
    '72291 09816 90915 28017 35067 12748 58322 28718 35209 35396',
    '57251 21083 57915 13698 82091 44421 00675 10334 67110 31412',
    '67111 36990 86585 16398 31501 97016 51511 68517 14376 57618',
    '35155 65088 49099 89859 98238 73455 28331 63550 76479 18535',
    '89322 61854 89632 13293 30898 57064 20467 52590 70915 48141',
    '65498 59461 63718 02709 81994 30992 44889 57571 28289 05923',
    '23326 09729 97120 84433 57326 54893 82391 19325 97463 66730',
    '58360 41428 13883 03203 82490 37589 85243 74417 02913 27656',
    '18093 77344 40307 07469 21120 19130 20330 38019 76211 01100',
    '44929 32151 60842 44485 96376 69838 95228 68478 31235 52658',
    '21314 49576 85726 24334 41893 03968 64262 43410 77322 69780',
    '28073 18915 44110 10446 82325 27162 01052 65227 21116 60396',
    '66557 30925 47110 55785 37634 66820 65310 98965 26918 62056',
    '47693 12570 58635 66201 85581 00729 36065 98764 86117 91045',
    '33488 50346 11365 76867 53249 44166 80396 26579 78771 85560',
    '84552 96541 26654 08530 61434 44318 58676 97514 56614 06800',
    '70023 78776 59134 40171 27494 70420 56223 05389 94561 31407',
    '11270 00407 85473 32699 39081 45466 46458 80797 27082 66830',
    '63432 85878 56983 05235 80893 30657 57406 79545 71637 75254',
    '20211 49557 61581 40025 01262 28594 13021 64715 50979 25923',
    '09907 96547 37612 55176 56751 35751 78296 66454 77917 45011',
    '29961 48903 04639 94713 29621 07340 43751 89573 59614 58901',
    '93897 13111 79042 97828 56475 03203 19869 15140 28708 08599',
    '04801 09412 14722 13179 47647 77262 24142 54854 54033 21571',
    '85306 14228 81375 85043 06332 17518 29798 66223 71721 59160',
    '77166 92547 48738 98665 49494 50114 65406 28433 66393 79003',
    '97692 65672 14638 53067 36096 57120 91807 63832 71664 16274',
    '88880 07869 25602 90228 47210 40317 21186 08204 19000 42296',
    '61711 96377 92133 75751 14959 50156 60496 31862 94726 54736',
    '42523 08177 03675 15906 73502 35072 83540 56704 03867 43513',
    '62222 47715 89150 49530 98444 89333 09634 08780 76932 59939',
    '78054 19341 44737 74418 42631 29860 80998 88687 41326 04721']))
# Type Data Line
inputing = ''
i = 2
breaking = 0

# Fundamental Codes Programming Line
def FCPL():
    global inputing, i, breaking
    print('''
{0}
{1}

3.''' . format('=' * 50, '원주율을 3.을 제외하고 입력하시오'))
    while breaking == 0:
        inputing = input()
        if inputing == pi()[i]:
            i += 1
            if pi()[i] == ' ':
                i += 1
        else:
            print('''
소수 {0}번째자리 숫자는 {1}가 아닌 {2}입니다!!
{3}''' .format(str(i - 1), inputing, pi()[i], '=' * 50))
            breaking = 1

# Pyautogui Codes Programming Line
def PCPL():
    global breaking
    while breaking == 0:
        if click('1') or click('2') or click('3') or click('4') or click('5') or click('6') or click('7') or click('8') or click('9') or click('0'):
            while True:
                if not click('1') and not click('2') and not click('3') and not click('4') and not click('5') and not click('6') and not click('7') and not click('8') and not click('9') and not click('0'):
                    break
            pyautogui.press('enter')
    while True:
        pass

threading.Thread(target=FCPL).start()
threading.Thread(target=PCPL).start()