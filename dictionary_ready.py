"""
BotSpeak Dictionary Generator
Generates comprehensive mappings for language compression
"""

# Most common English words and phrases for numeric codes (100-999)
NUMERIC_MAPPINGS = {
    # Basic pronouns and articles
    "100": "the", "101": "a", "102": "an", "103": "I", "104": "you", "105": "he", "106": "she", "107": "it", "108": "we", "109": "they",
    "110": "me", "111": "him", "112": "her", "113": "us", "114": "them", "115": "my", "116": "your", "117": "his", "118": "their", "119": "our",
    
    # Common verbs
    "120": "is", "121": "are", "122": "was", "123": "were", "124": "be", "125": "been", "126": "being", "127": "have", "128": "has", "129": "had",
    "130": "do", "131": "does", "132": "did", "133": "will", "134": "would", "135": "could", "136": "should", "137": "can", "138": "may", "139": "might",
    "140": "go", "141": "come", "142": "get", "143": "make", "144": "take", "145": "give", "146": "see", "147": "know", "148": "think", "149": "say",
    "150": "tell", "151": "ask", "152": "work", "153": "play", "154": "run", "155": "walk", "156": "talk", "157": "look", "158": "find", "159": "help",
    
    # Common adjectives
    "160": "good", "161": "bad", "162": "big", "163": "small", "164": "new", "165": "old", "166": "young", "167": "high", "168": "low", "169": "long",
    "170": "short", "171": "hot", "172": "cold", "173": "warm", "174": "cool", "175": "fast", "176": "slow", "177": "easy", "178": "hard", "179": "nice",
    
    # Numbers and time
    "180": "one", "181": "two", "182": "three", "183": "four", "184": "five", "185": "six", "186": "seven", "187": "eight", "188": "nine", "189": "ten",
    "190": "today", "191": "tomorrow", "192": "yesterday", "193": "now", "194": "then", "195": "here", "196": "there", "197": "when", "198": "where", "199": "why",
    
    # Common conjunctions and prepositions
    "200": "and", "201": "or", "202": "but", "203": "so", "204": "if", "205": "because", "206": "that", "207": "this", "208": "these", "209": "those",
    "210": "in", "211": "on", "212": "at", "213": "to", "214": "for", "215": "with", "216": "by", "217": "from", "218": "up", "219": "down",
    "220": "out", "221": "off", "222": "over", "223": "under", "224": "about", "225": "into", "226": "onto", "227": "upon", "228": "within", "229": "without",
    
    # Common responses and interjections
    "230": "yes", "231": "no", "232": "ok", "233": "okay", "234": "sure", "235": "please", "236": "thanks", "237": "hello", "238": "hi", "239": "bye",
    "240": "sorry", "241": "excuse me", "242": "thank you", "243": "you're welcome", "244": "how are you", "245": "I'm fine", "246": "good morning", "247": "good night", "248": "goodbye", "249": "see you later",
    
    # Common question words and phrases
    "250": "what", "251": "who", "252": "how", "253": "which", "254": "whose", "255": "what is", "256": "who is", "257": "how is", "258": "where is", "259": "when is",
    "260": "what are", "261": "who are", "262": "how are", "263": "where are", "264": "when are", "265": "what do", "266": "how do", "267": "why do", "268": "what does", "269": "how does",
    
    # Common nouns
    "270": "time", "271": "person", "272": "year", "273": "way", "274": "day", "275": "thing", "276": "man", "277": "world", "278": "life", "279": "hand",
    "280": "part", "281": "child", "282": "eye", "283": "woman", "284": "place", "285": "work", "286": "week", "287": "case", "288": "point", "289": "government",
    "290": "company", "291": "number", "292": "group", "293": "problem", "294": "fact", "295": "water", "296": "food", "297": "money", "298": "home", "299": "house",
    
    # More common words
    "300": "right", "301": "left", "302": "side", "303": "back", "304": "front", "305": "end", "306": "start", "307": "beginning", "308": "middle", "309": "center",
    "310": "top", "311": "bottom", "312": "inside", "313": "outside", "314": "next", "315": "last", "316": "first", "317": "second", "318": "third", "319": "final",
    "320": "open", "321": "close", "322": "start", "323": "stop", "324": "begin", "325": "finish", "326": "continue", "327": "pause", "328": "wait", "329": "stay",
    
    # Feelings and emotions
    "330": "happy", "331": "sad", "332": "angry", "333": "excited", "334": "tired", "335": "hungry", "336": "thirsty", "337": "sick", "338": "well", "339": "fine",
    "340": "great", "341": "terrible", "342": "amazing", "343": "wonderful", "344": "awful", "345": "beautiful", "346": "ugly", "347": "smart", "348": "stupid", "349": "funny",
    
    # Actions and activities
    "350": "eat", "351": "drink", "352": "sleep", "353": "wake", "354": "buy", "355": "sell", "356": "read", "357": "write", "358": "listen", "359": "watch",
    "360": "learn", "361": "teach", "362": "study", "363": "remember", "364": "forget", "365": "understand", "366": "explain", "367": "show", "368": "hide", "369": "find",
    "370": "lose", "371": "win", "372": "try", "373": "succeed", "374": "fail", "375": "hope", "376": "wish", "377": "want", "378": "need", "379": "like",
    "380": "love", "381": "hate", "382": "prefer", "383": "choose", "384": "decide", "385": "agree", "386": "disagree", "387": "accept", "388": "refuse", "389": "allow",
    
    # Common phrases
    "390": "of course", "391": "no problem", "392": "I don't know", "393": "I think so", "394": "I hope so", "395": "maybe", "396": "probably", "397": "certainly", "398": "definitely", "399": "absolutely",
    "400": "never mind", "401": "it doesn't matter", "402": "that's okay", "403": "that's fine", "404": "that's great", "405": "that's terrible", "406": "I'm sorry", "407": "excuse me", "408": "pardon me", "409": "bless you",
    
    # Technology and modern terms
    "410": "computer", "411": "phone", "412": "internet", "413": "email", "414": "message", "415": "call", "416": "text", "417": "app", "418": "website", "419": "online",
    "420": "password", "421": "username", "422": "login", "423": "logout", "424": "download", "425": "upload", "426": "save", "427": "delete", "428": "copy", "429": "paste",
    
    # Body parts
    "430": "head", "431": "face", "432": "hair", "433": "neck", "434": "shoulder", "435": "arm", "436": "elbow", "437": "wrist", "438": "finger", "439": "thumb",
    "440": "chest", "441": "back", "442": "stomach", "443": "waist", "444": "hip", "445": "leg", "446": "knee", "447": "ankle", "448": "foot", "449": "toe",
    
    # Colors
    "450": "red", "451": "blue", "452": "green", "453": "yellow", "454": "orange", "455": "purple", "456": "pink", "457": "brown", "458": "black", "459": "white",
    "460": "gray", "461": "grey", "462": "silver", "463": "gold", "464": "light", "465": "dark", "466": "bright", "467": "dull", "468": "clear", "469": "cloudy",
    
    # Weather
    "470": "sun", "471": "moon", "472": "star", "473": "sky", "474": "cloud", "475": "rain", "476": "snow", "477": "wind", "478": "storm", "479": "lightning",
    "480": "sunny", "481": "cloudy", "482": "rainy", "483": "snowy", "484": "windy", "485": "stormy", "486": "humid", "487": "dry", "488": "wet", "489": "frozen",
    
    # Food and drink
    "490": "breakfast", "491": "lunch", "492": "dinner", "493": "snack", "494": "meal", "495": "coffee", "496": "tea", "497": "juice", "498": "soda", "499": "beer",
    "500": "wine", "501": "bread", "502": "meat", "503": "fish", "504": "chicken", "505": "beef", "506": "pork", "507": "fruit", "508": "vegetable", "509": "salad",
    "510": "soup", "511": "sandwich", "512": "pizza", "513": "pasta", "514": "rice", "515": "cheese", "516": "milk", "517": "butter", "518": "sugar", "519": "salt",
    
    # Transportation
    "520": "car", "521": "bus", "522": "train", "523": "plane", "524": "ship", "525": "boat", "526": "bike", "527": "walk", "528": "drive", "529": "fly",
    "530": "road", "531": "street", "532": "highway", "533": "bridge", "534": "tunnel", "535": "station", "536": "airport", "537": "port", "538": "parking", "539": "traffic",
    
    # Places
    "540": "city", "541": "town", "542": "village", "543": "country", "544": "state", "545": "province", "546": "region", "547": "area", "548": "zone", "549": "district",
    "550": "school", "551": "university", "552": "college", "553": "hospital", "554": "church", "555": "library", "556": "museum", "557": "park", "558": "store", "559": "shop",
    "560": "restaurant", "561": "hotel", "562": "bank", "563": "office", "564": "factory", "565": "farm", "566": "market", "567": "mall", "568": "theater", "569": "cinema",
    
    # Family and relationships
    "570": "family", "571": "parent", "572": "mother", "573": "father", "574": "son", "575": "daughter", "576": "brother", "577": "sister", "578": "husband", "579": "wife",
    "580": "friend", "581": "neighbor", "582": "colleague", "583": "boss", "584": "employee", "585": "teacher", "586": "student", "587": "doctor", "588": "nurse", "589": "lawyer",
    
    # Money and business
    "590": "dollar", "591": "cent", "592": "price", "593": "cost", "594": "cheap", "595": "expensive", "596": "free", "597": "pay", "598": "buy", "599": "sell",
    "600": "business", "601": "job", "602": "career", "603": "interview", "604": "meeting", "605": "appointment", "606": "schedule", "607": "deadline", "608": "project", "609": "task",
    
    # Education
    "610": "book", "611": "page", "612": "chapter", "613": "word", "614": "sentence", "615": "paragraph", "616": "story", "617": "novel", "618": "poem", "619": "essay",
    "620": "test", "621": "exam", "622": "quiz", "623": "homework", "624": "assignment", "625": "grade", "626": "score", "627": "pass", "628": "fail", "629": "graduate",
    
    # Entertainment
    "630": "music", "631": "song", "632": "dance", "633": "movie", "634": "film", "635": "show", "636": "play", "637": "game", "638": "sport", "639": "team",
    "640": "player", "641": "winner", "642": "loser", "643": "score", "644": "goal", "645": "point", "646": "match", "647": "competition", "648": "tournament", "649": "championship",
    
    # Health
    "650": "health", "651": "medicine", "652": "pill", "653": "vitamin", "654": "exercise", "655": "diet", "656": "weight", "657": "height", "658": "age", "659": "birthday",
    "660": "pain", "661": "hurt", "662": "injury", "663": "accident", "664": "emergency", "665": "hospital", "666": "doctor", "667": "nurse", "668": "patient", "669": "treatment",
    
    # Communication
    "670": "talk", "671": "speak", "672": "say", "673": "tell", "674": "ask", "675": "answer", "676": "reply", "677": "respond", "678": "question", "679": "statement",
    "680": "conversation", "681": "discussion", "682": "argument", "683": "debate", "684": "opinion", "685": "idea", "686": "thought", "687": "mind", "688": "brain", "689": "memory",
    
    # More useful phrases
    "690": "how much", "691": "how many", "692": "how long", "693": "how often", "694": "how far", "695": "how old", "696": "what time", "697": "what day", "698": "what color", "699": "what size",
    "700": "I want", "701": "I need", "702": "I like", "703": "I love", "704": "I hate", "705": "I think", "706": "I know", "707": "I believe", "708": "I hope", "709": "I wish",
    "710": "you are", "711": "you were", "712": "you will", "713": "you can", "714": "you should", "715": "you must", "716": "you may", "717": "you might", "718": "you could", "719": "you would",
    
    # More actions
    "720": "turn on", "721": "turn off", "722": "pick up", "723": "put down", "724": "sit down", "725": "stand up", "726": "lie down", "727": "wake up", "728": "get up", "729": "go to bed",
    "730": "come in", "731": "go out", "732": "come back", "733": "go away", "734": "come here", "735": "go there", "736": "hurry up", "737": "slow down", "738": "calm down", "739": "cheer up",
    
    # Additional common words
    "740": "always", "741": "never", "742": "sometimes", "743": "often", "744": "usually", "745": "rarely", "746": "hardly", "747": "barely", "748": "almost", "749": "quite",
    "750": "very", "751": "really", "752": "actually", "753": "especially", "754": "particularly", "755": "generally", "756": "specifically", "757": "exactly", "758": "approximately", "759": "roughly",
    
    # Emotions and states
    "760": "surprised", "761": "shocked", "762": "amazed", "763": "confused", "764": "worried", "765": "nervous", "766": "calm", "767": "relaxed", "768": "stressed", "769": "busy",
    "770": "free", "771": "available", "772": "ready", "773": "finished", "774": "done", "775": "complete", "776": "incomplete", "777": "perfect", "778": "broken", "779": "fixed",
    
    # More descriptive words
    "780": "important", "781": "interesting", "782": "boring", "783": "exciting", "784": "dangerous", "785": "safe", "786": "careful", "787": "careless", "788": "helpful", "789": "useless",
    "790": "useful", "791": "necessary", "792": "optional", "793": "required", "794": "forbidden", "795": "allowed", "796": "possible", "797": "impossible", "798": "probable", "799": "unlikely",
    
    # Technology terms
    "800": "computer", "801": "laptop", "802": "desktop", "803": "tablet", "804": "smartphone", "805": "keyboard", "806": "mouse", "807": "screen", "808": "monitor", "809": "printer",
    "810": "software", "811": "hardware", "812": "program", "813": "application", "814": "system", "815": "network", "816": "internet", "817": "wifi", "818": "bluetooth", "819": "cable",
    
    # More time expressions
    "820": "morning", "821": "afternoon", "822": "evening", "823": "night", "824": "midnight", "825": "noon", "826": "hour", "827": "minute", "828": "second", "829": "moment",
    "830": "early", "831": "late", "832": "on time", "833": "in time", "834": "before", "835": "after", "836": "during", "837": "while", "838": "until", "839": "since",
    
    # Locations and directions
    "840": "north", "841": "south", "842": "east", "843": "west", "844": "northeast", "845": "northwest", "846": "southeast", "847": "southwest", "848": "straight", "849": "turn",
    "850": "corner", "851": "intersection", "852": "block", "853": "mile", "854": "kilometer", "855": "meter", "856": "foot", "857": "inch", "858": "yard", "859": "distance",
    
    # Weather and nature
    "860": "tree", "861": "flower", "862": "grass", "863": "leaf", "864": "branch", "865": "root", "866": "seed", "867": "plant", "868": "garden", "869": "forest",
    "870": "mountain", "871": "hill", "872": "valley", "873": "river", "874": "lake", "875": "ocean", "876": "sea", "877": "beach", "878": "desert", "879": "island",
    
    # Clothing
    "880": "clothes", "881": "shirt", "882": "pants", "883": "dress", "884": "skirt", "885": "jacket", "886": "coat", "887": "shoes", "888": "socks", "889": "hat",
    "890": "wear", "891": "put on", "892": "take off", "893": "dress up", "894": "undress", "895": "fashion", "896": "style", "897": "color", "898": "size", "899": "fit",
    
    # Final common terms
    "900": "problem", "901": "solution", "902": "answer", "903": "question", "904": "issue", "905": "trouble", "906": "difficulty", "907": "challenge", "908": "opportunity", "909": "chance",
    "910": "choice", "911": "option", "912": "decision", "913": "result", "914": "consequence", "915": "effect", "916": "cause", "917": "reason", "918": "purpose", "919": "goal",
    "920": "plan", "921": "idea", "922": "suggestion", "923": "advice", "924": "tip", "925": "hint", "926": "clue", "927": "sign", "928": "signal", "929": "warning",
    "930": "danger", "931": "risk", "932": "threat", "933": "protection", "934": "safety", "935": "security", "936": "peace", "937": "war", "938": "fight", "939": "battle",
    "940": "victory", "941": "defeat", "942": "success", "943": "failure", "944": "progress", "945": "improvement", "946": "development", "947": "growth", "948": "change", "949": "difference",
    "950": "same", "951": "similar", "952": "different", "953": "opposite", "954": "reverse", "955": "forward", "956": "backward", "957": "upward", "958": "downward", "959": "sideways",
    "960": "increase", "961": "decrease", "962": "add", "963": "subtract", "964": "multiply", "965": "divide", "966": "equal", "967": "plus", "968": "minus", "969": "total",
    "970": "part", "971": "whole", "972": "half", "973": "quarter", "974": "third", "975": "percent", "976": "percentage", "977": "ratio", "978": "proportion", "979": "amount",
    "980": "quantity", "981": "quality", "982": "standard", "983": "level", "984": "degree", "985": "grade", "986": "class", "987": "category", "988": "type", "989": "kind",
    "990": "sort", "991": "variety", "992": "version", "993": "model", "994": "example", "995": "sample", "996": "instance", "997": "case", "998": "situation", "999": "condition"
}

