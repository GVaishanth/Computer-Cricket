#COMPUTER CRICKET
import random as r
import time as t
def toss():
    c=input("HEADS OR TAILS : ").upper()
    toss_options=["HEADS","TAILS"]
    a=r.choice(toss_options)
    t.sleep(0.2)
    print("'TOSS IN THROWN UP IN THE AIR'")
    t.sleep(1)
    t.sleep(0.2)
    print("'AND THE OUTCOME IS",a,".'")
    t.sleep(1)
    if c==a or (a.startswith('H') and c.startswith('H')) or (a.startswith('T') and c.startswith('T')):
        print("YOU WON THE TOSS🥳")
        n=0
        while True:
            b=input("BAT OR BOWL : ").upper()
            if n==0 and b!="BAT" and b!="BOWL":
                print("WRONG INPUT😠, TRY AGAIN")
                n+=1
            elif n==1 and b!="BAT" and b!="BOWL":
                print("WRONG INPUT😡, TRY AGAIN")
                n+=1
            elif n==2 and b!="BAT" and b!="BOWL":
                print("🤬,THIS IS YOUR LAST CHANCE TYPE BAT OR BOWL.")
                n+=1
            elif n==3 and b!="BAT" and b!="BOWL":
                game=['BAT','BOWL']
                b=r.choice(game)
                print("YOU ARE GOING TO",b,"😈 ENJOY")
                return b
            elif b=="BAT" or b=="BOWL":
                return b
    else:
        print("YOU LOST THE TOSS😑")
        game=['BAT','BOWL']
        b=r.choice(game)
        if lucky=="ALL" or lucky=='':
            if b=='BAT':
                print("COMPUTER CHOSE TO BAT, YOU ARE GOING TO BOWL")
            else:
                print("COMPUTER CHOSE TO BOWL, YOU ARE GOING TO BAT")
            if b=='BAT':
                return 'BOWL'
            else:
                return 'BAT'
        elif lucky=="BAT":
            b="BAT"
            print("COMPUTER CHOSE TO BOWL, YOU ARE GOING TO BAT")
            return b
        elif lucky=="BALL":
            b="BOWL"
            print("COMPUTER CHOSE TO BAT, YOU ARE GOING TO BOWL")
            return b
def luck():
    print("THIS IS TO CHECK WHICH KIND OF PLAYER[BATSMAN|BOWLER|ALL-ROUNDER] YOU ARE TODAY\n\
    (THIS IS NOT COMPULSORY IF YOU WANT TO SKIP, YOU CAN BY TYPING SKIP ELSE PRESS ENTER)\n")
    print("TYPE HERE : ",end='')
    q=input().upper()
    global lucky
    if q=="SKIP":
        lucky=''
        return
    else:
        print("NOTE : THIS WILL HELP YOU WHEN YOU LOSE THE TOSS.\n")
        print("[BASICALLY LETS YOU BOWL IF YOU ARE A BOWLER, LETS YOU BAT IF YOU ARE A BATSMAN.]")
        print("(IF YOU ARE AN ALL-ROUNDER THEN YOU WILL KNOW)\n")
        sa=di=ps=0
        print("TYPE 10 NUMBERS WHICHEVER COMES TO YOUR MIND")
        for i in range(10):
            print("ENTER NUMBER",i+1,' : ',end='')
            ra=input()
            if ra.isnumeric():
                ra=int(ra)
                if ra>10:
                    ra=10
                    print(ra)
                elif ra<1:
                    ra=1
                    print(ra)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                ra=r.choice(bowl)
                print(ra)
            c=r.choice(bowl)
            print("RANDOM NUMBER ENTERED BY COMPUTER :",c)
            if ra==c:
                sa+=1
            elif (ra-1)==c or (ra+1)==c or (c-1)==0 or (c+1)==0:
                ps+=1
            else:
                di+=1
        if (sa>=1 or ps>=3) and di<=3:
            print("YOU ARE A BOWLER AND YOU ARE GOOD IN PREDICTIONS.")
            lucky="BALL"
        elif (sa<=1 or ps<=1) and di>=5:
            print("YOU ARE A BATSMAN AND YOU ARE LUCKY.")
            lucky="BAT"
        else:
            print("YOU ARE AN ALL-ROUNDER AND KEEP IT UP.")
            lucky="ALL"
def tie():
    print("THINKING...")
    flag=r.choice(l)
    print("YOU ARE GOING TO PLAY",flag)
    choose(flag)
def choose(mode2):
    if mode2=="NORMAL":
        tn=toss()
        normal(tn)
    elif mode2=="CRAZY":
        tc=toss()
        crazy(tc)
    elif mode2=="INSANE":
        ti=toss()
        insane(ti)
    elif mode2=="MAD":
        tm=toss()
        mad(tm)
    elif mode2=="NOWAY":
        tw=toss()
        noway(tw)
    elif mode2=="B10":
        tb=toss()
        b10(tb)
    elif mode2=="TEST":
        tt=toss()
        test(tt)
