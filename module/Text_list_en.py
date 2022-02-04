# -*- coding: utf-8 -*-
#Text_list_en.py

def text_get():
    txt = {
               "0":"New Game",
               "1":"Quit",
               "2":"Sun is the image of the king.",
               "3":"The shade of the sun was ",
               "4":"thought to be the weakening ",
               "5":"of the king's power.",
               "6":"Save completed",
               "7":"Save failed",
               "8":"Load completed",
               "9":"Load failed",
               "10":"Load game",
               "11":"The sun went down.",
               "12":"The Great Priest declared",
               "13":"the start of the \"Regicide\".",
               "14":"The one who killed the king",
               "15":"becomes the next king.",
               "16":"The regiside ends when the king",
               "17":"survives for seven days.",
               "18":"",
               "19":"You also started to act as ",
               "20":"one aiming for the throne.",
               "21":"This phenomenon is",
               "22":"a solar eclipse,",
               "23":"but it is not known",
               "24":"at this time....",
               "50":"You changed weapon to a sword.",
               "51":"You changed weapon to a cane.",
               "52":"You changed weapon to an ax.",
               "53":"Please choose a weapon.",
               "100":"Unlocked.",
               "101":"Locked.",
               "102":"The gimmick was activated.",
               "103":"Destroyed the skull.",
               "104":"Crushed skull",
               "105":"is the destination.",
               "105_0":"Where are you going?",
               "105_1":"Frontier village",
               "105_2":"Royal Magic Institute",
               "105_3":"East capital",
               "105_4":"Inheritance altar",
               "105_6":"Old town harbor",
               "105_7":"The water gate is closed!",
               "106":"Beware of monsters.",
               "107":"The main gate is ahead.",
               "108":"Dead end",
               "109":"Old town, off-limits.",
               "110":"Port of the second district.",
               "111":"Thorns are covering the road.",
               "112":"Burned the thorns.",
               "113":"Got a torch.",
               "113_1":"Got a explosive.",
               "114":"There is nothing.",
               "115":"Got a Key-4.",
               "116":"Got a Information-3.",
               "117":"That's it!",
               "118":"My lord departed.",
               "119":"No matter how national law,",
               "120":"I won't let you kill him.",
               "121":"..........",
               "122":"You should die, kingslayer!!",
               "123":"Knight Captain",
               "124":"Got valuables.",
               "125":"You're kingslayer....",
               "126":"If you want to enter the ritual",
               "127":"You have to find Royal medal.",
               "128":"Take care....ho ho ho",
               "129":"Sacred district ahead.",
               "130":"The entrance to the village",
               "131":"Inheritance altar",
               "134":"There is no one now.",
               "135":"Opened the door.",
               "136":"Silver Knight",
               "137":"You're faster than I expected.",
               "138":"Soldiers! Hurry up!",
               "139":"Take on an enemy!",
               "140":"Blocked by bedrock.",
               "141":"You used explosives.",
               "142":"Stay away from the village.",
               "143":"There is a knight order.",
               "144":"All the villagers evacuated.",
               "145":"Only the village mayor is there.",
               "146":"What are yo doing, strenger?.",
               "147":"\"Curiosity killed the cat\".",
               "148":"I won't say bad things,",
               "149":"so go home early....",
               "150":"Everyone, attack!",
               "151":"Wear an armband",
               "151_1":"when entering beyond this.",
               "152":"Explosives available, danger.",
               "153":"Those who know the secrets,",
               "154":"must die.",
               "155":"Village mayor",
               "156":"Institute of Time",
               "157":"It's a brand new grave.",
               "200":"..........",
               "201":"Hello!",
               "202":"There're many monsters recently.",
               "203":"I haven't seen king for a while.",
               "204":"I know an underground passage.",
               "205":"Hello!",
               "206":"Hello!",
               "207":"The port is closed....Ugh....",
               "208":"Hello!",
               "209":"Hello!",
               "210":"Guard sleeping in the harbor.",
               "211":"Hello!",
               "212":"Hello!",
               "213":"This is a sacred district.",
               "214":"Did you need something?",
               "215":"Hello.",
               "216":"To meet the Great Priest,",
               "217":"head to the temple.",
               "218":"At the end of this road is ",
               "219":"the house of the Great Priest.",
               "220":"Welcome, traveler of regiside.",
               "221":"The king is a great man,",
               "222":"but I have to obey ",
               "223":"the commandments of the country.",
               "224":"The king gone to the altar.",
               "225":"The key is held by the aides.",
               "226":"Royal Magic Institute",
               "227":"Door control room",
               "228":"Laboratory entrance",
               "229":"Emergency contact.",
               "230":"This is a shift officer.",
               "231":"Detected an intruder.",
               "232":"Strengthen your vigilance.",
               "233":"That's all.",
               "234":"First basement floor",
               "235":"First adjustment room",
               "236":"Second adjustment room",
               "237":"Third adjustment room",
               "238":"Unlocked",
               "239":"The password is incorrect",
               "240":"Please enter the password",
               "241":"Library",
               "242":"Second basement floor",
               "243":"Third basement floor",
               "244":"Fourth adjustment room",
               "245":"Sixth adjustment room",
               "250":"The mysterious relic was found ",
               "2501":"in a frontier village.",
               "251":"Secret research is underway",
               "2511":"in the Magic Institute.",
               "252":"The heart of a monster is ",
               "2521":"enshrined in eastern capital.",
               "253":"It is recommended to check.",
               "254":"The key is....",
               "255":"Well, it looks like it's done.",
               "256":"Go to the basement of the temple.",
               "257":"That's where it all ends...",
               "300":"City guard",
               "301":"Residents of the city",
               "302":"Old man",
               "303":"Old woman",
               "304":"Villager",
               "305":"Resident",
               "306":"Great Priest",
               "307":"Magic Institute officer",
               "308":"Magic institute director",
               "309":"Oh, the regicide traveler....",
               "310":"You are an ignorant idiot.",
               "311":"Goodbye forever.",
               "312":"Got a Magical lantern.",
               "313":"Got a Valuables-3.",
               "400":"Got Medicine.",
               "401":"Will not open.",
               "402":"East capital",
               "403":"Taikyokuden is ahead",
               "404":"Repairing the warehouse",
               "405":"The door opened.",
               "406":"How brave you come!",       
               "407":"I was surprised.",       
               "408":"I pay tribute to ",
               "409":"your obsession.",
               "410":"I'll kill you in the style ",   
               "411":"of the eastern capital.",       
               "412":"Green knight",
               "413":"Got a Valuables-4.",
               "414":"Great luck",  
               "415":"Some luck",  
               "416":"Good luck",  
               "417":"Bad luck",  
               "418":"Terrible luck",                 
               "419":"fortune slip",                 
               "420":"King",                 
               "421":"Welcome to this place.",                 
               "422":"The Kingslayer's Traveller.",  
               "423":"This is the Inheritance altar.",
               "424":"The destination of Regicide.",
               "425":"Let me see with my own hands ",
               "426":"if you are worthy ",  
               "427":"of the throne.",
               "428":"The pedestal was set up.",
               "4281":"There is a mysterious hollow.",
               "429":"The crystal was installed.",
               "4291":"There is a round hollow.",
               "430":"A wooden box was placed.",
               "4301":"There is a small square hollow.",
               "431":"A coin was placed.",
               "4311":"There is a small round hollow.",
               "500":"Welcome, traveler.",
               "501":"Thank you for your service ",
               "502":"as the Kingslayer.",                       
               "503":"But if you came here without ",                
               "504":"choosing the throne, ",
               "505":"does that mean you have ",
               "506":"realized your true role?",
               "507":"What you have gathered is", 
               "508":"a fragment of the lost power ",
               "509":"of the Ouroboros.",
               "510":"We've been searching for",                    
               "511":"it for a long time....",
               "512":"We have only one goal.",   
               "513":"",   
               "514":"To destroy the flow of time.",
               "515":"Ouroboros is eternity's symbol.",
               "516":"Its power allows it to ",
               "517":"interfere with the timeline.",
               "518":"If the flow of time is ", 
               "519":"destroyed, there will be ",   
               "520":"no past and no future.",   
               "521":"All we have is now.",
               "522":"This means freedom from ",
               "523":"fear of the future. ",
               "524":"Look at this. This crystal is ",
               "525":"the flow of time itself.",
               "526":"Destroy it with your own hands.",                  
               "527":"You have the power to do so, ",
               "528":"having accomplished Regiside.",              
               "529":"You're a fool.",                        
               "530":"I'm disappointed in you.",                        
               "531":"So I guess I'll just have to ",                        
               "532":"do it myself after all.",
               "999":"I've only made it so far....",
               "999_1":"I'm so sorry!!",
               "1000":"About the old town",
               "1001":"The old town was closed due to",
               "1002":"an accident at ",
               "1003":"the Institute of Time.",
               "1004":"When the rescue team arrived",
               "1005":"at the site, the inhabitants ",
               "1006":"were aging rapidly,",
               "1007":"and some died of senility.",
               "1008":"",
               "1009":"About frontier village",
               "1010":"It is the birthplace of",
               "1011":"the current king and is a ",
               "1012":"peaceful place surrounded ",
               "1013":"by greenery.",
               "1014":"On the north side of ",
               "1015":"the village is an ancient ruin, ",
               "1016":"which is being investigated by ",
               "1017":"Cultural Properties Department.",
               "1018":"About the Royal Magic Institute",
               "1019":"There has been established ",
               "1020":"for the purpose of taking over ",
               "1021":"the Institute of time.",
               "1022":"There's an army-like discipline ",
               "1023":"with the director of ",
               "1024":"the magic institute at the top, ",
               "1025":"and it has military power ",
               "1026":"independent of the Knights.",
               "1027":"About the east capital",
               "1028":"The east capital has been ",
               "1029":"interacting with the kingdom ",
               "1030":"since ancient times.",
               "1031":"Of particular note is the study",
               "1032":"of immortality.   Therefore, ",
               "1033":"their lifespan is long.",
               "1034":"The characteristic mask is ",
               "1035":"a special product.",
               "1036":"About the sacred district",
               "1037":"The sacred district manages",
               "1038":"ritual with the great priest",
               "1039":"The deep part of the temple",
               "1040":"is tightly closed",
               "1041":"and no outsiders are allowed",
               "1042":"to enter.",
               "1043":"",
               "1044":"",
               "1045":"About Ouroboros",
               "1046":"",
               "1047":"",
               "1048":"",
               "1049":"The page is torn....",
               "1050":"",
               "1051":"",
               "1052":"",
               "1053":"",
               "2000":"Do you wont to get the throne?",
               "2001":"Ending 1",
               "2002":"You have won the throne.",
               "2003":"This is the end of this ",
               "2004":"Regicide.",
               "2005":"",
               "2006":"What will happen next time?",
               "2010":"Destroy the crystal?",
               "2011":"Ending 2",
               "2012":"You have destroyed timeline.",
               "2013":"There is no past, no future,",
               "2014":"and the happy now lasts forever.",
               "2015":"A world of peace has been ",
               "2016":"achieved at the expense of all",
               "2017":"possibilities of the future.",
               "2018":"",
               
               

    }
    return txt

