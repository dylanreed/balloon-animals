from PIL import Image 
from IPython.display import display 
import random
import json

#Inject all the shapes and set their weights

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

background = ["1","2","3","4","5","6","7"] 
background_weights = [14.2857143, 14.2857143, 14.2857143, 14.2857143, 14.2857143, 14.2857143, 14.2857143]

base = ["1","2","3","4","5","6","7","8","9","blank"] 
base_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

bottom = ["b1","b2","b3","b4","b5","b6","b7","b8","b9","b10","b11","b12","blank"] 
bottom_weights = [7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769]

down = ["d1","d2","d3","d4","d5","d6","d7","d8","d9","d10","d11","d12","blank"] 
down_weights = [7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769]

horz = ["h1","h2","h3","h4","h5","h6","h7","h8","h9","h10","h11","h12","blank"] 
horz_weights = [7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769]

up = ["u1","u2","u3","u4","u5","u6","u7","u8","u9","u10","u11","u12","blank"] 
up_weights = [7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769]

vert = ["v1","v2","v3","v4","v5","v6","v7","v8","v9","v10","v11","v12","blank"] 
vert_weights = [7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769]

top = ["t1","t2","t3","t4","t5","t6","t7","t8","t9","t10","t11","t12","blank"] 
top_weights = [7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769, 7.69230769]

shadow = ["shadow","blank"] 
shadow_weights = [50, 50]

outline = ["o25","o50","blank"]  
outline_weights = [33, 33, 34]

shine = ["s25", "s50", "s75", "blank"]  
shine_weights = [25, 25, 25, 25]

# Dictionary variable for each trait. 
# Eech trait corresponds to its file name
# Add more shapes and colours as you wish

background_files = {
    "1":"1",
    "2":"2",
    "3":"3",
    "4":"4",
    "5":"5",
    "6":"6",
    "7":"7"
}

base_files = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "blank": "blank"
}

bottom_files = {
    "b1": "b1",
    "b2": "b2",
    "b3": "b3",
    "b4": "b4",
    "b5": "b5",
    "b6": "b6",
    "b7": "b7",
    "b8": "b8",
    "b9": "b9",
    "b10":"b10",
    "b11": "b11",
    "b12": "b12",
    "blank": "blank"
}

down_files = {
    "d1": "d1",
    "d2": "d2",
    "d3": "d3",
    "d4": "d4",
    "d5": "d5",
    "d6": "d6",
    "d7": "d7",
    "d8": "d8",
    "d9": "d9",
    "d10":"d10",
    "d11": "d11",
    "d12": "d12",
    "blank": "blank"
}

horz_files = {
    "h1": "h1",
    "h2": "h2",
    "h3": "h3",
    "h4": "h4",
    "h5": "h5",
    "h6": "h6",
    "h7": "h7",
    "h8": "h8",
    "h9": "h9",
    "h10":"h10",
    "h11": "h11",
    "h12": "h12",
    "blank": "blank"
}

up_files = {
    "u1": "u1",
    "u2": "u2",
    "u3": "u3",
    "u4": "u4",
    "u5": "u5",
    "u6": "u6",
    "u7": "u7",
    "u8": "u8",
    "u9": "u9",
    "u10":"u10",
    "u11": "u11",
    "u12": "u12",
    "blank": "blank"
}

vert_files = {
    "v1": "v1",
    "v2": "v2",
    "v3": "v3",
    "v4": "v4",
    "v5": "v5",
    "v6": "v6",
    "v7": "v7",
    "v8": "v8",
    "v9": "v9",
    "v10":"v10",
    "v11": "v11",
    "v12": "v12",
    "blank": "blank"
}

outline_files = {
    "blank": "blank",
    "o25": "o25",
    "o50": "o50"
}

top_files = {
    "t1": "t1",
    "t2": "t2",
    "t3": "t3",
    "t4": "t4",
    "t5": "t5",
    "t6": "t6",
    "t7": "t7",
    "t8": "t8",
    "t9": "t9",
    "t10":"t10",
    "t11": "t11",
    "t12": "t12",
    "blank": "blank"
}

shadow_files = {
    "shadow": "shadow",
    "blank": "blank"
}

shine_files = {
    "blank": "blank",
    "s25": "s25",
    "s50": "s50",
    "s75": "s75"
}
#Create a function to generate unique image combinations
TOTAL_IMAGES = 2400 # Number of random unique images we want to generate ( 2 x 2 x 2 = 8)

all_images = [] 

def create_new_image():

    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    new_image ["base"] = random.choices(base, base_weights)[0]
    new_image ["bottom"] = random.choices(bottom, bottom_weights)[0]
    new_image ["down"] = random.choices(down, down_weights)[0]
    new_image ["horz"] = random.choices(horz, horz_weights)[0]
    new_image ["up"] = random.choices(up, up_weights)[0]
    new_image ["vert"] = random.choices(vert, vert_weights)[0]
    new_image ["outline"] = random.choices(outline, outline_weights)[0]
    new_image ["top"] = random.choices(top, top_weights)[0]
    new_image ["shadow"] = random.choices(shadow, shadow_weights)[0]
    new_image ["shine"] = random.choices(shine, shine_weights)[0]
    new_image ["background"] = random.choices(background, background_weights)[0]

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