def normal(v):
    if v=="BAT":
        print("START BATTING")
        bon=ton=0
        ban=''
        while True:
            ban=input()
            if ban.isnumeric():
                ban=int(ban)
                if ban>10:
                    ban=10
                    print(ban)
                elif ban<1:
                    ban=1
                    print(ban)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                ban=r.choice(bowl)
                print(ban)
            bon=r.choice(bowl)
            print(bon)
            if ban!=bon:
                ton+=ban
                print("CURRENT SCORE:",ton)
            else:
                print("TOTAL SCORE:",ton)
                print("'😮OUT😮'\nYOU HAVE DEFEND",ton+1,"RUN/RUNS.")
                break
        cn=ton
        print("\nSTART BOWLING")
        ban=ton=0
        bon=''
        while True:
            bon=input()
            if bon.isnumeric():
                bon=int(bon)
                if bon>10:
                    bon=10
                    print(bon)
                elif bon<1:
                    bon=1
                    print(bon)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                bon=r.choice(bowl)
                print(bon)
            ban=r.choice(bowl)
            print(ban)
            if ban!=bon:
                ton+=ban
                print("CURRENT SCORE:",ton)
            elif ban==bon:
                if ton==cn:
                    print("'😮OUT😮'")
                    print("TOTAL SCORE BY COMPUTER :",ton)
                    print("TOTAL SCORE BY YOU :",cn)
                    print("WELL THAT'S FANTASTIC(WTF), IT'S A TIE")
                    tie()
                    break
                else:
                    print("'😮OUT😮'")
                    print("TOTAL SCORE BY COMPUTER :",ton)
                    print("TOTAL SCORE BY YOU :",cn)
                    print("GG🥳, YOU WON BY",cn-ton,"RUNS.")   
                    break
            if ton>cn:
                    print("TOTAL SCORE BY COMPUTER :",ton)
                    print("TOTAL SCORE BY YOU :",cn)
                    print("WASTE, YOU LOST BY",ton-cn,"RUNS.")
                    break
    else:
        print("START BOWLING")
        ban=ton=0
        bon=''
        while True:
            bon=input()
            if bon.isnumeric():
                bon=int(bon)
                if bon>10:
                    bon=10
                    print(bon)
                elif bon<1:
                    bon=1
                    print(bon)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                bon=r.choice(bowl)
                print(bon)
            ban=r.choice(bowl)
            print(ban)
            if ban!=bon:
                ton+=ban
                print("CURRENT SCORE:",ton)  
            else:
                print("TOTAL SCORE:",ton)
                print("'😮OUT😮'\nYOU HAVE TO SCORE",ton+1,"RUN/RUNS TO WIN")
                break    
        cn=ton
        print("\nSTART BATTING")
        bon=ton=0
        ban=''
        while True:
            ban=input()
            if ban.isnumeric():
                ban=int(ban)
                if ban>10:
                    ban=10
                    print(ban)
                elif ban<1:
                    ban=1
                    print(ban)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                ban=r.choice(bowl)
                print(ban)
            bon=r.choice(bowl)
            print(bon)
            if ban!=bon:
                ton+=ban
                print("CURRENT SCORE:",ton)
            elif ban==bon:
                if ton==cn:
                    print("'😮OUT😮'")
                    print("TOTAL SCORE BY COMPUTER :",cn)
                    print("TOTAL SCORE BY YOU :",ton)
                    print("WELL THAT'S FANTASTIC(WTF), IT'S A TIE")
                    tie()
                    break
                else:
                    print("'😮OUT😮'")
                    print("TOTAL SCORE BY COMPUTER :",cn)
                    print("TOTAL SCORE BY YOU :",ton)
                    print("WASTE, YOU LOST BY",cn-ton,"RUNS.")   
                    break  
            if ton>cn:
                    print("TOTAL SCORE BY COMPUTER :",cn)
                    print("TOTAL SCORE BY YOU :",ton)
                    print("GG🥳, YOU WON BY",ton-cn,"RUNS.")
                    break    
