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

net = Network(height='1400px', width='1400px')   #define network

datei="satzgeschaefte.json"


data = json.load(open(datei, encoding="utf8"))            #load data

for key, val in data.items():   #loop through the data

  net.add_node(key, size=20, label=key, shape="box", group=1, title=val["obj"] ,color="DodgerBlue") #adds a node for each event

  for k, v in val.items():    #loops through the entries of each event
    if k == "issuer":       #issuer, the one giving something in the event
                    
      persons = []        #empty list, the issuer can be a range of persons
      for person in v:    #each person in the issuer list             
        net.add_node(person, size=10, group=2, color="Tomato")  #adds each person as a node               
        persons.append(person)                  #adds up a list of all the persons in the entry

      length = len(persons)-1
      if length == 0:
        length = 1

      for i in range(length):             #drawing the edges    
        if len(persons) > 1:                    #drawing the conections between the persons in the issuer entry     
          net.add_edge(persons[i], persons[i+1])                                  
        net.add_edge(persons[i], key, color="DodgerBlue")           #drawing the edge to the event

    if k == "recipient":    #the recievers in the event 

      recipients = []     #again empty list, the reciever can also be a compound
      for recipient in v:                 
        net.add_node(recipient, size= 10, group=3, color="green")  #each person as a node                
        recipients.append(recipient)                

      length = len(recipients)-1
      if length == 0:
        length = 1

      for i in range(length):              #drawing edges    
        if len(recipients) > 1:                     #linking all recievers together           
          net.add_edge(recipients[i], recipients[i+1], color="green")                    
        net.add_edge(key, recipients[i], color="DodgerBlue")            #edge between from the event to the reciever   
                
      # objs = val["obj"]      

      # obj = objs[1]
      # net.add_node(obj, size= 10, shape="diamond", group=3, color="orange")
      # net.add_edge(obj, key, color="DodgerBlue")  

          
 
        
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
