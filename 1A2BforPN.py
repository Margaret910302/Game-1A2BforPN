import random
# 結束、大學、教授、信封、聲調、
digits1 = [  ['ㄍ','ㄨ','ㄟ','ㄐ','ㄩ'], # 規矩 ㄍㄨㄟ ㄐㄩˇ
             ['ㄕ','ㄢ','ㄉ','ㄨ','ㄛ'], # 閃躲 ㄕㄢˇㄉㄨㄛˇ
             ['ㄈ','ㄚ','ㄐ','ㄩ','ㄢ'], # 髮捲 ㄈㄚˇㄐㄩㄢˇ
             ['ㄈ','ㄢ','ㄏ','ㄨ','ㄟ'], # 返回 ㄈㄢˇㄏㄨㄟˊ
             ['ㄐ','ㄧ','ㄠ','ㄅ','ㄢ'], # 攪拌 ㄐㄧㄠˇㄅㄢˋ
             ['ㄐ','ㄧ','ㄠ','ㄅ','ㄨ'], # 腳步 ㄐㄧㄠˇㄅㄨˋ
             ['ㄓ','ㄨ','ㄛ','ㄕ','ㄤ'], # 桌上 ㄓㄨㄛ ㄕㄤˋ
             ['ㄏ','ㄨ','ㄥ','厶','ㄜ'], # 紅色 ㄏㄨㄥˊ厶ㄜˋ
             ['ㄏ','ㄨ','ㄤ','厶','ㄜ'], # 黃色 ㄏㄨㄤˊ厶ㄜˋ
             ['ㄗ','ㄨ','ㄥ','厶','ㄜ'], # 棕色 ㄗㄨㄥ 厶ㄜˋ
             ['ㄆ','ㄛ','厶','ㄨ','ㄟ'], # 破碎 ㄆㄛˋ厶ㄨㄟˋ
             ['ㄕ','ㄡ','ㄅ','ㄧ','ㄠ'], # 手錶 ㄕㄡˇㄅㄧㄠˇ
             ['ㄔ','ㄠ','ㄑ','ㄩ','ㄣ'], # 超群 ㄔㄠ ㄑㄩㄣˊ
             ['ㄏ','ㄠ','ㄐ','ㄧ','ㄝ'], # 豪傑 ㄏㄠ ㄐㄧㄝˊ
             ['厶','ㄡ','ㄒ','ㄩ','ㄣ'], # 搜尋 厶ㄡ ㄒㄩㄣˊ
             ['ㄏ','ㄨ','ㄐ','ㄧ','ㄠ'], # 胡椒 ㄏㄨˊㄐㄧㄠ
             ['ㄌ','ㄧ','ㄤ','ㄩ','ㄢ']  # 良緣 ㄌㄧㄤˊㄩㄢˊ
        ]
digits2 = [ "規矩" ,"閃躲" ,"髮捲" ,"返回" ,"攪拌" ,"腳步" ,"桌上" ,"紅色" ,"黃色" ,"棕色" ,'破碎' ,'手錶' ,'超群' ,'豪傑' ,'搜尋' ,'胡椒' ,'良緣' ]
ansArraySize = len(digits1)
isAnsUse = [ 0 for i in range(ansArraySize)]

def the_game_ans():
    while(1):
        index = random.randint(0, ansArraySize - 1)
        isAnsUse[index] = 1
        if isAnsUse[index] == 1: break

    return digits1[index], digits2[index]

def evaluate_guess(secret, guess):
    """評估猜測，返回A和B的數量"""
    a = sum(1 for x, y in zip(secret, guess) if x == y)
    b = sum(1 for x in secret if x in guess) - a
    return a, b

def play_game():
    secret_number = the_game_ans()
    attempts = 0

    while True:
        user_input = input("請輸入你的猜測：")
        try:
            guess = list(user_input)
        except ValueError:
            print("請輸入有效的注音。")
            continue

        if len(guess) != 5 or len(set(guess)) != 5:
            print("請輸入五個不同的注音。")
            continue

        attempts += 1
        a, b = evaluate_guess(secret_number[0], guess)

        print(f"結果：{a}個A {b}個B")

        if a == 5:
            print(f"恭喜你猜對了！答案是 {secret_number[0]} => '{secret_number[1]}'，你用了 {attempts} 次猜測。")
            break
        else:
            print("結果：", end='')
            for i, g in enumerate(guess):
                if g == secret_number[0][i]:
                    print(f"{secret_number[0][i]}, ", end='')
                elif g in secret_number[0]:
                    print(f'{guess[i]}, ', end='')
                else:
                    print('錯, ', end='')
            print('\n')


if __name__ == "__main__":
    print("歡迎來到1A2B(注音版)！")
    print("所有詞語皆由注音\"ㄅ~ㄦ\"組成，不會出現相同注音，請在下方輸入注音符號。\n")
    print("***注意***")
    print("   詞語皆由五個注音組成，故需要提供五個構成中文詞語的注音符號<不包括聲調>\n")
    print("***範例輸入***")
    print("   猜測答案為： 胡椒")
    print("   請輸入： ㄏㄨㄐㄧㄠ\n")

    times = 0
    isGame = 1
    while(isGame):
        play_game()
        if(times == ansArraySize - 1):
            print("       最後一局啦!       ")
        if(times == ansArraySize): break
        ans = input("是否再來一局(是/否)：")
        times += 1
        try:
            isGame = 1 if (ans == '是' and times < ansArraySize + 1) else 0
        except:
            print("請輸入是or否")