def crazy(v):
    if v=="BAT":
        print("START BATTING")
        bon=ton=0
        ban=''
        while True:
            ban=input()
            if ban.isnumeric():
                ban=int(ban)
                if ban>10:
                    ban=10
                    print(ban)
                elif ban<1:
                    ban=1
                    print(ban)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                ban=r.choice(bowl)
                print(ban)
            bon=r.choice(bowl)
            print(bon)
            if ban!=bon:
                if (bon+1)==ban or (bon-1)==ban:
                    print("TOTAL SCORE:",ton)
                    print("'😮OUT😮'\nYOU HAVE DEFEND",ton+1,"RUN/RUNS.")   
                    break
                else:
                    ton+=ban
                print("CURRENT SCORE:",ton)
            else:
                ton+=ban**2
                print("WOW",ban**2)
                print("CURRENT SCORE:",ton)
        cn=ton
        print("\nSTART BOWLING")
        ban=ton=0
        bon=''
        while True:
            bon=input()
            if bon.isnumeric():
                bon=int(bon)
                if bon>10:
                    bon=10
                    print(bon)
                elif bon<1:
                    bon=1
                    print(bon)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                bon=r.choice(bowl)
                print(bon)
            ban=r.choice(bowl)
            print(ban)
            if ban!=bon:
                if (bon+1)==ban or (bon-1)==ban:
                    if ton==cn:
                        print("'😮OUT😮'")
                        print("TOTAL SCORE BY COMPUTER :",ton)
                        print("TOTAL SCORE BY YOU :",cn)
                        print("WELL THAT'S FANTASTIC(WTF), IT'S A TIE")
                        tie()
                        break
                    else:
                        print("'😮OUT😮'")
                        print("TOTAL SCORE BY COMPUTER :",ton)
                        print("TOTAL SCORE BY YOU :",cn)
                        print("GG🥳, YOU WON BY",cn-ton,"RUNS.")   
                        break
                else:
                    ton+=ban
                    print("CURRENT SCORE:",ton)
            else:
                ton+=ban**2
                print("WOW",ban**2)
                print("CURRENT SCORE:",ton)
            if ton>cn:
                    print("TOTAL SCORE BY COMPUTER :",ton)
                    print("TOTAL SCORE BY YOU :",cn)
                    print("WASTE, YOU LOST BY",ton-cn,"RUNS.")
                    break
    else:
        print("START BOWLING")
        ban=ton=0
        bon=''
        while True:
            bon=input()
            if bon.isnumeric():
                bon=int(bon)
                if bon>10:
                    bon=10
                    print(bon)
                elif bon<1:
                    bon=1
                    print(bon)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                bon=r.choice(bowl)
                print(bon)
            ban=r.choice(bowl)
            print(ban)
            if ban!=bon:
                if (bon+1)==ban or (bon-1)==ban:
                    print("TOTAL SCORE:",ton)
                    print("'😮OUT😮'\nYOU HAVE TO SCORE",ton+1,"RUN/RUNS TO WIN")
                    break
                else:
                    ton+=ban
                    print("CURRENT SCORE:",ton)  
            else:
                ton+=ban**2 
                print("WOW",ban**2)
                print("CURRENT SCORE:",ton)
        cn=ton
        print("\nSTART BATTING")
        bon=ton=0
        ban=''
        while True:
            ban=input()
            if ban.isnumeric():
                ban=int(ban)
                if ban>10:
                    ban=10
                    print(ban)
                elif ban<1:
                    ban=1
                    print(ban)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                ban=r.choice(bowl)
                print(ban)
            bon=r.choice(bowl)
            print(bon)
            if ban!=bon:
                if (bon+1)==ban or (bon-1)==ban:
                    if ton==cn:
                        print("'😮OUT😮'")
                        print("TOTAL SCORE BY COMPUTER :",cn)
                        print("TOTAL SCORE BY YOU :",ton)
                        print("WELL THAT'S FANTASTIC(WTF), IT'S A TIE")
                        tie()
                        break
                    else:
                        print("'😮OUT😮'")
                        print("TOTAL SCORE BY COMPUTER :",cn)
                        print("TOTAL SCORE BY YOU :",ton)
                        print("WASTE, YOU LOST BY",cn-ton,"RUNS.")   
                        break
                else:
                    ton+=ban
                    print("CURRENT SCORE:",ton)
            else:
                ton+=ban**2
                print("WOW",ban**2)
                print("CURRENT SCORE:",ton)
            if ton>cn:
                    print("TOTAL SCORE BY COMPUTER :",cn)
                    print("TOTAL SCORE BY YOU :",ton)
                    print("GG🥳, YOU WON BY",ton-cn,"RUNS.")
                    break
