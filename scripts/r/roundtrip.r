args = commandArgs(trailingOnly=TRUE)

if (length(args) != 2) {
   stop("arguments [input] [output]")
}

print(args)
print(args[0])
print(args[1])
print(args[2])

data <- read.csv(file=args[1], header=FALSE)
write.table(data, row.names=FALSE, col.names=FALSE, file=args[2], sep=",")

