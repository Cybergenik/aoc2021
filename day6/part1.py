def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()
    initial_pop = [int(x) for x in content[0].split(",")]

    for p in range(80):
        print(f"Pop{p}: {initial_pop}")
        for i in range(0, len(initial_pop)):
            if initial_pop[i] != 0:
               initial_pop[i] -= 1
            else:
               initial_pop[i] = 6
               initial_pop.append(8)
    print(len(initial_pop))

if __name__ == "__main__":
    raise SystemExit(main())