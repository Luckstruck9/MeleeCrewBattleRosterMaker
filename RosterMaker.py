# Roster Maker
# By Lucky "Luckstruck9" Lai

VersionNumber =  1
DateUpdated = "2/16/2021"

import os
import sys

os.system("pip install pillow")
os.system("cls")

from PIL import Image, ImageFont, ImageDraw, ImageTk

background_image = os.getcwd()+"/data/background.png"
rostersfile_directory = os.getcwd()+"/data/rosters.csv"
character_image_directory = os.getcwd()+"/data/characters/"

characters = [
		"Fox", "Falco", "Marth", "Roy", "Sheik", "Zelda", "Mario", "Luigi", "Bowser",
		"Dr Mario", "Peach", "Yoshi", "Donkey Kong", "Captain Falcon", "Ganondorf",
		"Ness", "Ice Climbers", "Kirby", "Samus", "Link", "Young Link", "Pichu",
		"Pikachu", "Jigglypuff", "Mewtwo", "Mr Game and Watch"]

scoreboardmode = False

def createnewroster(team1name, team2name):
	rostersfile = open(rostersfile_directory, "r")
	roster1data = {}
	roster2data = {}
	playernum = 1
	for rosterline in rostersfile:
		if rosterline!=",\n" and rosterline!="\n" and rosterline!="":
			temptag, tempcharacter = rosterline.split(",", 1)
			tempcharacter = tempcharacter.lower().replace(" ","").replace("\n","").replace("&","").replace(".","")
			if playernum<=5:
				roster1data[temptag] = tempcharacter
			elif playernum>5 and playernum<=10:
				roster2data[temptag] = tempcharacter
		playernum+=1

	pic1 = Image.open(background_image)
	pic1.load()
	draw1 = ImageDraw.Draw(pic1)

	pic2 = Image.open(background_image)
	pic2.load()
	draw2 = ImageDraw.Draw(pic2)

	font=ImageFont.truetype("impact.ttf", 48)
	fontstartingsize=48
	team1length = draw1.textsize(str(team1name),font=font)[0]
	if team1length>450:
		team1name = team1name[:len(team1name)//2] + team1name[len(team1name)//2:].replace(" ", "\n", 1)
		team1length = draw1.multiline_textsize(str(team1name),font=font)[0]
		team1X = 250-(team1length//2)
		while team1length>450:
			fontstartingsize-=2
			font = ImageFont.truetype("impact.ttf", fontstartingsize)
			team1length = draw1.multiline_textsize(str(team1name),font=font)[0]
		team1X = 250-(team1length//2)
		draw1.multiline_text((team1X, 50), str(team1name), (255, 255, 255), font=font, align="center")
	else:
		team1X = 250-(team1length//2)
		draw1.text((team1X, 50), str(team1name), (255, 255, 255), font=font, align="center")

	font=ImageFont.truetype("impact.ttf", 48)
	fontstartingsize=48
	team2length = draw2.textsize(str(team2name),font=font)[0]
	if team2length>450:
		team2name = team2name[:len(team2name)//2] + team2name[len(team2name)//2:].replace(" ", "\n", 1)
		team2length = draw2.multiline_textsize(str(team2name),font=font)[0]
		team2X = 250-(team2length//2)
		while team2length>450:
			fontstartingsize-=2
			font = ImageFont.truetype("impact.ttf", fontstartingsize)
			team2length = draw2.multiline_textsize(str(team2name),font=font)[0]
			team2X = 250-(team2length//2)
		draw2.multiline_text((team2X, 50), str(team2name), (255, 255, 255), font=font, align="center")
	else:
		team2X = 250-(team2length//2)
		draw2.text((team2X, 50), str(team2name), (255, 255, 255), font=font, align="center")

	ycoord = 175
	for player1 in roster1data.keys():
		font=ImageFont.truetype("impact.ttf", 48)
		character = roster1data[player1]
		characterimage = Image.open(os.getcwd()+"/data/characters/"+character+".png").resize((48, 48))
		playertextsize = draw1.textsize(str(player1), font=font)[0]
		startingsize = 48
		while playertextsize>=300:
			startingsize-=2
			font = ImageFont.truetype("impact.ttf", startingsize)
			playertextsize = draw1.textsize(str(player1), font=font)[0]
		playertextX = 250 - (playertextsize//2)
		draw1.text((playertextX, ycoord), str(player1), (255, 255, 255), font=font, align="center")
		pic1.paste(characterimage, [50, ycoord+8, 98, ycoord+56], mask=characterimage)
		pic1.paste(characterimage, [402, ycoord+8, 450, ycoord+56], mask=characterimage)
		ycoord+=75

	ycoord = 175
	for player2 in roster2data.keys():
		font=ImageFont.truetype("impact.ttf", 48)
		character = roster2data[player2]
		characterimage = Image.open(os.getcwd()+"/data/characters/"+character+".png").resize((48, 48))
		playertextsize = draw2.textsize(str(player2), font=font)[0]
		startingsize = 48
		while playertextsize>=300:
			startingsize-=2
			font = ImageFont.truetype("impact.ttf", startingsize)
			playertextsize = draw2.textsize(str(player2), font=font)[0]
		playertextX = 250 - (playertextsize//2)
		draw2.text((playertextX, ycoord), str(player2), (255, 255, 255), font=font, align="center")
		pic2.paste(characterimage, [50, ycoord+8, 98, ycoord+56], mask=characterimage)
		pic2.paste(characterimage, [402, ycoord+8, 450, ycoord+56], mask=characterimage)
		ycoord+=75

	if scoreboardmode:
		pic1.save(os.getcwd()+"/../Scoreboard Assistant/output/rosters/file1.png")
		pic2.save(os.getcwd()+"/../Scoreboard Assistant/output/rosters/file2.png")
	else:
		pic1.save(os.getcwd()+"/output/image1.png")
		pic2.save(os.getcwd()+"/output/image2.png")
	return

def strikeoutplayer(tempfilename, player):
	if scoreboardmode:
		tempimage = Image.open(os.getcwd()+"/../Scoreboard Assistant/output/rosters/"+tempfilename)
		playernum = int(player)
		ycoord = 110+(playernum*75)
		cross = Image.open(os.getcwd()+"/data/cross.png")
		tempimage.paste(cross, [0,ycoord,500,ycoord+50], mask=cross)
		tempimage.save(os.getcwd()+"/../Scoreboard Assistant/output/rosters/"+tempfilename)
	else:
		tempimage = Image.open(os.getcwd()+"/output/"+tempfilename)
		playernum = int(player)
		ycoord = 110+(playernum*75)
		cross = Image.open(os.getcwd()+"/data/cross.png")
		tempimage.paste(cross, [0,ycoord,500,ycoord+50], mask=cross)
		tempimage.save(os.getcwd()+"/output/"+tempfilename)
	return

def main():
	QuitAfterCommand=False
	global scoreboardmode
	if len(sys.argv)>1:
		for arg in sys.argv:
			if arg == "S":
				print("Scoreboard Mode Active")
				scoreboardmode = True
			if arg == "FM":
				if scoreboardmode:
					t1name = open(os.getcwd()+"/../Scoreboard Assistant/output/schoolselection/player1.txt", "r").readline()
					t2name = open(os.getcwd()+"/../Scoreboard Assistant/output/schoolselection/player2.txt", "r").readline()
				else:
					t1name = input("Name of School 1: ")
					t2name = input("Name of School 2: ")
				createnewroster(t1name, t2name)
				QuitAfterCommand = True
			if arg == "SW":
				print("Swapping files")
				if scoreboardmode:
					file1 = Image.open(os.getcwd()+"/../Scoreboard Assistant/output/rosters/file1.png")
					file2 = Image.open(os.getcwd()+"/../Scoreboard Assistant/output/rosters/file2.png")
					file1.save(os.getcwd()+"/../Scoreboard Assistant/output/rosters/file3.png")
					file2.save(os.getcwd()+"/../Scoreboard Assistant/output/rosters/file1.png")
					file3 = Image.open(os.getcwd()+"/../Scoreboard Assistant/output/rosters/file3.png")
					file3.save(os.getcwd()+"/../Scoreboard Assistant/output/rosters/file2.png")

					school1 = Image.open(os.getcwd()+"/../Scoreboard Assistant/output/schoolselection/image1.png")
					school2 = Image.open(os.getcwd()+"/../Scoreboard Assistant/output/schoolselection/image2.png")
					school1.save(os.getcwd()+"/../Scoreboard Assistant/output/schoolselection/image3.png")
					school2.save(os.getcwd()+"/../Scoreboard Assistant/output/schoolselection/image1.png")
					school3 = Image.open(os.getcwd()+"/../Scoreboard Assistant/output/schoolselection/image3.png")
					school3.save(os.getcwd()+"/../Scoreboard Assistant/output/schoolselection/image2.png")

					p1scorefile = open(os.getcwd()+"/../Scoreboard Assistant/output/schoolselection/score1.txt", "r")
					p2scorefile = open(os.getcwd()+"/../Scoreboard Assistant/output/schoolselection/score2.txt", "r")
					p1score = p1scorefile.readline()
					p2score = p2scorefile.readline()
					p1scorefile.close()
					p2scorefile.close()
					p1scorefilew = open(os.getcwd()+"/../Scoreboard Assistant/output/schoolselection/score1.txt", "w")
					p2scorefilew = open(os.getcwd()+"/../Scoreboard Assistant/output/schoolselection/score2.txt", "w")
					p1scorefilew.write(p2score)
					p2scorefilew.write(p1score)
					p1scorefilew.close()
					p2scorefilew.close()
				else:
					file1 = Image.open(os.getcwd()+"/output/image1.png")
					file2 = Image.open(os.getcwd()+"/output/image2.png")
					file1.save(os.getcwd()+"/output/rosters/image3.png")
					file2.save(os.getcwd()+"/output/image1.png")
					file3 = Image.open(os.getcwd()+"/output/image3.png")
					file3.save(os.getcwd()+"/output/image2.png")

				QuitAfterCommand = True
			if arg == "O":
				os.startfile(os.getcwd()+"/data/rosters.csv")
				QuitAfterCommand = True
			if arg.startswith("X"):
				if scoreboardmode:
					filetostrike = "file"+arg[1]+".png"
				else:
					filetostrike = "image"+arg[1]+".png"
				strikeoutplayer(filetostrike, arg[2])
				QuitAfterCommand = True
	if QuitAfterCommand:
		return
	while (True):
		options = ["1. Create new roster", "2. Strike out player", "3. View Output Folder", "4. Open Rosters.csv (source)","Press <Enter> to exit"]
		print("Options:\n"+"\n".join(options)+"\n")
		optionselected = input("Choice: ")
		print("\n"*2)
		if "1" in optionselected:
			team1name = input("Please enter the name of Team 1: ")
			team2name = input("Please enter the name of Team 2: ")
			createnewroster(team1name, team2name)
		elif "2" in optionselected:
			tempfilename = ""
			while (True):
				team = input("Please input a team (1 or 2): ")
				if team=="1":
					tempfilename = "image1.png"
					break
				elif team=="2":
					tempfilename = "image2.png"
					break
				else:
					print("You did not enter a valid team number!")
			while (True):
				player = input("Please enter the eliminated player (1-5): ")
				if player=="1" or player=="2" or player=="3" or player=="4" or player=="5":
					break
				else:
					print("You did not enter a valid player number!")
			strikeoutplayer(tempfilename, player)
		elif "3" in optionselected:
			if scoreboardmode:
				os.startfile(os.getcwd()+"/../Scoreboard Assistant/input/rosters/")
			else:
				os.startfile(os.getcwd()+"/output/")
		elif "4" in optionselected:
			os.startfile(os.getcwd()+"/data/rosters.csv")
		elif optionselected == "":
			return
		else:
			print("Invalid option entere! Please try again")
	return

main()