def insane(v):
    if v=="BAT":
        print("START BATTING")
        bon=ton=0
        ban=''
        while True:
            ban=input()
            if ban.isnumeric():
                ban=int(ban)
                if ban>10:
                    ban=10
                    print(ban)
                elif ban<1:
                    ban=1
                    print(ban)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                ban=r.choice(bowl)
                print(ban)
            bon=r.choice(bowl)
            print(bon)
            if ban!=bon:
                if (bon+1)==ban or (bon-1)==ban:
                    ton+=(ban*bon)
                    print("WOW",ban*bon)
                    print("CURRENT SCORE:",ton)
                else:
                    ton+=ban
                    print("CURRENT SCORE:",ton)
            else:
                print("TOTAL SCORE:",ton)
                print("'😮OUT😮'\nYOU HAVE DEFEND",ton+1,"RUN/RUNS.")   
                break
        cn=ton
        print("\nSTART BOWLING")
        ban=ton=0
        bon=''
        while True:
            bon=input()
            if bon.isnumeric():
                bon=int(bon)
                if bon>10:
                    bon=10
                    print(bon)
                elif bon<1:
                    bon=1
                    print(bon)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                bon=r.choice(bowl)
                print(bon)
            ban=r.choice(bowl)
            print(ban)
            if ban!=bon:
                if (bon+1)==ban or (bon-1)==ban:
                    ton+=(ban*bon)
                    print("WOW",ban*bon)
                    print("CURRENT SCORE:",ton)
                else:
                    ton+=ban
                    print("CURRENT SCORE:",ton)
            else:
                if ton==cn:
                    print("'😮OUT😮'")
                    print("TOTAL SCORE BY COMPUTER :",ton)
                    print("TOTAL SCORE BY YOU :",cn)
                    print("WELL THAT'S FANTASTIC(WTF), IT'S A TIE")
                    tie()
                    break
                else:
                    print("'😮OUT😮'")
                    print("TOTAL SCORE BY COMPUTER :",ton)
                    print("TOTAL SCORE BY YOU :",cn)
                    print("GG🥳, YOU WON BY",cn-ton,"RUNS.")   
                    break
            if ton>cn:
                print("TOTAL SCORE BY COMPUTER :",ton)
                print("TOTAL SCORE BY YOU :",cn)
                print("WASTE, YOU LOST BY",ton-cn,"RUNS.")
                break
    else:
        print("START BOWLING")
        ban=ton=0
        bon=''
        while True:
            bon=input()
            if bon.isnumeric():
                bon=int(bon)
                if bon>10:
                    bon=10
                    print(bon)
                elif bon<1:
                    bon=1
                    print(bon)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                bon=r.choice(bowl)
                print(bon)
            ban=r.choice(bowl)
            print(ban)
            if ban!=bon:
                if (bon+1)==ban or (bon-1)==ban:
                    ton+=(ban*bon)
                    print("WOW",ban*bon)
                    print("CURRENT SCORE:",ton)
                else:
                    ton+=ban
                    print("CURRENT SCORE:",ton)  
            else:
                print("TOTAL SCORE:",ton)
                print("'😮OUT😮'\nYOU HAVE TO SCORE",ton+1,"RUN/RUNS TO WIN")
                break
        cn=ton
        print("\nSTART BATTING")
        bon=ton=0
        ban=''
        while True:
            ban=input()
            if ban.isnumeric():
                ban=int(ban)
                if ban>10:
                    ban=10
                    print(ban)
                elif ban<1:
                    ban=1
                    print(ban)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                ban=r.choice(bowl)
                print(ban)
            bon=r.choice(bowl)
            print(bon)
            if ban!=bon:
                if (bon+1)==ban or (bon-1)==ban:
                    ton+=(ban*bon)
                    print("WOW",ban*bon)
                    print("CURRENT SCORE:",ton)
                else:
                    ton+=ban
                    print("CURRENT SCORE:",ton)
            else:
                if ton==cn:
                    print("'😮OUT😮'")
                    print("TOTAL SCORE BY COMPUTER :",cn)
                    print("TOTAL SCORE BY YOU :",ton)
                    print("WELL THAT'S FANTASTIC(WTF), IT'S A TIE")
                    tie()
                    break
                else:
                    print("'😮OUT😮'")
                    print("TOTAL SCORE BY COMPUTER :",cn)
                    print("TOTAL SCORE BY YOU :",ton)
                    print("WASTE, YOU LOST BY",cn-ton,"RUNS.")   
                    break
            if ton>cn:
                    print("TOTAL SCORE BY COMPUTER :",cn)
                    print("TOTAL SCORE BY YOU :",ton)
                    print("GG🥳, YOU WON BY",ton-cn,"RUNS.")
                    break
def mad(v):
    if v=="BAT":
        print("START BATTING")
        bon=ton=0
        ban=''
        while True:
            ban=input()
            if ban.isnumeric():
                ban=int(ban)
                if ban>10:
                    ban=10
                    print(ban)
                elif ban<1:
                    ban=1
                    print(ban)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                ban=r.choice(bowl)
                print(ban)
            bon=r.choice(bowl)
            print(bon)
            if ban!=bon:
                if (bon+1)==ban or (bon-1)==ban:
                    print("TOTAL SCORE:",ton)
                    print("'😮OUT😮'\nYOU HAVE DEFEND",ton+1,"RUN/RUNS.")   
                    break
                else:
                    ton+=(ban*bon)
                    print("CURRENT SCORE:",ton)
            else:
                ton+=(2*ban)
                print("CURRENT SCORE:",ton)
        cn=ton
        print("\nSTART BOWLING")
        ban=ton=0
        bon=''
        while True:
            bon=input()
            if bon.isnumeric():
                bon=int(bon)
                if bon>10:
                    bon=10
                    print(bon)
                elif bon<1:
                    bon=1
                    print(bon)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                bon=r.choice(bowl)
                print(bon)
            ban=r.choice(bowl)
            print(ban)
            if ban!=bon:
                if (bon+1)==ban or (bon-1)==ban:
                    if ton==cn:
                        print("'😮OUT😮'")
                        print("TOTAL SCORE BY COMPUTER :",ton)
                        print("TOTAL SCORE BY YOU :",cn)
                        print("WELL THAT'S FANTASTIC(WTF), IT'S A TIE")
                        tie()
                        break
                    else:
                        print("'😮OUT😮'")
                        print("TOTAL SCORE BY COMPUTER :",ton)
                        print("TOTAL SCORE BY YOU :",cn)
                        print("GG🥳, YOU WON BY",cn-ton,"RUNS.")   
                        break
                else:
                    ton+=(ban*bon)
                    print("CURRENT SCORE:",ton)
            else:
                ton+=(ban*2)
                print("CURRENT SCORE:",ton)
            if ton>cn:
                    print("TOTAL SCORE BY COMPUTER :",ton)
                    print("TOTAL SCORE BY YOU :",cn)
                    print("WASTE, YOU LOST BY",ton-cn,"RUNS.")
                    break
    else:
        print("START BOWLING")
        ban=ton=0
        bon=''
        while True:
            bon=input()
            if bon.isnumeric():
                bon=int(bon)
                if bon>10:
                    bon=10
                    print(bon)
                elif bon<1:
                    bon=1
                    print(bon)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                bon=r.choice(bowl)
                print(bon)
            ban=r.choice(bowl)
            print(ban)
            if ban!=bon:
                if (bon+1)==ban or (bon-1)==ban:
                    print("TOTAL SCORE:",ton)
                    print("'😮OUT😮'\nYOU HAVE TO SCORE",ton+1,"RUN/RUNS TO WIN")
                    break
                else:
                    ton+=(ban*bon)
                    print("CURRENT SCORE:",ton)  
            else:
                ton+=(ban*2)
                print("CURRENT SCORE:",ton)
        cn=ton
        print("\nSTART BATTING")
        bon=ton=0
        ban=''
        while True:
            ban=input()
            if ban.isnumeric():
                ban=int(ban)
                if ban>10:
                    ban=10
                    print(ban)
                elif ban<1:
                    ban=1
                    print(ban)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                ban=r.choice(bowl)
                print(ban)
            bon=r.choice(bowl)
            print(bon)
            if ban!=bon:
                if (bon+1)==ban or (bon-1)==ban:
                    if ton==cn:
                        print("'😮OUT😮'")
                        print("TOTAL SCORE BY COMPUTER :",cn)
                        print("TOTAL SCORE BY YOU :",ton)
                        print("WELL THAT'S FANTASTIC(WTF), IT'S A TIE")
                        tie()
                        break
                    else:
                        print("'😮OUT😮'")
                        print("TOTAL SCORE BY COMPUTER :",cn)
                        print("TOTAL SCORE BY YOU :",ton)
                        print("WASTE, YOU LOST BY",cn-ton,"RUNS.")   
                        break
                else:
                    ton+=(ban*bon)
                    print("CURRENT SCORE:",ton)
            else:
                ton+=(ban*2)
                print("CURRENT SCORE:",ton)
            if ton>cn:
                    print("TOTAL SCORE BY COMPUTER :",cn)
                    print("TOTAL SCORE BY YOU :",ton)
                    print("GG🥳, YOU WON BY",ton-cn,"RUNS.")
                    break
