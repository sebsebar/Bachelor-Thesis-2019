# -------- Loading libraries
pacman::p_load("gridExtra","grid","ggplot2","lattice","tidyverse","plyr", "ggpubr","cowplot", "svglite")

#######################################################
# ---------------- PREPARE ANEW DATA -----------------#
#######################################################

# set absolute working directory
abs_dic <- dirname(rstudioapi::getSourceEditorContext()$path)
setwd(abs_dic)
# set working directory to data folder
setwd("./ANEW_Data")

# ---- Load and clean ANEW data 
ANEW_data <- read.delim("ANEW2017All.txt", header=TRUE)
ANEW_data$ValSD <- gsub("[()]", "", ANEW_data$ValSD) 
ANEW_data$AroSD <- gsub("[()]", "", ANEW_data$ValSD)
ANEW_data$DomSD <- gsub("[()]", "", ANEW_data$DomSD)

# ----- Make new categories (high and low) for Valence and Arousal
quantile(ANEW_data$ValMn, c(.40, .50, .60)) # micah - these quantiles don't direclty correspond to the cutoffs- check with seb
quantile(ANEW_data$AroMn, c(.40, .50, .60))

# set cut-offs based on the quantiles just calculated
cuthigh <- 5.4
cutlow <- 4.6

# using the cut-offs to make four new categories for the new variable Val_Aro
# also omitting words with valence and arousal values below cuthigh and above cutlow
ANEW_data$Val_Aro_ANEW <- ifelse(ANEW_data$ValMn >= cuthigh & ANEW_data$AroMn >= cuthigh, 'ValHighAroHigh',
                               ifelse(ANEW_data$ValMn >= cuthigh & ANEW_data$AroMn <= cutlow, 'ValHighAroLow',
                                      ifelse(ANEW_data$ValMn <= cutlow & ANEW_data$AroMn >= cuthigh, 'ValLowAroHigh',
                                             ifelse(ANEW_data$ValMn <= cutlow & ANEW_data$AroMn <= cutlow, 'ValLowAroLow',
                                                    '0'))))

###########################################################
# ---------------- PREPARE PAVLOVIA DATA -----------------#
###########################################################

# set directory
setwd(abs_dic)
setwd("./Pavlovia_Data/Pavlovia_Completed")

# list of names in directory
pav_filenames = list.files(pattern = "PARTIC*") #list of filenames from WD
# empty dataframe to load the list of files
Pav_data = data.frame() 

# load Pavlovia data to empty dataframe
for (i in pav_filenames){ #loop over list of files
  #import the current file
  Pav <- read.delim(i,header=TRUE,sep = ",")
  Pav <- select(Pav,A_key_resp.keys, key_resp.keys,word, ParticipantID)
  Pav_data <- rbind(Pav_data,Pav)
}
Pav_data <- rename(Pav_data, c(A_key_resp.keys="Arousal", key_resp.keys= "Valence",word="Word"))

# Histograms of all participant ratings - to exclude subjects who only ever press the same key

hist1 <- ggplot(Pav_data, aes(x = Arousal))+ facet_grid(~ ParticipantID) + geom_histogram() # 1116 is excluded
hist2 <- ggplot(Pav_data, aes(x = Valence))+ facet_grid(~ ParticipantID) + geom_histogram() # 1116 is exclusion 

# discarding neutral "flatliners" with almost all ratings as 5
Pav_data <- filter(Pav_data, ParticipantID != 1116)

# make mean values for each word to make it comparable to the ANEW data
pav_mean_values <- data_frame()
for (i in unique(Pav_data$Word)){ #loop over list of files
  test <- filter(Pav_data, Word == i)
  test$Arousal_Mean_Pavlovia <- mean(test$Arousal)
  test$Valence_Mean_Pavlovia <- mean(test$Valence)
  test <- select(test,Word,Arousal_Mean_Pavlovia,Valence_Mean_Pavlovia) 
  pav_mean_values <- rbind(pav_mean_values,test)
}

Pav_data <- pav_mean_values%>% 
  distinct(Word, .keep_all = TRUE)

################################################################################
# --------------- Combine data: Pavlovia Data with ANEW Categories ----------- # 
################################################################################

#Merging ANEW and Pavlovia, assigning headers
total <- merge(Pav_data,ANEW_data,by="Word")
total <- rename(total, c(ValMn="Valence_Mean_ANEW", AroMn= "Arousal_Mean_ANEW"))