def text_get_s():
    txt = {

               "51":"Welcome.",
               "52":"Please select ",
               "53":"the item number.",
               "54":"",
               "55":"Note writing ",
               "56":"of guards",
               "57":"Do you want to buy?",
               "58":"Letter from ",
               "59":"the palace",
               "60":"Do you want to buy?",
               "61":"Large library key",
               "62":"Do you want to buy?",
               "63":"Big rusty key",
               "64":"",
               "65":"Do you want to buy?",
               "66":"Sold out",
               "67":"Not enough money.",
               "68":"",
               "69":"Thank you!",
    }
    return txt

def text_get_s2():
    txt = {

               "51":"Welcome.",
               "52":"Please select ",
               "53":"the item number.",
               "54":"",
               "55":"Military warrant",
               "56":"",
               "57":"Do you want to buy?",
               "58":"Village mayor's ",
               "59":"note writing",
               "60":"Do you want to buy?",
               "61":"Base key",
               "62":"Do you want to buy?",
               "63":"Armband of ",
               "64":"the Guard",
               "65":"Do you want to buy?",
               "66":"Sold out",
               "67":"Not enough money.",
               "68":"",
               "69":"Thank you!",
    }
    return txt

def text_get_s3():
    txt = {

               "51":"Welcome.",
               "52":"Please select ",
               "53":"the item number.",
               "54":"",
               "55":"Construction record",
               "56":"",
               "57":"Do you want to buy?",
               "58":"Researcher's memo",
               "59":"",
               "60":"Do you want to buy?",
               "61":"Red card key",
               "62":"Do you want to buy?",
               "63":"Green card key",
               "64":"",
               "65":"Do you want to buy?",
               "66":"Sold out",
               "67":"Not enough money.",
               "68":"",
               "69":"Thank you!",
    }
    return txt

