'''
Holds String variables that are used in quizApp to maintain readability of code
'''

questions = [
    "Which one better describes your face shape?",
    "How would you describe your jawline?",
    "How does your face's lower third look?",
    "In general, would you say your facial features are round or angular?",
    "What is your eye shape?",
    "What kind of lids do you have?",
    "What's your nose like?",
    "What shape are your brows?",
    "What shape are your lips?",
    "How would you describe the size of your eyes?",
    "Which one best describes the height of your nose?",
    "Choose the description that fits the width of your nose alar.",
    "Which statement is true about your mouth's size?",
    "What's your style like?",
    "How old are you?"
]

options = [
    [
        "rounded", 
        "oval", 
        "pear", 
        "square", 
        "heart", 
        "diamond", 
        "rectangle", 
        "oblong"
    ],
    [
        "very soft and rounded", 
        "slightly soft and rounded", 
        "rounded but soft", 
        "slightly angular but mostly soft", 
        "not too round", 
        "not too sharp", 
        "slightly sharp and angular",
        "extremely bony"
    ],
    [
        "it's visibly shorter than other parts of my face", 
        "it’s slightly shorter", 
        "it’s almost equal to other parts", 
        "it’s slightly longer than the other parts", 
        "it’s equal to other parts", 
        "it’s longer than the other parts", 
        "it’s visibly longer (but slightly rounded)", 
        "it’s longer than the other parts (and it’s sharp)"
    ],
    [
        "very rounded", 
        "rounded", 
        "slightly rounded", 
        "slightly rounded in some areas", 
        "not too rounded, not too sharp", 
        "slightly angular in some areas", 
        "sharp (in most areas)", 
        "very sharp and angular"
    ],
    [
        "round", 
        "almond", 
        "upturned", 
        "hooded", 
        "slightly rounded", 
        "downturned", 
        "protruding", 
        "wide-set"
    ],
    [
        "thick double eyelids", 
        "thin double eyelids", 
        "moderate double eyelids", 
        "hooded eyelids", 
        "tempered eyelids", 
        "partial eyelids", 
        "monolid", 
        "no eyelid"
    ],
    [
        "rounded and soft", 
        "slightly rounded and soft", 
        "moderately soft and rounded", 
        "slightly sharp but soft", 
        "not too rounded, not too sharp", 
        "slightly sharp and angular", 
        "very sharp and angular", 
        "bony, sharp, and very prominent"
    ],
    [
        "very arched and soft", 
        "slightly arched and soft", 
        "moderately arched and soft", 
        "slightly straight but soft", 
        "not too arched, not too soft", 
        "very sharp and angular", 
        "very arched but also very angular", 
        "straight, sharp, and prominent"
    ],
    [
        "small and rounded", 
        "not so small but very rounded", 
        "slightly wide but very rounded", 
        "slightly small but not so rounded", 
        "not too round, not too angular", 
        "slightly small but angular", 
        "wide and angular", 
        "very wide, sharp, and prominent"
    ],
    [
        "very wide and round", 
        "slightly wide and round", 
        "moderately wide but not too round", 
        "slightly narrow but also rounded", 
        "not too wide, not too narrow", 
        "slightly narrow", 
        "very narrow", 
        "hooded and narrow"
    ],
    [
        "very short", 
        "slightly short", 
        "moderately short", 
        "slightly long", 
        "not too short, not too long",
        "long", 
        "very long", 
        "long, bony, and prominent"
    ],
    [
        "it’s smaller than the distance between my eyes", 
        "it’s slightly smaller than the distance between my eyes", 
        "it’s moderately smaller than the distance between my eyes", 
        "it’s slightly wider than the distance between my eyes", 
        "it’s equal to the distance between my eyes", 
        "it’s visibly wider than the distance between my eyes", 
        "it’s very wider than the distance between my eyes", 
        "it’s wider, bony, and prominent"
    ],
    [
        "visibly smaller than the rim of my pupils.", 
        "slightly smaller than the rim of my pupils", 
        "moderately smaller than the rim of my pupils", 
        "slightly wider than the rim of my pupils", 
        "not too wide, not too small", 
        "moderately wider than the rim of my pupils", 
        "visibly wider than the rim of my pupils", 
        "wide, angular, and prominent"
    ],
    [
        "cute", 
        "chic", 
        "sexy", 
        "grunge", 
        "casual", 
        "trendy", 
        "classic", 
        "formal"
    ],
    [
        "16 or younger", 
        "17-19", 
        "20-24", 
        "25-29", 
        "30-35", 
        "36-39", 
        "40-45", 
        "46 or older"
    ]
]

descriptions = {
    'Ingenue' : "The Ingenue archetype resembles childlike, gentle, and delicate beauty. It’s the optimal choice for a refreshing-youthful feminine look, as it maintains the round features and creates a fleshy mid-face and plump limps. With more rounded and moderately angular, lower visual weight features. The best makeup styles for you are Energetic Cute, Fiercy Cute, and Sweet & Cool looks.",
    'Elegant' : "Elegant archetype resembles a gentle, serene, graceful, and delicate persona. It is more formal than the Ingenue archetype, focusing on your femininity rather than your childlike beauty. Based on your archetypes, the best makeup styles for you are French Girl Makeup, Rich Girl Makeup, and Korean Ladylike Makeup.",
    'Romantic' : "The Romantic archetype resembles a sensuous, soft, alluring, and mature feminine persona. Based on this archetype, the best makeup styles for you are Flirtatious Cute Makeup and Retro Honk Kong Girl Makeup.",
    'Gamine' : "Refreshing and courageous, the Gamine archetype resembles young and slightly masculine beauty. And its tomboyish vibe matches makeup styles like Airy Boyish and Soft Grunge looks.",
    'Natural' : "The Natural archetype resembles a casual, easygoing, and friendly persona. Because of that, the best makeup styles for you are the Effortless No Makeup look, Gentle Ladylike look, and Mori Kei Style. These styles create an approachable look with base makeup products.",
    'Modern' : "The Modern archetype resembles an immaculate, bold, and confident persona. It is vibrant, influential, and attention-grabbing. Based on this archetype, the best makeup styles for you are Cut Crease Eye Makeup, Siren Makeup, and Smokey Eye Makeup.",
    'Classic' : "The Classic Archetype: The rarest archetype, moderate to high visual weight and neither very angular and sharp nor very rounded and soft.",
    'Dramatic' : "The Dramatic archetype resembles dignity, intensity, extravagance, and charisma. Based on this archetype, the best makeup styles for you are Thai Makeup and Fiery Mean Makeup."
}