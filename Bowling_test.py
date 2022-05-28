import re

def calcualte_result(score_input):
    if not score_input:
        return 0
    return final_score(check_regex(score_input))

def check_regex(score_input):
    score_list = list(re.sub(r'[^\d/X]', '', score_input))
    return [10 - int(score_list[idx - 1]) if val == '/' else 10 if val == 'X' else int(val) for idx, val in enumerate(score_list)]

def final_score(throws, frame=1, total=0):
    
    if frame > 10 or not throws:
        return total
    elif throws[0] == 10:
        bonus = 0
        if len(throws) >= 3:
            bonus = sum(throws[1:3])
        elif len(throws) > 1:
            bonus = throws[1]
        return final_score(throws[1:], frame + 1, total + 10 + bonus)
    elif sum(throws[0:2]) == 10:
        bonus = 0
        if len(throws) >= 3:
            bonus = throws[2]
        return final_score(throws[2:], frame + 1, total + 10 + bonus)
    else:
        total += sum(throws[0:2])
        return final_score(throws[2:], frame + 1, total)



if __name__ == "__main__":
    """
    Main function which create user inputs 
    """
    user_input = ""
    no_of_frame = 13
    no_of_shots = 3
    no_of_pins_down = 0
    no_of_bonus_shots = 0
    bonus_no_of_pins_down = 0



    for frame in range(1, no_of_frame):
        if frame >  1 and frame <= 10:
            user_input += "-"
        if frame <= 10:
            print(f"Frame {frame}:")
            for shot in range(1,no_of_shots):
                old_no_of_pins_down = no_of_pins_down
                no_of_pins_down = int(input(f"\t shot {shot} (enter number of pins has down):"))
                no_of_pins_down += old_no_of_pins_down
                # print(f"\t shot {shot} (enter number of pins has down):")
                if frame < 10 and shot == 1 and no_of_pins_down == 10:
                    user_input += "X"
                    no_of_pins_down = 0
                    break
                elif frame < 10 and shot == 2 and no_of_pins_down == 10:
                    user_input += "/"
                    no_of_pins_down = 0
                elif frame == 10 and shot == 1 and no_of_pins_down == 10:
                    user_input += "X"
                    no_of_pins_down = 0
                    no_of_bonus_shots = 3
                    break 
                elif frame == 10 and shot == 2 and no_of_pins_down == 10:
                    user_input += "/"
                    no_of_pins_down = 0
                else:
                    no_of_pins_down = no_of_pins_down 
                    user_input += str(no_of_pins_down)

        if frame > 10 and no_of_bonus_shots != 0:
            if frame == 11:
             user_input += "-"
            print(f"Bonus shots {frame -10}:")
            for shot in range(1,no_of_bonus_shots):
                old_bonus_no_of_pins_down = bonus_no_of_pins_down
                bonus_no_of_pins_down = int(input(f"\t (enter number of pins has down):"))
                bonus_no_of_pins_down += old_bonus_no_of_pins_down
                if old_bonus_no_of_pins_down == 0 and bonus_no_of_pins_down == 10 and shot == 1:
                    user_input += "X"
                    bonus_no_of_pins_down = 0
                    break
                elif old_bonus_no_of_pins_down > 1 and bonus_no_of_pins_down == 10 and shot == 1:
                    user_input += "/"
                    break
                else:
                    user_input += str(bonus_no_of_pins_down)
                    bonus_no_of_pins_down = bonus_no_of_pins_down  
                    break
  
        no_of_pins_down = 0        


    # score_input = input("Please enter the input:\n")
    print("Your score is :",calcualte_result(user_input))


