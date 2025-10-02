import random







def lottery_game(winning_numbers=None, player_numbers=None, Players_name =None):





 if winning_numbers is None:



  winning_numbers = random.sample(range(1, 61), 6)



 winning_numbers.sort()



 if player_numbers is None:



  player_numbers = []



  print("\nEnter 6 numbers between 1 and 60:")



  while len(player_numbers) < 6:





   try:



    num = int(input(f"Number {len(player_numbers)+1}: "))



    if num < 1 or num > 60:



     print("Invalid number! Must be between 1 and 60.")



    elif num in player_numbers:



     print("Duplicate number! Try again.")



    else:



     player_numbers.append(num)



   except ValueError:



    print("Invalid input! Enter a number.")



 player_numbers.sort()





 matches = len(set(winning_numbers) & set(player_numbers) )





 if matches == 6:



  prize = 2_000_000 

   



 else:



  prize = matches * 1000







  



 print("\n Lottery Results ")



 print("Winning Numbers:", winning_numbers)





 print("Your Numbers:", player_numbers)



 print("Matches:", matches)



 print("Congrats you won a Prize of ₱{:,.0f}".format(prize))











if __name__ == "__main__":





 print("\nWinning Numbers :")



 lottery_game("Kims Card"[37, 51, 9, 8, 50, 52], [8, 10, 15, 50, 20, 60])

 lottery_game("Maja Card"[37, 51, 9, 8, 50, 52], [40, 9, 15, 20, 23, 30])

 lottery_game("Sara Card"[37, 51, 9, 8, 50, 52], [35, 40, 10, 12, 15, 20])

 lottery_game("Pia Card"[37, 51, 9, 8, 50, 52], [45, 47, 50, 52, 60, 31])

 lottery_game("Bea Card"[37, 51, 9, 8, 50, 52], [40, 43, 15, 48, 47, 30])

 lottery_game("Julia Card"[37, 51, 9, 8, 50, 52], [5, 42, 12, 45, 20, 30])

 lottery_game("Donote Card"[37, 51, 9, 8, 50, 52], [33, 35, 42, 43, 60, 30])

 lottery_game("Beate"[37, 51, 9, 8, 50, 52], [23, 56, 10, 60, 40, 12])



  





 print("\nWinning Numbers:")



 lottery_game("Kims Card"[15, 20, 36, 43, 11, 22], [8, 10, 15, 50, 20, 60])

 lottery_game("Maja Card"[15, 20, 36, 43, 11, 22], [40, 9, 15, 20, 23, 30])

 lottery_game("Sara Card"[15, 20, 36, 43, 11, 22], [35, 40, 10, 12, 15, 20])

 lottery_game("Pia Card"[15, 20, 36, 43, 11, 22], [45, 47, 50, 52, 60, 31])

 lottery_game("Bea Card"[15, 20, 36, 43, 11, 22], [40, 43, 15, 48, 47, 30])

 lottery_game("Julia Card"[15, 20, 36, 43, 11, 22], [5, 42, 12, 45, 20, 30])

 lottery_game("Donote Card"[15, 20, 36, 43, 11, 22], [33, 35, 42, 43, 60, 30])

 lottery_game("Beate"[15, 20, 36, 43, 11, 22], [23, 56, 10, 60, 40, 12])







  





 print("\nWinning Numbers:")



 lottery_game("Kims Card"[4, 11, 14, 43, 46, 53], [8, 10, 15, 50, 20, 60])

 lottery_game("Maja Card"[4, 11, 14, 43, 46, 53], [40, 9, 15, 20, 23, 30])

 lottery_game("Sara Card"[4, 11, 14, 43, 46, 53], [35, 40, 10, 12, 15, 20])

 lottery_game("Pia Card"[4, 11, 14, 43, 46, 53], [45, 47, 50, 52, 60, 31])

 lottery_game("Bea Card"[4, 11, 14, 43, 46, 53], [40, 43, 15, 48, 47, 30])

 lottery_game("Julia Card"[4, 11, 14, 43, 46, 53], [5, 42, 12, 45, 20, 30])

 lottery_game("Donote Card"[4, 11, 14, 43, 46, 53], [33, 35, 42, 43, 60, 30])

 lottery_game("Beate"[4, 11, 14, 43, 46, 53], [23, 56, 10, 60, 40, 12])

