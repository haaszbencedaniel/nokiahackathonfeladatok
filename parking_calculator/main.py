from pathlib import Path

from datetime import datetime

def calculate_parking_fee(entry: datetime, exit: datetime) -> int:

    if exit < entry:
        raise ValueError("A kilépési idő nem lehet korábbi a belépéi időnél!")

    duration_minutes = (exit - entry).total_seconds() / 60

    if duration_minutes <= 30:
        return 0

    full_days = int(duration_minutes // (24 * 60))

    remaining_minutes = duration_minutes % (24 * 60)

    fee = full_days * 10000

    if remaining_minutes <= 30:

        pass
    elif remaining_minutes <= 30 + 3 * 60:

        billable_minutes = remaining_minutes - 30

        fee += (billable_minutes/60) * 300
    else:

        fee += 3 * 300

        billable_minutes = remaining_minutes - 30 - 3 * 60

        fee += (billable_minutes / 60) * 500

    return round(fee)



def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    lines = data.splitlines()

    results = []

    for line in lines[2:]:
        line = line.strip()
        if not line:
            continue

        parts = line.split()

        if len(parts) < 5:
            continue

        plate = parts[0]

        entry_str = parts[1] + " " + parts[2]

        exit_str = parts[3] + " " + parts[4]

        try:
            entry = datetime.strptime(entry_str, "%Y-%m-%d %H:%M:%S")

            exit = datetime.strptime(exit_str, "%Y-%m-%d %H:%M:%S")

            fee = calculate_parking_fee(entry, exit)

            results.append(f"{plate}\t{fee} Ft")

        except ValueError as e:
            results.append(f"{plate}\tHIBA: {e}")

    output = "\n".join(results)

    print(output)

    Path("output.txt").write_text(output, encoding="utf-8")



if __name__ == "__main__":
    main()
