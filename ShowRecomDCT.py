import pandas as pd
#read the data
df=pd.read_csv('Go_to_Show_decision.csv')
print(df)

#change the data to be numerical 
Nat={'UK':0,'USA':1,'N':2}
df['Nationality']=df['Nationality'].map(Nat)

Dec={'NO':0,'YES':1}
df['Go']=df['Go'].map(Dec)
print(df)

Selections=['Age','Experience','Rank','Nationality']
x=df[Selections]
y=df['Go']

print(x)

#Try Using Decision Tree
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

dtree=DecisionTreeClassifier()
dtree=dtree.fit(x,y)

#Decision tree uses earlier decisions to calculate the odds to wanting to go see a Singer or not.
plt.figure(figsize=(8, 6))
tree.plot_tree(dtree,feature_names=Selections,filled=True)
plt.show()

#Rank <= 6.5 means that every Singers with a rank of 6.5 or lower will follow the True
#samples = 13 means that there are 13 Singers left at this point in the decision, 

#value = [6, 7] means that of these 13 Singers, 6 will get a "NO", and 7 will get a "GO".
#gini = 0.497 refers to the quality of the split, and is always a number between 0.0 and 0.5
#Gini = (1 - (x/n)2 - (y/n).2) then we got (1 - (7 / 13).2 - (6 / 13)2 = 0.497)

#try to predict based on background  
#Should I show starring a 40 years old UK Singer, 10 years of experience, and a Singer ranking of 7?

class_label={1:'Go', 0:"Not Go"}

print("Based on the data you have inputted we recommend you to: ",[class_label[i] for i in dtree.predict([[40,10,7,0]])])
print("Based on the data you have inputted we recommend you to: ",[class_label[i] for i in dtree.predict([[40,10,6,0]])])

#----
def recom_dec():
    while True:
        try:
            X1 = int(input("Input Age of Artist: "))
            X2 = int(input("Experience (Years): "))
            X3 = int(input("Ranking: "))
            X4 = int(input("Nationality (0 for UK, 1 for USA and 2 for N/Other): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer value.")
    class_label={1:'Go', 0:"Not Go"}
    Model_Pred = [class_label[i] for i in dtree.predict([[X1,X2,X3,X4]])]
    Model_Preds= str(Model_Pred[0])
    
    print(f"if the artist with Age {X1} Experienced {X2} Years, Ranked {X3}, and Nationality {X4} We recommend you to : {Model_Preds} ")
    cont = input("Do you want to continue? (yes/no): ")
    if cont.lower() == "yes":
        recom_dec()  # recursive call to go back to the beginning
    else:
        print("Goodbye, thanks for using our service!  - Dhika")

recom_dec()