# Alphanumeric codes for moderately common terms (A01-Z99)
ALPHANUMERIC_MAPPINGS = {
    # Questions and inquiry phrases
    "A01": "what do you think", "A02": "do you understand", "A03": "can you help me", "A04": "would you like", "A05": "are you sure",
    "A06": "how do you feel", "A07": "what happened", "A08": "where did you go", "A09": "why did you", "A10": "when will you",
    "A11": "how can I", "A12": "what should I", "A13": "where should I", "A14": "why should I", "A15": "when should I",
    "A16": "do you know how", "A17": "do you know what", "A18": "do you know where", "A19": "do you know why", "A20": "do you know when",
    
    # Response and reaction phrases
    "B01": "I understand", "B02": "I don't understand", "B03": "that makes sense", "B04": "that's interesting", "B05": "I see what you mean",
    "B06": "let me think", "B07": "I'm not sure", "B08": "that's a good point", "B09": "you're absolutely right", "B10": "I disagree with that",
    "B11": "I have a question", "B12": "I have an idea", "B13": "I need help", "B14": "I'm confused", "B15": "I'm worried",
    "B16": "that's perfect", "B17": "that's terrible", "B18": "that's amazing", "B19": "that's awful", "B20": "that's wonderful",
    
    # Connector phrases and transitions
    "C01": "in addition", "C02": "furthermore", "C03": "moreover", "C04": "however", "C05": "nevertheless",
    "C06": "on the other hand", "C07": "as a result", "C08": "therefore", "C09": "consequently", "C10": "in conclusion",
    "C11": "for example", "C12": "for instance", "C13": "such as", "C14": "in other words", "C15": "that is to say",
    "C16": "first of all", "C17": "second of all", "C18": "last but not least", "C19": "in the beginning", "C20": "at the end",
    
    # Action and process phrases
    "D01": "let's get started", "D02": "let's continue", "D03": "let's try again", "D04": "let's move on", "D05": "let's take a break",
    "D06": "I need to go", "D07": "I have to leave", "D08": "I'll be right back", "D09": "please wait a moment", "D10": "just a second",
    "D11": "hurry up please", "D12": "take your time", "D13": "don't worry about it", "D14": "it's not a problem", "D15": "everything is fine",
    "D16": "pay attention", "D17": "listen carefully", "D18": "look at this", "D19": "think about it", "D20": "remember this",
    
    # Emotional and social expressions
    "E01": "I'm so happy", "E02": "I'm very sad", "E03": "I'm really angry", "E04": "I'm quite tired", "E05": "I'm extremely excited",
    "E06": "congratulations", "E07": "good luck", "E08": "best wishes", "E09": "happy birthday", "E10": "merry christmas",
    "E11": "I miss you", "E12": "I love you", "E13": "I care about you", "E14": "I'm proud of you", "E15": "I believe in you",
    "E16": "don't give up", "E17": "keep trying", "E18": "you can do it", "E19": "well done", "E20": "great job",
    
    # Professional and business phrases
    "F01": "I would like to", "F02": "I need to discuss", "F03": "let's schedule a meeting", "F04": "I'll send you an email", "F05": "please review this",
    "F06": "according to", "F07": "based on", "F08": "in terms of", "F09": "with regard to", "F10": "concerning",
    "F11": "as mentioned before", "F12": "as we discussed", "F13": "to summarize", "F14": "in summary", "F15": "to conclude",
    "F16": "I appreciate your", "F17": "thank you for your", "F18": "I look forward to", "F19": "please let me know", "F20": "feel free to",
    
    # Technology and digital phrases
    "G01": "artificial intelligence", "G02": "machine learning", "G03": "data analysis", "G04": "cloud computing", "G05": "cyber security",
    "G06": "social media", "G07": "mobile device", "G08": "operating system", "G09": "user interface", "G10": "search engine",
    "G11": "video conference", "G12": "online meeting", "G13": "digital marketing", "G14": "e-commerce", "G15": "blockchain",
    "G16": "virtual reality", "G17": "augmented reality", "G18": "internet of things", "G19": "big data", "G20": "automation",
    
    # Health and medical terms
    "H01": "health insurance", "H02": "medical examination", "H03": "prescription medicine", "H04": "physical therapy", "H05": "mental health",
    "H06": "blood pressure", "H07": "heart rate", "H08": "body temperature", "H09": "immune system", "H10": "nutritional value",
    "H11": "side effects", "H12": "allergic reaction", "H13": "chronic condition", "H14": "acute symptoms", "H15": "preventive care",
    "H16": "follow up appointment", "H17": "second opinion", "H18": "emergency room", "H19": "intensive care", "H20": "recovery process",
    
    # Education and learning phrases
    "I01": "distance learning", "I02": "online course", "I03": "research project", "I04": "group assignment", "I05": "final examination",
    "I06": "academic performance", "I07": "learning objective", "I08": "study materials", "I09": "educational resources", "I10": "curriculum development",
    "I11": "student engagement", "I12": "classroom management", "I13": "assessment criteria", "I14": "grading system", "I15": "peer review",
    "I16": "critical thinking", "I17": "problem solving", "I18": "creative writing", "I19": "public speaking", "I20": "time management",
    
    # Travel and transportation
    "J01": "flight schedule", "J02": "departure time", "J03": "arrival gate", "J04": "boarding pass", "J05": "luggage claim",
    "J06": "passport control", "J07": "customs declaration", "J08": "hotel reservation", "J09": "room service", "J10": "check in time",
    "J11": "public transportation", "J12": "taxi service", "J13": "rental car", "J14": "gas station", "J15": "parking meter",
    "J16": "traffic jam", "J17": "road construction", "J18": "speed limit", "J19": "highway exit", "J20": "toll booth",
    
    # Food and dining
    "K01": "restaurant menu", "K02": "daily special", "K03": "wine list", "K04": "appetizer", "K05": "main course",
    "K06": "dessert menu", "K07": "vegetarian option", "K08": "gluten free", "K09": "organic ingredients", "K10": "local produce",
    "K11": "table reservation", "K12": "waiting list", "K13": "take out order", "K14": "delivery service", "K15": "tip included",
    "K16": "dietary restrictions", "K17": "food allergy", "K18": "calorie count", "K19": "nutritional information", "K20": "cooking method",
    
    # Shopping and commerce
    "L01": "shopping list", "L02": "price comparison", "L03": "discount coupon", "L04": "special offer", "L05": "limited time",
    "L06": "customer service", "L07": "return policy", "L08": "warranty information", "L09": "installation service", "L10": "delivery charge",
    "L11": "payment method", "L12": "credit card", "L13": "cash payment", "L14": "online shopping", "L15": "mobile payment",
    "L16": "product review", "L17": "customer rating", "L18": "brand comparison", "L19": "quality assurance", "L20": "satisfaction guarantee",
    
    # Entertainment and leisure
    "M01": "movie theater", "M02": "concert hall", "M03": "sports stadium", "M04": "amusement park", "M05": "art gallery",
    "M06": "live performance", "M07": "streaming service", "M08": "video game", "M09": "board game", "M10": "outdoor activity",
    "M11": "weekend plans", "M12": "vacation destination", "M13": "tourist attraction", "M14": "guided tour", "M15": "adventure sport",
    "M16": "music festival", "M17": "cultural event", "M18": "local tradition", "M19": "seasonal celebration", "M20": "holiday season",
    
    # Home and family
    "N01": "household chores", "N02": "grocery shopping", "N03": "home improvement", "N04": "interior design", "N05": "garden maintenance",
    "N06": "family gathering", "N07": "birthday party", "N08": "wedding anniversary", "N09": "school pickup", "N10": "bedtime story",
    "N11": "morning routine", "N12": "evening schedule", "N13": "weekend activity", "N14": "family vacation", "N15": "holiday tradition",
    "N16": "pet care", "N17": "house cleaning", "N18": "meal preparation", "N19": "laundry day", "N20": "bill payment",
    
    # Work and career
    "O01": "job interview", "O02": "career development", "O03": "professional growth", "O04": "skill assessment", "O05": "performance review",
    "O06": "team building", "O07": "project management", "O08": "deadline pressure", "O09": "work life balance", "O10": "remote work",
    "O11": "business meeting", "O12": "client presentation", "O13": "sales target", "O14": "market research", "O15": "competitive analysis",
    "O16": "budget planning", "O17": "cost reduction", "O18": "quality improvement", "O19": "process optimization", "O20": "strategic planning",
    
    # Communication and relationships
    "P01": "personal relationship", "P02": "social interaction", "P03": "communication skills", "P04": "conflict resolution", "P05": "team collaboration",
    "P06": "active listening", "P07": "constructive feedback", "P08": "emotional intelligence", "P09": "cultural sensitivity", "P10": "mutual respect",
    "P11": "common interest", "P12": "shared experience", "P13": "different perspective", "P14": "open minded", "P15": "personal space",
    "P16": "quality time", "P17": "deep conversation", "P18": "meaningful connection", "P19": "trust building", "P20": "long term commitment",
    
    # Science and research
    "Q01": "scientific method", "Q02": "research hypothesis", "Q03": "experimental design", "Q04": "data collection", "Q05": "statistical analysis",
    "Q06": "peer review process", "Q07": "literature review", "Q08": "research findings", "Q09": "conclusion summary", "Q10": "future research",
    "Q11": "laboratory equipment", "Q12": "measurement accuracy", "Q13": "control variable", "Q14": "sample size", "Q15": "error margin",
    "Q16": "theoretical framework", "Q17": "practical application", "Q18": "innovation process", "Q19": "technology transfer", "Q20": "knowledge sharing",
    
    # Environment and sustainability
    "R01": "environmental protection", "R02": "climate change", "R03": "renewable energy", "R04": "sustainable development", "R05": "carbon footprint",
    "R06": "waste management", "R07": "recycling program", "R08": "energy efficiency", "R09": "water conservation", "R10": "biodiversity",
    "R11": "ecosystem balance", "R12": "natural resources", "R13": "pollution control", "R14": "green technology", "R15": "eco friendly",
    "R16": "environmental impact", "R17": "conservation effort", "R18": "wildlife protection", "R19": "habitat preservation", "R20": "sustainable living",
    
    # Finance and economics
    "S01": "financial planning", "S02": "investment strategy", "S03": "market analysis", "S04": "economic growth", "S05": "inflation rate",
    "S06": "interest rate", "S07": "exchange rate", "S08": "stock market", "S09": "real estate", "S10": "insurance policy",
    "S11": "retirement savings", "S12": "emergency fund", "S13": "debt management", "S14": "credit score", "S15": "loan application",
    "S16": "tax preparation", "S17": "budget allocation", "S18": "expense tracking", "S19": "income statement", "S20": "financial advisor",
    
    # Legal and governance
    "T01": "legal advice", "T02": "court hearing", "T03": "legal document", "T04": "contract agreement", "T05": "intellectual property",
    "T06": "privacy rights", "T07": "consumer protection", "T08": "regulatory compliance", "T09": "due process", "T10": "legal precedent",
    "T11": "government policy", "T12": "public service", "T13": "civic duty", "T14": "voting rights", "T15": "democratic process",
    "T16": "law enforcement", "T17": "judicial system", "T18": "constitutional rights", "T19": "legislative process", "T20": "political participation",
    
    # Sports and fitness
    "U01": "physical fitness", "U02": "exercise routine", "U03": "training program", "U04": "athletic performance", "U05": "sports equipment",
    "U06": "team strategy", "U07": "competitive spirit", "U08": "fair play", "U09": "injury prevention", "U10": "recovery time",
    "U11": "professional athlete", "U12": "amateur sport", "U13": "Olympic games", "U14": "world championship", "U15": "local tournament",
    "U16": "fitness goal", "U17": "personal best", "U18": "team effort", "U19": "individual achievement", "U20": "sport psychology",
    
    # Art and culture
    "V01": "artistic expression", "V02": "creative process", "V03": "cultural heritage", "V04": "traditional art", "V05": "modern design",
    "V06": "museum exhibition", "V07": "art collection", "V08": "cultural exchange", "V09": "artistic talent", "V10": "creative inspiration",
    "V11": "performance art", "V12": "visual arts", "V13": "musical composition", "V14": "literary work", "V15": "dramatic performance",
    "V16": "cultural diversity", "V17": "artistic movement", "V18": "aesthetic value", "V19": "cultural significance", "V20": "artistic legacy",
    
    # Philosophy and spirituality
    "W01": "philosophical question", "W02": "moral dilemma", "W03": "ethical consideration", "W04": "spiritual journey", "W05": "personal growth",
    "W06": "life purpose", "W07": "inner peace", "W08": "mindful living", "W09": "self reflection", "W10": "wisdom seeking",
    "W11": "truth seeking", "W12": "meaning of life", "W13": "human nature", "W14": "consciousness", "W15": "enlightenment",
    "W16": "meditation practice", "W17": "spiritual guidance", "W18": "moral compass", "W19": "value system", "W20": "belief structure",
    
    # Psychology and behavior
    "X01": "human behavior", "X02": "psychological study", "X03": "mental process", "X04": "cognitive function", "X05": "emotional response",
    "X06": "personality trait", "X07": "behavioral pattern", "X08": "social psychology", "X09": "developmental stage", "X10": "learning process",
    "X11": "memory formation", "X12": "decision making", "X13": "problem solving", "X14": "creative thinking", "X15": "analytical mind",
    "X16": "stress management", "X17": "coping mechanism", "X18": "resilience building", "X19": "emotional regulation", "X20": "mental wellness",
    
    # Future and innovation
    "Y01": "future technology", "Y02": "innovative solution", "Y03": "emerging trend", "Y04": "technological advancement", "Y05": "digital transformation",
    "Y06": "smart city", "Y07": "autonomous vehicle", "Y08": "space exploration", "Y09": "quantum computing", "Y10": "biotechnology",
    "Y11": "nanotechnology", "Y12": "renewable resources", "Y13": "sustainable future", "Y14": "global connectivity", "Y15": "human enhancement",
    "Y16": "artificial consciousness", "Y17": "virtual world", "Y18": "augmented human", "Y19": "digital society", "Y20": "technological singularity",
    
    # Miscellaneous important phrases
    "Z01": "emergency situation", "Z02": "urgent matter", "Z03": "immediate attention", "Z04": "top priority", "Z05": "critical thinking",
    "Z06": "important decision", "Z07": "significant change", "Z08": "major improvement", "Z09": "essential element", "Z10": "fundamental principle",
    "Z11": "basic requirement", "Z12": "minimum standard", "Z13": "maximum capacity", "Z14": "optimal solution", "Z15": "perfect balance",
    "Z16": "complete understanding", "Z17": "total agreement", "Z18": "full cooperation", "Z19": "absolute certainty", "Z20": "final decision",
    "Z21": "no questions asked", "Z22": "without a doubt", "Z23": "beyond belief", "Z24": "against all odds", "Z25": "once in a lifetime",
    "Z26": "all things considered", "Z27": "at the end of the day", "Z28": "when all is said and done", "Z29": "last but not least", "Z30": "better late than never",
    "Z31": "time will tell", "Z32": "practice makes perfect", "Z33": "actions speak louder", "Z34": "knowledge is power", "Z35": "honesty is best",
    "Z36": "safety first", "Z37": "quality over quantity", "Z38": "less is more", "Z39": "more or less", "Z40": "sooner or later",
    "Z41": "here and there", "Z42": "now and then", "Z43": "back and forth", "Z44": "up and down", "Z45": "in and out",
    "Z46": "on and off", "Z47": "hot and cold", "Z48": "black and white", "Z49": "give and take", "Z50": "trial and error",
    "Z51": "cause and effect", "Z52": "supply and demand", "Z53": "pros and cons", "Z54": "win or lose", "Z55": "sink or swim",
    "Z56": "do or die", "Z57": "make or break", "Z58": "hit or miss", "Z59": "all or nothing", "Z60": "now or never",
    "Z61": "take it or leave it", "Z62": "love it or hate it", "Z63": "use it or lose it", "Z64": "adapt or perish", "Z65": "evolve or die",
    "Z66": "learn or burn", "Z67": "grow or go", "Z68": "stay or leave", "Z69": "fight or flight", "Z70": "feast or famine",
    "Z71": "boom or bust", "Z72": "rich or poor", "Z73": "young or old", "Z74": "new or used", "Z75": "fresh or stale",
    "Z76": "real or fake", "Z77": "true or false", "Z78": "right or wrong", "Z79": "good or bad", "Z80": "fast or slow",
    "Z81": "big or small", "Z82": "long or short", "Z83": "high or low", "Z84": "near or far", "Z85": "early or late",
    "Z86": "before or after", "Z87": "above or below", "Z88": "inside or outside", "Z89": "front or back", "Z90": "left or right",
    "Z91": "top or bottom", "Z92": "first or last", "Z93": "best or worst", "Z94": "most or least", "Z95": "some or all",
    "Z96": "few or many", "Z97": "little or much", "Z98": "less or more", "Z99": "emergency stop"
}

