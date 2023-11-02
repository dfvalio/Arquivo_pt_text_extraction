import requests
import codecs

list_key_words = ["Élections%20parlement%20européen%202019","Élections%20européennes%202019","Abstention%20européenne%202019","Résultats%20électoraux%202019","Gagnants%20européens%202019","Élections%20européennes%20du%20Brexit%202019","Élections%20européennes%202019","Blogs%20des%20élections%20européennes","Élections%20européennes%20des%20médias%20sociaux","Élections%20européennes%20Twitter","Élections%20européennes%20Facebook","Élections%20européennes%20de%20bandes%20dessinées%202019","Enquête%20européenne%202019","Télévision%20européenne%202019","Débat%20de%20télévision%20européen","Caravane%20européenne%202019","Représentant%20européen%202019","Politique%20européenne%202019","Accessibilité%20des%20élections%20européennes%202019","Parité%20des%20élections%20européennes%202019","Candidats%20européens%202019","Députés%20européens%202019","Écologistes%20européens%202019","Élections%20européennes%202019%20Immigration","Liste%20européenne%202019","Européen%20vaincu%202019","European%20Right%202019","Libéraux%20européens%202019","Européen%20d'extrême%20droite","La%20gauche%20européenne%202019","Coalition%20européenne","Système%20électoral%20européen%202019","Future%20of%20Europe%202019","FAKENEWS%20EUROCHIERS%202019","Élections%20européennes%202019","Anti-Europeist%202019","Eurochists%20européens%202019","Idéologie%20européenne%202019","Financement%20de%20la%20campagne%20européenne%202019","Aisance%20pargé%20de%20maturissement"]

for word in list_key_words:
	url="https://arquivo.pt/textsearch?q="
	url=url+word+"&prettyPrint=true&maxItems=2000"

	file_name=word+".json"
	
	result = codecs.open(file_name, mode="w",encoding="utf-8")
	
	file = requests.get(url)
	
	result.write(file.text)