#Making new binned variables for Arousal and Valence using ANEW
total$Arousal_cutoff <- (ifelse(total$Val_Aro_ANEW == 'ValHighAroHigh', 'High', ifelse(total$Val_Aro_ANEW == 'ValLowAroHigh', 'High','Low')))
total$Valence_cutoff <- (ifelse(total$Val_Aro_ANEW == 'ValHighAroHigh', 'High', ifelse(total$Val_Aro_ANEW == 'ValHighAroLow', 'High','Low')))

###########################################################################
# --------- Find Spearman Correlation to plot Rating Consistency--------- #
###########################################################################

#arousal
cor.test(total$Arousal_Mean_Pavlovia,total$Arousal_Mean_ANEW, method = "spearman", exact=F)
#valence
cor.test(total$Valence_Mean_Pavlovia,total$Valence_Mean_ANEW, method = "spearman", exact=F)

##################################################################
# --------------- Plotting Word Selection Plots ---------------- # 
##################################################################
setwd(abs_dic)
# Plot for the Pavlovia data
PAV <- ggplot(total, aes(x = Valence_Mean_Pavlovia, y = Arousal_Mean_Pavlovia, colour=Val_Aro_ANEW)) + 
  geom_point(size = 1) + 
  scale_color_manual(values=c("#AA0000","#ff8383","#2C5AA0","#99b7e3","#FFF0B5"))+ 
  labs(title= "B. Pavlovia Word Ratings",x = "Valence", y = "Arousal") + 
  geom_hline(aes(yintercept = 5)) + 
  geom_vline(aes(xintercept = 5)) +
  scale_x_continuous(breaks = c(1,2,3,4,5,6,7,8,9), limits=c(1,9)) +
  scale_y_continuous(breaks = c(1,2,3,4,5,6,7,8,9), limits=c(1,9)) +
  theme_bw() + 
  scale_fill_manual(values = c('#999999','#E69F00'))+ 
  theme(legend.position = "none") +
  theme(title = element_text(size=14, face="bold"),axis.text.x = element_text(face = "bold", size = 14),axis.text.y = element_text(face = "bold", size = 14))

# Marginal density plot of x (top panel)
xdensity <- axis_canvas(PAV, axis = "x")+ 
  geom_density(data = total, aes(Valence_Mean_Pavlovia, fill=Valence_cutoff),alpha=.5)+
  theme(legend.position = "none",axis.title.x = element_blank(),axis.title.y = element_blank())+ 
  scale_fill_manual(values=c("#AA0000","#2C5AA0"))

# Marginal density plot of y (right panel)
ydensity <- axis_canvas(PAV, axis = "y", coord_flip = TRUE)+
  geom_density(data=total, aes(Arousal_Mean_Pavlovia, fill=Arousal_cutoff),alpha=.5) +
  theme(legend.position = "none",axis.title.x = element_blank(),axis.title.y = element_blank())+
  coord_flip()+ 
  scale_fill_manual(values=c("#272727","#A4A4A4"))

p <- insert_xaxis_grob(PAV, xdensity, grid::unit(.2, "null"), position = "top")
pp<- insert_yaxis_grob(p, ydensity, grid::unit(.2, "null"), position = "right")
P1 <- ggdraw(pp)

ggsave(filename="Figure2_B.svg", plot=P1, height = 6, width = 6)

# Plot for the ANEW data
ANEW <- ggplot(total, aes(x = Valence_Mean_ANEW, y = Arousal_Mean_ANEW, colour=Val_Aro_ANEW)) + 
  geom_point(size = 1)+ 
  scale_color_manual(values=c("#AA0000","#ff8383","#2C5AA0","#99b7e3","#FFF0B5"))+ 
  labs(title = "A. ANEW Word Ratings",x = "Valence", y = "Arousal") + geom_hline(aes(yintercept = 5)) + 
  geom_vline(aes(xintercept = 5)) +
  scale_x_continuous(breaks = c(1,2,3,4,5,6,7,8,9), limits=c(1,9)) +
  scale_y_continuous(breaks = c(1,2,3,4,5,6,7,8,9), limits=c(1,9)) +
  theme_bw()+ 
  scale_fill_manual(values = c('#999999','#E69F00'))+ 
  theme(legend.position = "none") + 
  theme(title = element_text(size=14, face="bold"),axis.text.x = element_text(face = "bold", size = 14),axis.text.y = element_text(face = "bold", size = 14))