def text_get_s4():
    txt = {

               "51":"Welcome.",
               "52":"Please select ",
               "53":"the item number.",
               "54":"",
               "55":"Note writing ",
               "56":"of Ashigaru",
               "57":"Do you want to buy?",
               "58":"Old scroll ",
               "59":"",
               "60":"Do you want to buy?",
               "61":"Demon mask",
               "62":"Do you want to buy?",
               "63":"Woman's mask",
               "64":"",
               "65":"Do you want to buy?",
               "66":"Sold out",
               "67":"Not enough money.",
               "68":"",
               "69":"Thank you!",
    }
    return txt

def text_get_s5():
    txt = {

               "51":"Welcome.",
               "52":"Please select ",
               "53":"the item number.",
               "54":"",
               "55":"Note writing ",
               "56":"of guards",
               "57":"Do you want to buy?",
               "58":"Letter from ",
               "59":"the palace",
               "60":"Do you want to buy?",
               "61":"Large library key",
               "62":"Do you want to buy?",
               "63":"Big rusty key",
               "64":"",
               "65":"Do you want to buy?",
               "66":"Sold out",
               "67":"Not enough money.",
               "68":"",
               "69":"Thank you!",
    }
    return txt

def text_get_s6():
    txt = {

               "51":"Welcome.",
               "52":"Please select ",
               "53":"the item number.",
               "54":"",
               "55":"Note writing ",
               "56":"of guards",
               "57":"Do you want to buy?",
               "58":"Letter from ",
               "59":"the palace",
               "60":"Do you want to buy?",
               "61":"Large library key",
               "62":"Do you want to buy?",
               "63":"Big rusty key",
               "64":"",
               "65":"Do you want to buy?",
               "66":"Sold out",
               "67":"Not enough money.",
               "68":"",
               "69":"Thank you!",
    }
    return txt