# 4-digit codes for longer words, technical terms, and expansion (0001-9999)
FOUR_DIGIT_MAPPINGS = {
    # Technical and scientific terms
    "0001": "artificial", "0002": "intelligence", "0003": "technology", "0004": "computer", "0005": "internet",
    "0006": "programming", "0007": "software", "0008": "hardware", "0009": "database", "0010": "algorithm",
    "0011": "automation", "0012": "optimization", "0013": "innovation", "0014": "development", "0015": "implementation",
    "0016": "configuration", "0017": "integration", "0018": "synchronization", "0019": "authentication", "0020": "authorization",
    
    # Medical and health terms
    "0021": "medicine", "0022": "treatment", "0023": "diagnosis", "0024": "therapy", "0025": "surgery",
    "0026": "prescription", "0027": "symptoms", "0028": "disease", "0029": "infection", "0030": "prevention",
    "0031": "rehabilitation", "0032": "recovery", "0033": "consultation", "0034": "examination", "0035": "vaccination",
    "0036": "medication", "0037": "antibiotics", "0038": "anesthesia", "0039": "radiology", "0040": "pathology",
    
    # Business and economics
    "0041": "management", "0042": "administration", "0043": "organization", "0044": "corporation", "0045": "enterprise",
    "0046": "investment", "0047": "marketing", "0048": "advertisement", "0049": "promotion", "0050": "distribution",
    "0051": "production", "0052": "manufacturing", "0053": "operation", "0054": "maintenance", "0055": "supervision",
    "0056": "coordination", "0057": "collaboration", "0058": "negotiation", "0059": "transaction", "0060": "acquisition",
    
    # Education and academic terms
    "0061": "education", "0062": "academic", "0063": "university", "0064": "research", "0065": "scholarship",
    "0066": "curriculum", "0067": "semester", "0068": "graduation", "0069": "certificate", "0070": "diploma",
    "0071": "professor", "0072": "instructor", "0073": "lecturer", "0074": "tutor", "0075": "mentor",
    "0076": "laboratory", "0077": "library", "0078": "textbook", "0079": "assignment", "0080": "presentation",
    
    # Legal and governmental terms
    "0081": "government", "0082": "legislation", "0083": "regulation", "0084": "constitution", "0085": "amendment",
    "0086": "parliament", "0087": "congress", "0088": "senate", "0089": "representative", "0090": "democracy",
    "0091": "election", "0092": "candidate", "0093": "campaign", "0094": "political", "0095": "citizen",
    "0096": "jurisdiction", "0097": "litigation", "0098": "arbitration", "0099": "mediation", "0100": "settlement",
    
    # Environmental and scientific terms
    "0101": "environment", "0102": "ecosystem", "0103": "biodiversity", "0104": "conservation", "0105": "pollution",
    "0106": "sustainability", "0107": "renewable", "0108": "recycling", "0109": "emission", "0110": "carbon",
    "0111": "greenhouse", "0112": "atmosphere", "0113": "temperature", "0114": "humidity", "0115": "precipitation",
    "0116": "geography", "0117": "geology", "0118": "meteorology", "0119": "astronomy", "0120": "physics",
    
    # Transportation and logistics
    "0121": "transportation", "0122": "logistics", "0123": "delivery", "0124": "shipping", "0125": "freight",
    "0126": "passenger", "0127": "vehicle", "0128": "automobile", "0129": "motorcycle", "0130": "bicycle",
    "0131": "aviation", "0132": "navigation", "0133": "destination", "0134": "departure", "0135": "arrival",
    "0136": "schedule", "0137": "timetable", "0138": "reservation", "0139": "booking", "0140": "confirmation",
    
    # Communication and media
    "0141": "communication", "0142": "information", "0143": "broadcast", "0144": "publication", "0145": "journalism",
    "0146": "television", "0147": "radio", "0148": "newspaper", "0149": "magazine", "0150": "advertisement",
    "0151": "documentary", "0152": "interview", "0153": "reporter", "0154": "photographer", "0155": "editor",
    "0156": "producer", "0157": "director", "0158": "screenwriter", "0159": "cinematography", "0160": "distribution",
    
    # Architecture and construction
    "0161": "architecture", "0162": "construction", "0163": "engineering", "0164": "blueprint", "0165": "foundation",
    "0166": "structure", "0167": "building", "0168": "infrastructure", "0169": "renovation", "0170": "maintenance",
    "0171": "contractor", "0172": "architect", "0173": "engineer", "0174": "designer", "0175": "carpenter",
    "0176": "electrician", "0177": "plumber", "0178": "painter", "0179": "decorator", "0180": "landscaper",
    
    # Arts and entertainment
    "0181": "entertainment", "0182": "performance", "0183": "exhibition", "0184": "festival", "0185": "celebration",
    "0186": "musician", "0187": "composer", "0188": "conductor", "0189": "orchestra", "0190": "symphony",
    "0191": "theater", "0192": "drama", "0193": "comedy", "0194": "tragedy", "0195": "romance",
    "0196": "sculpture", "0197": "painting", "0198": "photography", "0199": "literature", "0200": "poetry",
    
    # Sports and recreation
    "0201": "athletics", "0202": "competition", "0203": "tournament", "0204": "championship", "0205": "professional",
    "0206": "amateur", "0207": "training", "0208": "coaching", "0209": "referee", "0210": "spectator",
    "0211": "stadium", "0212": "gymnasium", "0213": "equipment", "0214": "uniform", "0215": "strategy",
    "0216": "technique", "0217": "performance", "0218": "achievement", "0219": "record", "0220": "victory",
    
    # Food and agriculture
    "0221": "agriculture", "0222": "farming", "0223": "cultivation", "0224": "harvesting", "0225": "irrigation",
    "0226": "fertilizer", "0227": "pesticide", "0228": "organic", "0229": "processing", "0230": "packaging",
    "0231": "nutrition", "0232": "vitamin", "0233": "mineral", "0234": "protein", "0235": "carbohydrate",
    "0236": "ingredient", "0237": "recipe", "0238": "cooking", "0239": "baking", "0240": "preparation",
    
    # Fashion and design
    "0241": "fashion", "0242": "designer", "0243": "clothing", "0244": "textile", "0245": "fabric",
    "0246": "pattern", "0247": "collection", "0248": "boutique", "0249": "accessory", "0250": "jewelry",
    "0251": "cosmetics", "0252": "perfume", "0253": "hairstyle", "0254": "makeup", "0255": "wardrobe",
    "0256": "trendy", "0257": "elegant", "0258": "sophisticated", "0259": "casual", "0260": "formal",
    
    # Psychology and philosophy
    "0261": "psychology", "0262": "philosophy", "0263": "consciousness", "0264": "personality", "0265": "behavior",
    "0266": "motivation", "0267": "emotion", "0268": "cognition", "0269": "perception", "0270": "memory",
    "0271": "learning", "0272": "intelligence", "0273": "creativity", "0274": "imagination", "0275": "intuition",
    "0276": "wisdom", "0277": "knowledge", "0278": "understanding", "0279": "insight", "0280": "enlightenment",
    
    # Geography and travel
    "0281": "geography", "0282": "continent", "0283": "hemisphere", "0284": "latitude", "0285": "longitude",
    "0286": "equator", "0287": "tropical", "0288": "climate", "0289": "landscape", "0290": "terrain",
    "0291": "tourism", "0292": "vacation", "0293": "holiday", "0294": "excursion", "0295": "adventure",
    "0296": "exploration", "0297": "expedition", "0298": "journey", "0299": "pilgrimage", "0300": "migration",
    
    # History and culture
    "0301": "history", "0302": "civilization", "0303": "culture", "0304": "tradition", "0305": "heritage",
    "0306": "ancestor", "0307": "generation", "0308": "century", "0309": "millennium", "0310": "ancient",
    "0311": "medieval", "0312": "renaissance", "0313": "modern", "0314": "contemporary", "0315": "revolution",
    "0316": "evolution", "0317": "development", "0318": "progress", "0319": "advancement", "0320": "transformation",
    
    # Religion and spirituality
    "0321": "religion", "0322": "spirituality", "0323": "worship", "0324": "prayer", "0325": "meditation",
    "0326": "ceremony", "0327": "ritual", "0328": "tradition", "0329": "belief", "0330": "faith",
    "0331": "doctrine", "0332": "scripture", "0333": "theology", "0334": "philosophy", "0335": "morality",
    "0336": "ethics", "0337": "virtue", "0338": "righteousness", "0339": "compassion", "0340": "forgiveness",
    
    # Mathematics and science
    "0341": "mathematics", "0342": "calculation", "0343": "equation", "0344": "formula", "0345": "geometry",
    "0346": "algebra", "0347": "calculus", "0348": "statistics", "0349": "probability", "0350": "analysis",
    "0351": "chemistry", "0352": "biology", "0353": "botany", "0354": "zoology", "0355": "anatomy",
    "0356": "physiology", "0357": "genetics", "0358": "evolution", "0359": "ecology", "0360": "microscopy",
    
    # More technical terms
    "0361": "encryption", "0362": "decryption", "0363": "cybersecurity", "0364": "firewall", "0365": "antivirus",
    "0366": "malware", "0367": "ransomware", "0368": "phishing", "0369": "spoofing", "0370": "hacking",
    "0371": "penetration", "0372": "vulnerability", "0373": "exploitation", "0374": "mitigation", "0375": "prevention",
    "0376": "detection", "0377": "monitoring", "0378": "surveillance", "0379": "intelligence", "0380": "reconnaissance",
    
    # Advanced concepts
    "0381": "artificial", "0382": "mechanical", "0383": "electrical", "0384": "electronic", "0385": "digital",
    "0386": "analog", "0387": "wireless", "0388": "satellite", "0389": "fiber", "0390": "broadband",
    "0391": "bandwidth", "0392": "frequency", "0393": "amplitude", "0394": "wavelength", "0395": "spectrum",
    "0396": "radiation", "0397": "electromagnetic", "0398": "quantum", "0399": "nuclear", "0400": "atomic",
    
    # More professional terms
    "0401": "professional", "0402": "specialist", "0403": "expert", "0404": "consultant", "0405": "advisor",
    "0406": "analyst", "0407": "strategist", "0408": "coordinator", "0409": "supervisor", "0410": "administrator",
    "0411": "executive", "0412": "manager", "0413": "director", "0414": "president", "0415": "chairman",
    "0416": "entrepreneur", "0417": "investor", "0418": "shareholder", "0419": "stakeholder", "0420": "participant",
    
    # Additional concepts
    "0421": "international", "0422": "multinational", "0423": "global", "0424": "universal", "0425": "comprehensive",
    "0426": "extensive", "0427": "intensive", "0428": "exclusive", "0429": "inclusive", "0430": "progressive",
    "0431": "conservative", "0432": "traditional", "0433": "conventional", "0434": "alternative", "0435": "innovative",
    "0436": "revolutionary", "0437": "evolutionary", "0438": "experimental", "0439": "theoretical", "0440": "practical",
    
    # Complex adjectives
    "0441": "extraordinary", "0442": "remarkable", "0443": "outstanding", "0444": "exceptional", "0445": "magnificent",
    "0446": "spectacular", "0447": "incredible", "0448": "unbelievable", "0449": "phenomenal", "0450": "tremendous",
    "0451": "enormous", "0452": "gigantic", "0453": "massive", "0454": "colossal", "0455": "immense",
    "0456": "miniature", "0457": "microscopic", "0458": "infinitesimal", "0459": "negligible", "0460": "insignificant",
    
    # Abstract concepts
    "0461": "existence", "0462": "reality", "0463": "imagination", "0464": "possibility", "0465": "probability",
    "0466": "certainty", "0467": "uncertainty", "0468": "ambiguity", "0469": "clarity", "0470": "confusion",
    "0471": "complexity", "0472": "simplicity", "0473": "sophistication", "0474": "elegance", "0475": "beauty",
    "0476": "harmony", "0477": "balance", "0478": "symmetry", "0479": "proportion", "0480": "perspective",
    
    # Scientific phenomena
    "0481": "phenomenon", "0482": "experiment", "0483": "observation", "0484": "hypothesis", "0485": "theory",
    "0486": "principle", "0487": "mechanism", "0488": "process", "0489": "procedure", "0490": "methodology",
    "0491": "technique", "0492": "approach", "0493": "strategy", "0494": "tactic", "0495": "method",
    "0496": "system", "0497": "framework", "0498": "structure", "0499": "organization", "0500": "arrangement",
    
    # Continue with more terms to reach 1000+ total mappings
    # Adding 500 more entries to reach our target
    "0501": "accomplishment", "0502": "achievement", "0503": "advancement", "0504": "agreement", "0505": "allegiance",
    "0506": "alliance", "0507": "alternative", "0508": "amazement", "0509": "announcement", "0510": "anticipation",
    "0511": "appreciation", "0512": "apprenticeship", "0513": "arrangement", "0514": "association", "0515": "assumption",
    "0516": "assurance", "0517": "atmosphere", "0518": "attachment", "0519": "attendance", "0520": "attraction",
    "0521": "authority", "0522": "availability", "0523": "background", "0524": "breakthrough", "0525": "capability",
    "0526": "catastrophe", "0527": "celebration", "0528": "characteristic", "0529": "circumstance", "0530": "classification",
    "0531": "collaboration", "0532": "combination", "0533": "commentary", "0534": "commercial", "0535": "commission",
    "0536": "commitment", "0537": "committee", "0538": "communication", "0539": "community", "0540": "comparison",
    "0541": "competition", "0542": "completion", "0543": "complicated", "0544": "composition", "0545": "comprehension",
    "0546": "concentration", "0547": "conception", "0548": "conclusion", "0549": "condition", "0550": "conference",
    "0551": "confidence", "0552": "confirmation", "0553": "confusion", "0554": "connection", "0555": "consideration",
    "0556": "consistency", "0557": "constitution", "0558": "construction", "0559": "consultation", "0560": "consumption",
    "0561": "contribution", "0562": "conversation", "0563": "cooperation", "0564": "coordination", "0565": "corporation",
    "0566": "correction", "0567": "correlation", "0568": "correspondence", "0569": "creativity", "0570": "credibility",
    "0571": "curiosity", "0572": "declaration", "0573": "decoration", "0574": "dedication", "0575": "definition",
    "0576": "demonstration", "0577": "department", "0578": "description", "0579": "destination", "0580": "destruction",
    "0581": "determination", "0582": "development", "0583": "difference", "0584": "difficulty", "0585": "dimension",
    "0586": "direction", "0587": "disappearance", "0588": "disappointment", "0589": "discipline", "0590": "discovery",
    "0591": "discussion", "0592": "distribution", "0593": "documentary", "0594": "domination", "0595": "elimination",
    "0596": "emergency", "0597": "employment", "0598": "encouragement", "0599": "engineering", "0600": "enhancement",
    "0601": "entertainment", "0602": "enthusiasm", "0603": "environment", "0604": "equipment", "0605": "establishment",
    "0606": "evaluation", "0607": "examination", "0608": "excitement", "0609": "execution", "0610": "exhibition",
    "0611": "existence", "0612": "expansion", "0613": "expectation", "0614": "experience", "0615": "experiment",
    "0616": "explanation", "0617": "exploration", "0618": "expression", "0619": "extension", "0620": "extraordinary",
    "0621": "fascination", "0622": "flexibility", "0623": "formulation", "0624": "foundation", "0625": "frequency",
    "0626": "generation", "0627": "government", "0628": "graduation", "0629": "guarantee", "0630": "guidance",
    "0631": "identification", "0632": "imagination", "0633": "implication", "0634": "importance", "0635": "impression",
    "0636": "improvement", "0637": "independence", "0638": "indication", "0639": "individual", "0640": "information",
    "0641": "inspiration", "0642": "installation", "0643": "institution", "0644": "instruction", "0645": "integration",
    "0646": "intelligence", "0647": "interaction", "0648": "international", "0649": "interpretation", "0650": "introduction",
    "0651": "investigation", "0652": "involvement", "0653": "journalism", "0654": "leadership", "0655": "legislation",
    "0656": "limitation", "0657": "maintenance", "0658": "management", "0659": "manufacturer", "0660": "measurement",
    "0661": "mechanism", "0662": "membership", "0663": "modification", "0664": "motivation", "0665": "movement",
    "0666": "navigation", "0667": "negotiation", "0668": "neighborhood", "0669": "observation", "0670": "occupation",
    "0671": "operation", "0672": "opportunity", "0673": "organization", "0674": "orientation", "0675": "participation",
    "0676": "partnership", "0677": "performance", "0678": "permission", "0679": "personality", "0680": "perspective",
    "0681": "phenomenon", "0682": "philosophy", "0683": "photograph", "0684": "population", "0685": "possibility",
    "0686": "preparation", "0687": "presentation", "0688": "preservation", "0689": "president", "0690": "prevention",
    "0691": "probability", "0692": "procedure", "0693": "production", "0694": "profession", "0695": "programming",
    "0696": "promotion", "0697": "proportion", "0698": "protection", "0699": "psychology", "0700": "publication",
    "0701": "qualification", "0702": "questionnaire", "0703": "realization", "0704": "recognition", "0705": "recommendation",
    "0706": "registration", "0707": "regulation", "0708": "relationship", "0709": "representation", "0710": "reputation",
    "0711": "requirement", "0712": "resolution", "0713": "responsibility", "0714": "restaurant", "0715": "satisfaction",
    "0716": "scholarship", "0717": "secretary", "0718": "selection", "0719": "significant", "0720": "simulation",
    "0721": "situation", "0722": "specification", "0723": "statement", "0724": "statistics", "0725": "strategy",
    "0726": "structure", "0727": "subscription", "0728": "suggestion", "0729": "supervision", "0730": "technology",
    "0731": "television", "0732": "temperature", "0733": "territory", "0734": "traditional", "0735": "transaction",
    "0736": "transformation", "0737": "transportation", "0738": "treatment", "0739": "understanding", "0740": "university",
    "0741": "vaccination", "0742": "variation", "0743": "vegetation", "0744": "verification", "0745": "vocabulary",
    "0746": "warehouse", "0747": "website", "0748": "withdrawal", "0749": "wonderful", "0750": "workplace",
    
    # Additional technical and specialized terms
    "0751": "acceleration", "0752": "accessibility", "0753": "accumulation", "0754": "acknowledgment", "0755": "acquisition",
    "0756": "activation", "0757": "adaptation", "0758": "administration", "0759": "advertisement", "0760": "affiliation",
    "0761": "aggregation", "0762": "algorithm", "0763": "allocation", "0764": "amendment", "0765": "amplification",
    "0766": "annotation", "0767": "anticipation", "0768": "application", "0769": "appreciation", "0770": "approximation",
    "0771": "architecture", "0772": "arrangement", "0773": "articulation", "0774": "aspiration", "0775": "assessment",
    "0776": "assignment", "0777": "assistance", "0778": "association", "0779": "assumption", "0780": "assurance",
    "0781": "authorization", "0782": "automation", "0783": "availability", "0784": "calculation", "0785": "calibration",
    "0786": "cancellation", "0787": "capability", "0788": "categorization", "0789": "centralization", "0790": "certification",
    "0791": "characterization", "0792": "circulation", "0793": "clarification", "0794": "classification", "0795": "collaboration",
    "0796": "collection", "0797": "combination", "0798": "communication", "0799": "compensation", "0800": "compilation",
    "0801": "completion", "0802": "complexity", "0803": "compliance", "0804": "composition", "0805": "comprehension",
    "0806": "compression", "0807": "computation", "0808": "concentration", "0809": "conceptualization", "0810": "configuration",
    "0811": "confirmation", "0812": "confrontation", "0813": "connection", "0814": "consciousness", "0815": "conservation",
    "0816": "consideration", "0817": "consolidation", "0818": "constitution", "0819": "construction", "0820": "consultation",
    "0821": "consumption", "0822": "contamination", "0823": "continuation", "0824": "contribution", "0825": "conversation",
    "0826": "conversion", "0827": "cooperation", "0828": "coordination", "0829": "corporation", "0830": "correlation",
    "0831": "correspondence", "0832": "crystallization", "0833": "cultivation", "0834": "customization", "0835": "deactivation",
    "0836": "deceleration", "0837": "declaration", "0838": "decompression", "0839": "decoration", "0840": "dedication",
    "0841": "deformation", "0842": "degradation", "0843": "demonstration", "0844": "denomination", "0845": "departure",
    "0846": "deployment", "0847": "depreciation", "0848": "description", "0849": "designation", "0850": "destination",
    "0851": "destruction", "0852": "determination", "0853": "development", "0854": "differentiation", "0855": "digitalization",
    "0856": "dimension", "0857": "direction", "0858": "disappearance", "0859": "disappointment", "0860": "discrimination",
    "0861": "discussion", "0862": "disintegration", "0863": "displacement", "0864": "distribution", "0865": "diversification",
    "0866": "documentation", "0867": "domination", "0868": "dramatization", "0869": "duplication", "0870": "education",
    "0871": "effectiveness", "0872": "elaboration", "0873": "elimination", "0874": "embarkation", "0875": "emergency",
    "0876": "employment", "0877": "encouragement", "0878": "engineering", "0879": "enhancement", "0880": "enlargement",
    "0881": "entertainment", "0882": "enthusiasm", "0883": "environment", "0884": "establishment", "0885": "estimation",
    "0886": "evaluation", "0887": "examination", "0888": "excavation", "0889": "excitement", "0890": "execution",
    "0891": "exhibition", "0892": "existence", "0893": "expansion", "0894": "expectation", "0895": "expedition",
    "0896": "experience", "0897": "experimentation", "0898": "explanation", "0899": "exploration", "0900": "expression",
    "0901": "extension", "0902": "extraction", "0903": "fabrication", "0904": "facilitation", "0905": "fascination",
    "0906": "federation", "0907": "fermentation", "0908": "fertilization", "0909": "figuration", "0910": "filtration",
    "0911": "finalization", "0912": "fingerprint", "0913": "flexibility", "0914": "fluctuation", "0915": "formalization",
    "0916": "formation", "0917": "formulation", "0918": "foundation", "0919": "fragmentation", "0920": "frequency",
    "0921": "frustration", "0922": "functionality", "0923": "fundamentals", "0924": "generalization", "0925": "generation",
    "0926": "globalization", "0927": "government", "0928": "graduation", "0929": "gravitation", "0930": "guarantee",
    "0931": "habituation", "0932": "harmonization", "0933": "headquarters", "0934": "hospitalization", "0935": "hybridization",
    "0936": "identification", "0937": "illustration", "0938": "imagination", "0939": "imitation", "0940": "immigration",
    "0941": "implementation", "0942": "implication", "0943": "importation", "0944": "impression", "0945": "improvement",
    "0946": "inauguration", "0947": "inclination", "0948": "incorporation", "0949": "independence", "0950": "indication",
    "0951": "individualization", "0952": "industrialization", "0953": "inflammation", "0954": "information", "0955": "initialization",
    "0956": "innovation", "0957": "inscription", "0958": "inspiration", "0959": "installation", "0960": "institution",
    "0961": "instruction", "0962": "instrumentation", "0963": "integration", "0964": "intelligence", "0965": "intensification",
    "0966": "interaction", "0967": "interconnection", "0968": "interference", "0969": "international", "0970": "interpretation",
    "0971": "interruption", "0972": "intersection", "0973": "intervention", "0974": "introduction", "0975": "investigation",
    "0976": "involvement", "0977": "irrigation", "0978": "isolation", "0979": "journalism", "0980": "justification",
    "0981": "laboratory", "0982": "leadership", "0983": "legislation", "0984": "liberation", "0985": "limitation",
    "0986": "liquidation", "0987": "localization", "0988": "lubrication", "0989": "magnetization", "0990": "maintenance",
    "0991": "management", "0992": "manifestation", "0993": "manipulation", "0994": "manufacturing", "0995": "materialization",
    "0996": "maximization", "0997": "measurement", "0998": "mechanization", "0999": "membership"
}

