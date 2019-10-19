import matplotlib.pyplot as plt
import numpy as np
import csv
x= []
y= []
x1=[]
y1=[]
x2=[]
y2=[]
x3=[]
y3=[]
x4=[]
y4=[]
x5=[]
y5=[]
x6=[]
y6=[]
x7=[]
y7=[]
x8=[]
y8=[]
x9=[]
y9=[]
x10=[]
y10=[]
x11=[]
y11=[]
x12=[]
y12=[]
x13=[]
y13=[]
x14=[]
y14=[]

print("\n\t\tWELCOME TO RESULT ANALYSIS")

while True:
	print("\n\t\t\tMAIN MENU\t")
	print("\n\t\t 1.GRAPHICAL ANALYSIS \n\t\t 2.DATA WISE ANALYSIS \n\t\t 3.EXIT ")
	option=input("\n\t\t Enter how you want to analyse marks  : ")

	if option==1:
            while True:
		 print("\n\t\t   =====GRAPH MENU=====\n")
		 print("\t\t    YEAR WISE ANALYSIS \n\t\t    1.2013\n\t\t    2.2014 \n\t\t    3.2015 \n\t\t    4.2016 \n\t\t    5.2017 \n\t\t    6.Exit")
		 type=input("\n\t\t    Enter your option : ")

		 with open('studentd.csv','r') as csvfile:
		   plots= csv.reader(csvfile,delimiter=',')
		   for row in plots:
		       x.append(int(row[0]))
		       y.append(int(row[2]))
		       x1.append(int(row[0]))
		       y1.append(int(row[3] ))
		       x2.append(int(row[0]))
		       y2.append(int(row[4]))

		       x3.append(int(row[5]))
		       y3.append(int(row[7]))
		       x4.append(int(row[5]))
		       y4.append(int(row[8])) 
		       x5.append(int(row[5]))
		       y5.append(int(row[9]))

		       x6.append(int(row[10]))
		       y6.append(int(row[12] ))
		       x7.append(int(row[10]))
		       y7.append(int(row[13]))
		       x8.append(int(row[10]))
		       y8.append(int(row[14]))
		  

		       x9.append(int(row[15]))
		       y9.append(int(row[17]))
		       x10.append(int(row[15]))
		       y10.append(int(row[18])) 
		       x11.append(int(row[15]))
		       y11.append(int(row[19]))

		       x12.append(int(row[20]))
		       y12.append(int(row[22]))
		       x13.append(int(row[20]))
		       y13.append(int(row[23]))
		       x14.append(int(row[20]))
		       y14.append(int(row[24]))

		 plt.xlabel('Roll No')
		 plt.ylabel('mark')
		 my_xticks=['1','2','3','4','5']
		 plt.xticks(x,my_xticks)

		 if type==1:
		   plt.plot(x,y,'^',color='k',label='TOC')
		   plt.plot(x1,y1,'+',label='SDL')
		   plt.plot(x2,y2,'*',label='CN')
		   plt.legend()
		   plt.grid()
		   plt.show()

		 elif type==2:
		   plt.plot(x3,y3,label='TOC')
		   plt.plot(x4,y4,label='SDL')
		   plt.plot(x5,y5,label='CN')
		   plt.legend()
		   plt.grid()
		   plt.show()

		 elif type==3:
		   plt.plot(x6,y6,label='TOC')
		   plt.plot(x7,y7,label='SDL')
		   plt.plot(x8,y8,label='CN')
		   plt.xticks(rotation=90)
		   plt.legend()
		   plt.show()

		 elif type==4:
		   plt.bar(x9,y9,color='b',alpha= 0.8)
		   plt.bar(x10,y10,color='g',alpha= 0.2)
		   plt.bar(x11,y11,color='r',alpha= 0.5)
		   plt.legend()
		   plt.show() 

		 elif type==5:
		   plt.plot(x12,y12,label='TOC')
		   plt.plot(x13,y13,label='SDL')
		   plt.plot(x14,y14,label='CN')
		   plt.legend()
		   plt.show()

		 
		 elif type==6:
			break

                 else:
                     print("\n\t\t    .....SORRY YOU ENTERED WRONG CHOICE.....")
                         
	elif option==2:
           while True:
   
                 print("\n\t\t   =====DATA MENU=====\n")
		 print(" \n\t\t    1.HIGGEST SCORE PER YEAR \n\t\t    2.LOWEST SCORE PER YEAR \n\t\t    3.AVERAGE SCORE PER YEAR\n\t\t    4.Exit")
		 type1=input("\n\t\t    Enter your option : ") 

                 if type1==1:
                    while True :
           	      list1=[59,80,79,85,69]
		      list2=[99,75,88,45,68]
		      list3=[78,85,47,78,68]
		      list4=[78,72,82,78,81]
		      list5=[76,65,78,67,76]
		      list6=[75,67,90,74,87]
		      list7=[86,78,68,89,74]
		      list8=[78,67,75,87,78]
		      list9=[74,73,81,83,71]
		      list10=[68,75,65,67,89]
		      list11=[72,72,89,67,56]
		      list12=[73,67,80,73,82]
		      list13=[78,69,70,72,73]
	              list14=[65,76,60,81,81]
                      list15=[75,78,68,83,78]


                      print("\n\t\t   *****SUBJECT MENU*****")
                      print("\n\t\t    1.TOC \n\t\t    2.SDL \n\t\t    3.CN \n\t\t    4.Exit ")
                      option1=input("\n\t\t   Enter the subject No. : ")
                      if option1==1:
                                   print"\n\t\t\t =====TOC=====\n"
				   print"\t\t  Highest marks in TOC in 2013:=:",max(list1);
				   print"\t\t  Highest marks in TOC in 2014:=:",max(list4);
				   print"\t\t  Highest marks in TOC in 2015:=:",max(list7);
				   print"\t\t  Highest marks in TOC in 2016:=:",max(list10);
				   print"\t\t  Highest marks in TOC in 2017:=:",max(list13);

				   
				   
				   
                      elif option1==2:
                                   print"\n\t\t\t =====SDL=====\n"
				   print"\t\t  Highest marks in SDL in 2013:=:",max(list2);
				   print"\t\t  Highest marks in SDL in 2014:=:",max(list5);
				   print"\t\t  Highest marks in SDL in 2015:=:",max(list8);
				   print"\t\t  Highest marks in SDL in 2016:=:",max(list11);
				   print"\t\t  Highest marks in SDL in 2017:=:",max(list14);


                      elif option1==3:
                                   print"\n\t\t\t =====CN=====\n"
				   print"\t\t  Highest marks in CN in 2013:=:",max(list3);
				   print"\t\t  Highest marks in CN in 2014:=:",max(list6);
				   print"\t\t  Highest marks in CN in 2015:=:",max(list9);
				   print"\t\t  Highest marks in CN in 2016:=:",max(list12);
				   print"\t\t  Highest marks in CN in 2017:=:",max(list15);


                      elif option1==4:
                                   break
		      else:
                           print("\n\t\t    .....SORRY YOU ENTERED WRONG CHOICE.....")
                         	   				   

                 elif type1==2:
                   while True :
           	      list1=[59,80,79,85,69]
		      list2=[99,75,88,45,68]
		      list3=[78,85,47,78,68]
		      list4=[78,72,82,78,81]
		      list5=[76,65,78,67,76]
		      list6=[75,67,90,74,87]
		      list7=[86,78,68,89,74]
		      list8=[78,67,75,87,78]
		      list9=[74,73,81,83,71]
		      list10=[68,75,65,67,89]
		      list11=[72,72,89,67,56]
		      list12=[73,67,80,73,82]
		      list13=[78,69,70,72,73]
	              list14=[65,76,60,81,81]
                      list15=[75,78,68,83,78]


                      print("\n\t\t   ******SUBJECT MENU*****")
                      print("\n\t\t    1.TOC \n\t\t    2.SDL \n\t\t    3.CN \n\t\t    4.Exit ")
                      option2=input("\n\t\t   Enter the subject No. : ")
                      if option2==1:
                                   print"\n\t\t\t =====TOC=====\n"
				   print"\t\t  Lowest marks in TOC in 2013:=:",min(list1);
				   print"\t\t  Lowest marks in TOC in 2014:=:",min(list4);
				   print"\t\t  Lowest marks in TOC in 2015:=:",min(list7);
				   print"\t\t  Lowest marks in TOC in 2016:=:",min(list10);
				   print"\t\t  Lowest marks in TOC in 2017:=:",min(list13);				  
				   
		      elif option2==2:
                                   print"\n\t\t\t =====SDL=====\n"
				   print"\t\t  Lowest marks in SDL in 2013:=:",min(list2);
				   print"\t\t  Lowest marks in SDL in 2014:=:",min(list5);
				   print"\t\t  Lowest marks in SDL in 2015:=:",min(list8);
				   print"\t\t  Lowest marks in SDL in 2016:=:",min(list11);
				   print"\t\t  Lowest marks in SDL in 2017:=:",min(list14);				   
                      elif option2==3:
                                   print"\n\t\t\t ======CN=====\n"
				   print"\t\t  Lowest marks in CN in 2013:=:",min(list3);
				   print"\t\t  Lowest marks in CN in 2014:=:",min(list6);
				   print"\t\t  Lowest marks in CN in 2015:=:",min(list9);
				   print"\t\t  Lowest marks in CN in 2016:=:",min(list12);
				   print"\t\t  Lowest marks in CN in 2017:=:",min(list15);

                      elif option2==4:
                                   break
                      else:
                            print("\n\t\t    .....SORRY YOU ENTERED WRONG CHOICE.....")
                         
				   
                 elif type1==3:
                       while True :
		   	      list1=[59,80,79,85,69]
			      list2=[99,75,88,45,68]
			      list3=[78,85,47,78,68]
			      list4=[78,72,82,78,81]
			      list5=[76,65,78,67,76]
			      list6=[75,67,90,74,87]
			      list7=[86,78,68,89,74]
			      list8=[78,67,75,87,78]
			      list9=[74,73,81,83,71]
			      list10=[68,75,65,67,89]
			      list11=[72,72,89,67,56]
			      list12=[73,67,80,73,82]
			      list13=[78,69,70,72,73]
			      list14=[65,76,60,81,81]
		              list15=[75,78,68,83,78]
		              print("\n\t\t   ******SUBJECT MENU*****")
		              print("\n\t\t    1.TOC \n\t\t    2.SDL \n\t\t    3.CN \n\t\t    4.Exit ")
		              option3=input("\n\t\t   Enter the subject No. : ")
                              if option3==1:
                                   print"\n\t\t\t =====TOC=====\n"
				   print"\t\t  Average score in TOC in 2013:=:",(sum(list1)/len(list1));
				   print"\t\t  Average score in TOC in 2014:=:",(sum(list4)/len(list4));
				   print"\t\t  Average score in TOC in 2015:=:",(sum(list7)/len(list7));
				   print"\t\t  Average score in TOC in 2016:=:",(sum(list10)/len(list10));
				   print"\t\t  Average score in TOC in 2017:=:",(sum(list13)/len(list13));			  
				   
		              elif option3==2:
                                   print"\n\t\t\t =====SDL=====\n"
				   print"\t\t  Average score in SDL in 2013:=:",(sum(list2)/len(list2));
				   print"\t\t  Average score in SDL in 2014:=:",(sum(list5)/len(list5));
				   print"\t\t  Average score in SDL in 2015:=:",(sum(list8)/len(list8));
				   print"\t\t  Average score in SDL in 2016:=:",(sum(list11)/len(list11));
			           print"\t\t  Average score in SDL in 2017:=:",(sum(list14)/len(list14));				   
                              elif option3==3:
                                   print"\n\t\t\t ======CN=====\n"
				   print"\t\t  Average score in CN in 2013:=:",(sum(list3)/len(list3));
				   print"\t\t  Average score in CN in 2014:=:",(sum(list6)/len(list6));
				   print"\t\t  Average score in CN in 2015:=:",(sum(list9)/len(list9));
				   print"\t\t  Average score in CN in 2016:=:",(sum(list12)/len(list12));
				   print"\t\t  Average score in CN in 2017:=:",(sum(list15)/len(list15));

                              elif option3==4:
                                   break
                              else:
                                 print("\n\t\t    .....SORRY YOU ENTERED WRONG CHOICE.....")
                         	 
                 elif type1==4:
                       break

                 else:
                     print("\n\t\t    .....SORRY YOU ENTERED WRONG CHOICE.....")
                         


	elif option==3:
                print("\n\t\t\t\t*****THANK-YOU*****\n\t")
                print("\t\t\t\t=====PROJECT BY=====")
                print("\t\t\t\t  Shreya Joshi")
                print("\t\t\t\t  Priti Gumaste")
                print("\t\t\t\t  Srushtee Khadpekar")
                print("\n\n\t\t\t\t=====GUIDED BY=====")
                print("\t\t\t\tPROF.SAJAL PRAMANIK SIR \n\n")
                break

        else:
             print("\n\t\t    .....SORRY YOU ENTERED WRONG CHOICE.....")
                         
 



