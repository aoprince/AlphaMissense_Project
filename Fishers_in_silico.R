# create dataframe 
project_data <- data.frame(
  "aligned" = c(57, 55),
  "not_aligned" = c(63, 65),
  row.names = c("REVEL", "AlphaMissense"),
  stringsAsFactors = FALSE
)

colnames(project_data) <- c("Aligned", "Not Aligned")

project_data

# create mosaic plot
mosaicplot(project_data,
           main = "Mosaic Plot",
           color = TRUE
           )

chisq.test(project_data)$expected

# fishers exact
test <- fisher.test(project_data)
test

# print p value
test$p.value

#transform data to allow for easier use with ggstatsplot
x <- c()
for (row in rownames(project_data)) {
  for (col in colnames(project_data)) {
    x <- rbind(x, matrix(rep(c(row, col), project_data[row, col]), 
                         ncol = 2, byrow = TRUE))
  }
}
in_silico_df <- as.data.frame(x)
colnames(in_silico_df) <- c("Aligned", "Not_Aligned")
in_silico_df

# Fishers Exact with raw data
test <- fisher.test(table(in_silico_df))

# combine plot and stats test
library(ggstatsplot)
ggbarstats(
  in_silico_df, Aligned, Not_Aligned,
  results.subtitle = FALSE,
  subtitle = paste0(
    "Fisher's exact test", ", p-value = ",
    ifelse(test$p.value < 0.001, "0.001", round(test$p.value, 3))
  )
)  


