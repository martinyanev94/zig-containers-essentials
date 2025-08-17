outer_count = 0
inner_count = 0

while outer_count < 3:
    inner_count = 0  # reset inner_count for each outer iteration
    while inner_count < 5:
        print(f"Outer: {outer_count}, Inner: {inner_count}")
        inner_count += 1
    outer_count += 1
