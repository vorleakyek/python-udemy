# Python is a bit different from other programming languages in that it does not have block scope. 
# This means that variables created nested in other blocks of code e.g. for loops, if statements, while loops etc. 
# don't get local scope. They are given function scope if they are within a function or global scope if they are not.  


#CASE 1: 
game_level = 10 
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5: 
  new_enemy = enemies[0] 

#out of the block scope can still access the variable 
print(new_enemy) 


#CASE 2: 
#But, it will be scope within a function 
game_level = 10 
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
  if game_level < 5: 
    new_enemy = enemies[0] 

#out of the function scope - can't access the variable within a function  
print(new_enemy) 

#CASE 3: 
#can move "print" inside of the function but outside of the block scope
def create_enemy():
  new_enemy = ""
  if game_level < 5: 
    new_enemy = enemies[0] 
  
  # within the function scope but outside of the if-block - can access the variable  
  print(new_enemy) 
