import csv
import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

def write_output(data):
	with open('allrecipes.csv', mode='w',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["page_url","title","cook_time","description","recipe_instructions","image_url","recipe_ingredients","prep_time","servings","total_time","current_timestamp"])
		for row in data:
			writer.writerow(row)

def fetch_data():
    url = "https://www.allrecipes.com/recipes/84/healthy-recipes/"
    headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "cookie": "TMog=ne36dfc08cb794030b17b01f3c22e245210; globalTI_SID=00b5eca4-0431-4239-9861-4e12d39a3adc; Mint=ne36dfc08cb794030b17b01f3c22e245210; lb_ld=search; _ga=GA1.2.600332016.1671274409; _gid=GA1.2.1788508126.1671274409; _pbjs_userid_consent_data=3524755945110770; __gads=ID=cdfd258f7da6d13f:T=1671274409:S=ALNI_MaoY5A2fRrJU4YdGW6vjTtfEAVtSg; __gpi=UID=00000b92321bf570:T=1671274409:RT=1671274409:S=ALNI_MZyflqPyPY0wHGVddXSAVCaLU3VsQ; _cb=CwmFRvBRfXEmB8ePiF; _cb_svref=null; _li_dcdm_c=.allrecipes.com; _lc2_fpi=6c17f56c0790--01gmfvfbg376509wgjabrfxr5e; _fbp=fb.1.1671274409514.959635862; _lr_retry_request=true; _lr_env_src_ats=false; _v__chartbeat3=ypKeDm4g82DxzJst; _SUPERFLY_lockout=1; _gat_UA-37680041-42=1; _chartbeat5=150|1822|%2Frecipes%2F84%2Fhealthy-recipes%2F|https%3A%2F%2Fwww.allrecipes.com%2Frecipe%2F13107%2Fmiso-soup%2F|BUTpbxCKlJe5DORKA-CS4wG4VkUlz||c|Bz_IUoDlBTbRz0HUTChCAtaBsIlmB|allrecipes.com|::150|1218|%2Frecipes%2F84%2Fhealthy-recipes%2F|https%3A%2F%2Fwww.allrecipes.com%2Frecipe%2F233531%2Fquick-whole-wheat-chapati%2F|r_GY5CvH4GYH4c1dD4mlGiBk7mmq||c|B8AOYIBkjUlvDD8L-oBVJBkACnmbbk|allrecipes.com|; pc=8; _chartbeat2=.1671274409422.1671275672670.1.y-rdcbl1dvQBWEYgODLf2eb7n.8; _v__cb_cp=BGV-07BXna4hBA-oLTDTkbXxDKnCw8; _chartbeat4=t=CYEH0xDE3ot5Dx-WXCGHMLPDryvzW&E=1&x=0&c=0.29&y=8838&w=746",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    response = requests.request("GET", url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = str(soup.find("script",{"type":"application/ld+json"})).replace("</script>","").split('application/ld+json">')[1]
    json_data = json.loads(data)
    for datas in json_data:
        for url_data in datas['itemListElement']:
            urls = url_data['url']
            response1 = requests.request("GET", urls, headers=headers)
            soup1 = BeautifulSoup(response1.text, 'html.parser')
            if soup1.find("h2",{"class":"comp mntl-structured-ingredients__heading mntl-text-block"}) == None:
                continue
            data1 = str(soup1.find("script",{"type":"application/ld+json"})).replace("</script>","").split('application/ld+json">')[1]
            json_data1 = json.loads(data1)
            for all_recipe_data in json_data1:
                page_url = urls
                print(page_url)
                title = all_recipe_data['headline']
                try:
                    cook_time = all_recipe_data['cookTime'].replace("PT","").replace("M"," min")
                except:
                    cook_time = ''
                description = all_recipe_data['description']
                instruction_step = []
                for recipe_instruction in all_recipe_data['recipeInstructions']:
                    directions = recipe_instruction['text']
                    instruction_step.append(directions)
                recipe_instructions = ";".join(instruction_step).replace(".;","; ")
                image_url = all_recipe_data['image']['url']
                inngredient_step = []
                for recipe_ingredient in all_recipe_data['recipeIngredient']:
                    inngredient_step.append(recipe_ingredient)
                recipe_ingredients = ", ".join(inngredient_step)
                try:
                    prep_time = all_recipe_data['prepTime'].replace("PT","").replace("M"," min")
                except:
                    prep_time = ''
                servings = str(all_recipe_data['recipeYield']).replace("['","").replace("']","")
                try:
                    total_time = all_recipe_data['totalTime'].replace("PT","").replace("M"," min")
                except:
                    total_time = ''
                now = datetime.now()
                current_timestamp = now.strftime("20%y-%m-%dT%H:%M:%SZ")

                store =[page_url,title,cook_time,description,recipe_instructions,image_url,recipe_ingredients,prep_time,servings,total_time,current_timestamp]
                yield store
                
def scrape():
    data = fetch_data()
    write_output(data)
scrape()