background_count ={}
for item in base:
    background_count[item] = 0

base_count = {}
for item in base:
    base_count[item] = 0

bottom_count = {}
for item in bottom:
    bottom_count[item] = 0

down_count = {}
for item in down:
    down_count[item] = 0

horz_count = {}
for item in horz:
    horz_count[item] = 0

up_count = {}
for item in up:
    up_count[item] = 0

vert_count = {}
for item in vert:
    vert_count[item] = 0

outline_count = {}
for item in outline:
    outline_count[item] = 0

top_count = {}
for item in top:
    top_count[item] = 0

shadow_count = {}
for item in shadow:
    shadow_count[item] = 0

shine_count = {}
for item in shine:
    shine_count[item] = 0

for image in all_images:
    background_count[image["background"]] += 1
    base_count[image["base"]] += 1
    bottom_count[image["bottom"]] += 1
    down_count[image["down"]] += 1
    horz_count[image["horz"]] += 1
    up_count[image["up"]] += 1
    vert_count[image["vert"]] += 1
    outline_count[image["outline"]] += 1
    top_count[image["top"]] += 1
    shadow_count[image["shadow"]] += 1
    shine_count[image["shine"]] += 1


#print(background_count)
print(background_count)
print(base_count)
print(bottom_count)
print(down_count)
print(horz_count)
print(up_count)
print(vert_count)
print(top_count)
print(shadow_count)
print(outline_count)
print(shine_count)


#Generate Metadata for all Traits

METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)


#Generate Images

for item in all_images:

    im1 = Image.open(f'./layers/base/{base_files[item["base"]]}.png').convert('RGBA')
    im2 = Image.open(f'./layers/bottom/{bottom_files[item["bottom"]]}.png').convert('RGBA')
    im3 = Image.open(f'./layers/down/{down_files[item["down"]]}.png').convert('RGBA')
    im4 = Image.open(f'./layers/horz/{horz_files[item["horz"]]}.png').convert('RGBA')
    im5 = Image.open(f'./layers/up/{up_files[item["up"]]}.png').convert('RGBA')
    im6 = Image.open(f'./layers/vert/{vert_files[item["vert"]]}.png').convert('RGBA')
    im8 = Image.open(f'./layers/shine/{shine_files[item["shine"]]}.png').convert('RGBA')
    im7 = Image.open(f'./layers/top/{top_files[item["top"]]}.png').convert('RGBA')
    im10 = Image.open(f'./layers/shadow/{shadow_files[item["shadow"]]}.png').convert('RGBA')
    im9 = Image.open(f'./layers/outline/{outline_files[item["outline"]]}.png').convert('RGBA')
    im11 = Image.open(f'./layers/background/{background_files[item["background"]]}.png').convert('RGBA')

    #Create each composite
    com1 = Image.alpha_composite(im11, im1)
    com2 = Image.alpha_composite(com1, im2)
    com3 = Image.alpha_composite(com2, im3)
    com4 = Image.alpha_composite(com3, im4)
    com5 = Image.alpha_composite(com4, im5)
    com6 = Image.alpha_composite(com5, im6)
    com7 = Image.alpha_composite(com6, im7)
    com8 = Image.alpha_composite(com7, im8)
    com9 = Image.alpha_composite(com8, im9)
    com10 = Image.alpha_composite(com9, im10)

    #Convert to RGB
    rgb_im = com10.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)

#Generate Metadata

#f = open('./metadata/all-traits.json',) 
#data = json.load(f)

#IMAGES_BASE_URI = "ADD_IMAGES_BASE_URI_HERE/"
#PROJECT_NAME = "Balloon Animals"

#def getAttribute(key, value):
#    return {
#        "trait_type": key,
#        "value": value
#    }
#for i in data:
#    token_id = i['tokenId']
#    token = {
#        "image": IMAGES_BASE_URI + str(token_id) + '.png',
#        "tokenId": token_id,
#        "name": PROJECT_NAME + ' ' + str(token_id),
#        "attributes": []
#    }
#    token["attributes"].append(getAttribute("Background", i["Background"]))
#    token["attributes"].append(getAttribute("Back Legs", i["Back Legs"]))
#    token["attributes"].append(getAttribute("base", i["base"]))
#    token["attributes"].append(getAttribute("Ears", i["Ears"]))
#    token["attributes"].append(getAttribute("Front Legs", i["Front Legs"]))
#    token["attributes"].append(getAttribute("Head", i["Head"]))
#    token["attributes"].append(getAttribute("up", i["up"]))
#    token["attributes"].append(getAttribute("shine", i["shine"]))
#    token["attributes"].append(getAttribute("Outline", i["Outline"]))

#    with open('./metadata/' + str(token_id), 'w') as outfile:
#        json.dump(token, outfile, indent=4)
#f.close()