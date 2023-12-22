import json
import os

def getData():
    with open('videos-teded.json') as json_file:
        data = json.load(json_file)
        return data
    
def populateNode(m, node, i):
    st1 = data[i]["title"]
    description = node["description"]
    if len(node["description"]) > 2048:
        description = node["description"][:2045] + "..."
    m[str(i)] = {
        "name": st1.replace("&quot;", ""),
        "description": description,
        "texts": ["text1.md"],
        "videos": [node["id"]],
        "node_type": "general",
        "parent_id": "0a",
        "thumbnail": node["thumbnail"]
    }

def populate(m, node, i):
    populateNode(m, node, i)
    
def save_to_json(videos, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(videos, f, ensure_ascii=False, indent=4)
    
data = getData()

def createNodesJSON():
    m = {}
    for i in range(len(data)):
        populate(m, data[i], i)
    save_to_json(m, 'nodes.json')


def createGraphJSON():
    m={}
    for i in range(len(data)):
        m[str(i)] = ["Intro to Vitsi AI"]
    save_to_json(m, 'graph.json')

def populateTexts():
    os.mkdir("nodes")
    for i in range(len(data)):
        path = os.path.join("nodes", str(i))  
        os.mkdir(path)
        path = os.path.join(path, "text1.md")  
        st1 = data[i]["text"]
        with open(path, 'w') as f:
            f.write(st1.replace('\n', ' ').replace('\r', ''))


createNodesJSON()
# createGraphJSON()
# populateTexts()