def noway(v):
    if v=="BAT":
        print("START BATTING")
        bon=ton=0
        ban=''
        while True:
            ban=input()
            if ban.isnumeric():
                ban=int(ban)
                if ban>10:
                    ban=10
                    print(ban)
                elif ban<1:
                    ban=1
                    print(ban)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                ban=r.choice(bowl)
                print(ban)
            bon=r.choice(bowl)
            print(bon)
            if ban!=bon:
                if (bon+1)==ban or (bon-1)==ban:
                    ton+=(ban+bon)
                    print("CURRENT SCORE:",ton)
                else:
                    print("TOTAL SCORE:",ton)
                    print("'😮OUT😮'\nYOU HAVE DEFEND",ton+1,"RUN/RUNS.")   
                    break
            else:
                ton+=(ban**2)
                print("CURRENT SCORE:",ton)
        cn=ton
        print("\nSTART BOWLING")
        ban=ton=0
        bon=''
        while True:
            bon=input()
            if bon.isnumeric():
                bon=int(bon)
                if bon>10:
                    bon=10
                    print(bon)
                elif bon<1:
                    bon=1
                    print(bon)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                bon=r.choice(bowl)
                print(bon)
            ban=r.choice(bowl)
            print(ban)
            if ban!=bon:
                if (bon+1)==ban or (bon-1)==ban:
                    ton+=(ban+bon)
                    print("CURRENT SCORE:",ton)
                else:
                    if ton==cn:
                        print("'😮OUT😮'")
                        print("TOTAL SCORE BY COMPUTER :",ton)
                        print("TOTAL SCORE BY YOU :",cn)
                        print("WELL THAT'S FANTASTIC(WTF), IT'S A TIE")
                        tie()
                        break
                    else:
                        print("'😮OUT😮'")
                        print("TOTAL SCORE BY COMPUTER :",ton)
                        print("TOTAL SCORE BY YOU :",cn)
                        print("GG🥳, YOU WON BY",cn-ton,"RUNS.")   
                        break
            else:
                ton+=(ban**2)
                print("CURRENT SCORE:",ton)
            if ton>cn:
                    print("TOTAL SCORE BY COMPUTER :",ton)
                    print("TOTAL SCORE BY YOU :",cn)
                    print("WASTE, YOU LOST BY",ton-cn,"RUNS.")
                    break
    else:
        print("START BOWLING")
        ban=ton=0
        bon=''
        while True:
            bon=input()
            if bon.isnumeric():
                bon=int(bon)
                if bon>10:
                    bon=10
                    print(bon)
                elif bon<1:
                    bon=1
                    print(bon)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                bon=r.choice(bowl)
                print(bon)
            ban=r.choice(bowl)
            print(ban)
            if ban!=bon:
                if (bon+1)==ban or (bon-1)==ban:
                    ton+=(ban+bon)
                    print("CURRENT SCORE:",ton)
                else:
                    print("TOTAL SCORE:",ton)
                    print("'😮OUT😮'\nYOU HAVE TO SCORE",ton+1,"RUN/RUNS TO WIN")
                    break 
            else:
                ton+=(ban**2) 
                print("CURRENT SCORE:",ton)
        cn=ton
        print("\nSTART BATTING")
        bon=ton=0
        ban=''
        while True:
            ban=input()
            if ban.isnumeric():
                ban=int(ban)
                if ban>10:
                    ban=10
                    print(ban)
                elif ban<1:
                    ban=1
                    print(ban)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                ban=r.choice(bowl)
                print(ban)
            bon=r.choice(bowl)
            print(bon)
            if ban!=bon:
                if (bon+1)==ban or (bon-1)==ban:
                    ton+=(ban+bon)
                    print("CURRENT SCORE:",ton)
                else:
                    if ton==cn:
                        print("'😮OUT😮'")
                        print("TOTAL SCORE BY COMPUTER :",cn)
                        print("TOTAL SCORE BY YOU :",ton)
                        print("WELL THAT'S FANTASTIC(WTF), IT'S A TIE")
                        tie()
                        break
                    else:
                        print("'😮OUT😮'")
                        print("TOTAL SCORE BY COMPUTER :",cn)
                        print("TOTAL SCORE BY YOU :",ton)
                        print("WASTE, YOU LOST BY",cn-ton,"RUNS.")   
                        break
            else:
                ton+=(ban**2)
                print("CURRENT SCORE:",ton)
            if ton>cn:
                    print("TOTAL SCORE BY COMPUTER :",cn)
                    print("TOTAL SCORE BY YOU :",ton)
                    print("GG🥳, YOU WON BY",ton-cn,"RUNS.")
                    break
