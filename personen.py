from pyvis.network import Network
import json

var = {
    "physics": {
    "barnesHut": {
      "gravitationalConstant": -6050,
      "springLength": 170,
      "springConstant": 0.125
    },
    "minVelocity": 0.75
  }
}

net = Network(height='1400px', width='1400px', directed=True)   #define network

datei="beispiel.json"

setColor = "DodgerBlue"

data = json.load(open(datei, encoding="utf8"))            #load data

for key, val in data.items():   #loop through the data

  place = val["link_place"][1]

  set_lable = key + "\n" + val["date"] + "\n" + val["type"] +"\n" + place
  net.add_node(key, size=20, label=set_lable, shape="box", group=1, color="DodgerBlue") #adds a node for each event    

  for k, v in val.items():    #loops through the entries of each event

    # if k == "link_place":
      
    #   entries = []
    #   for entry in v:    #each person in the issuer list                             
    #     entries.append(entry)    
    #   net.add_node(entries[0], size=10, group=2, color="Orange")
    #   net.add_edge(key, entries[0], color="DodgerBlue")

    if k == "issuer":       #issuer, the one giving something in the event
                    
      persons = []        #empty list, the issuer can be a range of persons
      for person in v:    #each person in the issuer list             
        net.add_node(person, size=10, group=2, color="Orange")  #adds each person as a node               
        persons.append(person)                  #adds up a list of all the persons in the entry
      
      length = len(persons)-1
      if length == 0:
        length = 1

      for i in range(length):             #drawing the edges    
        if len(persons) > 1:                    #drawing the conections between the persons in the issuer entry, bi-directional        
          net.add_edge(persons[i], persons[i+1], color="Orange")
          net.add_edge(persons[i+1], persons[i], color="Orange")

      # if val["type"] == "satz":
      #   setColor = "Tomato"
      # elif val["type"] == "erbe":
      #   setColor = "DodgerBlue"
      # elif val["type"] == "verkauf":
      #   setColor = "Orange"

      net.add_edge(persons[i], key, color=setColor, width=3)           #drawing the edge to the event, directed, since they are issuer here, from the person to the event

    if k == "recipient":    #the recievers in the event 

      recipients = []     #again empty list, the reciever can also be a compound
      for recipient in v:                 
        net.add_node(recipient, size= 10, group=3, color="Orange")  #each person as a node                
        recipients.append(recipient)                

      for i in range(len(recipients)-1):              #drawing edges    
        if len(recipients) > 1:                     #bi-directional, linking all recievers together           
          net.add_edge(recipients[i], recipients[i+1], color="Orange")
          net.add_edge(recipients[i+1], recipients[i], color="Orange")
      
      # if val["type"] == "satz":
      #   setColor = "Tomato"
      # elif val["type"] == "erbe":
      #   setColor = "DodgerBlue"
      # elif val["type"] == "verkauf":
      #   setColor = "Purple"

      net.add_edge(key, recipients[i], color=setColor, width=3)            #edge between from the event to the reciever  

net.show_buttons()

# net.set_options("""var options = {
#   "edges": {
#     "color": {
#       "inherit": true
#     },
#     "smooth": false
#   },
#   "physics": {
#     "barnesHut": {
#       "gravitationalConstant": -6050,
#       "springLength": 170,
#       "springConstant": 0.125
#     },
#     "minVelocity": 0.75
#   }
# }""")
name = datei.replace(".json","1.html")
net.show(name)
