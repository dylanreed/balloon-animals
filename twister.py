from PIL import Image 
from IPython.display import display 
import random
import json

#Inject all the shapes and set their weights

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

backgroundc = ["None", "A little", "More", "A Lot", "Filled"] 
backgroundc_weights = [10, 15, 20, 25, 30]

backgroundm = ["None", "A little", "More", "A Lot", "Filled"] 
backgroundm_weights = [30, 10, 15, 20, 25]

backgroundy = ["None", "A little", "More", "A Lot", "Filled"] 
backgroundy_weights = [25, 30, 10, 15, 20]

bodyc = ["None", "A little", "More", "A Lot", "Filled"] 
bodyc_weights = [20, 25, 30, 10, 15]

bodym = ["None", "A little", "More", "A Lot", "Filled"] 
bodym_weights = [15, 20, 25, 30, 10]

bodyy = ["None", "A little", "More", "A Lot", "Filled"] 
bodyy_weights = [10, 15, 20, 25, 30]

outlinec = ["None", "A little", "More", "A Lot", "Filled"] 
outlinec_weights = [30, 10, 15, 20, 25]

outlinem = ["None", "A little", "More", "A Lot", "Filled"] 
outlinem_weights = outlinec_weights = [25, 30, 10, 15, 20]

outliney = ["None", "A little", "More", "A Lot", "Filled"]  
outliney_weights = outlinec_weights = [20, 25, 30, 10, 15]

# Dictionary variable for each trait. 
# Eech trait corresponds to its file name
# Add more shapes and colours as you wish

backgroundc_files = {
    "None": "cbg1",
    "A little": "cbg2",
    "More": "cbg3",
    "A Lot": "cbg4",
    "Filled": "cbg5"
}

backgroundm_files = {
    "None": "cbg1",
    "A little": "cbg2",
    "More": "cbg3",
    "A Lot": "cbg4",
    "Filled": "cbg5"
}

backgroundy_files = {
    "None": "cbg1",
    "A little": "cbg2",
    "More": "cbg3",
    "A Lot": "cbg4",
    "Filled": "cbg5"
}

bodyc_files = {
    "None": "cbg1",
    "A little": "cbg2",
    "More": "cbg3",
    "A Lot": "cbg4",
    "Filled": "cbg5"
}

bodym_files = {
    "None": "cbg1",
    "A little": "cbg2",
    "More": "cbg3",
    "A Lot": "cbg4",
    "Filled": "cbg5"
}

bodyy_files = {
    "None": "cbg1",
    "A little": "cbg2",
    "More": "cbg3",
    "A Lot": "cbg4",
    "Filled": "cbg5"
}

outlinec_files = {
    "None": "cbg1",
    "A little": "cbg2",
    "More": "cbg3",
    "A Lot": "cbg4",
    "Filled": "cbg5"
}

outlinem_files = {
    "None": "cbg1",
    "A little": "cbg2",
    "More": "cbg3",
    "A Lot": "cbg4",
    "Filled": "cbg5"
}

outliney_files = {
    "None": "cbg1",
    "A little": "cbg2",
    "More": "cbg3",
    "A Lot": "cbg4",
    "Filled": "cbg5"
}

#Create a function to generate unique image combinations
TOTAL_IMAGES = 10 # Number of random unique images we want to generate ( 2 x 2 x 2 = 8)

all_images = [] 

def create_new_image():

    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    new_image ["Cyan Background"] = random.choices(backgroundcs, backgroundc_weights)[0]
    new_image ["Magenta Background"] = random.choices(backgroundm, backgroundm_weights)[0]
    new_image ["Yellow Backgroun"] = random.choices(backgroundy, backgroundy_weights)[0]
    new_image ["Cyan Body"] = random.choices(bodyc, bodyc_weights)[0]
    new_image ["Magenta Body"] = random.choices(bodym, bodym_weights)[0]
    new_image ["Yellow Body"] = random.choices(bodyy, bodyy_weights)[0]
    new_image ["Cyan Outline"] = random.choices(outlinec, outlinec_weights)[0]
    new_image ["Magenta Outline"] = random.choices(outlinem, outlinem_weights)[0]
    new_image ["Yellow Outline"] = random.choices(outliney, outliney_weights)[0]


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

backgroundc_count = {}
for item in backgroundc:
    backgroundc_count[item] = 0

backgroundm_count = {}
for item in backgroundm:
    backgroundm_count[item] = 0

backgroundy_count = {}
for item in backgroundy:
    backgroundy_count[item] = 0

bodyc_count = {}
for item in bodyc:
    bodyc_count[item] = 0

bodym_count = {}
for item in bodym:
    bodym_count[item] = 0

bodyy_count = {}
for item in bodyy:
    bodyy_count[item] = 0

outlinec_count = {}
for item in outlinec:
    outlinec_count[item] = 0

outlinem_count = {}
for item in outlinem:
    outlinem_count[item] = 0

outliney_count = {}
for item in outliney:
    outliney_count[item] = 0

for image in all_images:
    backgroundc_count[image["Cyan Background"]] += 1
    backgroundm_count[image["Magenta Background"]] += 1
    backgroundy_count[image["Yellow Background"]] += 1
    bodyc_count[image["Cyan Body"]] += 1
    bodym_count[image["Magenta Body"]] += 1
    bodyy_count[image["Yellow Body"]] += 1
    outlinec_count[image["Cyan Outline"]] += 1
    outlinem_count[image["Magenta Outline"]] += 1
    outliney_count[image["Yellow Outline"]] += 1


print(backgroundc_count)
print(backgroundm_count)
print(backgroundy_count)
print(bodyc_count)
print(bodym_count)
print(bodyy_count)
print(outlinec_count)
print(outlinem_count)
print(outliney_count)


#Generate Metadata for all Traits

METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)


#Generate Images

for item in all_images:

    im1 = Image.open(f'./layers/background c/{background_files[item["Background"]]}.png').convert('RGBA')
    im2 = Image.open(f'./layers/background m/{back_files[item["Back Legs"]]}.png').convert('RGBA')
    im3 = Image.open(f'./layers/background y/{body_files[item["Body"]]}.png').convert('RGBA')
    im4 = Image.open(f'./layers/body c/{ears_files[item["Ears"]]}.png').convert('RGBA')
    im5 = Image.open(f'./layers/body m/{front_files[item["Front Legs"]]}.png').convert('RGBA')
    im6 = Image.open(f'./layers/body y/{head_files[item["Head"]]}.png').convert('RGBA')
    im7 = Image.open(f'./layers/outline c/{neck_files[item["Neck"]]}.png').convert('RGBA')
    im8 = Image.open(f'./layers/outline m/{tail_files[item["Tail"]]}.png').convert('RGBA')
    im9 = Image.open(f'./layers/outline y/{outline_files[item["Outline"]]}.png').convert('RGBA')

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