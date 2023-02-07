def solve(numheads, numlegs):
    chicken = (numlegs - 2 * numheads) / 2
    rabbit = numheads - chicken
    return chicken, rabbit

numheads = int(input("Number of heads: "))
numlegs = int(input("Number of legs: "))
chicken, rabbit = solve(numheads, numlegs)
print(f"We have {chicken} chickens and {rabbit} rabbits!")