def item_get():
    txt = {

               "0":"Sold out",
               "1":"Information-1",
               "2":"Information-2",
               "3":"Key-1",
               "4":"Key-2",
               "5":"Torch",
               "6":"Valuables-1",
               "7":"Key-3",
               "8":"Information-3",
    }
    return txt

def item_get2():
    txt = {

               "0":"Sold out",
               "1":"Information-4",
               "2":"Information-5",
               "3":"Key-5",
               "4":"Armband",
               "5":"Explosive",
               "6":"Valuables-2",
               "7":"Key-6",
               "8":"Information-6",
    }
    return txt

def item_get3():
    txt = {

               "0":"Sold out",
               "1":"Information-7",
               "2":"Information-8",
               "3":"Card key-1",
               "4":"Card key-2",
               "5":"Magical lantern",
               "6":"Valuables-3",
               "7":"Card key-3",
               "8":"Information-9",
    }
    return txt

def item_get4():
    txt = {

               "0":"Sold out",
               "1":"Information-10",
               "2":"Scroll",
               "3":"Mask-1",
               "4":"Mask-2",
               "5":"Medicine",
               "6":"Valuables-4",
               "7":"Key-4",
               "8":"Information-11",
    }
    return txt

def item_get5():
    txt = {

               "0":"Sold out",
               "1":"Key-4",
               "2":"Key-7",
               "3":"Key-8",
               "4":"Key-9",
               "5":"Nautical chart-1",
               "6":"Nautical chart-2",
               "7":"Nautical chart-3",
               "8":"Nautical chart-4",
    }
    return txt

