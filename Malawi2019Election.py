# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 23:09:18 2024

@author: IAN CARTER KULANI
"""
#This software prompts the user to enter total number of published centers,total number of registered votes, total number of null and void votes, total number of valid votes and total valid votes for each candidate. Afterward,it determines the candidate with the majority of votes and displays the results on the screen.
#NOTE:For a candidate to be a majority winner the candidate total valid votes should be greater than majority votes.
print("==============================MALAWI ELECTROL COMMISSION==============================\n")
Totalpublishedcenters=int(input("Enter Total published centers:"))
#Get the total number of registered votes
TotalRegisteredvoters=int(input("Enter Total Registered Voters/Turnout:"))
#Get Total number of votes cast
Totalvotescast=int(input("Enter Total Votes Cast/Total Votes:"))
#Get total number of Null_&_Void votes
Nullandvoid=int(input("Enter Total Null_&_Void Votes/Invalid Votes:"))
#Get Total Valid Votes for All candidates
Totalvalidvotes=int(input("Enter Total Valid Votes:"))
#Get Total Valid Votes For Dr Lazarus MacCrthy Chakwera
Totalvalidvotesfor_Lazarusmaccarthychakwera=int(input("Enter Total Valid Votes For Dr Lazarus MacCrthy Chakwera:"))
#Get Total Valid Votes For Dr Saulos Klaus Chilima
Totalvalidvotesfor_Saulosklauschilima=int(input("Enter Total Valid Votes For Dr Saulos Klaus Chilima:"))
#Get Total Valid Votes For Professor John Eugene Chisi
Totalvalidvotesfor_ProfessorJohneugeneschisi=int(input("Enter Total Valid Votes For Professor John Eugene Chisi:"))
#Get Total Valid Votes For Reverend Hadwick Kayiya
Totalvalidvotesfor_ReverendHadwickayiya=int(input("Enter Total Valid Votes For Reverend Hadwick Kayiya:"))
#Get  For Peter DSD Kuwani
Totalvalidvotesfor_Peterkuwani=int(input("Enter Total Valid Votes For Peter DSD Kuwani:"))
#Get Total Valid Votes For Atupele Muluzi
Totalvalidvotesfor_Atupelemuluzi=int(input("Enter Total Valid Votes For Atupele Muluzi:"))
#Get Total Valid Votes For Professor Arthu Peter Mutharika
Totalvalidvotesfor_profarthurpetermuthalika=int(input("Enter Total Valid Votes For Professor Arthu Peter Mutharika:"))

percent=100

if Totalvalidvotesfor_Lazarusmaccarthychakwera>Totalvalidvotes/2+1:
   print("Congratulations Dr Lazarus MacCrthy Chakwera is the winner of 2019 Election\n\n") 
#
elif Totalvalidvotesfor_Saulosklauschilima>Totalvalidvotes/2+1:
   print("Congratulations Dr Saulos Klaus Chilima you're the winner of 2019 Election\n\n") 
#
elif Totalvalidvotesfor_ProfessorJohneugeneschisi>Totalvalidvotes/2+1:
   print("Congratulations Professor John Eugene Chisi you're the winner of 2019 Election\n\n") 
#     
elif Totalvalidvotesfor_ReverendHadwickayiya>Totalvalidvotes/2+1:
   print("Congratulations Reverend Hadwick Kayiya is the winner of 2019 Election\n\n") 
#
elif Totalvalidvotesfor_Peterkuwani>Totalvalidvotes/2+1:
   print("Congratulations candidate E you're the winner of 2019 Election\n\n") 
#
elif Totalvalidvotesfor_Atupelemuluzi>Totalvalidvotes/2+1:
   print("Congratulations Atupele Muluzi you're the winner of 2019 Election\n\n") 
#
elif Totalvalidvotesfor_profarthurpetermuthalika>Totalvalidvotes/2+1:
   print("Congratulations Professor Arthu Peter Muthalika you're the winner of 2020 Election\n\n")   
else:
     print("No majority winner was found RUNOFF May be required\n\n\n")  


print("_________________________________ELECTION STATISTICS_____________________________________\n")   
#calculating Percentage 
 
#Calculating percentage for total votes cast
Percentage=round(Totalvalidvotes*percent/Totalvalidvotes, 2);
print("Total Votes Cast in percentage=",Percentage)
#Calculating percentage for total valid votes for all canidates
Percentage=round(Totalvalidvotes*percent/Totalvotescast, 2);
print("Total Valid Votes for all candidtes in percentage=",Percentage)
#Calculating percentage for null_&_void votes
Percentage=round(Nullandvoid*percent/Totalvalidvotes, 2);
print("Total Null_&_Void in percentage=",Percentage)
#calculating total registered voters/turnout
Percentage=round(Totalvotescast*percent/TotalRegisteredvoters, 2);
print("Total Registered voters/turnout in percentage=",Percentage)
#Calculating percentage for Dr Lazarus MacCrthy Chakwera
Percentage=round(Totalvalidvotesfor_Lazarusmaccarthychakwera*percent/Totalvalidvotes, 2);
print("Dr Lazarus MacCrthy Chakwera in percent=",Percentage)
#Calculating percentage for Dr Saulos Klaus Chilima
Percentage=round(Totalvalidvotesfor_Saulosklauschilima*percent/Totalvalidvotes, 2);
print("Total Valid Votes For Dr Saulos Klaus Chilima in percentage=",Percentage)
#Calculating percentage for Professor John Eugene Chisi
Percentage=round(Totalvalidvotesfor_ProfessorJohneugeneschisi*percent/Totalvalidvotes, 2);
print("Total Valid Votes For Professor John Eugene Chisi in percentage=",Percentage)
#Calculating percentage for Reverend Hadwick Kayiya
Percentage=round(Totalvalidvotesfor_ReverendHadwickayiya*percent/Totalvalidvotes, 2);
print("Total Valid Votes For Reverend Hadwick Kayiya in percentage=",Percentage)
#Calculating percentage for Peter DSD Kuwani
Percentage=round(Totalvalidvotesfor_Peterkuwani*percent/Totalvalidvotes, 2);
print("Total Valid Votes For Peter DSD Kuwani in percentage=",Percentage)
#Calculating percentage for Atupele Muluzi
Percentage=round(Totalvalidvotesfor_Atupelemuluzi*percent/Totalvalidvotes, 2);
print("Total Valid Votes For Atupele Muluzi in percentage=",Percentage)
#Calculating percentage for Professor Arthu Peter Muthalika
Percentage=round(Totalvalidvotesfor_profarthurpetermuthalika*percent/Totalvalidvotes, 2);
print("Total Valid Votes For Professor Arthu Peter Muthalika in percentage=",Percentage)

print("==========================================================================================\n")







