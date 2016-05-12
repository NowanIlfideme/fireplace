from ..utils import *


##
# Minions

class OG_202:
	"Mire Keeper"
	choose = ("OG_202a", "OG_202b")

class OG_202a:
	play = Summon(CONTROLLER, "OG_202c")

class OG_202b:
	play = AT_MAX_MANA(CONTROLLER) | GainEmptyMana(CONTROLLER, 1)


class OG_313:
	"Addled Grizzly"
	events = Summon(CONTROLLER, MINION).after(
		Buff(Summon.CARD, "OG_313e")
	)

OG_313e = buff(+1, +1)


##
#Spells

class OG_047:
	"Feral Rage"
	choose = ("OG_047a", "OG_047b")

class OG_047a:
	play = Buff(FRIENDLY_HERO, "OG_047e")

OG_047e = buff(atk=4)

class OG_047b:
	play = GainArmor(FRIENDLY_HERO, 8)
