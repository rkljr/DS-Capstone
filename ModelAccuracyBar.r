
setwd ("C:/Users/richa/Downloads")
library(reshape2)
library(ggplot2)

source("D:/R/functions.R")

barData <- data.frame(Model=c('Regression', 'SVM', 'Tree','KNN'), value=c(0.8260869565217391, 0.8260869565217391, 0.8260869565217391, 0.8260869565217391))

#barData$category <- factor(barData$category, levels = c("Budget","Actual"))
thmPantoneBalance <- theme_bw() + 
  theme(axis.text.x = element_text(size=15, face = "plain", colour = pantoneHawethornRose),
        axis.text.y = element_text(size=15, face = "plain", colour = pantoneHawethornRose),
        axis.title.x = element_text(size=15, face = "plain", hjust = 0.5, vjust = 1, colour = pantoneMutedClay),
        axis.title.y = element_text(size=15, face = "plain", hjust = 0.5, vjust = 1, colour = pantoneMutedClay),
        axis.line.x = element_line(color=pantoneHawethornRose, linewidth = .25),
        axis.line.y = element_line(color=pantoneHawethornRose, linewidth = .25),
        plot.title = element_text(size = 15, hjust = 0.5, colour = pantoneMutedClay),
        panel.border = element_blank(),
        panel.grid  = element_blank(),
        legend.title = element_blank(),
        legend.text = element_text(size=15, colour = pantoneMutedClay),
        panel.grid.major = element_line(color = "grey70",
                                        size = 0.5,
                                        linetype = 1),
        panel.grid.minor = element_line(color = "grey90",
                                        size = 0.5,
                                        linetype = 1)
  )

plt.a <- ggplot() +
  geom_hline(yintercept = seq(0, 1, by = 0.25), colour = "grey90", linewidth = 0.3) +
  #geom_hline(yintercept = seq(0, 3, by = 1), colour = "grey70", linewidth = 0.3) +
  geom_bar(data = barData, stat = "identity", aes(x = Model, y = value), fill = pantoneVeryPeri, width = NULL, linewidth = 0.3, position = position_dodge(), na.rm = TRUE) +
  # Add the axis titles
  labs(x = 'Model', y = 'Accuracy') +
  #Add a title
  ggtitle("Model Accuracy with Best Parameters") +
  # apply theme
  thmPantoneBalance

plt.a

# Save the Plot
ggsave(filename = 'ModelAccuracy.png', plot = plt.a, width = 200, height = 124, units="mm", dpi = 600, type="cairo-png")
