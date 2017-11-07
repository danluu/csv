args = commandArgs(trailingOnly=TRUE)

if (length(args) != 2) {
   stop("arguments [input] [output]")
}

print(args)
print(args[0])
print(args[1])
print(args[2])

data <- read.csv(file=args[1])
write.csv(data, file=args[2])