def b10(v):
    if v=="BAT":
        print("START BATTING")
        bon=ton=0
        ban=''
        balls=0
        while balls<10:
            ban=input()
            if ban.isnumeric():
                ban=int(ban)
                if ban>10:
                    ban=10
                    print(ban)
                elif ban<7:
                    ban=7
                    print(ban)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                ban=r.choice(bowlb)
                print(ban)
            bon=r.choice(bowlb)
            print(bon)
            balls+=1
            if ban!=bon:
                ton+=ban
                print("CURRENT SCORE:",ton,"| BALLS LEFT:",(10-balls))
            else:
                print("TOTAL SCORE:",ton)
                print("'😮OUT😮'\nYOU HAVE DEFEND",ton+1,"RUN/RUNS.")
                break
        else:
            print("10 BALLS DONE! TOTAL SCORE:",ton)
            print("YOU HAVE DEFEND",ton+1,"RUN/RUNS.")
        cn=ton
        print("\nSTART BOWLING")
        ban=ton=0
        bon=''
        balls=0
        while balls<10:
            bon=input()
            if bon.isnumeric():
                bon=int(bon)
                if bon>10:
                    bon=10
                    print(bon)
                elif bon<7:
                    bon=7
                    print(bon)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                bon=r.choice(bowlb)
                print(bon)
            ban=r.choice(bowlb)
            print(ban)
            balls+=1
            if ban!=bon:
                ton+=ban
                print("CURRENT SCORE:",ton,"| BALLS LEFT:",(10-balls))
            elif ban==bon:
                if ton==cn:
                    print("'😮OUT😮'")
                    print("TOTAL SCORE BY COMPUTER :",ton)
                    print("TOTAL SCORE BY YOU :",cn)
                    print("WELL THAT'S FANTASTIC(WTF), IT'S A TIE")
                    tie()
                    break
                else:
                    print("'😮OUT😮'")
                    print("TOTAL SCORE BY COMPUTER :",ton)
                    print("TOTAL SCORE BY YOU :",cn)
                    print("GG🥳, YOU WON BY",cn-ton,"RUNS.")   
                    break
            if ton>cn:
                    print("TOTAL SCORE BY COMPUTER :",ton)
                    print("TOTAL SCORE BY YOU :",cn)
                    print("WASTE, YOU LOST BY",ton-cn,"RUNS.")
                    break
        else:
            print("10 BALLS DONE!")
            print("TOTAL SCORE BY COMPUTER :",ton)
            print("TOTAL SCORE BY YOU :",cn)
            if ton>cn:
                print("WASTE, YOU LOST BY",ton-cn,"RUNS.")
            elif ton==cn:
                print("WELL THAT'S FANTASTIC(WTF), IT'S A TIE")
                tie()
            else:
                print("GG🥳, YOU WON BY",cn-ton,"RUNS.")
    else:
        print("START BOWLING")
        ban=ton=0
        bon=''
        balls=0
        while balls<10:
            bon=input()
            if bon.isnumeric():
                bon=int(bon)
                if bon>10:
                    bon=10
                    print(bon)
                elif bon<7:
                    bon=7
                    print(bon)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                bon=r.choice(bowlb)
                print(bon)
            ban=r.choice(bowlb)
            print(ban)
            balls+=1
            if ban!=bon:
                ton+=ban
                print("CURRENT SCORE:",ton,"| BALLS LEFT:",(10-balls))
            else:
                print("TOTAL SCORE:",ton)
                print("'😮OUT😮'\nYOU HAVE TO SCORE",ton+1,"RUN/RUNS TO WIN")
                break    
        else:
            print("10 BALLS DONE! TOTAL SCORE:",ton)
            print("YOU HAVE TO SCORE",ton+1,"RUN/RUNS TO WIN.")
        cn=ton
        print("\nSTART BATTING")
        bon=ton=0
        ban=''
        balls=0
        while balls<10:
            ban=input()
            if ban.isnumeric():
                ban=int(ban)
                if ban>10:
                    ban=10
                    print(ban)
                elif ban<7:
                    ban=7
                    print(ban)
            else:
                print("ENTERED VALUE IS NOT A NUMBER. SO CHOOSING A RANDOM NUMBER.")
                ban=r.choice(bowlb)
                print(ban)
            bon=r.choice(bowlb)
            print(bon)
            balls+=1
            if ban!=bon:
                ton+=ban
                print("CURRENT SCORE:",ton,"| BALLS LEFT:",(10-balls))
            elif ban==bon:
                if ton==cn:
                    print("'😮OUT😮'")
                    print("TOTAL SCORE BY COMPUTER :",cn)
                    print("TOTAL SCORE BY YOU :",ton)
                    print("WELL THAT'S FANTASTIC(WTF), IT'S A TIE")
                    tie()
                    break
                else:
                    print("'😮OUT😮'")
                    print("TOTAL SCORE BY COMPUTER :",cn)
                    print("TOTAL SCORE BY YOU :",ton)
                    print("WASTE, YOU LOST BY",cn-ton,"RUNS.")   
                    break 
            if ton>cn:
                    print("TOTAL SCORE BY COMPUTER :",cn)
                    print("TOTAL SCORE BY YOU :",ton)
                    print("GG🥳, YOU WON BY",ton-cn,"RUNS.")
                    break
        else:
            print("10 BALLS DONE!")
            print("TOTAL SCORE BY COMPUTER :",cn)
            print("TOTAL SCORE BY YOU :",ton)
            if ton>cn:
                print("GG🥳, YOU WON BY",ton-cn,"RUNS.")
            elif ton==cn:
                print("WELL THAT'S FANTASTIC(WTF), IT'S A TIE")
                tie()
            else:
                print("WASTE, YOU LOST BY",cn-ton,"RUNS.")
