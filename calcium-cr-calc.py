def calculate_ratio(uca, scr, sca, ucr):
    """
    Calculates the calcium/creatinine ratio.

    :param uca: urinary calcium concentration (mg/dl)
    :param scr: serum creatinine (mg/dl)
    :param sca: serum calcium concentration (mg/dl)
    :param ucr: urinary creatinine concentration (mg/dl)
    :return: calcium/creatinine ratio
    """
    try:
        ratio = (uca * scr) / (sca * ucr)
        return ratio
    except ZeroDivisionError:
        print("Error: Serum calcium and urinary creatinine concentrations must be non-zero.")
        return None

def main():
    print("Please enter the following values in mg/dl.")

    try:
        uca = float(input("Enter urinary calcium concentration (UCa): "))
        scr = float(input("Enter serum creatinine (SCr): "))
        sca = float(input("Enter serum calcium concentration (SCa): "))
        ucr = float(input("Enter urinary creatinine concentration (UCr): "))

        ratio = calculate_ratio(uca, scr, sca, ucr)

        if ratio is not None:
            print(f"The calcium/creatinine ratio is: {ratio:.5f}")
            if ratio <= 0.01:
                print("Ratio is less than or equal to 0.01. This may indicate FHH in 80% of cases.")
            elif ratio <= 0.02:
                print("Ratio is less than or equal to 0.02. Patients should be tested for mutations in the CaSR gene.")
            else:
                print("Ratio is above 0.02. This is above the typical range for FHH.")

    except ValueError:
        print("Invalid input. Please enter numerical values only.")

if __name__ == "__main__":
    main()
