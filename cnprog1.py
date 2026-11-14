
drop = 0
count = 0
inp = []

cap = int(input("Enter the bucket size:\n"))
process = int(input("Enter the processing rate:\n"))
nsec = int(input("Enter the number of seconds you want to simulate:\n"))

for i in range(nsec):
    pkt = int(input(f"Enter the size of the packet entering at {i + 1} sec:\n"))
    inp.append(pkt)

print("\nSecond | Packet Received | Packet Sent | Packet Left | Dropped")
print("--------------------------------------------------------------")

    # Simulation for the duration of incoming packets
for i in range(nsec):
    count += inp[i]
    if count > cap:
        drop = count - cap
        count = cap

    mini = min(count, process)
    count -= mini
    print(f"{i + 1}\t {inp[i]}\t\t {mini}\t\t {count}\t\t {drop}")
    drop = 0

    # Drain remaining packets in the bucket after input stops
i = nsec
while count != 0:
    if count > cap:
        drop = count - cap
        count = cap

    mini = min(count, process)
    count -= mini
    print(f"{i + 1}\t 0\t\t {mini}\t\t {count}\t\t {drop}")
    drop = 0
    i += 1

