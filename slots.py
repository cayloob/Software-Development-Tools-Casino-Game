import random
import pygame

#slot machine 
class slots_machine():
    def __init__(self, fiat_bux, bet):
        self.fiat_bux = fiat_bux
        self.bet = bet
        self.spin_count = 0
        self.force_win = 10
     

    def gen(self):
        self.spin_count += 1
        numbers = [0,1,2,3,4,5,6,7,8,9]
        common = [0,1,5,8]
        rare = [3,4,6,9]
        weights = [20,8,6,8,8,8,8,6,8,20]

        first, second, third = random.choices(numbers,weights= weights, k= 3)

        if first == second:
            weights[first] += 10
            third = random.choices(numbers, weights= weights, k = 1)[0]

        if self.spin_count == self.force_win:
            self.spin_count = random.randint(0,self.force_win)
            first = random.choices(numbers, weights = weights, k= 1)[0]
            second = first
            third = first
        
        result = [first, second, third]

        if first == second and first == third:
            if first in common:
                self.fiat_bux += 2 * self.bet

            elif first in rare:
                self.fiat_bux += 5 * self.bet

            else:
                #ability to implement more bonus games later
                #bonus_game = random.randint(0,2)
                bonus_game = 0
                return result, self.fiat_bux, bonus_game 
        else:
            self.fiat_bux -= self.bet


            
        return result, self.fiat_bux      
    
    def wheel_spin(self):
        colors = {'r':50,'o':25, 'y':500, 'g':200, 'c':0, 'b':100, 'p':1000, 'pi': 75}
        weights = [25,16,12,12,6,15,6,16]

        spin = random.choices(list(colors.keys()), weights, k =1)[0]

        if spin != 0:
            self.fiat_bux += colors[spin]
            free_games = 0

        else:
            free_games = random.randint(1,5) * 10
            
        return spin, self.fiat_bux, free_games
        