def test(v):
    print("SORRY CURRENTLY WORKING ON IT, WILL BE AVAILABLE IN 1 WEEK.")
#main block
l=["NORMAL","CRAZY","INSANE","MAD","NOWAY","B10","TEST"]
bowl=[1,2,3,4,5,6,7,8,9,10]
bowlb=[7,8,9,10]
bowlt=[1,2,3,4,5,6]
print("RULES:\nYOU CAN ENTER ANY NUMBER IN THIS LIST",bowl,".\nANY ENTERED NUMBER IS GREATER THAN 10,\
THEN THAT WILL BE TAKEN AS 10.\nANY ENTERED NUMBER IS LESS THAN 1,THEN THAT NUMBER WILL BE TAKEN AS 1\n\
ANY VALUE OTHER THAN NUMBER WILL BE REPLACED BY A RANDOM NUMBER\n\
ONLY 6 NUMBERS FOR TEST MATCH AND ONLY 4 NUMBERS FOR B10\n\
ALL TIE-BREAKERS WILL BE A RANDOM MATCH \n")
print("GAME MODES:\nNORMAL - JUST BASIC MATH AND SAME NUMBER==OUT\n\
CRAZY - SAME NUMBER==MULTIPLY, PRECEDING OR SUCCEEDING NUMBER==OUT\n\
INSANE - SAME NUMBER==OUT, PRECEDING OR SUCCEEDING NUMBER==MULTIPLY\n\
MAD - SAME NUMBER==ADD, PRECEDING OR SUCCEEDING NUMBER==OUT AND ANY OTHER NUMBER==MULTIPLY\n\
NOWAY - SAME NUMBER==MULTIPLY, PRECEDING OR SUCCEEDING NUMBER==ADD AND ANY OTHER NUMBER==OUT\n\
B10 - [7,8,9,10] ARE THE ONLY NUMBERS ALLOWED, SAME NUMBER==OUT AND ONLY 10 BALLS MATCH\n\
TEST(YET TO BE ADDED) - [1,2,3,4,5,6] ARE THE ONLY NUMBERS ALLOWED, SAME NUMBER==OUT AND 2 INNINGS MATCH\n")
luck()
print("ENJOY THE GAME😁\n\n")
n1=rand=chan=0
mode1=' '
mode=flag=''
while True:
    if mode!=mode1 and rand==0 and chan==0:
        mode=input("ENTER THE GAME MODE[NORMAL|CRAZY|INSANE|MAD|NOWAY|B10|TEST|QUIT] : ").upper()
    else:
        mode=mode1
    if mode=="NORMAL":
        tn=toss()
        normal(tn)
        con=input("[CONTINUE|CHANGE|RANDOM(DEFAULT)|QUIT]\n").upper()
        if con=="CONTINUE":
            mode1="NORMAL"
        elif con=="CHANGE":
            mode1=input("ENTER THE GAME MODE WHICH YOU WANT TO PLAY NEXT : ").upper()
            chan=1
        elif con=="QUIT":
            break
        else:
            mode1=r.choice(["CRAZY","INSANE","MAD","NOWAY","B10","TEST"])
            rand=1
            print("YOU ARE GOING TO PLAY",mode1)
    elif mode=="CRAZY":
        tc=toss()
        crazy(tc)
        con=input("[CONTINUE|CHANGE|RANDOM(DEFAULT)|QUIT]\n").upper()
        if con=="CONTINUE":
            mode1="CRAZY"
        elif con=="CHANGE":
            mode1=input("ENTER THE GAME MODE WHICH YOU WANT TO PLAY NEXT : ").upper()
            chan=1
        elif con=="QUIT":
            break
        else:
            mode1=r.choice(["NORMAL","INSANE","MAD","NOWAY","B10","TEST"])
            rand=1
            print("YOU ARE GOING TO PLAY",mode1)
    elif mode=="INSANE":
        ti=toss()
        insane(ti)
        con=input("[CONTINUE|CHANGE|RANDOM(DEFAULT)|QUIT]\n").upper()
        if con=="CONTINUE":
            mode1="INSANE"
        elif con=="CHANGE":
            mode1=input("ENTER THE GAME MODE WHICH YOU WANT TO PLAY NEXT : ").upper()
            chan=1
        elif con=="QUIT":
            break
        else:
            mode1=r.choice(["NORMAL","CRAZY","MAD","NOWAY","B10","TEST"])
            rand=1
            print("YOU ARE GOING TO PLAY",mode1)
    elif mode=="MAD":
        tm=toss()
        mad(tm)
        con=input("[CONTINUE|CHANGE|RANDOM(DEFAULT)|QUIT]\n").upper()
        if con=="CONTINUE":
            mode1="MAD"
        elif con=="CHANGE":
            mode1=input("ENTER THE GAME MODE WHICH YOU WANT TO PLAY NEXT : ").upper()
            chan=1
        elif con=="QUIT":
            break
        else:
            mode1=r.choice(["NORMAL","CRAZY","INSANE","NOWAY","B10","TEST"])
            rand=1
            print("YOU ARE GOING TO PLAY",mode1)
    elif mode=="NOWAY":
        tw=toss()
        noway(tw)
        con=input("[CONTINUE|CHANGE|RANDOM(DEFAULT)|QUIT]\n").upper()
        if con=="CONTINUE":
            mode1="NOWAY"
        elif con=="CHANGE":
            mode1=input("ENTER THE GAME MODE WHICH YOU WANT TO PLAY NEXT : ").upper()
            chan=1
        elif con=="QUIT":
            break
        else:
            mode1=r.choice(["NORMAL","CRAZY","INSANE","MAD","B10","TEST"])
            rand=1
            print("YOU ARE GOING TO PLAY",mode1)
    elif mode=="B10":
        tb=toss()
        b10(tb)
        con=input("[CONTINUE|CHANGE|RANDOM(DEFAULT)|QUIT]\n").upper()
        if con=="CONTINUE":
            mode1="B10"
        elif con=="CHANGE":
            mode1=input("ENTER THE GAME MODE WHICH YOU WANT TO PLAY NEXT : ").upper()
            chan=1
        elif con=="QUIT":
            break
        else:
            mode1=r.choice(["NORMAL","CRAZY","INSANE","MAD","NOWAY","TEST"])
            rand=1
            print("YOU ARE GOING TO PLAY",mode1)
    elif mode=="TEST":
        print("SORRY CURRENTLY WORKING ON THIS")
        con=input("[CHANGE|RANDOM(DEFAULT)|QUIT]\n").upper()
        if con=="CHANGE":
            mode1=input("ENTER THE GAME MODE WHICH YOU WANT TO PLAY NEXT : ").upper()
            chan=1
        elif con=="QUIT":
            break
        else:
            mode1=r.choice(["NORMAL","CRAZY","INSANE","MAD","NOWAY","B10"])
            rand=1
            print("YOU ARE GOING TO PLAY",mode1)
    elif mode=="QUIT":
        print("\nARE YOU SURE THAT YOU WANT TO QUIT THIS GAME(YES/NO)?",end=' ')
        q=input().upper()
        if q=="YES":
            break
        else:
            pass
    elif mode not in l and n1==0:
        print("GAMEMODENOTFOUNDERROR:",mode,",THIS GAME MODE IS NOT THERE IN THE [NORMAL|CRAZY|INSANE|MAD|NOWAY|B10|TEST|QUIT],😠 SO TRY AGAIN.\n")
        n1+=1
        rand=0
        chan=0
    elif mode not in l and n1==1:
        print("GAMEMODENOTFOUNDERROR:",mode,",THIS GAME MODE IS NOT THERE IN THE [NORMAL|CRAZY|INSANE|MAD|NOWAY|B10|TEST|QUIT],😡 SO TRY AGAIN.\n")
        n1+=1
        rand=0
        chan=0
    elif mode not in l and n1==2:
        print("🤬, LOOK YOU IDIOT",mode,",THIS GAME MODE IS NOT THERE IN THE [NORMAL|CRAZY|INSANE|MAD|NOWAY|B10|TEST|QUIT].\n")
        n1+=1
        rand=0
        chan=0
    elif mode not in l and n1==3:
        mode=r.choice(l)
        print("YOU ARE GOING TO PLAY",mode,"😈 ENJOY")
        choose(mode)
        print("NOW PLEASE SELECT A PROPER GAME MODE🙏🙏🙏\n")
