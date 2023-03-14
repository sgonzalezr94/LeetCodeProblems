from math import log2, log10


def check_valid_power(n: int) -> bool:
    if (log2(n) % 1) == 0:
        print(f"{n} is effectively a power of 2, with {int(log2(n))} as the power.")
    else:
        print(f"{n} is not a power of 2 with the following {log2(n)} power")


check_valid_power(1427247692705959881058285969449495136382746624)
