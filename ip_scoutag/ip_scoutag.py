'''

I R I S H P I R A T E S . O R G

	Mod Name: 	ip_scoutag
	Mod URL:	http://mods.irishpirates.org/scoutag
	Mod Author:	[IP] Gues7
	
	Mod Description:
		This mod adds LIVE DAMAGE STATS for the SCOUT ONLY to any server its running on. On a successful scout attack, you and the victim will receive stats for the hit.
		An optional feature is to turn on headshot notification TO THE WHOLE SERVER if someone is killed with a scout headshot.
		
	Mod Instuctions:
		Install this the same way as any other EventScripts Addon.
		
		Thie script registeres three server cvars that allow you to change the operation of the script in real time. Unloading the script will not unload these cvars.
		
		ip_scoutag_enable			-	turns the script on/off (1/0), this does not load/unload the script, the script must be loaded already.
		ip_scoutag_announce			-	turns the advertisements at the start of each round on/off (1/0)
		ip_scoutag_annouce_headshot - 	turns on/off (1/0) the announcing of headshot kills with the scout
		
	Mod Usage:
		This mod is only permitted for use on official Irish Pirates test servers unless prior permission is saught from the author.

		
	Changelog:
		
		24/5/09 : 
			* Changed information reporting to inform both victim & player
			* Added public CVAR for version information
			* Added ability to announce headshots to the whole server.
			* Restricted public headshot reporting if it is a TA/TK
			* Added Damage information to the report
		25/5/09 :
			* Changed the reporting strings to NOT NOTIFY the attacker of damage.
			* Changed the reporting strings to use color.
			* Fixed some typo's
			* Now uses centertell to notify with TaG for each hit
			* 
'''
import es
import playerlib

info = es.AddonInfo() 
info.name     = "IrishPirates Scout Tag" 
info.version  = "0.3" 
info.url      = "http://www.irishpirates.org" 
info.basename = "ip_scoutag" 
info.author   = "Gues7"

ip_scoutag = es.ServerVar(info.name, info.version, info.url).makepublic()
ip_scoutag_enable = es.ServerVar("ip_scoutag_enable", 1, "Enable the Scout Tag plugin")
ip_scoutag_announce = es.ServerVar("ip_scoutag_announce", 1, "Enable the Scout Tag advertisement")
ip_scoutag_announce_headshot = es.ServerVar("ip_scoutag_announce_headshot", 1, "Enable headshot advertisements for scoutag")

def round_start(ev):
	if ip_scoutag_enable > 0 and ip_scoutag_announce > 0:
		es.msg("#multi", "#green[Scout Tag]#default... you have to try it to find out :)")

def player_hurt(ev):
	if ip_scoutag_enable > 0 and ev['weapon'] == "scout":
		
		victim = playerlib.getPlayer(ev['userid'])
		attacker = playerlib.getPlayer(ev['attacker'])
		
		es.centertell(ev['attacker'], 'TaG')
		
		if int(ev["hitgroup"]) == 1:
			if ip_scoutag_announce_headshot > 0:
				es.msg("#multi", "#green [Scout Tag] : #default %s just #lightgreen HEADSHOT #default %s with the scout!" % (attacker.name, victim.name))
			else:
				es.tell(attacker, "#multi", "#green [Scout Tag] : #default You just HEADSHOT %s for %s damage" % (victim.name, ev["dmg_health"]))
				es.tell(victim, "#multi", "#green [Scout Tag] : #default %s just HEADSHOT you!" % attacker.name)
            attackercash = attacker.get("cash")
            attacker.set("cash", attackercash + 500)
		elif int(ev["hitgroup"]) == 2:
			es.tell(attacker, "#multi", "#green [Scout Tag] : #default You just shot %s in the #lightgreen CHEST #default" % (victim.name))
			es.tell(victim, "#multi", "#green [Scout Tag] : #default %s just shot your in the #lightgreen CHEST #default for #lightgreen %s #default damage" % (attacker.name, ev["dmg_health"]))
		elif int(ev["hitgroup"]) == 3:
			es.tell(attacker, "#multi", "#green [Scout Tag] : #default You just shot %s in the #lightgreen STOMACH #default" % (victim.name))
			es.tell(victim, "#multi", "#green [Scout Tag] : #default %s just shot your in the #lightgreen STOMACH #default for #lightgreen %s #default damage" % (attacker.name, ev["dmg_health"]))
		elif int(ev["hitgroup"]) == 4:
			es.tell(attacker, "#multi", "#green [Scout Tag] : #default You just shot %s in the #lightgreen LEFT ARM #default" % (victim.name))
			es.tell(victim, "#multi", "#green [Scout Tag] : #default %s just shot your in the #lightgreen LEFT ARM #default for #lightgreen %s #default damage" % (attacker.name, ev["dmg_health"]))
		elif int(ev["hitgroup"]) == 5:
			es.tell(attacker, "#multi", "#green [Scout Tag] : #default You just shot %s in the #lightgreen RIGHT ARM #default" % (victim.name))
			es.tell(victim, "#multi", "#green [Scout Tag] : #default %s just shot your in the #lightgreen RIGHT ARM #default for #lightgreen %s #default damage" % (attacker.name, ev["dmg_health"]))
		elif int(ev["hitgroup"]) == 6:
			es.tell(attacker, "#multi", "#green [Scout Tag] : #default You just shot %s in the #lightgreen LEFT LEG #default" % (victim.name))
			es.tell(victim, "#multi", "#green [Scout Tag] : #default %s just shot your in the #lightgreen LEFT LEG #default for #lightgreen %s #default damage" % (attacker.name, ev["dmg_health"]))
		elif int(ev["hitgroup"]) == 7:
			es.tell(attacker, "#multi", "#green [Scout Tag] : #default You just shot %s in the #lightgreen RIGHT LEG #default" % (victim.name))
			es.tell(victim, "#multi", "#green [Scout Tag] : #default %s just shot your in the #lightgreen RIGHT LEG #default for #lightgreen %s #default damage" % (attacker.name, ev["dmg_health"]))