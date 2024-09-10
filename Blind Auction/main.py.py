logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
dict = {}
values = []
names = []
def high_bid(names_of):
    for key in dict:
        value = dict[key]
        values.append(value)
    high = max(values)
    index_of_high = values.index(high)
    bidder_name = names_of[index_of_high]
    print(f"\n highest bid is {high} from {bidder_name}")


def auction():
    name = input("\n what is your name? \n ")
    names.append(name)
    bid = int(input("\n what is your bid? rs. "))
    dict[name] = bid
    more = int(input("\n are there other users who want to bid? if Yes type 1 or 0 for No "))
    if more == 1:
        auction()
    else:
        high_bid(names)

auction()

