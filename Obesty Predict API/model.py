import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from collections import Counter
from imblearn import under_sampling,over_sampling
from imblearn.over_sampling import RandomOverSampler
from sklearn.model_selection import train_test_split


def prediction(input_data):
    data='https://raw.githubusercontent.com/AmmarTaradifa/Capstone-Bangkit-2023-BoBy/main/ObesityDataSet_raw_and_data_sinthetic.csv'
    df=pd.read_csv(data)

    FAF=(df.FAF==0).sum()
    TUE=(df.TUE==0).sum()


    df['FAF']=df['FAF'].replace(0,np.NaN)
    df['TUE']=df['TUE'].replace(0,np.NaN)

    from sklearn.preprocessing import LabelEncoder
    encoder=LabelEncoder()

    NObeyesdad=encoder.fit_transform(df['NObeyesdad'])
    NObeyesdad
    df['NObeyesdad']=NObeyesdad

    df.loc[(df['FAF'].isnull()) & (df['TUE'].isnull())] #ganti nilainya dengan mean

    df.NObeyesdad.value_counts()

    faf_label_0=df[df['NObeyesdad']==0]['FAF'].mean()
    faf_label_1=df[df['NObeyesdad']==1]['FAF'].mean()
    faf_label_2=df[df['NObeyesdad']==2]['FAF'].mean()
    faf_label_3=df[df['NObeyesdad']==3]['FAF'].mean()
    faf_label_4=df[df['NObeyesdad']==4]['FAF'].mean()
    faf_label_5=df[df['NObeyesdad']==5]['FAF'].mean()
    faf_label_6=df[df['NObeyesdad']==6]['FAF'].mean()

    tue_label_0=df[df['NObeyesdad']==0]['TUE'].mean()
    tue_label_1=df[df['NObeyesdad']==1]['TUE'].mean()
    tue_label_2=df[df['NObeyesdad']==2]['TUE'].mean()
    tue_label_3=df[df['NObeyesdad']==3]['TUE'].mean()
    tue_label_4=df[df['NObeyesdad']==4]['TUE'].mean()
    tue_label_5=df[df['NObeyesdad']==5]['TUE'].mean()
    tue_label_6=df[df['NObeyesdad']==6]['TUE'].mean()

    #mengganti nilai FAF 
    df.loc[df['NObeyesdad']==0,'FAF']=df.loc[df['NObeyesdad']==0,'FAF'].fillna(faf_label_0)
    df.loc[df['NObeyesdad']==1,'FAF']=df.loc[df['NObeyesdad']==1,'FAF'].fillna(faf_label_1)
    df.loc[df['NObeyesdad']==2,'FAF']=df.loc[df['NObeyesdad']==2,'FAF'].fillna(faf_label_2)
    df.loc[df['NObeyesdad']==3,'FAF']=df.loc[df['NObeyesdad']==3,'FAF'].fillna(faf_label_3)
    df.loc[df['NObeyesdad']==4,'FAF']=df.loc[df['NObeyesdad']==4,'FAF'].fillna(faf_label_4)
    df.loc[df['NObeyesdad']==5,'FAF']=df.loc[df['NObeyesdad']==5,'FAF'].fillna(faf_label_5)
    df.loc[df['NObeyesdad']==6,'FAF']=df.loc[df['NObeyesdad']==6,'FAF'].fillna(faf_label_6)

    #MENGGANTI NILAI tue
    df.loc[df['NObeyesdad']==0,'TUE']=df.loc[df['NObeyesdad']==0,'TUE'].fillna(tue_label_0)
    df.loc[df['NObeyesdad']==1,'TUE']=df.loc[df['NObeyesdad']==1,'TUE'].fillna(tue_label_1)
    df.loc[df['NObeyesdad']==2,'TUE']=df.loc[df['NObeyesdad']==2,'TUE'].fillna(tue_label_2)
    df.loc[df['NObeyesdad']==3,'TUE']=df.loc[df['NObeyesdad']==3,'TUE'].fillna(tue_label_3)
    df.loc[df['NObeyesdad']==4,'TUE']=df.loc[df['NObeyesdad']==4,'TUE'].fillna(tue_label_4)
    df.loc[df['NObeyesdad']==5,'TUE']=df.loc[df['NObeyesdad']==5,'TUE'].fillna(tue_label_5)
    df.loc[df['NObeyesdad']==6,'TUE']=df.loc[df['NObeyesdad']==6,'TUE'].fillna(tue_label_6)

    # Q1=df.quantile(0.25)
    # Q3=df.quantile(0.75)
    # IQR=Q3-Q1
    # df=df[~((df<(Q1-1.5*IQR))|(df>(Q3+1.5*IQR))).any(axis=1)]

        #untuk gender
    Gender=encoder.fit_transform(df['Gender'])
    Gender

    #untuk gamily history weight
    family_history_with_overweight=encoder.fit_transform(df['family_history_with_overweight'])
    family_history_with_overweight

    #untuk CAEC
    CAEC=encoder.fit_transform(df['CAEC'])
    CAEC

    #untuk FAVC
    FAVC=encoder.fit_transform(df['FAVC'])
    FAVC

    #untuk SMOKE
    SMOKE=encoder.fit_transform(df['SMOKE'])
    SMOKE

    #untuk SCC
    SCC=encoder.fit_transform(df['SCC'])
    SCC

    #untuk CALC
    CALC=encoder.fit_transform(df['CALC'])
    CALC

    #untuk MTRANS
    MTRANS=encoder.fit_transform(df['MTRANS'])
    MTRANS

    df['Gender']=Gender
    df['family_history_with_overweight']=family_history_with_overweight
    df['CAEC']=CAEC
    df['FAVC']=FAVC
    df['SCC']=SCC
    df['SMOKE']=SMOKE
    df['CALC']=CALC
    df['MTRANS']=MTRANS

    label=df['NObeyesdad']
    features=df[['Weight','family_history_with_overweight','Height','Age','FAVC']]

    X=features
    y=label
    ros=RandomOverSampler()
    X_resample,y_resample=ros.fit_resample(X,y)
    # print(sorted(Counter(y_resample).items()),y_resample.shape)

    X_train, X_test, y_train,y_test=train_test_split(X_resample,y_resample,test_size=0.2, random_state=123)

    scaler=StandardScaler()
    X_train=scaler.fit_transform(X_train)
    X_test=scaler.transform(X_test)

    from sklearn.tree import DecisionTreeClassifier
   
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    pred = clf.predict(X_test)
    # print(confusion_matrix(y_test,pred))
    # print(classification_report(y_test,pred))

    # accuracy = accuracy_score(y_test, pred)
    # print("Accuracy:", accuracy)

    # y_pred_prob = clf.predict_proba(X_test)  # Predict class probabilities
    # loss = log_loss(y_test, y_pred_prob)
    # print("Loss:", loss)
    # print(confusion_matrix(y_test,pred))
    # print(classification_report(y_test,pred))

    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshape=input_data_as_numpy_array.reshape(1,-1)
    input_data_reshape_std=scaler.transform(input_data_reshape)
    prediction=clf.predict(input_data_reshape_std)
    
    print(prediction)

    import pickle
    filename='decision_model.pkl'
    pickle.dump(clf,open(filename,'wb'))
    pickle.dump(scaler,open('standar.pkl','wb'))

    model = pickle.load(open('decision_model.pkl','rb'))

    if (prediction==0):
        print('\nNormal_Weight')
    elif(prediction==1):
        print('\nOverweight_Level_I')
    elif(prediction==2):
        print('\nOverweight_Level_II')
    elif(prediction==3):
        print('\nObesity_Type_I')
    elif (prediction==4):
        print('\nInsufficient_Weight')
    elif(prediction==5):
        print('\nObesity_Type_II')
    else:
        print('\nObesity_Type_III')

weight=input('Masukkan berat badan anda:')
riwayat=input('Ada riwayat obesitas?: ')
riwayat=riwayat.lower()
height=input("Masukkan tinggi badan: ")
Age=input("Masukkan umur: ")
FAVC=input("Sering mengkonsumsi daging?: ")
FAVC=FAVC.lower()

if (riwayat=='iya'):
    riwayat=1
else:
    riwayat=0

if(FAVC=='iya'):
    FAVC=1
else:
    FAVC=0
        
prediction([weight,riwayat,height,Age,FAVC])


