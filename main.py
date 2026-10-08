def main():
    scores = input("Enter scores separated by space: ")

    scores = [float(score) for score in scores.split()]

    if not scores:
        print("No scores entered.")
        return

    total = sum(scores)
    average = total / len(scores)
    maximum = max(scores)
    minimum = min(scores)

    print("Scores:", scores)
    print("Sum:", total)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)


main()