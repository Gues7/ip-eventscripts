import es
import playerlib
import repeat

info = es.AddonInfo() 
info.name     = "IrishPirates Tea-Bag" 
info.version  = "0.1" 
info.url      = "http://www.irishpirates.org" 
info.basename = "ip_teabag" 
info.author   = "Gues7"

ip_teabag   = es.ServerVar(info.name, info.version, info.url).makepublic()

def load():
    global checkTeabag
    checkTeaBag = {}
    es.msg("#multi", "#lightgreen[#greenTea-Bag#lightgreen]#default has loaded successfully")

def unload():
    global checkTeabag
    es.msg("#multi", "#lightgreen[#greenTea-Bag#lightgreen]#default has been unloaded")
    if repeat.find('checkForTeabag') > 0:
        checkTeabag.stop

def player_death(ev):
    global checkTeabag
    if ev['attacker'] > 0:
        checkTeabag = repeat.create('checkForTeabag', doWork, (ev['userid'], ev['attacker']))
        checkTeabag.start(1, 10)
        
def round_start(ev):
    global checkTeabag
    if repeat.find('checkForTeabag') > 0:
        checkTeabag.stop

def doWork(arg1, arg2):
    global checkTeabag
    victim      = playerlib.getPlayer(arg1)
    attacker    = playerlib.getPlayer(arg2)
    isDucking   = es.getplayerprop(arg2, 'CBasePlayer.localdata.m_Local.m_bDucked')
    
    victimPos   = victim.x + victim.y + victim.z
    attackerPos = attacker.x + attacker.y + attacker.z
    if (attackerPos - victimPos) <= 50: # Change this to change sensitivity
        if isDucking > 0:
            checkTeabag.stop
            es.centermsg("%s just got teabagged!!!" % victim.name)
            es.emitsound(player, arg2, 'bot/owned.wav', 1.0, 0.5)
            es.msg("#multi", "#lightgreen[#greenTea-Bag#lightgreen] %s#default has just tea-bagged #lightgreen%s#default!" % (attacker.name, victim.name))