# Predicting Solar Power Generation from Weather Data
# Train, Validation, Test Set ID Allocation

# Alex Kim
# June 2019

library(tidyverse)
set.seed(1)

# Read/consolidate the Data
nsrdb_16 <- read_csv("data/105130_36.17_-115.14_2016.csv", skip = 2)
nsrdb_17 <- read_csv("data/105130_36.17_-115.14_2017.csv", skip = 2)
nsrdb <- bind_rows(nsrdb_16, nsrdb_17)
rm(nsrdb_16, nsrdb_17)

# Generate unique IDs for each day
ids <- transmute(nsrdb, ID = str_c(Year, Month, Day, sep="-"))
ids <- unlist(distinct(ids))
n <- length(ids)
rm(nsrdb)

# Define proportions for the training, validation, and test set
train_proportion <- 0.4
valid_proportion <- 0.1

# Allocate training set IDs
train_size <- round(train_proportion * n)
train_indexes <- sample(1:n, size = train_size)
train_ids <- ids[train_indexes]

# Allocate validation set IDs
ids <- ids[-train_indexes]
n <- length(ids)
valid_size <- round(valid_proportion * n)
valid_indexes <- sample(1:n, size = valid_size)
valid_ids <- ids[valid_indexes]

# Allocate test set IDs
test_ids <- ids[-valid_indexes]

# Save ID allocations to CSV
write_csv(as_tibble(train_ids), "data-allocations/train.csv", col_names = FALSE)
write_csv(as_tibble(valid_ids), "data-allocations/valid.csv", col_names = FALSE)
write_csv(as_tibble(test_ids), "data-allocations/test.csv", col_names = FALSE)

rm(train_proportion, train_size, train_indexes, valid_proportion, valid_size, valid_indexes)