# Combine all mappings into the complete BotSpeak dictionary
def generate_botspeak_dictionary():
    """Generate the complete BotSpeak dictionary combining all code ranges"""
    botspeak_dict = {}
    
    # Add numeric mappings (100-999)
    botspeak_dict.update(NUMERIC_MAPPINGS)
    
    # Add alphanumeric mappings (A01-Z99)
    botspeak_dict.update(ALPHANUMERIC_MAPPINGS)
    
    # Add 4-digit mappings (0001-9999)
    botspeak_dict.update(FOUR_DIGIT_MAPPINGS)
    
    return botspeak_dict

# Generate the complete dictionary
botspeak_dict = generate_botspeak_dictionary()

# Create reverse mapping for decoding
def create_reverse_mapping(dictionary):
    """Create reverse mapping for decoding codes back to text"""
    return {value: key for key, value in dictionary.items()}

reverse_botspeak_dict = create_reverse_mapping(botspeak_dict)

# Validation functions
def validate_dictionary():
    """Validate the dictionary for duplicates and completeness"""
    codes = list(botspeak_dict.keys())
    values = list(botspeak_dict.values())
    
    # Check for duplicate codes
    if len(codes) != len(set(codes)):
        print("WARNING: Duplicate codes found!")
        return False
    
    # Check for duplicate values
    if len(values) != len(set(values)):
        print("WARNING: Duplicate values found!")
        return False
    
    print(f"Dictionary validation passed!")
    print(f"Total entries: {len(botspeak_dict)}")
    print(f"Numeric codes (100-999): {len(NUMERIC_MAPPINGS)}")
    print(f"Alphanumeric codes (A01-Z99): {len(ALPHANUMERIC_MAPPINGS)}")
    print(f"4-digit codes (0001-9999): {len(FOUR_DIGIT_MAPPINGS)}")
    
    return True

# Print statistics
def print_dictionary_stats():
    """Print comprehensive statistics about the dictionary"""
    validate_dictionary()
    
    print("\n=== BotSpeak Dictionary Statistics ===")
    print(f"Total unique mappings: {len(botspeak_dict)}")
    print(f"Code ranges covered:")
    print(f"  - Numeric (100-999): {len(NUMERIC_MAPPINGS)} entries")
    print(f"  - Alphanumeric (A01-Z99): {len(ALPHANUMERIC_MAPPINGS)} entries") 
    print(f"  - 4-digit (0001-9999): {len(FOUR_DIGIT_MAPPINGS)} entries")
    
    # Sample entries from each range
    print(f"\nSample entries:")
    print(f"  Numeric: {dict(list(NUMERIC_MAPPINGS.items())[:3])}")
    print(f"  Alphanumeric: {dict(list(ALPHANUMERIC_MAPPINGS.items())[:3])}")
    print(f"  4-digit: {dict(list(FOUR_DIGIT_MAPPINGS.items())[:3])}")

if __name__ == "__main__":
    print_dictionary_stats()
