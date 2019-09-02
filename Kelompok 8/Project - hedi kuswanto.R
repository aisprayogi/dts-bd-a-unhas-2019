

#PEMBAGIAN DATA 70% dan 30%
s <- sample(2, nrow(Data_obesitas), replace = T, prob = c(0.7, 0.3)) 
train_TP2 <- Data_obesitas[s == 1,]
test_TP2 <- Data_obesitas[s == 2,]
dim(train_TP1)
dim(test_TP2)

#CART
library(rpart)
library(caret)
visual_TP2 <- rpart(status_obesitas ~.,train_TP2, method = "class")
rpartpred <- predict(visual_TP2,test_TP2,type = "class")
cfm_TP <- confusionMatrix(rpartpred,test_TP2$status_obesitas)

library(pROC)
library(ROCR)
rpartprobte_TP <- predict(visual_TP2,test_TP2,type = "prob")
auc_TP <- auc(test_TP2$status_obesitas,rpartprobte_TP[,2])

library(C50)
visual_TP2_1 <- C5.0(status_obesitas ~.,train_TP2)
rpartpred <- predict(visual_TP2_1,test_TP2,type = "class")
cfm_TP_1 <- confusionMatrix(rpartpred,test_TP2$status_obesitas)

library(pROC)
library(ROCR)
rpartprobte_TP_1 <- predict(visual_TP2_1,test_TP2,type = "prob")
auc_TP_1 <- auc(test_TP2$status_obesitas,rpartprobte_TP_1[,2])

#Melihat Keseimbangan Data
prop.table(table(Variabel$status_obesitas))
barplot(prop.table(table(Variabel$status_obesitas)),
        col = rainbow(2),
        ylim = c(0,1),
        main = "Sebelum SMOTE")

#Menyeimbangkan Data
#SMOTE
library(DMwR)
##Model 5:5
model1 <- SMOTE(status_obesitas ~ ., Tanpa_SMOTE, k=5, perc.over = 250, perc.under=150)

##Model 4:6
model2 <- SMOTE(status_obesitas ~ ., train_TP2, k=5, perc.over = 350)

##Model 6:4
model3 <- SMOTE(status_obesitas ~ ., Tanpa_SMOTE, k=5, perc.over = 600)

#Hasil SMOTE    
model1 <- as.data.set(spss.system.file('E:dataobes1.sav'))
model2 <- as.data.set(spss.system.file('E:dataobes2.sav'))
model3 <- as.data.set(spss.system.file('E:dataobes3.sav'))
smote1 <- data.frame(model1)
smote2 <- data.frame(model2)
smote3 <- data.frame(model3)

barplot(prop.table(table(smote2$status_obesitas)),
        col = c(30,31),
        ylim = c(0,1),
        main = "Oversampling 250 dan Undersampling 150")

#PEMBAGIAN DATA 70% DAN 30%
s <- sample(2, nrow(smote1), replace = T, prob = c(0.7, 0.3)) # training row indices
Data_obesitas_train_sm12 <- smote1[s == 1,]
Data_obesitas_test_sm12 <- smote1[s == 2,]

#PEMBAGIAN DATA 70% DAN 30%
s <- sample(2, nrow(smote2), replace = T, prob = c(0.7, 0.3)) # training row indices
Data_obesitas_train_sm22 <- smote2[s == 1,]
Data_obesitas_test_sm22 <- smote2[s == 2,]

#PEMBAGIAN DATA 70% DAN 30%
s <- sample(2, nrow(smote3), replace = T, prob = c(0.7, 0.3)) # training row indices
Data_obesitas_train_sm32 <- smote3[s == 1,]
Data_obesitas_test_sm32 <- smote3[s == 2,]


#Melihat Keseimbangan Data
prop.table(table(smote3$status_obesitas))
barplot(prop.table(table(smote3$status_obesitas)),
        col = rainbow(2),
        ylim = c(0,1),
        main = "SMOTE")


#CART
library(rpart)
library(caret)

#70%
visual7 <- rpart(status_obesitas ~.,Data_obesitas_train_sm12, method = "class")
visual8 <- rpart(status_obesitas ~.,Data_obesitas_train_sm22, method = "class")
visual9 <- rpart(status_obesitas ~.,Data_obesitas_train_sm32, method = "class")

#70%
rpartpred7 <- predict(visual7,Data_obesitas_test_sm12,type = "class")
rpartpred8 <- predict(visual8,Data_obesitas_test_sm22,type = "class")
rpartpred9 <- predict(visual9,Data_obesitas_test_sm32,type = "class")
cfm7 <- confusionMatrix(rpartpred7,Data_obesitas_test_sm12$status_obesitas)
cfm8 <- confusionMatrix(rpartpred8,Data_obesitas_test_sm22$status_obesitas)
cfm9 <- confusionMatrix(rpartpred9,Data_obesitas_test_sm32$status_obesitas)

library(pROC)
library(ROCR)
rpartprobte_sm7 <- predict(visual7,Data_obesitas_test_sm12,type = "prob")
rpartprobte_sm8 <- predict(visual8,Data_obesitas_test_sm22,type = "prob")
rpartprobte_sm9 <- predict(visual9,Data_obesitas_test_sm32,type = "prob")
auc7 <- auc(Data_obesitas_test_sm12$status_obesitas,rpartprobte_sm7[,2])
auc8 <- auc(Data_obesitas_test_sm22$status_obesitas,rpartprobte_sm8[,2])
auc9 <- auc(Data_obesitas_test_sm32$status_obesitas,rpartprobte_sm9[,2])

#C50
library(C50)
Data_obesitas_train_sm32 <- Data_obesitas_train_sm32[-25]
visual7_2 <- C5.0(status_obesitas ~.,Data_obesitas_train_sm12)
visual8_2 <- C5.0(status_obesitas ~.,Data_obesitas_train_sm22)
visual9_2 <- C5.0(status_obesitas ~.,Data_obesitas_train_sm32)

#70%
rpartpred7_2 <- predict(visual7_2,Data_obesitas_test_sm12,type = "class")
rpartpred8_2 <- predict(visual8_2,Data_obesitas_test_sm22,type = "class")
rpartpred9_2 <- predict(visual9_2,Data_obesitas_test_sm32,type = "class")
cfm7_2 <- confusionMatrix(rpartpred7_2,Data_obesitas_test_sm12$status_obesitas)
cfm8_2 <- confusionMatrix(rpartpred8_2,Data_obesitas_test_sm22$status_obesitas)
cfm9_2 <- confusionMatrix(rpartpred9_2,Data_obesitas_test_sm32$status_obesitas)


library(pROC)
library(ROCR)
rpartprobte_sm7_2 <- predict(visual7_2,Data_obesitas_test_sm12,type = "prob")
rpartprobte_sm8_2 <- predict(visual8_2,Data_obesitas_test_sm22,type = "prob")
rpartprobte_sm9_2 <- predict(visual9_2,Data_obesitas_test_sm32,type = "prob")
auc7_2 <- auc(Data_obesitas_test_sm12$status_obesitas,rpartprobte_sm7_2[,2])
auc8_2 <- auc(Data_obesitas_test_sm22$status_obesitas,rpartprobte_sm8_2[,2])
auc9_2 <- auc(Data_obesitas_test_sm32$status_obesitas,rpartprobte_sm9_2[,2])

