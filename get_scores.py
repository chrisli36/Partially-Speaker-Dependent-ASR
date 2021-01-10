#! /usr/bin/python

# We are getting 10 scores from each trial
# The 4 treatments are:
# 	(1) unadapted training process that tests the target speaker
# 	(2) adapted training process that tests the target speaker
# 	(3) unadapted training process that tests many speakers
# 	(4) adapted training process that tests many speakers
#
# The goal is to show that adapting the training process
# improves WER on the target speaker while not affecting
# WER overall
#
# In other words, we want (2) to be better than (1)
# and (3) to be about the same as (4)


import os
import sys

def isDelineater(letter):
	return (letter==" " or letter=="|")
	
def separate(string):
	# this functions separates the words/numbers by whitepace and pipe
	output = []
	previous = " "
	word = ""
	for letter in string:
		if not isDelineater(letter) and isDelineater(previous):
			word = letter
		elif not isDelineater(letter) and not isDelineater(previous):
			word += letter
		elif isDelineater(letter) and not isDelineater(previous):
			output.append(word)
		previous = letter
	output.append(word)
	return output

# the user must input the randomly chosen target speaker
print "Target speaker? "
targetSpeaker = raw_input()

for whichSpeakers in ["with","without"]:
	for whichTraining in ["adapted","unadapted"]:
	
		print "---------------------------------------------------"
		print "The {} training {} the target speaker test set".format(whichTraining,whichSpeakers)
		print "---------------------------------------------------"
		
		# Move to directory
		os.chdir("{}_{}/exp/".format(whichTraining, whichSpeakers))
		
		# iterates through the 3 trials * 10 scores = 30 score files
		for trial in range(1,4):
			WERs = []
			if whichSpeakers == "with":
				speakerWERs = []
		
			print "TRIAL " + str(trial)
			
			for score in range(1,11):
				fin = open("tri4_nnet_{}/decode_test/score_{}/ctm_39phn.filt.sys".format(trial,score), "r")
				scoreList = [separate(line.strip()) for line in fin]
				# print scoreList
				for count in range(len(scoreList)):
					if targetSpeaker in scoreList[count]:
						speakerIndex = count
					elif "SPKR" in scoreList[count]:
						begin = count
					elif "Sum/Avg" in scoreList[count]:
						end = count
				
				if "speakerIndex" not in globals():
					print "You have entered or chosen the target speaker incorrectly"
					sys.exit()
						
				# this is to get a more accurate WER
				if whichSpeakers == "with":
					Errs = [float(scoreList[i][7]) for i in range(begin+2, end, 2)]
				else:
					Errs = [float(scoreList[i][7]) for i in range(begin+2, end, 2) if targetSpeaker not in scoreList[i]]
				WERs.append(str(sum(Errs)/len(Errs)))
				
				# appends to speakerWER if the speaker was tested
				if whichSpeakers == "with":
					speakerWERs.append(str(float(scoreList[speakerIndex][7])))
					
				fin.close()
				
			print("General WER scores: " + ",".join(WERs))
			if whichSpeakers == "with":
				print("Speaker WER scores: " + ",".join(speakerWERs))
		print "\n"
				
		# Move back to the /kaldi/egs/timit directory
		os.chdir("../../")