def item_get6():
    txt = {

               "0":"Sold out",
               "1":"King's key",
               "2":"Information-2",
               "3":"Key-1",
               "4":"Key-2",
               "5":"Torch",
               "6":"Valuables-1",
               "7":"Key-4",
               "8":"Information-3",
    }
    return txt

def item_get_t():
    txt = {
               "1":["Note writing of guards",
                    "There was an inspection of",
                    "the emergency passage in ",
                    "the royal palace.",
                    "The equipment",
                    "in the large library",
                    "needs to be re-inspected.",],
               "2":["Letter from the palace",
                    "The port will be closed ",
                    "for a while.",
                    "In an emergency, ",
                    "use the second district",
                    "of the old town.",],
               "3":["Large library key",
                    "The key to the ",
                    "large library",
                    "on the outskirts ",
                    "of the city.",],
               "4":["Big rusty key",
                    "A big key with ",
                    "a special structure."],
               "5":["Torch",
                    "Used to illuminate",
                    "the darkness",
                    "and burn vegetation.",],
               "6":["Old medal",
                    "Rust-stained medal.",
                    "The crest of the ",
                    "royal family is carved."],
               "7":["Jailer's key",
                    "The key to the dungeon ",
                    "of the city."],
               "8":["Knight's note writing",
                    "As the \"Regicide\" began, ",
                    "the king headed",
                    "for the inheritance ",
                    "altar.",
                    "I also have to think ",
                    "about what I should do."],

    }
    return txt

def item_get_t2():
    txt = {
               "1":["Military warrant",
                    "The village will be ",
                    "under the command",
                    "of the Knights",
                    "until the investigation",
                    "of the northern mine ",
                    "is completed.",
                    "Follow the instructions.",],
               "2":["Village mayor's memo",
                    "A messenger came from ",
                    "the city.",
                    "It is finally released ",
                    "from the role",
                    "of keeping the secret ",
                    "of the village.",
                    "I got my hands too dirty.",],
               "3":["Base key",
                    "The key to the base",
                    "set up in the village.",],
               "4":["Armband",
                    "Armband of the ",
                    "Guard of the base."],
               "5":["Explosive",
                    "A powerful explosive ",
                    "that can destroy rock.",],
               "6":["Crystal ball",
                    "A crystal ball found in the ",
                    "mine north of the village.",
                    "Something like",
                    "a black snake",
                    "can be seen inside.",],
               "7":["Mysterious area key",
                    "Key to the mysterious area ",
                    "of the sacred district."],
               "8":["Knight's note writing",
                    "I can't agree with everything ",
                    "the king does, ",
                    " but I can't help it.",],

    }
    return txt

def item_get_t3():
    txt = {
               "1":["Construction record",
                    "June 2",
                    "The durability test of ",
                    "the deepest storage ",
                    "was conducted.",
                    "No abnormality.",],
               "2":["Researcher's memo",
                    "Stop growing.  ",
                    "Flow of time slows down.",
                    "Hurry to select the  ",
                    "right medium.",
                    "Predict the next ",
                    "solar eclipse."],
               "3":["Red card key",
                    "Card key used in the ",
                    "Royal Magic Institute.",
                    "",
                    "",],
               "4":["Green card key",
                    "Card key used in the ",
                    "Royal Magic Institute.",
                    "",
                    "",],
               "5":["Magical lantern",
                    "A lantern powered by ",
                    "magical power ",
                    "prototyped at ",
                    "Royal Magic Institute."],
               "6":["Mysterious pedestal",
                    "A mysterious metal pedestal ",
                    "stored in the deepest",
                    "part of the ",
                    "Royal Magic Institute."],
               "7":["Purple card key",
                    "Card key used in the ",
                    "Royal Magic Institute.",
                    "Used to enter the ",
                    "deepest vault.",],
               "8":["Director's note writing",
                    "If the hypothesis ",
                    "is correct, the next  ",
                    "solar eclipse will be ",
                    "the last regicide. ",
                    "All for the eternal peace ",
                    "of the world."],

    }
    return txt

