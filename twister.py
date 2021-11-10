from PIL import Image 
from IPython.display import display 
import random
import json

#Inject all the shapes and set their weights

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

backgrounds = ["Blue", "Dark Blue", "Green", "Magenta", "Orange", "Purple", "White", "Yellow Green"] 
background_weights = [12, 12, 12, 12, 12, 12, 12, 16]

body = ["Black", "Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "White"]
body_weights = [11, 11, 11, 11, 11, 11, 11, 11, 12]

back = ["Black", "Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "White"]
back_weights = [11, 11, 11, 11, 11, 11, 11, 11, 12]

ears = ["Black", "Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "White"]
ears_weights = [11, 11, 11, 11, 11, 11, 11, 11, 12]

front = ["Black", "Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "White"] 
front_weights = [11, 11, 11, 11, 11, 11, 11, 11, 12]

head = ["Black", "Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "White"] 
head_weights = [11, 11, 11, 11, 11, 11, 11, 11, 12]

neck = ["Black", "Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "White"] 
neck_weights = [11, 11, 11, 11, 11, 11, 11, 11, 12]

tail = ["Black", "Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "White"] 
tail_weights = [11, 11, 11, 11, 11, 11, 11, 11, 12]

outline = ["Black"] 
outline_weights = [100]

# Dictionary variable for each trait. 
# Eech trait corresponds to its file name
# Add more shapes and colours as you wish

background_files = {
    "Blue": "bg_blue",
    "Dark Blue": "bg_dark_blue",
    "Green": "bg_green",
    "Magenta": "bg_magenta",
    "Orange": "bg_orange",
    "Purple": "bg_purple",
    "White": "bg_white",
    "Yellow Green": "bg_yellow_green"
}

back_files = {
    "Black": "back_legs_black",
    "Red": "back_legs_red",
    "Orange": "back_legs_orange",
    "Yellow": "back_legs_yellow",
    "Green": "back_legs_green",
    "Blue": "back_legs_blue",
    "Indigo": "back_legs_indigo",
    "Violet": "back_legs_orange",
    "White": "back_legs_white"  
}

body_files = {
    "Black": "body_black",
    "Red": "body_red",
    "Orange": "body_orange",
    "Yellow": "body_yellow",
    "Green": "body_green",
    "Blue": "body_blue",
    "Indigo": "body_indigo",
    "Violet": "body_violet",
    "White": "body_white"
}

ears_files = {
    "Black": "ears_black",
    "Red": "ears_red",
    "Orange": "ears_orange",
    "Yellow": "ears_yellow",
    "Green": "ears_green",
    "Blue": "ears_blue",
    "Indigo": "ears_indigo",
    "Violet": "ears_violet",
    "White": "ears_white"
}

front_files = {
    "Black": "front_legs_black",
    "Red": "front_legs_red",
    "Orange": "front_legs_orange",
    "Yellow": "front_legs_yellow",
    "Green": "front_legs_green",
    "Blue": "front_legs_blue",
    "Indigo": "front_legs_indigo",
    "Violet": "front_legs_violet",
    "White": "front_legs_white"
}

head_files = {
    "Black": "head_black",
    "Red": "head_red",
    "Orange": "head_orange",
    "Yellow": "head_yellow",
    "Green": "head_green",
    "Blue": "head_blue",
    "Indigo": "head_indigo",
    "Violet": "head_violet",
    "White": "head_white"
}

neck_files = {
    "Black": "neck_black",
    "Red": "neck_red",
    "Orange": "neck_orange",
    "Yellow": "neck_yellow",
    "Green": "neck_green",
    "Blue": "neck_blue",
    "Indigo": "neck_indigo",
    "Violet": "neck_violet",
    "White": "neck_white"
}

tail_files = {
    "Black": "tail_black",
    "Red": "tail_red",
    "Orange": "tail_orange",
    "Yellow": "tail_yellow",
    "Green": "tail_green",
    "Blue": "tail_blue",
    "Indigo": "tail_indigo",
    "Violet": "tail_violet",
    "White": "tail_white"
}

outline_files = {
    "Black": "outline",
}

#Create a function to generate unique image combinations
TOTAL_IMAGES = 12 # Number of random unique images we want to generate ( 2 x 2 x 2 = 8)

all_images = [] 

def create_new_image():

    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    new_image ["Background"] = random.choices(backgrounds, background_weights)[0]
    new_image ["Back Legs"] = random.choices(back, back_weights)[0]
    new_image ["Front Legs"] = random.choices(front, front_weights)[0]
    new_image ["Body"] = random.choices(body, body_weights)[0]
    new_image ["Ears"] = random.choices(ears, ears_weights)[0]
    new_image ["Head"] = random.choices(head, head_weights)[0]
    new_image ["Neck"] = random.choices(neck, neck_weights)[0]
    new_image ["Tail"] = random.choices(tail, tail_weights)[0]
    new_image ["Outline"] = random.choices(outline, outline_weights)[0]


    if new_image in all_images:
        return create_new_image()
    else:
        return new_image


# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 

    new_trait_image = create_new_image()

    all_images.append(new_trait_image)

#Return true if all images are unique

def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))

#add token id

i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

#print all images

print(all_images)

#get trait count

background_count = {}
for item in backgrounds:
    background_count[item] = 0

back_count = {}
for item in back:
    back_count[item] = 0

body_count = {}
for item in body:
    body_count[item] = 0

ears_count = {}
for item in ears:
    ears_count[item] = 0

front_count = {}
for item in front:
    front_count[item] = 0

head_count = {}
for item in head:
    head_count[item] = 0

neck_count = {}
for item in neck:
    neck_count[item] = 0

tail_count = {}
for item in tail:
    tail_count[item] = 0

outline_count = {}
for item in outline:
    outline_count[item] = 0

for image in all_images:
    background_count[image["Background"]] += 1
    back_count[image["Back Legs"]] += 1
    body_count[image["Body"]] += 1
    ears_count[image["Ears"]] += 1
    front_count[image["Front Legs"]] += 1
    head_count[image["Head"]] += 1
    neck_count[image["Neck"]] += 1
    outline_count[image["Outline"]] += 1
    tail_count[image["Tail"]] += 1


print(background_count)
print(back_count)
print(body_count)
print(ears_count)
print(front_count)
print(head_count)
print(neck_count)
print(outline_count)
print(tail_count)


#Generate Metadata for all Traits

METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)


#Generate Images

for item in all_images:

    im1 = Image.open(f'./layers/backgrounds/{background_files[item["Background"]]}.png').convert('RGBA')
    im2 = Image.open(f'./layers/back/{back_files[item["Back Legs"]]}.png').convert('RGBA')
    im3 = Image.open(f'./layers/body/{body_files[item["Body"]]}.png').convert('RGBA')
    im4 = Image.open(f'./layers/ears/{ears_files[item["Ears"]]}.png').convert('RGBA')
    im5 = Image.open(f'./layers/front/{front_files[item["Front Legs"]]}.png').convert('RGBA')
    im6 = Image.open(f'./layers/head/{head_files[item["Head"]]}.png').convert('RGBA')
    im7 = Image.open(f'./layers/neck/{neck_files[item["Neck"]]}.png').convert('RGBA')
    im8 = Image.open(f'./layers/tail/{tail_files[item["Tail"]]}.png').convert('RGBA')
    im9 = Image.open(f'./layers/outline/{outline_files[item["Outline"]]}.png').convert('RGBA')

    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)
    com5 = Image.alpha_composite(com4, im6)
    com6 = Image.alpha_composite(com5, im7)
    com7 = Image.alpha_composite(com6, im8)
    com8 = Image.alpha_composite(com7, im9)

    #Convert to RGB
    rgb_im = com8.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)

#Generate Metadata

f = open('./metadata/all-traits.json',) 
data = json.load(f)

IMAGES_BASE_URI = "ADD_IMAGES_BASE_URI_HERE/"
PROJECT_NAME = "Balloon Animals"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }
for i in data:
    token_id = i['tokenId']
    token = {
        "image": IMAGES_BASE_URI + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }
    token["attributes"].append(getAttribute("Background", i["Background"]))
    token["attributes"].append(getAttribute("Back Legs", i["Back Legs"]))
    token["attributes"].append(getAttribute("Body", i["Body"]))
    token["attributes"].append(getAttribute("Ears", i["Ears"]))
    token["attributes"].append(getAttribute("Front Legs", i["Front Legs"]))
    token["attributes"].append(getAttribute("Head", i["Head"]))
    token["attributes"].append(getAttribute("Neck", i["Neck"]))
    token["attributes"].append(getAttribute("Tail", i["Tail"]))
    token["attributes"].append(getAttribute("Outline", i["Outline"]))

    with open('./metadata/' + str(token_id), 'w') as outfile:
        json.dump(token, outfile, indent=4)
f.close()