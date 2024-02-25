# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 23:09:18 2024

@author: IAN CARTER KULANI
"""

print("==============================MALAWI ELECTROL COMMISSION==============================\n")
Totalpublishedcenters=int(input("Enter Total published centers:"))
#Get the total number of registered votes
TotalRegisteredvotes=int(input("Enter Total Registered Votes:"))
#Get Total number of votes cast
Totalvotescast=int(input("Enter Total Votes Cast:"))
#Get total number of Null_&_Void votes
Nullandvoid=int(input("Enter Total Null and Void Votes:"))
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
   
majority_percent=Totalvalidvotesfor_Lazarusmaccarthychakwera*percent/Totalvalidvotes;
print("Dr Lazarus MacCrthy Chakwerain percent=", majority_percent)
majority_percent=Totalvalidvotesfor_Saulosklauschilima*percent/Totalvalidvotes;
print("Total Valid Votes For Dr Saulos Klaus Chilima in percent=", majority_percent)
majority_percent=Totalvalidvotesfor_ProfessorJohneugeneschisi*percent/Totalvalidvotes;
print("Total Valid Votes For Professor John Eugene Chisi in percent=", majority_percent)
majority_percent=Totalvalidvotesfor_ReverendHadwickayiya*percent/Totalvalidvotes;
print("Total Valid Votes For Reverend Hadwick Kayiya in percent=", majority_percent)
majority_percent=Totalvalidvotesfor_Peterkuwani*percent/Totalvalidvotes;
print("Total Valid Votes For Peter DSD Kuwani in percent=",majority_percent)
majority_percent=Totalvalidvotesfor_Atupelemuluzi*percent/Totalvalidvotes;
print("Total Valid Votes For Atupele Muluzi in percent=",majority_percent)
majority_percent=Totalvalidvotesfor_profarthurpetermuthalika*percent/Totalvalidvotes;
print("Total Valid Votes For Professor Arthu Peter Muthalika in percent=",majority_percent)

print("==========================================================================================\n")