def item_get_t4():
    txt = {
               "1":["Note writing of Ashigaru",
                    "Strengthen security until  ",
                    "the warehouse",
                    "is repaired.",
                    "Beware of bandits.",
                    "in the large library",
                    "needs to be re-inspected.",],
               "2":["Old scroll",
                    "Taikyokuden must be ",
                    "isolated from the ",
                    "outside world.",
                    "Traditionally, this is ",
                    "achieved by using ",
                    "river water."],
               "3":["Demon mask",
                    "A demon mask peculiar ",
                    "to the eastern capital.",
                    "However, it is not ",
                    "designed to be worn",
                    "by humans."],
               "4":["Woman's mask",
                    "A woman's mask peculiar ",
                    "to the eastern capital.",
                    "However, it is not ",
                    "designed to be worn",
                    "by humans."],
               "5":["medicine",
                    "A drug made in the ",
                    "eastern capital. ",
                    "HP gradually recovers.",],
               "6":["Mysterious wooden box",
                    "A wooden box stored in ",
                    "the deepest part of ",
                    "Taikyokuden. It is ",
                    "tightly sealed with ",
                    "amulets and chains."],
               "7":["Old man's mask",
                    "A old man's mask peculiar ",
                    "to the eastern capital.",
                    "However, it is not ",
                    "designed to be worn",
                    "by humans."],
               "8":["Diplomatic documents",
                    "I agree to keep the relics .",
                    "separately from your ",
                    "country. ",
                    "Please handle it with",
                    "great care.",],

    }
    return txt

def item_get_t5():
    txt = {
               "1":["Knight captain's key",
                    "The key given by the king  ",
                    "when he was appointed ",
                    "as knight captain.",],
               "2":["Silver Knight's key",
                    "The silver knight",
                    "who servedthe king",
                    "was originallya guard ",
                    "of the Great Priest.",],
               "3":["Director's key",
                    "The key given by the king ",
                    "when he was appointed ",
                    "director of ",
                    "the Institute of Time.",],
               "4":["Green Knight's key",
                    "The green knight,",
                    "an aide to the king,",
                    "was from the eastern",
                    "capital.",
                    "And he was good at ",
                    "swordsmanship."],
               "5":["Old nautical chart",
                    "A route to  ",
                    "frontier village",
                    "is drawn.",],
               "6":["Brand new nautical chart",
                    "A route to  ",
                    "Royal Magic Institute ",
                    "is drawn.",],
               "7":["Nautical chart of sand",
                    "A route to  ",
                    "east capital",
                    "is drawn.",],
               "8":["Nautical chart of king",
                    "A route to ",
                    "inheritance altar ",
                    "is drawn.",],

    }
    return txt

def item_get_t6():
    txt = {
               "1":["King's key",
                    "The key that the king had.",
                    "",
                    "",                    
                    "Which door does it ",
                    "correspond to?",],
               "2":["Letter from the palace",
                    "The port will be closed ",
                    "for a while.",
                    "In an emergency, ",
                    "use the second district",
                    "of the old town.",],
               "3":["Large library key",
                    "The key to the ",
                    "large library",
                    "on the outskirts ",
                    "of the city.",],
               "4":["Big rusty key",
                    "A big key with ",
                    "a special structure."],
               "5":["Old nautical chart",
                    "A route to a frontier village ",
                    "is drawn.",],
               "6":["Old medal",
                    "Rust-stained medal.",
                    "The crest of the ",
                    "royal family is carved."],
               "7":["Jailer's key",
                    "The key to the dungeon ",
                    "of the city."],
               "8":["Knight's note writing",
                    "As the \"Regicide\" began, ",
                    "the king headed",
                    "for the inheritance ",
                    "altar.",
                    "I also have to think ",
                    "about what I should do."],

    }
    return txt