# Marginal density plot of x (top panel)
xdensity2 <- axis_canvas(ANEW, axis = "x")+ 
  geom_density(data = total, aes(Valence_Mean_ANEW, fill=Valence_cutoff),alpha=.5)+
  theme(legend.position = "none",axis.title.x = element_blank(),axis.title.y = element_blank())+ 
  scale_fill_manual(values=c("#AA0000","#2C5AA0"))
  
# Marginal density plot of y (right panel)
ydensity2 <- axis_canvas(ANEW, axis = "y", coord_flip = TRUE)+
  geom_density(data=total, aes(Arousal_Mean_ANEW, fill=Arousal_cutoff),alpha=.5) +
  theme(legend.position = "none",axis.title.x = element_blank(),axis.title.y = element_blank())+
  coord_flip()+ 
  scale_fill_manual(values=c("#272727","#A4A4A4"))

p1 <- insert_xaxis_grob(ANEW, xdensity2, grid::unit(.2, "null"), position = "top")
p2<- insert_yaxis_grob(p1, ydensity2, grid::unit(.2, "null"), position = "right")
P2 <- ggdraw(p2)

ggsave(filename="Figure2_A.svg", plot=P2, height = 6, width = 6)


#######################################################################
# ------------------- Plots for rating consistency ------------------ #
#######################################################################

# Plot rating consistency for arousal and valence
P3 <- ggplot(total, aes(x=Arousal_Mean_Pavlovia, y=Arousal_Mean_ANEW))+ 
  geom_point(size = 1)+ 
  geom_abline(intercept = 0, slope = 1,colour="red",size=1)+
  scale_x_continuous(breaks = c(1,2,3,4,5,6,7,8,9), limits=c(1,9)) +
  scale_y_continuous(breaks = c(1,2,3,4,5,6,7,8,9), limits=c(1,9)) +
  theme_bw()+
  labs(title = "D. Rating Consistency Arousal", x = "Mean Arousal Rating: Pavlovia", y = "Mean Arousal Rating: ANEW") +
  annotate("text", x = 2, y = 8.5, label = "Spearman Correlation",size=4, fontface="bold")+
  annotate("text", x = 2, y = 8, label = "rho = 0.7669351",size=4, fontface="bold") +
  annotate("text", x = 2, y = 7.5, label = "P-value = 2.2e-16",size=4, fontface="bold") + 
  theme(legend.position = "none")+ 
  theme(title = element_text(face = "bold", size = 14),axis.text.x = element_text(face = "bold", size = 14),axis.text.y = element_text(face = "bold", size = 14),panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
        panel.background = element_blank(), axis.line = element_line(colour = "black"))

ggsave(filename="Figure2_D.svg", plot=P3, height = 6, width = 6)

P4 <- ggplot(total, aes(x=Valence_Mean_Pavlovia, y=Valence_Mean_ANEW))+ 
  geom_point(size = 1) + 
  geom_abline(intercept = 0, slope = 1,colour="red",size=1)+
  scale_x_continuous(breaks = c(1,2,3,4,5,6,7,8,9), limits=c(1,9)) +
  scale_y_continuous(breaks = c(1,2,3,4,5,6,7,8,9), limits=c(1,9)) +
  theme_bw()+
  labs(title = "C. Rating Consistency Valence",x = "Mean Valence Rating: Pavlovia", y = "Mean Valence Rating: ANEW") +
  annotate("text", x = 2, y = 8.5, label = "Spearman Correlation",size=4, fontface="bold")+
  annotate("text", x = 2, y = 8, label = "rho = 0.9316756",size=4, fontface="bold") +
  annotate("text", x = 2, y = 7.5, label = "P-value = 2.2e-16",size=4, fontface="bold") + 
  theme(legend.position = "none") + 
  theme(title = element_text(face = "bold", size = 14),axis.text.x = element_text(face = "bold", size = 14),axis.text.y = element_text(face = "bold", size = 14),panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
    panel.background = element_blank(), axis.line = element_line(colour = "black"))

ggsave(filename="Figure2_C.svg", plot=P4, height = 6, width = 6)
