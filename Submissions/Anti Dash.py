# bot code goes here
from Game.Skills import *
from Game.projectiles import *
from ScriptingHelp.usefulFunctions import *
from Game.playerActions import defense_actions, attack_actions, projectile_actions
from gameSettings import HP, LEFTBORDER, RIGHTBORDER, LEFTSTART, RIGHTSTART, PARRYSTUN


# PRIMARY CAN BE: Teleport, Super Saiyan, Meditate, Dash Attack, Uppercut, One Punch
# SECONDARY CAN BE : Hadoken, Grenade, Boomerang, Bear Trap

# TODO FOR PARTICIPANT: Set primary and secondary skill here
PRIMARY_SKILL = TeleportSkill
SECONDARY_SKILL = Hadoken

#constants, for easier move return
#movements
JUMP = ("move", (0,1))
FORWARD = ("move", (1,0))
BACK = ("move", (-1,0))
JUMP_FORWARD = ("move", (1,1))
JUMP_BACKWARD = ("move", (-1, 1))

# attacks and block
LIGHT = ("light",)
HEAVY = ("heavy",)
BLOCK = ("block",)

PRIMARY = get_skill(PRIMARY_SKILL)
SECONDARY = get_skill(SECONDARY_SKILL)

# no move, aka no input
NOMOVE = "NoMove"
# for testing
moves = SECONDARY,
moves_iter = iter(moves)

# TODO FOR PARTICIPANT: WRITE YOUR WINNING BOT
class Script:
    def __init__(self):
        self.primary = PRIMARY_SKILL
        self.secondary = SECONDARY_SKILL
       
    # DO NOT TOUCH
    def init_player_skills(self):
        return self.primary, self.secondary
   
    # MAIN FUNCTION that returns a single move to the game manager
    def get_move(self, player, enemy, player_projectiles, enemy_projectiles):
        distance = get_distance(player,enemy)
        backAgainstWall = get_pos(player)[0] in {0,1,15,14}
        
        if secondary_on_cooldown(enemy):
            if distance <= 1:
                return(LIGHT)
            elif 1<distance<5:
                return SECONDARY
            else:
                return BACK

        if distance <= 2 and backAgainstWall:
            return PRIMARY
        if not secondary_on_cooldown(enemy) and distance<5:
            return JUMP_BACKWARD
        if get_past_move == JUMP_BACKWARD:
            if secondary_on_cooldown:
                return SECONDARY
            else:
                return FORWARD
        if not secondary_on_cooldown(enemy) and 5<distance<7:
            if secondary_on_cooldown:
                return(SECONDARY)
            else:
                if primary_on_cooldown:
                    return PRIMARY
    

